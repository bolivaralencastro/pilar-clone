# Script para extrair Design System do PilarHomes.com.br

Write-Host "Extraindo Design System de pilarhomes.com.br..." -ForegroundColor Cyan
Write-Host ""

$url = "https://pilarhomes.com.br/"
$response = Invoke-WebRequest -Uri $url -UseBasicParsing
$html = $response.Content

# Criar diretorio para salvar assets
$outputDir = "c:\Users\boliv\Documents\Pilar\design_system_analysis"
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# 1. EXTRAIR CSS FILES
Write-Host "=== EXTRAINDO ARQUIVOS CSS ===" -ForegroundColor Green
$cssLinks = [regex]::Matches($html, '<link[^>]*href="([^"]+\.css[^"]*)"')
$cssFiles = @()

foreach ($match in $cssLinks) {
    $cssUrl = $match.Groups[1].Value
    if ($cssUrl -notmatch '^http') {
        $cssUrl = "https://pilarhomes.com.br" + $cssUrl
    }
    Write-Host "Baixando: $cssUrl" -ForegroundColor Yellow
    
    try {
        $cssContent = Invoke-WebRequest -Uri $cssUrl -UseBasicParsing
        $fileName = [System.IO.Path]::GetFileName($cssUrl) -replace '\?.*', ''
        $cssFiles += @{
            url = $cssUrl
            content = $cssContent.Content
            fileName = $fileName
        }
        
        # Salvar arquivo CSS
        $cssContent.Content | Out-File -FilePath "$outputDir\$fileName" -Encoding UTF8
        Write-Host "  Salvo: $fileName" -ForegroundColor Green
    } catch {
        Write-Host "  Erro ao baixar: $_" -ForegroundColor Red
    }
}

# 2. ANALISAR CORES
Write-Host ""
Write-Host "=== ANALISANDO PALETA DE CORES ===" -ForegroundColor Green
$colors = @{}
$allCss = ($cssFiles | ForEach-Object { $_.content }) -join "`n"
$allCss += $html

# Extrair cores hexadecimais
$hexColors = [regex]::Matches($allCss, '#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})\b')
foreach ($match in $hexColors) {
    $color = $match.Value.ToUpper()
    if (-not $colors.ContainsKey($color)) {
        $colors[$color] = 1
    } else {
        $colors[$color]++
    }
}

# Extrair cores RGB/RGBA
$rgbColors = [regex]::Matches($allCss, 'rgba?\([^)]+\)')
foreach ($match in $rgbColors) {
    $color = $match.Value
    if (-not $colors.ContainsKey($color)) {
        $colors[$color] = 1
    } else {
        $colors[$color]++
    }
}

# Ordenar por frequencia
$topColors = $colors.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 30

Write-Host "Top 30 cores mais usadas:" -ForegroundColor Yellow
$colorReport = @"
# PALETA DE CORES

"@
foreach ($color in $topColors) {
    Write-Host "  $($color.Key): $($color.Value) vezes" -ForegroundColor Cyan
    $colorReport += "$($color.Key) - Usado $($color.Value) vezes`n"
}

# 3. ANALISAR TIPOGRAFIA
Write-Host ""
Write-Host "=== ANALISANDO TIPOGRAFIA ===" -ForegroundColor Green
$fonts = [regex]::Matches($allCss, "font-family:\s*([^;{}]+)")
$fontSizes = [regex]::Matches($allCss, "font-size:\s*([^;{}]+)")
$fontWeights = [regex]::Matches($allCss, "font-weight:\s*([^;{}]+)")

$uniqueFonts = @{}
foreach ($match in $fonts) {
    $font = $match.Groups[1].Value.Trim()
    if (-not $uniqueFonts.ContainsKey($font)) {
        $uniqueFonts[$font] = 1
    } else {
        $uniqueFonts[$font]++
    }
}

Write-Host "Familias de fonte:" -ForegroundColor Yellow
$fontReport = @"

# TIPOGRAFIA

## Familias de Fonte:
"@
foreach ($font in $uniqueFonts.GetEnumerator() | Sort-Object -Property Value -Descending) {
    Write-Host "  $($font.Key)" -ForegroundColor Cyan
    $fontReport += "- $($font.Key)`n"
}

# 4. ANALISAR ESPACAMENTO
Write-Host ""
Write-Host "=== ANALISANDO ESPACAMENTOS ===" -ForegroundColor Green
$paddings = [regex]::Matches($allCss, "padding[^:]*:\s*([^;{}]+)")
$margins = [regex]::Matches($allCss, "margin[^:]*:\s*([^;{}]+)")

$spacingValues = @{}
foreach ($match in $paddings + $margins) {
    $value = $match.Groups[1].Value.Trim()
    if ($value -match '\d+(px|rem|em)') {
        if (-not $spacingValues.ContainsKey($value)) {
            $spacingValues[$value] = 1
        } else {
            $spacingValues[$value]++
        }
    }
}

Write-Host "Valores de espacamento mais comuns:" -ForegroundColor Yellow
$spacingReport = @"

# ESPACAMENTOS (Padding/Margin)

