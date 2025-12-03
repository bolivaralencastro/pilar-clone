# ============================================================================
# 🏠 Pilar Homes - Script de Busca Interativo
# ============================================================================
# Uso: .\pilar_search.ps1
# Ou com parâmetros:
#   .\pilar_search.ps1 -PropertyType apartment -MaxPrice 3000000 -Region "Jardim América"
# ============================================================================

param(
    [ValidateSet("sell", "rent")]
    [string]$TransactionType = "sell",
    
    [int]$Page = 1,
    
    [ValidateRange(1, 50)]
    [int]$PerPage = 10,
    
    [ValidateSet("", "apartment", "house", "penthouse", "land", "commercial", "duplex", "studio", "flat")]
    [string]$PropertyType = "",
    
    [int]$MinPrice = 0,
    [int]$MaxPrice = 0,
    [int]$MinArea = 0,
    [int]$MaxArea = 0,
    [int]$Bedrooms = 0,
    [int]$Suites = 0,
    [int]$ParkingSpots = 0,
    
    [string]$City = "",
    [string]$Region = "",
    
    [switch]$ExclusiveOnly,
    [switch]$ExportJson,
    [switch]$ExportCsv,
    [switch]$ShowStats
)

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================

$API_BASE = "https://pilarhomes.com.br/api"
$HEADERS = @{
    "Accept" = "application/json"
    "Accept-Language" = "pt-BR,pt;q=0.9"
    "Referer" = "https://pilarhomes.com.br/"
    "Origin" = "https://pilarhomes.com.br"
}

# ============================================================================
# FUNÇÕES
# ============================================================================

function Format-Price {
    param([decimal]$Value)
    if ($Value -eq 0 -or $null -eq $Value) { return "Sob consulta" }
    return "R$ {0:N0}" -f $Value
}

function Get-Properties {
    param([hashtable]$Params)
    
    $queryParts = @()
    foreach ($key in $Params.Keys) {
        if ($null -ne $Params[$key] -and $Params[$key] -ne "" -and $Params[$key] -ne 0) {
            $value = [System.Web.HttpUtility]::UrlEncode($Params[$key].ToString())
            $queryParts += "$key=$value"
        }
    }
    
    $url = "$API_BASE/properties?" + ($queryParts -join "&")
    
    try {
        $response = Invoke-RestMethod -Uri $url -Method GET -Headers $HEADERS
        return $response
    }
    catch {
        Write-Host "❌ Erro ao acessar API: $_" -ForegroundColor Red
        return $null
    }
}

function Show-PropertyCard {
    param($Property)
    
    $price = if ($Property.askingPrice) { $Property.askingPrice } else { $Property.rentPrice }
    $priceType = if ($Property.rentPrice -and -not $Property.askingPrice) { "/mes" } else { "" }
    
    Write-Host "----------------------------------------------------" -ForegroundColor DarkGray
    
    # Localizacao
    $location = "$($Property.region), $($Property.city)"
    Write-Host "[LOCAL] $location" -ForegroundColor Yellow
    
    # Tipo e area
    $type = $Property.propertyType.name
    $areaText = "$($Property.area) m2"
    Write-Host "   [TIPO] $type | $areaText" -ForegroundColor White
    
    # Preco
    $formattedPrice = Format-Price $price
    if ($Property.isExclusive) {
        Write-Host "   [PRECO] $formattedPrice$priceType * EXCLUSIVO *" -ForegroundColor Green
    } else {
        Write-Host "   [PRECO] $formattedPrice$priceType" -ForegroundColor Green
    }
    
    # Caracteristicas
    $features = @()
    if ($Property.bedrooms) { $features += "$($Property.bedrooms) quartos" }
    if ($Property.suites) { $features += "$($Property.suites) suites" }
    if ($Property.bathrooms) { $features += "$($Property.bathrooms) banheiros" }
    if ($Property.parkingSpots) { $features += "$($Property.parkingSpots) vagas" }
    Write-Host "   [INFO] $($features -join ' | ')" -ForegroundColor Cyan
    
    # Condominio
    if ($Property.condoFee -and $Property.condoFee -gt 0) {
        Write-Host "   [COND] $(Format-Price $Property.condoFee)" -ForegroundColor DarkGray
    }
    
    # Link
    Write-Host "   [LINK] https://pilarhomes.com.br/imovel/$($Property.slug)" -ForegroundColor Blue
    
    # Codigo
    Write-Host "   [COD] #$($Property.commercialId) | $($Property.company.name)" -ForegroundColor DarkGray
}

function Export-ToJson {
    param($Properties, $Filename)
    
    $data = @()
    foreach ($p in $Properties) {
        $data += @{
            id = $p.id
            codigo = $p.commercialId
            tipo = $p.propertyType.name
            bairro = $p.region
            cidade = $p.city
            preco = $p.askingPrice
            aluguel = $p.rentPrice
            area = $p.area
            quartos = $p.bedrooms
            suites = $p.suites
            vagas = $p.parkingSpots
            condominio = $p.condoFee
            exclusivo = $p.isExclusive
            url = "https://pilarhomes.com.br/imovel/$($p.slug)"
            imobiliaria = $p.company.name
        }
    }
    
    $data | ConvertTo-Json -Depth 5 | Out-File -FilePath $Filename -Encoding UTF8
    Write-Host "`n✅ Exportado para $Filename" -ForegroundColor Green
}

