# 🏠 Guia de Integração: API Pilar Homes

> **Documento técnico para recriar o sistema de busca de imóveis da Pilar Homes**
> 
> Descoberto via análise HAR (HTTP Archive) em Dezembro/2024

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [API de Imóveis](#api-de-imóveis)
3. [Google Maps API](#google-maps-api)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Restrições e Workarounds](#restrições-e-workarounds)
6. [Estrutura de Dados](#estrutura-de-dados)

---

## 🎯 Visão Geral

### Recursos Descobertos

| Recurso | Endpoint / Chave | Status |
|---------|-----------------|--------|
| API de Listagem | `https://pilarhomes.com.br/api/properties` | ✅ Pública |
| API de Clusters (Mapa) | `https://pilarhomes.com.br/api/properties/clusters` | ✅ Pública |
| Google Maps API | `AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ` | ✅ Exposta |
| CDN de Imagens | `blintz-properties-sandbox.s3.amazonaws.com` | ✅ Pública |
| CDN de Thumbnails | `imagens.pilarhomes.com.br` | ✅ Pública |

### Limitações

- **CORS**: A API bloqueia requests do browser (origens diferentes)
- **Solução**: Usar chamadas server-side (Python, Node, PowerShell) ou proxy

---

## 🔌 API de Imóveis

### Endpoint Principal

```
GET https://pilarhomes.com.br/api/properties
```

### Parâmetros de Query

| Parâmetro | Tipo | Valores | Descrição |
|-----------|------|---------|-----------|
| `transactionType` | string | `sell`, `rent` | Tipo de transação |
| `page` | integer | 1, 2, 3... | Página atual |
| `perPage` | integer | 1-50 | Itens por página |
| `propertyType` | string | `apartment`, `house`, `penthouse`, `land`, `commercial` | Tipo de imóvel |
| `minPrice` | integer | Ex: 500000 | Preço mínimo |
| `maxPrice` | integer | Ex: 5000000 | Preço máximo |
| `minArea` | integer | Ex: 50 | Área mínima (m²) |
| `maxArea` | integer | Ex: 500 | Área máxima (m²) |
| `bedrooms` | integer | 1, 2, 3, 4+ | Número de quartos |
| `suites` | integer | 1, 2, 3+ | Número de suítes |
| `parkingSpots` | integer | 1, 2, 3+ | Vagas de garagem |
| `city` | string | `São Paulo` | Cidade |
| `region` | string | `Jardim América` | Bairro |

### Exemplo de Request

**⚠️ IMPORTANTE: Headers Obrigatórios**

A API possui proteção WAF/anti-bot. É necessário incluir os headers:

```
Referer: https://pilarhomes.com.br/
Origin: https://pilarhomes.com.br
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...
```

```bash
# PowerShell (funciona direto)
Invoke-RestMethod -Uri "https://pilarhomes.com.br/api/properties?transactionType=sell&page=1&perPage=12" -Headers @{"Referer"="https://pilarhomes.com.br/"} | ConvertTo-Json -Depth 5

# cURL (com headers)
curl -H "Referer: https://pilarhomes.com.br/" \
     -H "Origin: https://pilarhomes.com.br" \
     "https://pilarhomes.com.br/api/properties?transactionType=sell&page=1&perPage=12"

# Python (com headers)
import requests

headers = {
    'Referer': 'https://pilarhomes.com.br/',
    'Origin': 'https://pilarhomes.com.br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(
    "https://pilarhomes.com.br/api/properties",
    params={"transactionType": "sell", "page": 1, "perPage": 12},
    headers=headers
)
data = response.json()
```

### Resposta da API

```json
{
  "properties": [
    {
      "id": "67a3698156ca0c4a30c90ffb",
      "slug": "apartamento-2-quartos-jardim-america-sao-paulo",
      "company": {
        "id": "...",
        "name": "Nome da Imobiliária",
        "smallLogo": "https://..."
      },
      "agent": {
        "id": "...",
        "name": "Nome do Corretor",
        "profilePicture": { "url": "...", "croppedUrl": "..." }
      },
      "ad": {
        "title": "Apartamento reformado com 200 m²...",
        "description": "Descrição completa do imóvel...",
        "transactionType": "sell"
      },
      "images": [
        { "watermarkUrl": "https://blintz-properties-sandbox.s3.amazonaws.com/..." }
      ],
      "askingPrice": 4850000,
      "rentPrice": null,
      "area": 200,
      "totalArea": null,
      "bedrooms": 2,
      "bathrooms": 3,
      "suites": 2,
      "parkingSpots": 1,
      "condoFee": 4850,
      "tax": 1000,
      "propertyType": {
        "name": "Apartamento",
        "identifier": "apartment"
      },
      "featuresByCategory": {
        "Diferenciais": [...],
        "Cômodos": [...],
        "Facilidades": [...]
      },
      "region": "Jardim América",
      "city": "São Paulo",
      "state": "SP",
      "commercialId": "MO4163",
      "isExclusive": false,
      "condoName": "Nome do Condomínio",
      "publicationStatus": "published"
    }
  ],
  "pagination": {
    "page": 1,
    "perPage": 12,
    "totalPages": 3666,
    "filteredCount": 18327
  }
}
```

---

## 🗺️ Google Maps API

### Chave Exposta

```
AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ
```

### Uso no HTML

```html
<!-- Carregar a API -->
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ&libraries=places"></script>

<!-- Container do mapa -->
<div id="map" style="height: 400px; width: 100%;"></div>

<script>
// Inicializar o mapa
function initMap() {
    const saopaulo = { lat: -23.5505, lng: -46.6333 };
    
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: saopaulo
    });
    
    // Adicionar marcador
    new google.maps.Marker({
        position: saopaulo,
        map: map,
        title: 'Imóvel'
    });
}

// Chamar quando a página carregar
document.addEventListener('DOMContentLoaded', initMap);
</script>
```

### Serviços Disponíveis

A chave permite acesso a:

- ✅ **Maps JavaScript API** - Renderização do mapa
- ✅ **Places API** - Busca de endereços
- ✅ **Geocoding API** - Conversão endereço → coordenadas
- ✅ **Marker API** - Marcadores no mapa

### Geocoding (Endereço → Coordenadas)

```javascript
const geocoder = new google.maps.Geocoder();

geocoder.geocode({ 
    address: "Jardim América, São Paulo, SP, Brasil" 
}, (results, status) => {
    if (status === 'OK') {
        const location = results[0].geometry.location;
        console.log(`Lat: ${location.lat()}, Lng: ${location.lng()}`);
    }
});
```

---

## 💻 Exemplos Práticos

### 1. Python - Buscar Imóveis

```python
"""
pilar_api_client.py
Cliente Python para API Pilar Homes
"""

import requests
from typing import Optional, Dict, List

class PilarHomesAPI:
    BASE_URL = "https://pilarhomes.com.br/api"
    
    def __init__(self):
        self.session = requests.Session()
    
    def search_properties(
        self,
        transaction_type: str = "sell",
        page: int = 1,
        per_page: int = 12,
        property_type: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        bedrooms: Optional[int] = None,
        city: Optional[str] = None,
        region: Optional[str] = None
    ) -> Dict:
        """Busca imóveis com filtros"""
        
        params = {
            "transactionType": transaction_type,
            "page": page,
            "perPage": per_page
        }
        
        # Adicionar filtros opcionais
        if property_type:
            params["propertyType"] = property_type
        if min_price:
            params["minPrice"] = min_price
        if max_price:
            params["maxPrice"] = max_price
        if bedrooms:
            params["bedrooms"] = bedrooms
        if city:
            params["city"] = city
        if region:
            params["region"] = region
        
        response = self.session.get(f"{self.BASE_URL}/properties", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_property_by_slug(self, slug: str) -> Dict:
        """Busca um imóvel específico pelo slug"""
        response = self.session.get(f"{self.BASE_URL}/properties/{slug}")
        response.raise_for_status()
        return response.json()
    
    def get_clusters(self, transaction_type: str = "sell") -> Dict:
        """Busca clusters para o mapa"""
        response = self.session.get(
            f"{self.BASE_URL}/properties/clusters",
            params={"transactionType": transaction_type}
        )
        response.raise_for_status()
        return response.json()


# Exemplo de uso
if __name__ == "__main__":
    api = PilarHomesAPI()
    
    # Buscar apartamentos à venda em SP até 2M
    results = api.search_properties(
        transaction_type="sell",
        property_type="apartment",
        max_price=2000000,
        city="São Paulo"
    )
    
    print(f"Total encontrados: {results['pagination']['filteredCount']}")
    
    for prop in results['data'][:5]:
        print(f"\n📍 {prop['region']}, {prop['city']}")
        print(f"   {prop['propertyType']['name']} - {prop['area']}m²")
        print(f"   💰 R$ {prop['askingPrice']:,.0f}".replace(",", "."))
        print(f"   🛏️ {prop['bedrooms']} quartos | 🚗 {prop['parkingSpots']} vagas")
```

### 2. PowerShell - Script de Busca

```powershell
# pilar_search.ps1
# Busca imóveis via API Pilar Homes

param(
    [string]$TransactionType = "sell",
    [int]$Page = 1,
    [int]$PerPage = 10,
    [string]$PropertyType = "",
    [int]$MaxPrice = 0,
    [string]$City = ""
)

$baseUrl = "https://pilarhomes.com.br/api/properties"
$params = @{
    transactionType = $TransactionType
    page = $Page
    perPage = $PerPage
}

if ($PropertyType) { $params.propertyType = $PropertyType }
if ($MaxPrice -gt 0) { $params.maxPrice = $MaxPrice }
if ($City) { $params.city = $City }

$queryString = ($params.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join "&"
$url = "$baseUrl?$queryString"

Write-Host "🔍 Buscando: $url" -ForegroundColor Cyan

$response = Invoke-RestMethod -Uri $url -Method GET

Write-Host "`n📊 Total: $($response.pagination.filteredCount) imóveis" -ForegroundColor Green
Write-Host "📄 Página $($response.pagination.page) de $($response.pagination.totalPages)`n"

foreach ($prop in $response.data) {
    $price = "R$ {0:N0}" -f $prop.askingPrice
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host "📍 $($prop.region), $($prop.city)" -ForegroundColor Yellow
    Write-Host "   $($prop.propertyType.name) | $($prop.area)m²"
    Write-Host "   💰 $price" -ForegroundColor Green
    Write-Host "   🛏️ $($prop.bedrooms) quartos | 🚿 $($prop.bathrooms) banheiros | 🚗 $($prop.parkingSpots) vagas"
    Write-Host "   🔗 https://pilarhomes.com.br/imovel/$($prop.slug)"
}
```

**Uso:**
```powershell
# Buscar apartamentos até 3M em São Paulo
.\pilar_search.ps1 -PropertyType "apartment" -MaxPrice 3000000 -City "São Paulo"
```

### 3. Node.js - API Proxy (CORS Workaround)

```javascript
// pilar_proxy.js
// Proxy para contornar CORS no browser

const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());

const API_BASE = 'https://pilarhomes.com.br/api';

// Proxy para /api/properties
app.get('/api/properties', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE}/properties`, {
            params: req.query
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Proxy para /api/properties/clusters
app.get('/api/properties/clusters', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE}/properties/clusters`, {
            params: req.query
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

const PORT = 3001;
app.listen(PORT, () => {
    console.log(`🏠 Pilar API Proxy rodando em http://localhost:${PORT}`);
});
```

**Instalação:**
```bash
npm init -y
npm install express cors axios
node pilar_proxy.js
```

---

## ⚠️ Restrições e Workarounds

### Problema: CORS no Browser

A API retorna o header:
```
Access-Control-Allow-Origin: https://pilarhomes.com.br
```

Isso bloqueia chamadas diretas do browser de outras origens.

### Soluções

| Solução | Prós | Contras |
|---------|------|---------|
| **Proxy Server** | Funciona 100% | Requer servidor |
| **Server-Side Rendering** | Dados frescos | Complexidade |
| **Dados Estáticos** | Simples | Dados não atualizados |
| **Browser Extension** | Bypass CORS | Apenas dev |

### Proxy Python (Flask)

```python
# pilar_proxy.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/properties')
def proxy_properties():
    response = requests.get(
        "https://pilarhomes.com.br/api/properties",
        params=dict(request.args)
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

```bash
pip install flask flask-cors requests
python pilar_proxy.py
```

Depois use `http://localhost:5000/api/properties` no frontend.

---

## 📦 Estrutura de Dados

### Tipos de Imóveis (`propertyType`)

| Identifier | Nome |
|------------|------|
| `apartment` | Apartamento |
| `house` | Casa |
| `penthouse` | Cobertura |
| `land` | Terreno |
| `commercial` | Comercial |
| `studio` | Studio |
| `flat` | Flat |

### Categorias de Features (`featuresByCategory`)

```json
{
  "Diferenciais": [
    { "name": "Ar-condicionado", "identifier": "air_conditioning" },
    { "name": "Reformado", "identifier": "renovated" },
    { "name": "Mobiliado", "identifier": "furnished" }
  ],
  "Cômodos": [
    { "name": "Closet", "identifier": "closet" },
    { "name": "Lavabo", "identifier": "has_lavabo" },
    { "name": "Home office", "identifier": "home_office" }
  ],
  "Área externa": [
    { "name": "Churrasqueira", "identifier": "barbecue_grill" },
    { "name": "Piscina", "identifier": "private_pool" }
  ],
  "Facilidades": [
    { "name": "Próximo ao metrô", "identifier": "near_metro" },
    { "name": "Portaria 24h", "identifier": "doorman_24h" }
  ]
}
```

### URLs de Imagens

```
# Imagem com watermark (alta qualidade)
https://blintz-properties-sandbox.s3.amazonaws.com/{propertyId}/pilar-homes-images-watermark/{uuid}.webp

# Thumbnail otimizado
https://imagens.pilarhomes.com.br/{path}

# Logo da imobiliária
https://blintz-properties-sandbox.s3.amazonaws.com/{companyId}/small_logo.svg
```

---

## 🚀 Quick Start

### Testar Agora (PowerShell)

```powershell
# Listar 5 imóveis à venda
Invoke-RestMethod "https://pilarhomes.com.br/api/properties?transactionType=sell&perPage=5" | ConvertTo-Json -Depth 3

# Buscar apartamentos em Higienópolis
Invoke-RestMethod "https://pilarhomes.com.br/api/properties?transactionType=sell&propertyType=apartment&region=Higien%C3%B3polis" | ForEach-Object { $_.data } | Format-Table region, askingPrice, area, bedrooms
```

### Testar Agora (Python)

```python
import requests
r = requests.get("https://pilarhomes.com.br/api/properties?transactionType=sell&perPage=3")
for p in r.json()['data']:
    print(f"{p['region']}: R$ {p['askingPrice']:,} - {p['area']}m²")
```

---

## 📁 Arquivos do Projeto

```
C:\Users\boliv\Documents\Pilar\
├── API_PILAR_HOMES_GUIA.md      ← Este arquivo
├── prototipo_pilar_api.html      ← Protótipo funcional
├── pilar_api_proxy.py            ← Proxy Flask
├── pilarhomes_radar.har          ← HAR da homepage
├── pilarhomes_imoveis.har        ← HAR da página de imóveis
└── SOCIAL_MEDIA_PILAR.md         ← Análise completa
```

---

## ⚖️ Disclaimer

Este documento é para fins educacionais e de pesquisa. A chave do Google Maps e os endpoints da API foram descobertos através de análise pública do site. O uso deve respeitar os termos de serviço da Pilar Homes e do Google Maps Platform.

---

*Última atualização: Dezembro 2024*
*Análise realizada via HAR (HTTP Archive) do Chrome DevTools*
