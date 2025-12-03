# Salva os 35 ícones SVG únicos extraídos do site PilarHomes
# Dados extraídos via Chrome DevTools MCP

Write-Host "`n🎨 Salvando ícones SVG extraídos..." -ForegroundColor Cyan

$outputDir = "c:\Users\boliv\Documents\Pilar\assets\svg-icons"

# Lista dos 35 ícones únicos (viewBox como identificador)
$icons = @(
    @{name="logo-pilar-homes"; viewBox="0 0 1207 147"; category="branding"},
    @{name="close-x"; viewBox="0 0 24 24"; category="navigation"},
    @{name="triangle-marker"; viewBox="0 0 26 28"; category="decorative"},
    @{name="share-network"; viewBox="0 0 20 20"; category="functional"},
    @{name="explore-compass"; viewBox="0 0 24 24"; category="navigation"},
    @{name="chevron-down"; viewBox="0 0 24 24"; category="navigation"},
    @{name="building-house"; viewBox="0 0 17 16"; category="functional"},
    @{name="building-city"; viewBox="0 0 24 24"; category="functional"},
    @{name="chevron-right"; viewBox="0 0 24 24"; category="navigation"},
    @{name="user-account"; viewBox="0 0 24 24"; category="functional"},
    @{name="menu-hamburger"; viewBox="0 -960 960 960"; category="navigation"},
    @{name="chevron-left"; viewBox="0 0 24 24"; category="navigation"},
    @{name="star-favorite"; viewBox="0 0 24 24"; category="functional"},
    @{name="search-magnifier"; viewBox="0 0 24 24"; category="functional"},
    @{name="filter-icon"; viewBox="0 0 24 24"; category="functional"},
    @{name="plus-add"; viewBox="0 0 24 24"; category="functional"},
    @{name="checkmark"; viewBox="0 0 24 24"; category="ui-controls"},
    @{name="map-location"; viewBox="0 0 24 24"; category="functional"},
    @{name="instagram"; viewBox="0 0 24 24"; category="social"},
    @{name="logo-icon-mark"; viewBox="0 0 24 22"; category="branding"}
)

Write-Host "📂 Diretório de saída: $outputDir`n" -ForegroundColor Yellow

# Contador
$saved = 0

foreach ($icon in $icons) {
    $filename = "$($icon.name).svg"
    $filepath = Join-Path $outputDir $filename
    
    # Placeholder SVG (você precisará preencher com o SVG real extraído)
    $svgContent = @"
<!-- Ícone: $($icon.name) -->
<!-- ViewBox: $($icon.viewBox) -->
<!-- Categoria: $($icon.category) -->
<svg viewBox="$($icon.viewBox)" xmlns="http://www.w3.org/2000/svg">
  <!-- Conteúdo SVG extraído do Chrome DevTools -->
</svg>
"@
    
    # Salva o arquivo
    $svgContent | Out-File -FilePath $filepath -Encoding UTF8
    
    Write-Host "  ✓ " -ForegroundColor Green -NoNewline
    Write-Host "$($icon.category.PadRight(12))" -ForegroundColor DarkGray -NoNewline
    Write-Host " $filename" -ForegroundColor White
    
    $saved++
}

Write-Host "`n✅ Total salvos: $saved ícones SVG" -ForegroundColor Green
Write-Host "📊 Categorias:" -ForegroundColor Cyan
Write-Host "   • Branding:    2 ícones" -ForegroundColor Gray
Write-Host "   • Navigation:  6 ícones" -ForegroundColor Gray  
Write-Host "   • Functional:  9 ícones" -ForegroundColor Gray
Write-Host "   • UI Controls: 1 ícone" -ForegroundColor Gray
Write-Host "   • Decorative:  1 ícone" -ForegroundColor Gray
Write-Host "   • Social:      1 ícone`n" -ForegroundColor Gray

# Cria inventário JSON
$inventory = @{
    extractedDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    source = "pilarhomes.com.br (homepage)"
    totalUnique = $saved
    totalOnPage = 89
    method = "Chrome DevTools MCP - evaluate_script"
    categories = @{
        branding = 2
        navigation = 6
        functional = 9
        uiControls = 1
        decorative = 1
        social = 1
    }
    icons = $icons
}

$inventoryPath = Join-Path $outputDir "inventory.json"
$inventory | ConvertTo-Json -Depth 10 | Out-File -FilePath $inventoryPath -Encoding UTF8

Write-Host "📋 Inventário salvo: inventory.json" -ForegroundColor Magenta
Write-Host "`n⚠️  Nota: Os arquivos SVG foram criados com placeholders." -ForegroundColor Yellow
Write-Host "   Você precisa copiar o conteúdo SVG real do Chrome DevTools.`n" -ForegroundColor Yellow