function Export-ToCsv {
    param($Properties, $Filename)
    
    $data = @()
    foreach ($p in $Properties) {
        $data += [PSCustomObject]@{
            Codigo = $p.commercialId
            Tipo = $p.propertyType.name
            Bairro = $p.region
            Cidade = $p.city
            Preco = $p.askingPrice
            Aluguel = $p.rentPrice
            AreaM2 = $p.area
            Quartos = $p.bedrooms
            Suites = $p.suites
            Vagas = $p.parkingSpots
            Condominio = $p.condoFee
            Exclusivo = $p.isExclusive
            URL = "https://pilarhomes.com.br/imovel/$($p.slug)"
            Imobiliaria = $p.company.name
        }
    }
    
    $data | Export-Csv -Path $Filename -NoTypeInformation -Encoding UTF8
    Write-Host "`n✅ Exportado para $Filename" -ForegroundColor Green
}

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

Write-Host ""
Write-Host "===========================================================" -ForegroundColor Magenta
Write-Host "  PILAR HOMES - BUSCA DE IMOVEIS" -ForegroundColor White
Write-Host "===========================================================" -ForegroundColor Magenta

# Montar parâmetros
$params = @{
    transactionType = $TransactionType
    page = $Page
    perPage = $PerPage
}

if ($PropertyType) { $params.propertyType = $PropertyType }
if ($MinPrice -gt 0) { $params.minPrice = $MinPrice }
if ($MaxPrice -gt 0) { $params.maxPrice = $MaxPrice }
if ($MinArea -gt 0) { $params.minArea = $MinArea }
if ($MaxArea -gt 0) { $params.maxArea = $MaxArea }
if ($Bedrooms -gt 0) { $params.bedrooms = $Bedrooms }
if ($Suites -gt 0) { $params.suites = $Suites }
if ($ParkingSpots -gt 0) { $params.parkingSpots = $ParkingSpots }
if ($City) { $params.city = $City }
if ($Region) { $params.region = $Region }
if ($ExclusiveOnly) { $params.isExclusive = $true }

# Mostrar filtros aplicados
Write-Host ""
Write-Host "[FILTROS]" -ForegroundColor Cyan
$transactionLabel = if ($TransactionType -eq "sell") { "Venda" } else { "Aluguel" }
Write-Host "   Tipo: $transactionLabel" -ForegroundColor Gray

if ($PropertyType) { Write-Host "   Imovel: $PropertyType" -ForegroundColor Gray }
if ($MinPrice -gt 0) { Write-Host "   Preco min: $(Format-Price $MinPrice)" -ForegroundColor Gray }
if ($MaxPrice -gt 0) { Write-Host "   Preco max: $(Format-Price $MaxPrice)" -ForegroundColor Gray }
if ($City) { Write-Host "   Cidade: $City" -ForegroundColor Gray }
if ($Region) { Write-Host "   Bairro: $Region" -ForegroundColor Gray }
if ($Bedrooms -gt 0) { Write-Host "   Quartos: $Bedrooms+" -ForegroundColor Gray }

Write-Host ""
Write-Host "Buscando..." -ForegroundColor Yellow

# Fazer busca
$result = Get-Properties -Params $params

if ($null -eq $result) {
    Write-Host "Falha na busca. Verifique sua conexão." -ForegroundColor Red
    exit 1
}

# Acessar propriedades (API retorna 'properties' ou 'data')
$properties = if ($result.properties) { $result.properties } else { $result.data }
$pagination = $result.pagination

# Mostrar estatisticas
Write-Host ""
Write-Host "[RESULTADOS]" -ForegroundColor Green
Write-Host "   Total encontrado: $($pagination.filteredCount.ToString('N0')) imoveis" -ForegroundColor White
Write-Host "   Pagina: $($pagination.page) de $($pagination.totalPages)" -ForegroundColor Gray
Write-Host "   Exibindo: $($properties.Count) imoveis" -ForegroundColor Gray

# Mostrar cards
foreach ($prop in $properties) {
    Show-PropertyCard -Property $prop
}

Write-Host "----------------------------------------------------" -ForegroundColor DarkGray

# Exportar se solicitado
if ($ExportJson) {
    $filename = "pilar_export_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"
    Export-ToJson -Properties $properties -Filename $filename
}

if ($ExportCsv) {
    $filename = "pilar_export_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
    Export-ToCsv -Properties $properties -Filename $filename
}

# Estatisticas extras
if ($ShowStats) {
    Write-Host ""
    Write-Host "[ESTATISTICAS]" -ForegroundColor Magenta
    Write-Host "----------------------------------------------------" -ForegroundColor DarkGray
    
    $prices = $properties | Where-Object { $_.askingPrice -gt 0 } | Select-Object -ExpandProperty askingPrice
    if ($prices.Count -gt 0) {
        $avgPrice = ($prices | Measure-Object -Average).Average
        $minPriceFound = ($prices | Measure-Object -Minimum).Minimum
        $maxPriceFound = ($prices | Measure-Object -Maximum).Maximum
        
        Write-Host "   Preco medio:   $(Format-Price $avgPrice)" -ForegroundColor Cyan
        Write-Host "   Menor preco:   $(Format-Price $minPriceFound)" -ForegroundColor Green
        Write-Host "   Maior preco:   $(Format-Price $maxPriceFound)" -ForegroundColor Yellow
    }
    
    $areas = $properties | Where-Object { $_.area -gt 0 } | Select-Object -ExpandProperty area
    if ($areas.Count -gt 0) {
        $avgArea = ($areas | Measure-Object -Average).Average
        Write-Host "   Area media:    $([math]::Round($avgArea, 0)) m2" -ForegroundColor Cyan
    }
    
    # Bairros
    $regions = $properties | Group-Object -Property region | Sort-Object Count -Descending | Select-Object -First 5
    Write-Host ""
    Write-Host "   Top Bairros:" -ForegroundColor White
    foreach ($r in $regions) {
        Write-Host "     - $($r.Name): $($r.Count) imoveis" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "Busca concluida!" -ForegroundColor Green
Write-Host ""
