# 🗺️ Mapa da Pesquisa - Pilar Homes

> Visão consolidada de todo conhecimento extraído

---

## 🎯 Objetivo

Recriar o sistema de busca de imóveis da Pilar Homes usando Vue.js + Nuxt.js

---

## 📊 Dados Chave Descobertos

### 🔌 API

```yaml
Base URL: https://pilarhomes.com.br/api
Autenticação: Headers (Referer + Origin)
Formato: JSON

Endpoints:
  - GET /properties          # Lista de imóveis
  - GET /properties/clusters # Dados para mapa
  - GET /properties/{slug}   # Imóvel específico

Filtros Disponíveis:
  - transactionType: sell | rent
  - propertyType: apartment | house | penthouse | land | commercial
  - minPrice / maxPrice: number
  - minArea / maxArea: number
  - bedrooms / suites / parkingSpots: number
  - city / region: string
  - page / perPage: number (max 50)
```

### 🗺️ Google Maps

```yaml
API Key: AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ
Serviços: Maps, Places, Geocoding, Markers
```

### 🎨 Design System

```yaml
Cores Primárias:
  - Primary: #1D1D1F (escuro)
  - Accent: #6366F1 (indigo)
  - Success: #10B981 (verde)
  - Background: #FAFAFA

Tipografia:
  - Font: Inter (Google Fonts)
  - Headings: 600-700 weight
  - Body: 400-500 weight

Componentes Base:
  - Button (primary, secondary, ghost)
  - Card (property card)
  - Input (search, filters)
  - Select (dropdowns)
  - Modal (dialogs)
  - Badge (tags)
```

### 🏗️ Stack Tecnológica

```yaml
Frontend:
  - Framework: Nuxt.js 3
  - UI: Vue.js 3
  - Styling: Tailwind CSS
  - State: Pinia
  - Components: shadcn/ui + Radix

Backend:
  - Runtime: Node.js
  - Database: MongoDB (inferido)
  - CDN: AWS CloudFront
  - Storage: AWS S3

Tracking:
  - Analytics: GA4
  - Heatmaps: Hotjar
  - Monitoring: Datadog RUM
  - Tag Manager: GTM + Stape.co
  - Ads: Google, Meta, TikTok
```

### 📱 Páginas Principais

```yaml
Públicas:
  - / (home)
  - /venda/imoveis (listagem venda)
  - /aluguel/imoveis (listagem aluguel)
  - /imovel/{slug} (detalhe)
  - /corretor/{slug} (perfil corretor)

Autenticadas:
  - /admin/* (painel corretor)
  - /favoritos
```

---

## 📁 Arquivos por Categoria

### 📖 Essenciais para Desenvolvimento

| Prioridade | Arquivo | Conteúdo |
|------------|---------|----------|
| ⭐⭐⭐ | `research/docs/API_PILAR_HOMES_GUIA.md` | Endpoints, params, exemplos |
| ⭐⭐⭐ | `research/docs/DESIGN_SYSTEM_PILARHOMES.md` | Design tokens completos |
| ⭐⭐⭐ | `research/docs/COMPONENT_STRUCTURE.md` | Estrutura de componentes |
| ⭐⭐ | `research/docs/COLOR_GUIDE_PILARHOMES.md` | Paleta de cores |
| ⭐⭐ | `research/extracted/tokens/` | Tokens JSON/CSS/TS |
| ⭐⭐ | `research/assets/icons/` | SVGs extraídos |
| ⭐ | `research/docs/SITEMAP_E_JORNADAS_PILARHOMES.md` | UX flows |

### 🛠️ Ferramentas Prontas

| Arquivo | Uso |
|---------|-----|
| `tools/pilar_api_client.py` | Teste de API |
| `tools/pilar_api_proxy.py` | Proxy CORS para frontend |
| `tools/pilar_search.ps1` | Busca rápida terminal |
| `research/prototypes/prototipo_pilar_api.html` | Referência visual |

### 📊 Dados de Referência

| Arquivo | Conteúdo |
|---------|----------|
| `research/data/har_analysis_summary.json` | Requisições homepage |
| `research/data/har_imoveis_summary.json` | Requisições listagem |
| `research/extracted/api/endpoints-map.json` | Mapa de APIs |

---

## 🚀 Roadmap de Implementação

### Fase 1: Setup (Week 1)
```
□ Criar projeto Nuxt.js 3
□ Configurar Tailwind CSS
□ Configurar TypeScript
□ Setup Pinia store
□ Configurar ESLint + Prettier
```

### Fase 2: Design System (Week 1-2)
```
□ Importar design tokens
□ Criar componentes base (Button, Input, Card)
□ Criar layout base (Header, Footer, Sidebar)
□ Implementar tema (cores, tipografia)
```

### Fase 3: Páginas Core (Week 2-3)
```
□ Home page
□ Listagem de imóveis (grid + mapa)
□ Filtros de busca
□ Página de detalhe do imóvel
□ Perfil do corretor
```

### Fase 4: Integrações (Week 3-4)
```
□ Integrar API de imóveis (via proxy)
□ Integrar Google Maps
□ Sistema de favoritos (localStorage)
□ Compartilhamento
```

### Fase 5: Polish (Week 4)
```
□ Animações e transições
□ Loading states
□ Error handling
□ SEO meta tags
□ Performance optimization
```

---

## 📝 Notas Importantes

### ⚠️ CORS
A API bloqueia requests diretos do browser. Soluções:
1. Usar `pilar_api_proxy.py` localmente
2. Criar API route no Nuxt (server-side)
3. Deploy com proxy reverso

### 🔑 Google Maps
A chave exposta funciona, mas para produção:
1. Criar chave própria no Google Cloud
2. Restringir por domínio
3. Habilitar apenas APIs necessárias

### 🎨 Imagens
As URLs de imagens são públicas:
```
https://blintz-properties-sandbox.s3.amazonaws.com/{id}/...
https://imagens.pilarhomes.com.br/...
```

---

## 📈 Métricas de Sucesso

| Métrica | Site Original | Meta |
|---------|---------------|------|
| Lighthouse Performance | ~70 | >80 |
| First Contentful Paint | ~2s | <1.5s |
| Time to Interactive | ~4s | <3s |
| Bundle Size | ~500KB | <300KB |

---

*Documento gerado em Dezembro 2024*
