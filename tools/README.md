# 🛠️ Tools - Ferramentas de Integração

> Ferramentas para interagir com a API da Pilar Homes

---

## 📦 Arquivos

| Arquivo | Linguagem | Descrição |
|---------|-----------|-----------|
| `pilar_api_client.py` | Python | Cliente completo para API |
| `pilar_api_proxy.py` | Python/Flask | Proxy para contornar CORS |
| `pilar_search.ps1` | PowerShell | Script de busca interativo |

---

## 🐍 Cliente Python

### Instalação

```bash
pip install requests
```

### Uso como Script

```bash
python pilar_api_client.py
```

### Uso como Módulo

```python
from pilar_api_client import PilarHomesAPI

api = PilarHomesAPI()

# Buscar apartamentos até 3M
result = api.search(
    transaction_type="sell",
    property_type="apartment",
    max_price=3000000,
    city="São Paulo"
)

print(f"Total: {result.total_count} imóveis")

for prop in result.properties:
    print(f"{prop.region}: {prop.format_price()} - {prop.area}m²")
```

### Métodos Disponíveis

| Método | Descrição |
|--------|-----------|
| `search()` | Busca com filtros |
| `get_by_slug()` | Busca por slug |
| `get_clusters()` | Dados para mapa |
| `search_all()` | Busca com paginação automática |

### Parâmetros de Busca

| Parâmetro | Tipo | Valores |
|-----------|------|---------|
| `transaction_type` | str | `sell`, `rent` |
| `property_type` | str | `apartment`, `house`, `penthouse`, `land` |
| `min_price` / `max_price` | int | Preço em R$ |
| `min_area` / `max_area` | int | Área em m² |
| `bedrooms` | int | Número de quartos |
| `suites` | int | Número de suítes |
| `parking_spots` | int | Vagas de garagem |
| `city` | str | Nome da cidade |
| `region` | str | Nome do bairro |

---

## 🌐 Proxy Flask

### Instalação

```bash
pip install flask flask-cors requests
```

### Uso

```bash
python pilar_api_proxy.py
```

### Endpoints Disponíveis

| Endpoint | Descrição |
|----------|-----------|
| `http://localhost:5000/api/properties` | Listagem de imóveis |
| `http://localhost:5000/api/properties/clusters` | Clusters para mapa |
| `http://localhost:5000/health` | Health check |

### Exemplo no Frontend

```javascript
// Com proxy rodando
fetch('http://localhost:5000/api/properties?transactionType=sell&perPage=12')
  .then(r => r.json())
  .then(data => console.log(data.properties));
```

---

## 💻 PowerShell Script

### Uso Básico

```powershell
.\pilar_search.ps1
```

### Com Filtros

```powershell
# Apartamentos até 2M
.\pilar_search.ps1 -PropertyType apartment -MaxPrice 2000000

# Casas em São Paulo com 3+ quartos
.\pilar_search.ps1 -PropertyType house -City "São Paulo" -Bedrooms 3

# Aluguel com estatísticas
.\pilar_search.ps1 -TransactionType rent -ShowStats

# Exportar para CSV
.\pilar_search.ps1 -PerPage 50 -ExportCsv

# Exportar para JSON
.\pilar_search.ps1 -PerPage 50 -ExportJson
```

### Parâmetros Disponíveis

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `-TransactionType` | sell/rent | Tipo de transação |
| `-PropertyType` | string | Tipo do imóvel |
| `-MinPrice` | int | Preço mínimo |
| `-MaxPrice` | int | Preço máximo |
| `-City` | string | Cidade |
| `-Region` | string | Bairro |
| `-Bedrooms` | int | Quartos mínimos |
| `-PerPage` | int | Itens por página (max 50) |
| `-Page` | int | Número da página |
| `-ShowStats` | switch | Mostrar estatísticas |
| `-ExportCsv` | switch | Exportar CSV |
| `-ExportJson` | switch | Exportar JSON |

---

## 🔑 Configuração da API

### Headers Obrigatórios

```
Referer: https://pilarhomes.com.br/
Origin: https://pilarhomes.com.br
User-Agent: Mozilla/5.0 ...
```

### Google Maps Key

```
AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ
```

---

## 📊 Estatísticas Atuais

- **18.330+** imóveis à venda
- **3.666** páginas de resultados
- **Bairros populares:** Jardim América, Higienópolis, Vila Mariana, Itaim Bibi

---

*Última atualização: Dezembro 2024*
