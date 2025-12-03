# Extração simplificada de CSS e estrutura da PilarHomes

$outputDir = "c:\Users\boliv\Documents\Pilar\extracted"
$apiDir = "$outputDir\api"
$cssDir = "$outputDir\css"
$tokensDir = "$outputDir\tokens"

# Criar diretórios
New-Item -ItemType Directory -Path $apiDir -Force | Out-Null
New-Item -ItemType Directory -Path $cssDir -Force | Out-Null
New-Item -ItemType Directory -Path $tokensDir -Force | Out-Null

Write-Host "Extraindo dados de pilarhomes.com.br..." -ForegroundColor Cyan

# Baixar página principal
$url = "https://pilarhomes.com.br"
$response = Invoke-WebRequest -Uri $url -UseBasicParsing
$html = $response.Content

# Salvar HTML
$html | Out-File "$outputDir\index.html" -Encoding UTF8
Write-Host "HTML salvo: index.html" -ForegroundColor Green

# Extrair links CSS
$cssPattern = 'href="([^"]+\.css[^"]*)"'
$cssLinks = ([regex]::Matches($html, $cssPattern) | ForEach-Object { $_.Groups[1].Value })

Write-Host "CSS files encontrados: $($cssLinks.Count)" -ForegroundColor Yellow

# Baixar cada CSS
$allCss = ""
$count = 0
foreach ($cssLink in $cssLinks) {
    try {
        $count++
        if ($count -gt 10) { break }
        
        $cssUrl = if ($cssLink.StartsWith("http")) { $cssLink } else { "https://pilarhomes.com.br$cssLink" }
        $fileName = "style_$count.css"
        
        $cssResp = Invoke-WebRequest -Uri $cssUrl -UseBasicParsing -TimeoutSec 10
        $cssContent = $cssResp.Content
        
        $cssContent | Out-File "$cssDir\$fileName" -Encoding UTF8
        $allCss += $cssContent + "`n`n"
        
        Write-Host "  OK: $fileName" -ForegroundColor Green
    } catch {
        Write-Host "  ERRO: $cssLink" -ForegroundColor Red
    }
}

# Salvar CSS combinado
$allCss | Out-File "$cssDir\combined.css" -Encoding UTF8
Write-Host "`nCSS combinado salvo: combined.css" -ForegroundColor Green

# Extrair design tokens
Write-Host "`nExtraindo design tokens..." -ForegroundColor Cyan

# CSS Variables
$varPattern = '--([\w-]+):\s*([^;]+);'
$variables = @{}
[regex]::Matches($allCss, $varPattern) | ForEach-Object {
    $varName = $_.Groups[1].Value
    $varValue = $_.Groups[2].Value.Trim()
    $variables[$varName] = $varValue
}

Write-Host "CSS Variables: $($variables.Count)" -ForegroundColor Yellow

# Cores (hex)
$hexPattern = '#[0-9a-fA-F]{3,6}'
$colors = [regex]::Matches($allCss, $hexPattern) | ForEach-Object { $_.Value } | Sort-Object -Unique

Write-Host "Cores hex: $($colors.Count)" -ForegroundColor Yellow

# Font families
$fontPattern = 'font-family:\s*([^;]+);'
$fonts = [regex]::Matches($allCss, $fontPattern) | ForEach-Object { $_.Groups[1].Value.Trim() } | Sort-Object -Unique

Write-Host "Font families: $($fonts.Count)" -ForegroundColor Yellow

# Criar JSON de tokens
$tokens = @{
    extractedAt = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    source = $url
    cssVariables = $variables
    colors = $colors
    fonts = $fonts
}

$tokens | ConvertTo-Json -Depth 10 | Out-File "$tokensDir\design-tokens.json" -Encoding UTF8
Write-Host "`nTokens salvos: design-tokens.json" -ForegroundColor Green

# Criar CSS de tokens
$tokensCss = ":root {`n"
foreach ($key in $variables.Keys | Sort-Object) {
    $tokensCss += "  --$key`: $($variables[$key]);`n"
}
$tokensCss += "}`n"

$tokensCss | Out-File "$tokensDir\design-tokens.css" -Encoding UTF8
Write-Host "Tokens CSS salvos: design-tokens.css" -ForegroundColor Green

# Mapa de endpoints
$endpoints = @{
    base = "https://api.pilarhomes.com.br"
    cdn = @{
        images = "https://imagens.pilarhomes.com.br"
        static = "https://static.pilarhomes.com.br"
    }
    aws = "https://blintz-properties-sandbox.s3.amazonaws.com"
    routes = @(
        "/properties",
        "/agents",
        "/companies",
        "/properties/:id"
    )
}

$endpoints | ConvertTo-Json -Depth 10 | Out-File "$apiDir\endpoints-map.json" -Encoding UTF8
Write-Host "Endpoints mapeados: endpoints-map.json" -ForegroundColor Green

Write-Host "`n=== EXTRACAO CONCLUIDA ===" -ForegroundColor Cyan
Write-Host "Arquivos em: $outputDir" -ForegroundColor Yellow
