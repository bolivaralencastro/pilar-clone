# Script alternativo: Extração via HTTP requests (sem DevTools)
# Captura HTML, CSS, JavaScript e reconstrói informações

param(
    [string]$Url = "https://pilarhomes.com.br",
    [string]$OutputDir = "c:\Users\boliv\Documents\Pilar\extracted"
)

Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  EXTRAÇÃO VIA HTTP - PILARHOMES (Método Alternativo)" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Criar estrutura de diretórios
$apiDir = Join-Path $OutputDir "api"
$cssDir = Join-Path $OutputDir "css"
$tokensDir = Join-Path $OutputDir "tokens"

@($OutputDir, $apiDir, $cssDir, $tokensDir) | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Path $_ -Force | Out-Null
        Write-Host "✓ Criado: $_" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "PASSO 1: Baixando página principal..." -ForegroundColor Yellow

try {
    $response = Invoke-WebRequest -Uri $Url -UseBasicParsing
    $html = $response.Content
    $htmlPath = Join-Path $OutputDir "index.html"
    $html | Out-File -FilePath $htmlPath -Encoding UTF8
    Write-Host "✓ HTML salvo: $htmlPath" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "PASSO 2: Extraindo links de CSS e JS..." -ForegroundColor Yellow
    
    # Regex para encontrar links CSS
    $cssLinks = [regex]::Matches($html, '<link[^>]+href=[''"]([^''"]+\.css[^''"]*)') | 
        ForEach-Object { $_.Groups[1].Value }
    
    # Regex para encontrar scripts
    $jsLinks = [regex]::Matches($html, '<script[^>]+src=[''"]([^''"]+\.js[^''"]*)') | 
        ForEach-Object { $_.Groups[1].Value }
    
    Write-Host "  - CSS files encontrados: $($cssLinks.Count)" -ForegroundColor Cyan
    Write-Host "  - JS files encontrados: $($jsLinks.Count)" -ForegroundColor Cyan
    
    Write-Host ""
    Write-Host "PASSO 3: Baixando arquivos CSS..." -ForegroundColor Yellow
    
    $cssFiles = @()
    foreach ($cssLink in $cssLinks | Select-Object -First 10) {
        try {
            $cssUrl = if ($cssLink -match '^https?://') { 
                $cssLink 
            } else { 
                "https://pilarhomes.com.br$cssLink" 
            }
            
            $fileName = Split-Path $cssLink -Leaf
            if ([string]::IsNullOrWhiteSpace($fileName)) {
                $fileName = "style_$([guid]::NewGuid().ToString().Substring(0,8)).css"
            }
            
            $cssContent = Invoke-WebRequest -Uri $cssUrl -UseBasicParsing
            $cssPath = Join-Path $cssDir $fileName
            $cssContent.Content | Out-File -FilePath $cssPath -Encoding UTF8
            
            $cssFiles += @{
                Url = $cssUrl
                Path = $cssPath
                Size = $cssContent.Content.Length
            }
            
            Write-Host "  OK $fileName ($($cssContent.Content.Length) bytes)" -ForegroundColor Green
        } catch {
            Write-Host "  ERRO ao baixar: $cssLink" -ForegroundColor Red
        }
    }
    
    Write-Host ""
    Write-Host "PASSO 4: Analisando CSS para extrair design tokens..." -ForegroundColor Yellow
    
    # Juntar todo CSS
    $allCss = ""
    foreach ($cssFile in $cssFiles) {
        $allCss += Get-Content $cssFile.Path -Raw -ErrorAction SilentlyContinue
        $allCss += "`n`n"
    }
    
    # Salvar CSS completo
    $mainCssPath = Join-Path $cssDir "main-combined.css"
    $allCss | Out-File -FilePath $mainCssPath -Encoding UTF8
    Write-Host "  ✓ CSS combinado salvo: $mainCssPath" -ForegroundColor Green
    
    # Extrair CSS variables
    $cssVars = [regex]::Matches($allCss, '--([a-zA-Z0-9-]+)\s*:\s*([^;]+);') | 
        ForEach-Object {
            @{
                Variable = $_.Groups[1].Value
                Value = $_.Groups[2].Value.Trim()
            }
        }
    
    Write-Host "  - CSS Variables encontradas: $($cssVars.Count)" -ForegroundColor Cyan
    
    # Extrair cores (hex, rgb, hsl)
    $colors = [regex]::Matches($allCss, '#([0-9a-fA-F]{3,6})|rgb\([^)]+\)|hsl\([^)]+\)') | 
        ForEach-Object { $_.Value } | 
        Sort-Object -Unique
    
    Write-Host "  - Cores encontradas: $($colors.Count)" -ForegroundColor Cyan
    
    # Extrair font-families
    $fonts = [regex]::Matches($allCss, 'font-family\s*:\s*([^;]+);') | 
        ForEach-Object { $_.Groups[1].Value.Trim() } | 
        Sort-Object -Unique
    
    Write-Host "  - Font families encontradas: $($fonts.Count)" -ForegroundColor Cyan
    
    Write-Host ""
    Write-Host "PASSO 5: Gerando arquivo de Design Tokens..." -ForegroundColor Yellow
    
    # Criar objeto de tokens
    $tokens = @{
        metadata = @{
            source = $Url
            extractedAt = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
            method = "HTTP extraction"
        }
        colors = @{
            primary = @($colors | Select-Object -First 20)
            all = $colors
        }
        typography = @{
            fontFamilies = $fonts
        }
        cssVariables = $cssVars
    }
    
    $tokensJsonPath = Join-Path $tokensDir "design-tokens.json"
    $tokens | ConvertTo-Json -Depth 10 | Out-File -FilePath $tokensJsonPath -Encoding UTF8
    Write-Host "  ✓ Tokens JSON: $tokensJsonPath" -ForegroundColor Green
    
    # Criar arquivo CSS de tokens
    $tokensCss = @"
/**
 * Design Tokens - PilarHomes
 * Extraído em: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
 * Fonte: $Url
 */

:root {
$(
    $cssVars | ForEach-Object {
        "  --$($_.Variable): $($_.Value);"
    }
)
}

/* Cores principais extraídas */
$(
    $colors | Select-Object -First 20 | ForEach-Object -Begin { $i = 1 } -Process {
        "/* Color $i`: $_ */"
        $i++
    }
)

/* Font Families */
$(
    $fonts | ForEach-Object {
        "/* $_ */"
    }
)
"@
    
    $tokensCssPath = Join-Path $tokensDir "design-tokens.css"
    $tokensCss | Out-File -FilePath $tokensCssPath -Encoding UTF8
    Write-Host "  ✓ Tokens CSS: $tokensCssPath" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "PASSO 6: Analisando HTML para mapear estrutura Nuxt..." -ForegroundColor Yellow
    
    # Extrair scripts Nuxt
    $nuxtScripts = [regex]::Matches($html, '<script[^>]+src=[''"]([^''"]*_nuxt[^''"]*)') | 
        ForEach-Object { $_.Groups[1].Value }
    
    Write-Host "  - Scripts Nuxt encontrados: $($nuxtScripts.Count)" -ForegroundColor Cyan
    
    # Tentar extrair __NUXT__ data inline
    if ($html -match 'window\.__NUXT__\s*=\s*(\{.+?\});') {
        Write-Host "  ✓ Dados __NUXT__ encontrados no HTML!" -ForegroundColor Green
        $nuxtDataPath = Join-Path $apiDir "nuxt-data-inline.js"
        "window.__NUXT__ = " + $matches[1] + ";" | Out-File -FilePath $nuxtDataPath -Encoding UTF8
        Write-Host "    Salvo em: $nuxtDataPath" -ForegroundColor Gray
    }
    
    Write-Host ""
    Write-Host "PASSO 7: Mapeando endpoints conhecidos da API..." -ForegroundColor Yellow
    
    $endpoints = @{
        base = "https://api.pilarhomes.com.br"
        cdn = @{
            images = "https://imagens.pilarhomes.com.br"
            static = "https://static.pilarhomes.com.br"
        }
        aws = @{
            s3 = "https://blintz-properties-sandbox.s3.amazonaws.com"
        }
        discovered = @(
            @{ path = "/properties"; method = "GET"; description = "Lista de propriedades" }
            @{ path = "/properties/:id"; method = "GET"; description = "Detalhes de propriedade" }
            @{ path = "/agents"; method = "GET"; description = "Lista de corretores" }
            @{ path = "/companies"; method = "GET"; description = "Lista de boutiques" }
        )
    }
    
    $endpointsPath = Join-Path $apiDir "endpoints-map.json"
    $endpoints | ConvertTo-Json -Depth 10 | Out-File -FilePath $endpointsPath -Encoding UTF8
    Write-Host "  ✓ Mapa de endpoints: $endpointsPath" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "  EXTRAÇÃO CONCLUÍDA COM SUCESSO!" -ForegroundColor Green
    Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Arquivos gerados em: $OutputDir" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  📁 API:" -ForegroundColor Cyan
    Write-Host "     - endpoints-map.json" -ForegroundColor Gray
    Write-Host "     - nuxt-data-inline.js (se encontrado)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  📁 CSS:" -ForegroundColor Cyan
    Write-Host "     - main-combined.css ($($allCss.Length) chars)" -ForegroundColor Gray
    Write-Host "     - $($cssFiles.Count) arquivos CSS individuais" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  📁 Tokens:" -ForegroundColor Cyan
    Write-Host "     - design-tokens.json ($($cssVars.Count) variables)" -ForegroundColor Gray
    Write-Host "     - design-tokens.css" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Próximo passo: Use esses tokens no protótipo Vercel!" -ForegroundColor Yellow
    Write-Host ""
    
} catch {
    Write-Host "✗ ERRO: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host $_.ScriptStackTrace -ForegroundColor DarkRed
}
