# Script para analisar a stack tecnológica do site pilarhomes.com.br

Write-Host "Analisando a stack tecnológica de pilarhomes.com.br..." -ForegroundColor Cyan
Write-Host ""

# Fazer requisição HTTP e capturar headers e conteúdo
$url = "https://pilarhomes.com.br/"
$response = Invoke-WebRequest -Uri $url -UseBasicParsing

Write-Host "=== ANALISE DE HEADERS ===" -ForegroundColor Green
$response.Headers.GetEnumerator() | ForEach-Object {
    Write-Host "$($_.Key): $($_.Value)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== ANALISE DO HTML ===" -ForegroundColor Green

$html = $response.Content

# Detectar Next.js
if ($html -match '__NEXT_DATA__|_next/static|__next|next\.js') {
    Write-Host "[OK] Next.js detectado" -ForegroundColor Green
}

# Detectar React
if ($html -match 'react|React') {
    Write-Host "[OK] React detectado" -ForegroundColor Green
}

# Detectar frameworks CSS
if ($html -match 'tailwind|tw-') {
    Write-Host "[OK] Tailwind CSS detectado" -ForegroundColor Green
}

if ($html -match 'bootstrap') {
    Write-Host "[OK] Bootstrap detectado" -ForegroundColor Green
}

# Detectar bibliotecas de analytics
if ($html -match 'google-analytics|gtag|ga\.js') {
    Write-Host "[OK] Google Analytics detectado" -ForegroundColor Green
}

if ($html -match 'gtm\.js|googletagmanager') {
    Write-Host "[OK] Google Tag Manager detectado" -ForegroundColor Green
}

# Detectar outras bibliotecas comuns
if ($html -match 'webpack') {
    Write-Host "[OK] Webpack detectado" -ForegroundColor Green
}

if ($html -match 'vercel') {
    Write-Host "[OK] Hospedado na Vercel" -ForegroundColor Green
}

# Extrair scripts e links
Write-Host ""
Write-Host "=== SCRIPTS PRINCIPAIS ===" -ForegroundColor Green
$scripts = [regex]::Matches($html, '<script[^>]*src="([^"]+)"')
$scripts | Select-Object -First 10 | ForEach-Object {
    Write-Host $_.Groups[1].Value -ForegroundColor Cyan
}

Write-Host ""
Write-Host "=== STYLESHEETS ===" -ForegroundColor Green
$styles = [regex]::Matches($html, '<link[^>]*href="([^"]+\.css[^"]*)"')
$styles | Select-Object -First 10 | ForEach-Object {
    Write-Host $_.Groups[1].Value -ForegroundColor Cyan
}

Write-Host ""
Write-Host "=== META TAGS IMPORTANTES ===" -ForegroundColor Green
$metas = [regex]::Matches($html, '<meta[^>]*>')
$metas | Where-Object { $_.Value -match 'generator|framework|viewport|og:' } | Select-Object -First 10 | ForEach-Object {
    Write-Host $_.Value -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== ANALISE COMPLETA ===" -ForegroundColor Magenta
Write-Host "Procurando por __NEXT_DATA__ (dados do Next.js)..." -ForegroundColor White

if ($html -match '__NEXT_DATA__') {
    $nextDataMatch = [regex]::Match($html, '__NEXT_DATA__[^<]*')
    if ($nextDataMatch.Success) {
        Write-Host "[OK] Aplicacao Next.js confirmada!" -ForegroundColor Green
        Write-Host "Preview dos dados:" -ForegroundColor Yellow
        Write-Host $nextDataMatch.Value.Substring(0, [Math]::Min(500, $nextDataMatch.Value.Length))
    }
}