"@
foreach ($spacing in $spacingValues.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 20) {
    Write-Host "  $($spacing.Key): $($spacing.Value) vezes" -ForegroundColor Cyan
    $spacingReport += "$($spacing.Key) - Usado $($spacing.Value) vezes`n"
}

# 5. ANALISAR BORDER RADIUS
Write-Host ""
Write-Host "=== ANALISANDO BORDER RADIUS ===" -ForegroundColor Green
$borderRadius = [regex]::Matches($allCss, "border-radius:\s*([^;{}]+)")

$radiusValues = @{}
foreach ($match in $borderRadius) {
    $value = $match.Groups[1].Value.Trim()
    if (-not $radiusValues.ContainsKey($value)) {
        $radiusValues[$value] = 1
    } else {
        $radiusValues[$value]++
    }
}

Write-Host "Valores de border-radius:" -ForegroundColor Yellow
$radiusReport = @"

# BORDER RADIUS

"@
foreach ($radius in $radiusValues.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 15) {
    Write-Host "  $($radius.Key): $($radius.Value) vezes" -ForegroundColor Cyan
    $radiusReport += "$($radius.Key) - Usado $($radius.Value) vezes`n"
}

# 6. ANALISAR SOMBRAS
Write-Host ""
Write-Host "=== ANALISANDO SOMBRAS ===" -ForegroundColor Green
$shadows = [regex]::Matches($allCss, "box-shadow:\s*([^;{}]+)")

$shadowValues = @{}
foreach ($match in $shadows) {
    $value = $match.Groups[1].Value.Trim()
    if (-not $shadowValues.ContainsKey($value)) {
        $shadowValues[$value] = 1
    } else {
        $shadowValues[$value]++
    }
}

Write-Host "Valores de sombra:" -ForegroundColor Yellow
$shadowReport = @"

# SOMBRAS (Box Shadow)

"@
foreach ($shadow in $shadowValues.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 10) {
    Write-Host "  $($shadow.Key): $($shadow.Value) vezes" -ForegroundColor Cyan
    $shadowReport += "$($shadow.Key) - Usado $($shadow.Value) vezes`n"
}

# 7. EXTRAIR CLASSES TAILWIND
Write-Host ""
Write-Host "=== ANALISANDO CLASSES TAILWIND ===" -ForegroundColor Green
$tailwindClasses = [regex]::Matches($html, 'class="([^"]*)"')

$classUsage = @{}
foreach ($match in $tailwindClasses) {
    $classes = $match.Groups[1].Value.Split(' ')
    foreach ($class in $classes) {
        if ($class -match '^(tw-|sm:|md:|lg:|xl:|2xl:|hover:|focus:)' -or $class -match '^(text-|bg-|p-|m-|flex|grid|rounded)') {
            if (-not $classUsage.ContainsKey($class)) {
                $classUsage[$class] = 1
            } else {
                $classUsage[$class]++
            }
        }
    }
}

Write-Host "Classes utilitarias mais usadas:" -ForegroundColor Yellow
$tailwindReport = @"

# CLASSES UTILITARIAS (Tailwind)

"@
foreach ($class in $classUsage.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 30) {
    Write-Host "  $($class.Key): $($class.Value) vezes" -ForegroundColor Cyan
    $tailwindReport += "$($class.Key) - Usado $($class.Value) vezes`n"
}

# 8. ANALISAR BREAKPOINTS
Write-Host ""
Write-Host "=== ANALISANDO BREAKPOINTS ===" -ForegroundColor Green
$mediaQueries = [regex]::Matches($allCss, '@media[^{]+')

$breakpoints = @{}
foreach ($match in $mediaQueries) {
    $query = $match.Value.Trim()
    if (-not $breakpoints.ContainsKey($query)) {
        $breakpoints[$query] = 1
    } else {
        $breakpoints[$query]++
    }
}

Write-Host "Media queries encontradas:" -ForegroundColor Yellow
$breakpointReport = @"

# BREAKPOINTS (Media Queries)

"@
foreach ($bp in $breakpoints.GetEnumerator() | Sort-Object -Property Value -Descending) {
    Write-Host "  $($bp.Key): $($bp.Value) vezes" -ForegroundColor Cyan
    $breakpointReport += "$($bp.Key) - Usado $($bp.Value) vezes`n"
}

# SALVAR RELATORIO COMPLETO
Write-Host ""
Write-Host "=== SALVANDO RELATORIO ===" -ForegroundColor Green

$fullReport = @"
# Design System - PilarHomes.com.br
**Analise realizada em:** $(Get-Date -Format "dd/MM/yyyy HH:mm:ss")

$colorReport

$fontReport

$spacingReport

$radiusReport

$shadowReport

$tailwindReport

$breakpointReport

---
*Analise automatica extraida do site pilarhomes.com.br*
"@

$fullReport | Out-File -FilePath "$outputDir\design_tokens_raw.md" -Encoding UTF8

Write-Host "Relatorio salvo em: $outputDir\design_tokens_raw.md" -ForegroundColor Green
Write-Host ""
Write-Host "=== ANALISE COMPLETA ===" -ForegroundColor Magenta
Write-Host "Arquivos salvos em: $outputDir" -ForegroundColor Yellow
