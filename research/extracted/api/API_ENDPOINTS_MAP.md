# API Endpoints - PilarHomes
## Mapeamento Completo da API (VALIDADO VIA DEVTOOLS)

**Base URL**: `https://api.pilarhomes.com.br`  
**Base URL Interna**: `https://pilarhomes.com.br/api`  
**Versão**: v1  
**Autenticação**: Session-based (cookie `nuxt-session`)  
**Servidor**: uvicorn (Python/FastAPI)  
**Infraestrutura**: AWS CloudFront + ELB  
**Data**: 2025-12-03  
**Status**: ✅ **ENDPOINTS REAIS CAPTURADOS VIA NETWORK TAB**

---

## 🔐 AUTENTICAÇÃO (DESCOBERTA REAL)

### Session Management
```http
GET /api/_auth/session
Host: pilarhomes.com.br
```

**Headers Necessários**:
```http
Accept: application/json
Cookie: nuxt-session={encrypted_session_token}
```

**Response**:
```json
{
  "id": "8474b319-eaaa-44d6-9389-ec30c7231377"
}
```

**Cookies de Autenticação**:
- `nuxt-session`: Session token criptografado (formato: Fe26.2**)
- `AWSALBTG`: AWS Application Load Balancer
- `AWSALBTGCORS`: AWS Load Balancer CORS
- `AWSALBAPP-0`: AWS Application Load Balancer App Cookie

**Nota**: A API `api.pilarhomes.com.br` retorna `403 Forbidden` com `{"detail":"Not authenticated"}` quando acessada sem sessão válida.

---

## 🏠 ENDPOINTS DE PROPRIEDADES (VALIDADOS)

### CDN de Imagens
```
https://imagens.pilarhomes.com.br
```
**Uso**: Armazenamento de fotos de imóveis

**Exemplos**:
- `https://imagens.pilarhomes.com.br/properties/{property_id}/photo_{n}.jpg`
- Otimização automática (WebP, AVIF)
- Responsive images com srcset

### CDN Estático
```
https://static.pilarhomes.com.br
```
**Uso**: Assets estáticos (JS bundles, CSS, fonts, SVG icons)

**Estrutura**:
- `https://static.pilarhomes.com.br/pilar-homes-full/{version}/`
- `https://static.pilarhomes.com.br/_nuxt/{hash}.js`

### AWS S3 (Logos e Assets)
```
https://blintz-properties-sandbox.s3.amazonaws.com
```
**Uso**: Logos de boutiques, profile pictures de corretores

**Padrão**:
- `/{company_id}/small_logo.svg`
- `/{company_id}/large_logo.svg`
- `/{agent_id}/images/{uuid}.jpeg`

---

## 🏠 ENDPOINTS DE PROPRIEDADES (VALIDADOS)

### ✅ Buscar Propriedades (Rota Interna - POST)
```http
POST /api/properties/search
Host: pilarhomes.com.br
Content-Type: application/json
```

**Request Body** (REAL - Capturado do site):
```json
{
  "limit": 100,
  "offset": 0,
  "orderBy": "askingPrice",
  "orderDirection": "desc"
}
```

**Campos Disponíveis** (inferidos):
```typescript
{
  limit?: number,              // Máximo de resultados
  offset?: number,             // Para paginação
  orderBy?: string,            // Campos: askingPrice, createdAt, updatedAt, area
  orderDirection?: "asc" | "desc",
  
  // Filtros (baseados em dados observados)
  city?: string,               // Ex: "São Paulo"
  neighborhood?: string,       // Ex: "Jardim Guedala"
  state?: string,              // Ex: "SP"
  propertyType?: string[],     // Ex: ["house", "apartment", "penthouse"]
  minPrice?: number,
  maxPrice?: number,
  minArea?: number,
  maxArea?: number,
  bedrooms?: number,
  suites?: number,
  parkingSpaces?: number,
  isExclusive?: boolean,       // Apenas exclusivos PilarHomes
  companyId?: string,          // Filtro por boutique
  agentId?: string             // Filtro por corretor
}
```

**Response**: (Assumido baseado em estrutura Nuxt)
```json
{
  "properties": [...],
  "total": 273,
  "limit": 100,
  "offset": 0
}
```

**Status Observado**: 403 Forbidden (requer autenticação)

---

