# 📚 Research - Índice da Pesquisa

> Documentação completa da análise do site pilarhomes.com.br

## 🗺️ [RESEARCH_MAP.md](RESEARCH_MAP.md) - Mapa Visual da Pesquisa

**Comece por aqui!** O mapa consolida todas as descobertas importantes em um único documento.

---

## 📂 Estrutura

```
research/
├── docs/                    # 📄 Documentação escrita
├── analysis/                # 🔬 Análises técnicas detalhadas
│   └── design_system/       # Análise do design system
├── assets/                  # 🎨 Assets extraídos
│   ├── icons/               # Ícones SVG
│   ├── logos/               # Logos das imobiliárias
│   └── screenshots/         # Capturas de tela
├── data/                    # 📊 Dados estruturados (JSON)
├── har-files/               # 🌐 Arquivos de network (HAR)
├── prototypes/              # 🎯 Protótipos HTML funcionais
├── scripts/                 # ⚙️ Scripts de extração
└── extracted/               # 📦 Código extraído
    ├── api/                 # Mapeamento de APIs
    ├── css/                 # CSS extraído
    └── tokens/              # Design tokens
```

---

## 📄 Documentação Principal

### Visão Geral
| Arquivo | Descrição |
|---------|-----------|
| [OSINT_CONSOLIDADO.md](docs/OSINT_CONSOLIDADO.md) | Análise OSINT completa |
| [DADOS_COMPLETOS_PILARHOMES.md](docs/DADOS_COMPLETOS_PILARHOMES.md) | Dados consolidados |
| [DESAFIO.MD](docs/DESAFIO.MD) | Contexto do desafio |
| [RESPOSTA_DESAFIO_PD.md](docs/RESPOSTA_DESAFIO_PD.md) | Resposta ao desafio |

### Tecnologia & Stack
| Arquivo | Descrição |
|---------|-----------|
| [STACK_ANALYSIS_PILARHOMES.md](docs/STACK_ANALYSIS_PILARHOMES.md) | Stack tecnológica completa |
| [API_PILAR_HOMES_GUIA.md](docs/API_PILAR_HOMES_GUIA.md) | ⭐ Guia da API (endpoints, params) |
| [ANALISE_ENGINEERING_BLOG.md](docs/ANALISE_ENGINEERING_BLOG.md) | Análise do blog de engenharia |

### Design System
| Arquivo | Descrição |
|---------|-----------|
| [DESIGN_SYSTEM_PILARHOMES.md](docs/DESIGN_SYSTEM_PILARHOMES.md) | Design system completo |
| [DESIGN_SYSTEM_SUMMARY.md](docs/DESIGN_SYSTEM_SUMMARY.md) | Resumo do design system |
| [COLOR_GUIDE_PILARHOMES.md](docs/COLOR_GUIDE_PILARHOMES.md) | Paleta de cores |
| [COMPONENT_STRUCTURE.md](docs/COMPONENT_STRUCTURE.md) | Estrutura de componentes |
| [IMPLEMENTATION_GUIDE_PILARHOMES.md](docs/IMPLEMENTATION_GUIDE_PILARHOMES.md) | Guia de implementação |
| [EXTRACAO_ICONES_SVG.md](docs/EXTRACAO_ICONES_SVG.md) | Ícones SVG extraídos |

### Produto & UX
| Arquivo | Descrição |
|---------|-----------|
| [SITEMAP_E_JORNADAS_PILARHOMES.md](docs/SITEMAP_E_JORNADAS_PILARHOMES.md) | Mapa do site e jornadas |
| [PLATAFORMA_WHITE_LABEL_PILAR.md](docs/PLATAFORMA_WHITE_LABEL_PILAR.md) | Plataforma white-label |
| [ANALISE_SOUPILAR_REDE_CORRETORES.md](docs/ANALISE_SOUPILAR_REDE_CORRETORES.md) | Rede de corretores |

### Marketing & Social
| Arquivo | Descrição |
|---------|-----------|
| [SOCIAL_MEDIA_PILAR.md](docs/SOCIAL_MEDIA_PILAR.md) | Redes sociais e métricas |
| [VIDEO_REBRANDING.MD](docs/VIDEO_REBRANDING.MD) | Análise de rebranding |
| [EQUIPE.MD](docs/EQUIPE.MD) | Equipe Pilar |

---

## 📊 Dados Extraídos

### JSON Data (`data/`)
| Arquivo | Descrição |
|---------|-----------|
| `har_analysis_summary.json` | Resumo da análise HAR homepage |
| `har_imoveis_summary.json` | Resumo da análise HAR /imoveis |
| `social_media_pilar.json` | Dados de redes sociais |

### HAR Files (`har-files/`)
| Arquivo | Descrição |
|---------|-----------|
| `pilarhomes_radar.har` | HAR da homepage |
| `pilarhomes_imoveis.har` | HAR da página de imóveis |
| `home.har` | HAR alternativo home |
| `imoveis.har` | HAR alternativo imóveis |

### Extracted (`extracted/`)
| Pasta | Conteúdo |
|-------|----------|
| `api/` | Endpoints, tipos TypeScript, mapa de APIs |
| `css/` | CSS extraído do site |
| `tokens/` | Design tokens (CSS, JSON, TS) |

---

## 🎨 Assets

### Ícones (`assets/icons/`)
- SVGs funcionais
- SVGs de navegação
- SVGs de propriedades
- SVGs de redes sociais

### Logos (`assets/logos/`)
- Logos das imobiliárias parceiras

---

## ⚙️ Scripts de Extração

| Script | Linguagem | Função |
|--------|-----------|--------|
| `analyze_har.py` | Python | Análise de HAR homepage |
| `analyze_har_imoveis.py` | Python | Análise de HAR imóveis |
| `extract_api_and_tokens.ps1` | PowerShell | Extração de API e tokens |
| `extract_design_system.ps1` | PowerShell | Extração design system |
| `extract_svgs.ps1` | PowerShell | Extração de SVGs |
| `logo_extractor.py` | Python | Extração de logos |
| `social_media_extractor.py` | Python | Extração redes sociais |

---

## 🎯 Protótipos

| Arquivo | Descrição |
|---------|-----------|
| `prototipo_pilar_api.html` | Protótipo com API real + Maps |
| `comparador-imoveis.html` | Comparador de imóveis |

---

## 🔑 Descobertas Principais

### API Pública
```
Endpoint: https://pilarhomes.com.br/api/properties
Headers:  Referer: https://pilarhomes.com.br/
Métodos:  GET
```

### Google Maps
```
Key: AIzaSyB6TCbFAul6VL_VEWQ9-_pmOWhjas1ALGQ
```

### CDN de Imagens
```
S3: blintz-properties-sandbox.s3.amazonaws.com
CDN: imagens.pilarhomes.com.br
```

---

*Última atualização: Dezembro 2024*
