# Script para extrair variaveis CSS e componentes

Write-Host "Analisando variaveis CSS e componentes..." -ForegroundColor Cyan

$url = "https://pilarhomes.com.br/"
$response = Invoke-WebRequest -Uri $url -UseBasicParsing
$html = $response.Content

# Extrair CSS inline e variaveis
Write-Host "=== EXTRAINDO VARIAVEIS CSS ===" -ForegroundColor Green

# Procurar por :root e variaveis CSS
$rootVars = [regex]::Matches($html, '--[a-zA-Z0-9-]+:\s*[^;]+')
$cssVars = @{}

foreach ($match in $rootVars) {
    $varDef = $match.Value
    if ($varDef -match '--([a-zA-Z0-9-]+):\s*(.+)') {
        $varName = $matches[1]
        $varValue = $matches[2].Trim()
        if (-not $cssVars.ContainsKey($varName)) {
            $cssVars[$varName] = $varValue
        }
    }
}

Write-Host "Variaveis CSS encontradas:" -ForegroundColor Yellow
foreach ($var in $cssVars.GetEnumerator() | Sort-Object -Property Key) {
    Write-Host "  --$($var.Key): $($var.Value)" -ForegroundColor Cyan
}

# Extrair estrutura de componentes
Write-Host ""
Write-Host "=== ANALISANDO ESTRUTURA DE COMPONENTES ===" -ForegroundColor Green

$components = @{
    'Buttons' = [regex]::Matches($html, '<button[^>]*class="([^"]+)"').Count
    'Links' = [regex]::Matches($html, '<a[^>]*class="([^"]+)"').Count
    'Images' = [regex]::Matches($html, '<img[^>]*').Count
    'Forms' = [regex]::Matches($html, '<form[^>]*').Count
    'Inputs' = [regex]::Matches($html, '<input[^>]*').Count
    'Divs com classes' = [regex]::Matches($html, '<div[^>]*class="([^"]+)"').Count
    'Sections' = [regex]::Matches($html, '<section[^>]*').Count
    'Articles' = [regex]::Matches($html, '<article[^>]*').Count
    'Headers' = [regex]::Matches($html, '<header[^>]*').Count
    'Footers' = [regex]::Matches($html, '<footer[^>]*').Count
    'Nav' = [regex]::Matches($html, '<nav[^>]*').Count
}

Write-Host "Elementos HTML encontrados:" -ForegroundColor Yellow
foreach ($comp in $components.GetEnumerator() | Sort-Object -Property Value -Descending) {
    Write-Host "  $($comp.Key): $($comp.Value)" -ForegroundColor Cyan
}

# Extrair atributos data-v (componentes Vue)
Write-Host ""
Write-Host "=== COMPONENTES VUE IDENTIFICADOS ===" -ForegroundColor Green
$vueComponents = [regex]::Matches($html, 'data-v-[a-f0-9]+')
$uniqueVueComps = @{}

foreach ($match in $vueComponents) {
    $comp = $match.Value
    if (-not $uniqueVueComps.ContainsKey($comp)) {
        $uniqueVueComps[$comp] = 1
    } else {
        $uniqueVueComps[$comp]++
    }
}

Write-Host "Componentes Vue escopados:" -ForegroundColor Yellow
foreach ($comp in $uniqueVueComps.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 20) {
    Write-Host "  $($comp.Key): $($comp.Value) instancias" -ForegroundColor Cyan
}

# Extrair icones SVG
Write-Host ""
Write-Host "=== ANALISANDO ICONES ===" -ForegroundColor Green
$svgIcons = [regex]::Matches($html, '<svg[^>]*>(.*?)</svg>')
Write-Host "Total de icones SVG encontrados: $($svgIcons.Count)" -ForegroundColor Yellow

# Analisar viewBox dos SVGs para identificar tamanhos padroes
$viewBoxes = [regex]::Matches($html, 'viewBox="([^"]+)"')
$iconSizes = @{}
foreach ($match in $viewBoxes) {
    $size = $match.Groups[1].Value
    if (-not $iconSizes.ContainsKey($size)) {
        $iconSizes[$size] = 1
    } else {
        $iconSizes[$size]++
    }
}

Write-Host "ViewBox patterns (tamanhos de icones):" -ForegroundColor Yellow
foreach ($size in $iconSizes.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 10) {
    Write-Host "  $($size.Key): $($size.Value) vezes" -ForegroundColor Cyan
}

# Salvar relatorio
$outputDir = "c:\Users\boliv\Documents\Pilar\design_system_analysis"
$componentReport = @"
# ANALISE DE COMPONENTES E VARIAVEIS

## Variaveis CSS Custom Properties
$(($cssVars.GetEnumerator() | Sort-Object -Property Key | ForEach-Object { "--$($_.Key): $($_.Value)" }) -join "`n")

## Contagem de Elementos HTML
$(($components.GetEnumerator() | Sort-Object -Property Value -Descending | ForEach-Object { "$($_.Key): $($_.Value)" }) -join "`n")

## Componentes Vue Identificados
$(($uniqueVueComps.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 20 | ForEach-Object { "$($_.Key): $($_.Value) instancias" }) -join "`n")

## Icones SVG
Total: $($svgIcons.Count) icones

### Tamanhos de ViewBox
$(($iconSizes.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 10 | ForEach-Object { "$($_.Key): $($_.Value) vezes" }) -join "`n")
"@

$componentReport | Out-File -FilePath "$outputDir\components_analysis.md" -Encoding UTF8
Write-Host ""
Write-Host "Relatorio de componentes salvo!" -ForegroundColor Green