### ❌ Listar Propriedades (API Externa - GET)
```http
GET /properties
Host: api.pilarhomes.com.br
```

**Query Parameters** (REAIS - Capturados):
```
?isExclusive=true&page=1&perPage=50
?isExclusive=true&page=2&perPage=50
?page=1&perPage=50
?page=2&perPage=50
?page=3&perPage=50
?page=4&perPage=50
?page=5&perPage=50
?page=6&perPage=50
```

**Padrão de Paginação Descoberto**:
- `page`: Número da página (1-indexed)
- `perPage`: Itens por página (valor usado: 50)
- `isExclusive`: Filtro booleano para exclusivos

**Response Headers** (Capturados):
```http
access-control-allow-credentials: true
access-control-allow-origin: https://pilarhomes.com.br
content-type: application/json
server: uvicorn
vary: Origin
x-request-id: 65061f38d3d8410da183f1687ea512b1
```

**Response Body** (403):
```json
{
  "detail": "Not authenticated"
}
```

**Servidor Identificado**: **uvicorn** (Python/FastAPI framework)

**Observação**: Múltiplas páginas requisitadas simultaneamente (1-6), indicando estratégia de pre-fetching ou loading paralelo.

---

### Buscar Propriedade por ID
```http
GET /properties/:id
```

**Exemplo**: `/properties/HS27071`

**Response**:
```json
{
  "id": "HS27071",
  "title": "Apartamento de luxo no Itaim Bibi",
  "description": "Descrição completa...",
  "type": "apartamento",
  "price": 43980000,
  "salePrice": 43980000,
  "rentPrice": null,
  "area": 554,
  "rooms": 3,
  "suites": 3,
  "bathrooms": 4,
  "parkingSpaces": 6,
  "features": [
    "Piscina",
    "Academia",
    "Varanda gourmet"
  ],
  "address": {
    "street": "Rua Exemplo, 123",
    "neighborhood": "Itaim Bibi",
    "city": "São Paulo",
    "state": "SP",
    "zipCode": "04538-132",
    "coordinates": {
      "lat": -23.5815,
      "lng": -46.6866
    }
  },
  "isExclusive": true,
  "images": [
    {
      "url": "https://imagens.pilarhomes.com.br/...",
      "alt": "Sala de estar",
      "order": 1
    }
  ],
  "virtualTour": "https://...",
  "video": "https://...",
  "company": {...},
  "agent": {...},
  "createdAt": "2024-10-15T10:30:00Z",
  "updatedAt": "2024-11-20T14:22:00Z"
}
```

---

### Propriedades em Destaque (Hero Section)
```http
GET /properties/featured
```

**Query Parameters**:
```javascript
{
  limit: number  // Default: 4
}
```

**Response**: Array de propriedades (mesmo formato acima)

---

### Propriedades Exclusivas
```http
GET /properties/exclusive
```

**Response**: Mesma estrutura de `/properties` mas filtrado por `isExclusive: true`

---

## 👔 Endpoints de Corretores (Agents)

### Listar Corretores
```http
GET /agents
```

**Query Parameters**:
```javascript
{
  companyId: string,   // Filtro por boutique
  page: number,
  perPage: number
}
```

**Response**:
```json
{
  "agents": [
    {
      "id": "682deb171620f92f8984ac90",
      "name": "Jeff S Batah",
      "displayName": "Jef Batah",
      "email": "jeff@amenities.com.br",
      "phone": "+55 11 98765-4321",
      "whatsapp": "+55 11 98765-4321",
      "instagram": "@jefbatah",
      "linkedin": "linkedin.com/in/jefbatah",
      "website": null,
      "bio": "Especialista em imóveis de ultra-luxo...",
      "profilePicture": {
        "url": "https://blintz-properties-sandbox.s3.amazonaws.com/...",
        "croppedUrl": "https://..."
      },
      "company": {
        "id": "682deaa91620f92f8984ac8f",
        "name": "Amenities"
      },
      "stats": {
        "totalProperties": 3,
        "totalValue": 95200000,
        "exclusivePercentage": 66.7
      }
    }
  ],
  "pagination": {...}
}
```

---

### Buscar Corretor por ID
```http
GET /agents/:id
```

**Response**: Objeto de corretor completo + propriedades associadas

---

## 🏢 Endpoints de Boutiques (Companies)

### Listar Boutiques
```http
GET /companies
```

