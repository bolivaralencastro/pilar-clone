# Script para extrair API calls, CSS e montar tokens do PilarHomes
# Data: 3 de Dezembro de 2025

Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  EXTRAÇÃO DE API, CSS E DESIGN TOKENS - PILARHOMES" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Diretórios de output
$outputDir = "c:\Users\boliv\Documents\Pilar\extracted"
$apiDir = "$outputDir\api"
$cssDir = "$outputDir\css"
$tokensDir = "$outputDir\tokens"

# Criar diretórios se não existirem
@($outputDir, $apiDir, $cssDir, $tokensDir) | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Path $_ -Force | Out-Null
        Write-Host "✓ Criado: $_" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "PASSO 1: Aguardando navegação para pilarhomes.com.br..." -ForegroundColor Yellow
Write-Host "         (As ferramentas Chrome DevTools farão isso automaticamente)" -ForegroundColor Gray
Write-Host ""

# Nota: A navegação será feita via Chrome DevTools MCP tools
# Este script documenta o processo e organiza os outputs

Write-Host "PASSO 2: Preparando para captura de Network Requests..." -ForegroundColor Yellow
Write-Host "         - Filtro: api.pilarhomes.com.br" -ForegroundColor Gray
Write-Host "         - Output: $apiDir\network-requests.json" -ForegroundColor Gray
Write-Host ""

Write-Host "PASSO 3: Preparando para extração de CSS..." -ForegroundColor Yellow
Write-Host "         - Target: CSS principal da aplicação" -ForegroundColor Gray
Write-Host "         - Output: $cssDir\main.css" -ForegroundColor Gray
Write-Host ""

Write-Host "PASSO 4: Estrutura de arquivos que será gerada:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  extracted/" -ForegroundColor Cyan
Write-Host "  ├── api/" -ForegroundColor Cyan
Write-Host "  │   ├── network-requests.json    (dump completo Network tab)" -ForegroundColor Gray
Write-Host "  │   ├── endpoints-map.json       (mapa de endpoints principais)" -ForegroundColor Gray
Write-Host "  │   └── har-export.har           (HAR file completo)" -ForegroundColor Gray
Write-Host "  ├── css/" -ForegroundColor Cyan
Write-Host "  │   ├── main.css                 (CSS principal extraído)" -ForegroundColor Gray
Write-Host "  │   └── variables.css            (CSS variables isoladas)" -ForegroundColor Gray
Write-Host "  └── tokens/" -ForegroundColor Cyan
Write-Host "      ├── design-tokens.json       (cores, fonts, spacing)" -ForegroundColor Gray
Write-Host "      ├── design-tokens.css        (CSS variables)" -ForegroundColor Gray
Write-Host "      └── design-tokens.js         (JavaScript/TypeScript)" -ForegroundColor Gray
Write-Host ""

Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  AGUARDANDO EXECUÇÃO DAS FERRAMENTAS CHROME DEVTOOLS" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Este script prepara a estrutura. Os próximos passos usarão:" -ForegroundColor Yellow
Write-Host "  1. mcp_chrome-devtoo_navigate_page" -ForegroundColor Gray
Write-Host "  2. mcp_chrome-devtoo_list_network_requests" -ForegroundColor Gray
Write-Host "  3. mcp_chrome-devtoo_get_network_request" -ForegroundColor Gray
Write-Host "  4. mcp_chrome-devtoo_evaluate_script (para CSS)" -ForegroundColor Gray
Write-Host ""
