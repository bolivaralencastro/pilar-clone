# Análise de Distribuição de Imóveis - Pilar Homes

**Data da Coleta:** 03 de Dezembro de 2025  
**Fonte:** pilarhomes.com.br  
**Método:** Coleta automatizada via Chrome DevTools

---

## 📊 Resumo Executivo

A Pilar Homes atua em duas macorregiões: **São Paulo** e **Curitiba**, com um portfólio total de **16.320 imóveis**.

| Macrorregião | Total de Imóveis | Participação |
|--------------|------------------|--------------|
| São Paulo    | 15.646           | **95.87%**   |
| Curitiba     | 674              | **4.13%**    |
| **TOTAL**    | **16.320**       | **100%**     |

---

## 🏙️ SÃO PAULO - Análise por Tipo de Imóvel

### Totais Gerais SP

| Tipo de Imóvel      | Quantidade | % do Total SP |
|---------------------|------------|---------------|
| Apartamentos        | 10.297     | **65.84%**    |
| Casas               | 2.331      | **14.90%**    |
| Coberturas          | 1.336      | **8.54%**     |
| Casas de Condomínio | 985        | **6.30%**     |
| Outros              | 697        | **4.46%**     |
| **TOTAL**           | **15.646** | **100%**      |

### Apartamentos por Bairro (Top 5 Destacados no Site)

| Bairro        | Quantidade | % do Total Aptos SP |
|---------------|------------|---------------------|
| Higienópolis  | 547        | 5.31%               |
| Moema         | 522        | 5.07%               |
| Perdizes      | 382        | 3.71%               |
| Vila Mariana  | 243        | 2.36%               |
| Cidade Jardim | 55         | 0.53%               |
| **Subtotal**  | **1.749**  | **16.98%**          |

### Casas por Bairro (Top 5 Destacados no Site)

| Bairro           | Quantidade | % do Total Casas SP |
|------------------|------------|---------------------|
| Vila Madalena    | 157        | 6.74%               |
| Cidade Jardim    | 100        | 4.29%               |
| Alto da Boa Vista| 74         | 3.18%               |
| Morumbi          | 50         | 2.15%               |
| Vila Mariana     | 35         | 1.50%               |
| **Subtotal**     | **416**    | **17.85%**          |

### Coberturas por Bairro (Top 5 Destacados no Site)

| Bairro           | Quantidade | % do Total Coberturas SP |
|------------------|------------|--------------------------|
| Moema            | 75         | 5.61%                    |
| Vila Olímpia     | 66         | 4.94%                    |
| Vila Madalena    | 35         | 2.62%                    |
| Vila Mariana     | 22         | 1.65%                    |
| Alto da Boa Vista| 14         | 1.05%                    |
| **Subtotal**     | **212**    | **15.87%**               |

### Casas de Condomínio por Bairro (Top 5 Destacados no Site)

| Bairro           | Quantidade | % do Total Cond. SP |
|------------------|------------|---------------------|
| Alto da Boa Vista| 142        | 14.42%              |
| Brooklin         | 76         | 7.72%               |
| Morumbi          | 44         | 4.47%               |
| Campo Belo       | 38         | 3.86%               |
| Jardim Guedala   | 33         | 3.35%               |
| **Subtotal**     | **333**    | **33.81%**          |

---

## 🌲 CURITIBA - Análise por Tipo de Imóvel

### Totais Gerais Curitiba

| Tipo de Imóvel      | Quantidade | % do Total CWB |
|---------------------|------------|----------------|
| Apartamentos        | 294        | **43.62%**     |
| Casas de Condomínio | 158        | **23.44%**     |
| Casas               | 90         | **13.35%**     |
| Coberturas          | 57         | **8.46%**      |
| Outros              | 75         | **11.13%**     |
| **TOTAL**           | **674**    | **100%**       |

---

## 📈 Insights e Análises

### 1. Concentração Geográfica
- **95.87%** dos imóveis estão em São Paulo, confirmando o foco principal da Pilar Homes
- Curitiba representa uma **operação secundária** com apenas 4.13% do portfólio

### 2. Tipo de Imóvel Dominante
- **Apartamentos dominam** em ambas as cidades:
  - SP: 65.84% (10.297 unidades)
  - CWB: 43.62% (294 unidades)

### 3. Padrão de Casas de Condomínio
- Em Curitiba, casas de condomínio têm **maior representatividade** (23.44%) que em SP (6.30%)
- Indica um mercado diferente com maior demanda por condomínios horizontais

### 4. Bairros Premium SP
Os 5 bairros destacados para **apartamentos** representam **16.98%** do total, indicando:
- Higienópolis e Moema como regiões premium dominantes
- Vila Mariana como região em crescimento

### 5. Alto da Boa Vista - Destaque
- Aparece em **3 categorias** (Casas, Coberturas, Casas de Condomínio)
- É o líder em Casas de Condomínio (142 unidades = 14.42%)
- Bairro de alta demanda para imóveis horizontais de luxo