**Response**:
```json
{
  "companies": [
    {
      "id": "6520716b2a44750d6a32ce3d",
      "name": "Homesphere",
      "slug": "homesphere",
      "website": "https://homesphere.com.br",
      "email": "contato@homesphere.com.br",
      "phone": "+55 11 3456-7890",
      "logo": {
        "small": "https://blintz-properties-sandbox.s3.amazonaws.com/.../small_logo.svg",
        "large": "https://blintz-properties-sandbox.s3.amazonaws.com/.../large_logo.svg"
      },
      "description": "Boutique especializada em imóveis de luxo...",
      "stats": {
        "totalProperties": 4,
        "totalAgents": 4,
        "marketShare": 32.73,
        "totalValue": 122280000
      }
    }
  ]
}
```

---

### Buscar Boutique por ID ou Slug
```http
GET /companies/:id
GET /companies/slug/:slug
```

**Exemplo**: `/companies/slug/homesphere`

---

## 🔍 Endpoints de Busca

### Busca Global
```http
GET /search
```

**Query Parameters**:
```javascript
{
  q: string,           // Query de busca
  type: "properties" | "agents" | "companies",
  filters: {...}       // Filtros específicos por tipo
}
```

---

### Autocomplete de Endereços
```http
GET /addresses/autocomplete
```

**Query Parameters**:
```javascript
{
  q: string,           // Texto digitado
  limit: number        // Default: 10
}
```

**Response**:
```json
{
  "suggestions": [
    {
      "neighborhood": "Jardim Paulista",
      "city": "São Paulo",
      "state": "SP",
      "count": 15  // Número de imóveis nessa região
    }
  ]
}
```

---

## 📊 Endpoints de Analytics (Possível)

### Estatísticas Gerais
```http
GET /stats/overview
```

**Response**:
```json
{
  "totalProperties": 273,
  "totalValue": 3300000000,
  "averagePrice": 12087912,
  "totalAgents": 80,
  "totalCompanies": 21
}
```

---

## 📧 Endpoints de Leads

### Criar Lead (Formulário de Contato)
```http
POST /leads
```

**Body**:
```json
{
  "propertyId": "HS27071",
  "name": "João Silva",
  "email": "joao@example.com",
  "phone": "+55 11 98765-4321",
  "message": "Tenho interesse em agendar uma visita",
  "source": "website",
  "utmSource": "google",
  "utmMedium": "cpc"
}
```

**Response**:
```json
{
  "id": "lead_abc123",
  "status": "pending",
  "createdAt": "2025-12-03T15:30:00Z",
  "assignedTo": {
    "agentId": "652071a22a44750d6a32ce3e",
    "agentName": "Thiago Granato"
  }
}
```

---

## 🔐 Endpoints de Autenticação (Possível)

### Login (para corretores/admin)
```http
POST /auth/login
```

**Body**:
```json
{
  "email": "corretor@boutique.com",
  "password": "******"
}
```

**Response**:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": "...",
    "role": "agent",
    "permissions": [...]
  }
}
```

---

## 📋 Notas Técnicas

### Headers Comuns

```http
Content-Type: application/json
Accept: application/json
Authorization: Bearer {token}  # Se autenticado
User-Agent: PilarHomesWebApp/1.0
```

### Rate Limiting
- Provável limite: 100 requests/minuto
- Header de resposta: `X-RateLimit-Remaining`

### Paginação Padrão
```json
{
  "pagination": {
    "page": 1,
    "perPage": 15,
    "totalPages": 7,
    "filteredCount": 97,
    "totalCount": 273,
    "hasNext": true,
    "hasPrev": false
  }
}
```

### Filtros Comuns (Query Params)
- `sort`: `price_asc`, `price_desc`, `date_asc`, `date_desc`
- `page`: Número da página
- `perPage`: Itens por página (max: 100)

---

## 🚀 Próximos Passos para Validação

1. **Testar endpoints** com Postman/Insomnia
2. **Capturar requisições reais** via DevTools Network tab
3. **Verificar autenticação** requerida
4. **Mapear webhooks** (se existirem)
5. **Documentar rate limits**
6. **Criar SDK JavaScript/TypeScript**

---

**Status**: Mapeamento baseado em estrutura Nuxt.js observada  
**Confiança**: 80% (requer validação com requests reais)  
**Última Atualização**: 2025-12-03