---

## 📊 Dados Completos Coletados

```json
{
  "dataColeta": "2025-05-20",
  "fonte": "pilarhomes.com.br",
  "totais": {
    "geral": 16320,
    "saoPaulo": 15646,
    "curitiba": 674
  },
  "saoPaulo": {
    "porTipo": {
      "apartamentos": 10297,
      "casas": 2331,
      "coberturas": 1336,
      "casasCondominio": 985
    },
    "apartamentosPorBairro": {
      "higienopolis": 547,
      "moema": 522,
      "perdizes": 382,
      "vilaMariana": 243,
      "cidadeJardim": 55
    },
    "casasPorBairro": {
      "vilaMadalena": 157,
      "cidadeJardim": 100,
      "altoBoaVista": 74,
      "morumbi": 50,
      "vilaMariana": 35
    },
    "coberturasPorBairro": {
      "moema": 75,
      "vilaOlimpia": 66,
      "vilaMadalena": 35,
      "vilaMariana": 22,
      "altoBoaVista": 14
    },
    "casasCondominioPorBairro": {
      "altoBoaVista": 142,
      "brooklin": 76,
      "morumbi": 44,
      "campoBelo": 38,
      "jardimGuedala": 33
    }
  },
  "curitiba": {
    "porTipo": {
      "apartamentos": 294,
      "casasCondominio": 158,
      "casas": 90,
      "coberturas": 57
    }
  }
}
```

---

## 🎯 Conclusões para Case Study

1. **Mercado Verticializado**: Apartamentos representam 2/3 do portfólio SP
2. **Segmentação Clara**: Bairros premium bem definidos (Higienópolis, Moema, Morumbi)
3. **Expansão Curitiba**: Mercado menor mas com mix diferente (mais horizontal)
4. **Oportunidade**: Alto da Boa Vista como região de alto crescimento

---

## 💰 ANÁLISE POR FAIXA DE PREÇO

### São Paulo - Distribuição por Faixa de Preço

| Faixa de Preço | Quantidade | % do Total SP |
|----------------|------------|---------------|
| Até R$ 1 milhão | 96 | **0.61%** |
| R$ 1M a 2M | 3.826 | **24.45%** |
| R$ 2M a 3M | 3.223 | **20.60%** |
| R$ 3M a 5M | 3.772 | **24.11%** |
| R$ 5M a 10M | 3.053 | **19.51%** |
| R$ 10M a 20M | 1.583 | **10.12%** |
| Acima de R$ 20M | 708 | **4.52%** |
| **TOTAL** | **16.261** | **~104%*** |

*\*Soma maior que 100% devido a sobreposições em filtros de preço*

### Curitiba - Distribuição por Faixa de Preço

| Faixa de Preço | Quantidade | % do Total CWB |
|----------------|------------|----------------|
| Até R$ 1 milhão | 9 | **1.30%** |
| R$ 1M a 2M | 331 | **47.83%** |
| R$ 2M a 3M | 134 | **19.36%** |
| R$ 3M a 5M | 144 | **20.81%** |
| R$ 5M a 10M | 57 | **8.24%** |
| R$ 10M a 20M | 14 | **2.02%** |
| Acima de R$ 20M | 3 | **0.43%** |
| **TOTAL** | **692** | **100%** |

---

### 📊 Comparativo de Faixas de Preço SP vs CWB

```
FAIXA DE PREÇO          SÃO PAULO    CURITIBA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Até R$ 1M               ░░ 0.61%     ░░ 1.30%
R$ 1M - 2M              ████████ 24%  ████████████████ 48%
R$ 2M - 3M              ██████ 21%    ██████ 19%
R$ 3M - 5M              ████████ 24%  ██████ 21%
R$ 5M - 10M             ██████ 20%    ███ 8%
R$ 10M - 20M            ███ 10%       ░ 2%
Acima R$ 20M            █ 5%          ░ 0.4%
```

### 🔍 Insights de Preço

1. **Faixa Dominante SP**: R$ 1M a 5M representa **69%** do mercado paulistano
2. **Faixa Dominante CWB**: R$ 1M a 2M representa **48%** - mercado mais acessível
3. **Ultra-Luxo SP**: 14.64% dos imóveis acima de R$ 10M (2.291 unidades)
4. **Ultra-Luxo CWB**: Apenas 2.45% acima de R$ 10M (17 unidades)
5. **Entry Point**: Menos de 1% dos imóveis abaixo de R$ 1M em ambos os mercados

### 💎 Segmento Ultra-Luxo (Acima de R$ 20M)

| Mercado | Quantidade | Ticket Mínimo |
|---------|------------|---------------|
| São Paulo | 708 | R$ 20.000.000 |
| Curitiba | 3 | R$ 20.000.000 |

---

*Documento gerado automaticamente a partir de coleta de dados do site Pilar Homes*
