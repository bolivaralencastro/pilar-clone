# Sitemap e Jornadas dos Stakeholders - PilarHomes

## 📊 Resumo Executivo

**Total de URLs mapeadas**: 84 URLs únicas  
**Páginas institucionais**: 5  
**Páginas de busca/filtros**: 52  
**Páginas de bairros**: 1 (template reutilizável)  
**Páginas de imóveis**: 12 (amostras)  
**Coleções/Curadorias**: 3  
**Links externos**: 3

---

## 🗺️ Arquitetura de Informação - Sitemap

```
pilarhomes.com.br/
│
├── 🏠 Home (/)
│   ├── Hero Section
│   │   ├── Busca por cidades e regiões
│   │   ├── Busca por bairros, endereços e condomínios
│   │   └── CTA: "Explorar imóveis"
│   │
│   ├── Propostas de Valor
│   │   ├── Liderança no alto padrão (R$ 3 bilhões negociados)
│   │   ├── Atendimento sob medida
│   │   └── Maior portfólio atualizado
│   │
│   ├── CTAs de Stakeholder
│   │   ├── 🔵 "Quero comprar"
│   │   ├── 🟢 "Quero vender"
│   │   └── 🟡 "Sou corretor"
│   │
│   ├── Produtos Especializados
│   │   ├── Exclusivos PilarHomes
│   │   ├── Coleções Compartilhadas
│   │   └── Off-Market
│   │
│   ├── Nossas Regiões (6 macro-regiões)
│   │   ├── São Paulo
│   │   ├── Curitiba
│   │   ├── Interior SP
│   │   ├── Alphaville SP
│   │   ├── Litoral Norte SP
│   │   └── Litoral Sul SP
│   │
│   ├── Exclusivos PilarHomes (carrossel de imóveis)
│   ├── Bairros em Destaque (8 bairros nobres)
│   ├── Curadorias Assinadas (3 influenciadores)
│   ├── Depoimentos de Clientes
│   └── SEO/Links de Cauda Longa
│       ├── Tipos de imóvel por bairro
│       └── Imóveis por endereço/POI
│
├── 🔍 Busca de Imóveis (/venda/imoveis/)
│   ├── Filtros por:
│   │   ├── Macro-região (São Paulo, Curitiba, Interior, etc.)
│   │   ├── Cidade
│   │   ├── Bairro/Região
│   │   ├── Tipo de imóvel (Apartamento, Casa, Cobertura, Duplex, Casa de Condomínio)
│   │   ├── Exclusividade (isExclusive=true)
│   │   ├── Ponto de interesse (POI com lat/lng)
│   │   └── Rua/Endereço específico
│   │
│   └── Exemplos de URLs:
│       ├── /venda/imoveis/sao-paulo-sp-brasil?isExclusive=true
│       ├── /venda/imoveis/sp-brasil?macroregions=São+Paulo
│       ├── /venda/imoveis/moema-sao-paulo-sp-brasil/apartamento
│       └── /venda/imoveis/sp-brasil/Rua%20Oscar%20Freire.../apartamento?poiLocationLat=...
│
├── 🏘️ Páginas de Bairros (/bairros/{bairro})
│   ├── Exemplo: /bairros/itaim-bibi
│   ├── Conteúdo:
│   │   ├── Descrição do bairro
│   │   ├── Links por tipo de imóvel (Apartamento, Cobertura, Duplex)
│   │   └── CTA "Ver todos os imóveis"
│   │
│   └── Bairros mapeados:
│       ├── Itaim Bibi, Jardim Paulista, Vila Nova Conceição
│       ├── Jardim América, Pinheiros, Alto de Pinheiros
│       ├── Jardim Europa, Jardim Paulistano, Moema
│       ├── Cidade Jardim, Perdizes, Vila Mariana
│       ├── Higienópolis, Morumbi, Vila Madalena
│       ├── Vila Olímpia, Alto da Boa Vista, Brooklin
│       └── Campo Belo, Jardim Guedala, Consolação
│
├── 🏡 Páginas de Imóveis (/imovel/{codigo}/{slug})
│   ├── Estrutura: /imovel/CODIGO/tipo-quartos-bairro-cidade
│   ├── Exemplos mapeados:
│   │   ├── VA040 - Casa de condomínio - Campo Comprido, Curitiba - R$ 3.350.000
│   │   ├── SB285 - Apartamento - Vila Mariana, SP - R$ 1.500.000
│   │   ├── AMS046 - Casa - Jardim Paulista, SP - R$ 60.000.000
│   │   └── HS27071 - Apartamento - Itaim Bibi, SP - R$ 43.980.000
│   │
│   └── Informações exibidas:
│       ├── Galeria de fotos (carrossel)
│       ├── Selo "Exclusivo" (se aplicável)
│       ├── Corretor responsável (foto + nome + imobiliária)
│       ├── Preço, código, área (útil/construída)
│       ├── Suítes, vagas, tipo, localização
│       └── CTA "Adicionar a minha coleção"
│
├── 📚 Coleções/Curadorias (/colecao/{nome})
│   ├── /colecao/casadevalentina (Lucila Zahran Turqueto)
│   ├── /colecao/fernanda-berendt (Fernanda Berendt - @CASA+)
│   ├── /colecao/nicole-gomes (Nicole Gomes - Casa e Jardim)
│   └── /colecoes/minha-colecao (Coleções do usuário)
│
├── 💎 Produtos Especializados
│   ├── /off-market
│   │   └── Imóveis de alto valor não anunciados publicamente
│   │
│   └── /venda/imoveis/.../isExclusive=true
│       └── Exclusivos PilarHomes (apenas na Pilar)
│
├── 📝 Páginas Institucionais
│   ├── /sobre-a-pilar
│   │   └── "Transformando o Mercado Imobiliário"
│   │       └── "Mais de R$ 3 bilhões negociados nos últimos 12 meses"
│   │
│   ├── /anunciar-imovel
│   │   └── Landing page para proprietários
│   │
│   ├── /politica-de-privacidade
│   ├── /termos-de-uso
│   └── /sitemap/sitemap.xml
│
├── 📱 Links Externos
│   ├── Blog: https://blog.pilarhomes.com.br/
│   │   └── UTM: ?utm_source=sitePilarHomes&utm_medium=menu&utm_campaign=header
│   │
│   ├── Rede Pilar (Corretores): https://www.soupilar.com.br/
│   ├── WhatsApp: https://wa.me/551140403627
│   └── Instagram: https://www.instagram.com.br/pilarhomes_
│
└── 🔐 Área Restrita
    └── "Entrar" (botão no header - não mapeado)
```

---

## 👥 Stakeholders Identificados

### 1. **Compradores de Alto Padrão** 🔵
- **Perfil**: Pessoas físicas buscando imóveis residenciais de luxo (R$ 1,5M - R$ 60M+)
- **Necessidades**: Exclusividade, curadoria, atendimento personalizado
- **Touchpoints**: "Quero comprar", busca por bairros nobres, exclusivos

### 2. **Proprietários/Vendedores** 🟢
- **Perfil**: Donos de imóveis de alto padrão querendo vender
- **Necessidades**: Exposição qualificada, preço justo, discrição (off-market)
- **Touchpoints**: "Quero vender", "Anunciar meu Imóvel", Off-Market

### 3. **Corretores Independentes/Imobiliárias** 🟡
- **Perfil**: Profissionais do mercado imobiliário querendo se associar à Pilar
- **Necessidades**: Leads qualificados, rede de parceiros, ferramentas
- **Touchpoints**: "Sou corretor", Rede Pilar (soupilar.com.br)

### 4. **Influenciadores/Curadores** 🎨
- **Perfil**: Personalidades de design e arquitetura
- **Necessidades**: Exposição de marca, conteúdo exclusivo
- **Touchpoints**: Coleções assinadas

---

## 🛤️ Jornadas dos Stakeholders

### 🔵 JORNADA DO COMPRADOR

#### **Fase 1: Descoberta e Inspiração**
```
1. Landing → Homepage
   ├── Visualiza hero "O endereço dos melhores endereços"
   ├── Vê números de credibilidade (R$ 3 bilhões negociados)
   └── Explora seções:
       ├── "Nossas Regiões" (6 macro-regiões)
       ├── "Exclusivos PilarHomes" (carrossel)
       └── "Bairros em Destaque" (8 bairros nobres)

2. Inspiração por Curadoria
   ├── Descobre "Curadorias Assinadas"
   ├── Clica em coleção de influenciador (ex: Lucila Zahran)
   └── Navega por imóveis selecionados por referência de design
```

**CTAs nesta fase**:
- "Explorar imóveis"
- "Ver bairro"
- Links de coleções

---

#### **Fase 2: Busca e Filtragem**
```
3. Busca Inicial
   ├── Opção A: Usa busca no hero
   │   ├── Seleciona cidade/região (combobox)
   │   └── Seleciona bairro/endereço (combobox dependente)
   │
   ├── Opção B: Clica em região específica
   │   └── Ex: "São Paulo" → /venda/imoveis/sp-brasil?macroregions=São+Paulo
   │
   └── Opção C: Clica em bairro de destaque
       └── Ex: "Itaim Bibi" → /bairros/itaim-bibi

4. Refinamento
   ├── Na página de busca, aplica filtros:
   │   ├── Tipo de imóvel (Apartamento, Casa, Cobertura, Duplex)
   │   ├── Exclusividade (checkbox "Exclusivos PilarHomes")
   │   └── Proximidade (POI: parques, clubes, ruas específicas)
   │
   └── Navega por URLs estruturadas:
       └── /venda/imoveis/{bairro}-{cidade}/apartamento?regions=...&cities=...
```

**CTAs nesta fase**:
- "Apartamento", "Cobertura", "Duplex", "Casa"
- "Exclusivos PilarHomes"
- Links de ruas e POIs (Parque Ibirapuera, Rua Oscar Freire, etc.)

---

#### **Fase 3: Avaliação de Imóveis**
```
5. Visualização de Resultados
   ├── Vê cards de imóveis com:
   │   ├── Selo "Exclusivo" (se aplicável)
   │   ├── Foto do corretor + imobiliária
   │   ├── Preço, código, área, suítes, vagas
   │   └── Localização (bairro, cidade)
   │
   └── Interage com:
       ├── Carrossel de fotos do card
       └── CTA "Adicionar a minha coleção"

6. Detalhes do Imóvel
   ├── Clica no card → vai para /imovel/{codigo}/{slug}
   ├── Explora galeria completa de fotos
   ├── Vê informações completas (área, suítes, vagas, tipo)
   ├── Identifica corretor responsável
   └── Adiciona à coleção pessoal
```

**CTAs nesta fase**:
- "Ver todos" (na seção de exclusivos)
- Cards de imóveis (link para página de detalhe)
- "Adicionar a minha coleção"

---

#### **Fase 4: Contato e Conversão**
```
7. Decisão de Contato
   ├── Opção A: Contato via imóvel
   │   └── (Provavelmente formulário de interesse - não visível no snapshot)
   │
   ├── Opção B: Contato geral
   │   ├── Footer: contato@pilarhomes.com.br
   │   └── WhatsApp: (11) 4040-3627
   │
   └── Opção C: Login para recursos premium
       └── Botão "Entrar" no header

8. Relacionamento Contínuo
   ├── Gerencia "Minha Coleção" (/colecoes/minha-colecao)
   ├── Compartilha coleções com familiares/amigos
   └── Recebe acompanhamento do corretor especialista
```

**CTAs nesta fase**:
- "Entrar" (header)
- "Quero comprar" (botão principal)
- Links de contato (email, WhatsApp)
- "Coleções Compartilhadas"

---

### 🟢 JORNADA DO VENDEDOR/PROPRIETÁRIO

#### **Fase 1: Descoberta da Pilar**
```
1. Chegada ao Site
   ├── Homepage → visualiza propostas de valor:
   │   ├── "R$ 3 bilhões negociados nos últimos 12 meses"
   │   ├── "Conexão direta com corretores especialistas"
   │   └── "Maior portfólio atualizado"
   │
   └── Identifica CTA "Quero vender"

2. Exploração de Diferenciais
   ├── Lê "O que dizem nossos clientes"
   │   └── Depoimento de Silvia Berger:
   │       "Sabrina mudou minha visão sobre corretores...
   │        vendeu meu apartamento em poucos meses após
   │        mais de um ano sem sucesso"
   │
   └── Descobre "Off-Market"
       └── "Privacidade para imóveis de alto valor não anunciados"
```

**CTAs nesta fase**:
- "Quero vender" (botão principal)
- Link "Off-Market"
- Depoimentos de clientes (prova social)

---

#### **Fase 2: Avaliação e Decisão**
```
3. Opções de Anúncio
   ├── Opção A: Anúncio Público
   │   └── Clica "Quero vender" ou "Anunciar meu Imóvel"
   │       → vai para /anunciar-imovel
   │
   └── Opção B: Discrição (Off-Market)
       └── Clica "Off-Market"
           → vai para /off-market
           └── "Privacidade para imóveis de alto valor não anunciados"

4. Conhecendo a Rede
   ├── Navega por "Sobre a Pilar" (/sobre-a-pilar)
   │   └── "Transformando o Mercado Imobiliário"
   │       └── "Conectamos compradores e vendedores a corretores
   │            especialistas com acesso ao maior portfólio de
   │            imóveis de alto padrão de São Paulo"
   │
   └── Vê exemplos de Exclusivos PilarHomes
       └── Entende o posicionamento premium
```

**CTAs nesta fase**:
- "Anunciar meu Imóvel" (/anunciar-imovel)
- "Off-Market" (/off-market)
- "Sobre a Pilar" (footer e header)

---

#### **Fase 3: Cadastro e Conversão**
```
5. Preenchimento de Formulário
   ├── Em /anunciar-imovel ou /off-market
   ├── Fornece informações do imóvel:
   │   ├── Tipo, localização, características
   │   ├── Expectativa de preço
   │   └── Preferência de discrição
   │
   └── Submete solicitação

6. Contato Inicial
   ├── Recebe contato de especialista da rede Pilar
   │   └── Horário comercial: Segunda a sexta, 9h-18h
   │       → WhatsApp (11) 4040-3627
   │       → Email contato@pilarhomes.com.br
   │
   └── Agendamento de visita/avaliação
```

**CTAs nesta fase**:
- Formulário em /anunciar-imovel
- Formulário em /off-market
- WhatsApp e Email (footer)

---

#### **Fase 4: Acompanhamento**
```
7. Gestão do Anúncio
   ├── Se público:
   │   ├── Imóvel publicado em /venda/imoveis/...
   │   ├── Selo "Exclusivo PilarHomes" (se parceria exclusiva)
   │   └── Aparece em homepage (carrossel de exclusivos)
   │
   └── Se Off-Market:
       └── Apresentação restrita a compradores qualificados

8. Fechamento
   ├── Corretor gerencia negociação
   ├── Vendedor recebe relatórios de visitação
   └── Conversão em venda
```

**CTAs nesta fase**:
- Login para área do proprietário (botão "Entrar")
- Contato direto com corretor

---

### 🟡 JORNADA DO CORRETOR/IMOBILIÁRIA

#### **Fase 1: Descoberta da Rede Pilar**
```
1. Chegada ao Site
   ├── Homepage → identifica CTA "Sou corretor"
   │
   └── Lê propostas de valor:
       ├── "R$ 3 bilhões negociados nos últimos 12 meses"
       ├── "Atendimento sob medida"
       └── "Maior portfólio atualizado"

2. Exploração de Benefícios
   ├── Vê depoimentos de corretores parceiros:
   │   ├── Renata Castro - Oásis Urbanos
   │   ├── Sabrina Lapyda - Mosaic Homes
   │   ├── André Sarubbi - Open Imóveis
   │   └── Eduardo Pontes (independente)
   │
   └── Nota presença de múltiplas imobiliárias:
       ├── Valsa Homes, Casa Valente, Sabiá Imóveis
       ├── Costa Cesar Imóveis, Amenities, Homesphere
       └── Galleria de Imóveis
```

**CTAs nesta fase**:
- "Sou corretor" (botão principal)
- Depoimentos de corretores parceiros
- Logos de imobiliárias parceiras

---

#### **Fase 2: Entendimento do Modelo**
```
3. Investigação da Rede
   ├── Clica "Sou corretor"
   │   └── Provavelmente redireciona para formulário ou
   │       modal com Typeform: ?typeform=lead-broker
   │
   └── Visita "Conheça a Rede Pilar"
       → https://www.soupilar.com.br/ (site externo)
       └── Descobre:
           ├── Modelo de parceria
           ├── Benefícios da rede
           └── Requisitos de adesão

4. Avaliação de Portfólio
   ├── Navega por imóveis em destaque
   │   └── Vê qualidade do portfólio (R$ 1,5M - R$ 60M)
   │
   └── Observa estrutura de apresentação:
       ├── Fotos profissionais
       ├── Informações completas
       └── Destaque para corretor responsável
           (foto + nome + logo imobiliária)
```

**CTAs nesta fase**:
- Link "Conheça a Rede Pilar" (https://www.soupilar.com.br/)
- Formulário "Sou corretor"
- Navegação por imóveis de parceiros

---

#### **Fase 3: Cadastro e Integração**
```
5. Submissão de Interesse
   ├── Preenche formulário "Sou corretor"
   │   ├── Dados pessoais e profissionais
   │   ├── CRECI
   │   ├── Área de atuação
   │   └── Imobiliária (se associado)
   │
   └── Recebe contato da equipe Pilar

6. Onboarding
   ├── Treinamento em plataforma Pilar
   ├── Acesso a ferramentas:
   │   ├── CRM
   │   ├── Publicação de imóveis
   │   └── Gestão de leads
   │
   └── Integração com rede de corretores
```

**CTAs nesta fase**:
- Formulário de cadastro (após "Sou corretor")
- Email de contato: contato@pilarhomes.com.br
- WhatsApp (11) 4040-3627

---

#### **Fase 4: Uso da Plataforma**
```
7. Publicação de Imóveis
   ├── Login via "Entrar" (header)
   ├── Acessa painel do corretor (não mapeado no snapshot)
   ├── Cadastra imóveis:
   │   ├── Escolhe exposição (pública ou off-market)
   │   ├── Upload de fotos profissionais
   │   └── Detalhamento completo
   │
   └── Imóvel publicado em:
       ├── /venda/imoveis/... (busca pública)
       ├── /bairros/{bairro} (páginas de bairro)
       └── Homepage (se exclusivo)

8. Gestão de Leads
   ├── Recebe leads qualificados:
   │   ├── Compradores que adicionaram imóvel à coleção
   │   ├── Solicitações de visita
   │   └── Contatos via formulário
   │
   └── Acompanha métricas:
       ├── Visualizações
       ├── Favoritos
       └── Taxa de conversão
```

**CTAs nesta fase**:
- "Entrar" (acesso à área do corretor)
- Publicação de imóveis (painel interno)
- Notificações de leads

---

### 🎨 JORNADA DO INFLUENCIADOR/CURADOR

#### **Fase 1: Parceria Inicial**
```
1. Convite da Pilar
   ├── Equipe Pilar identifica influenciador relevante:
   │   ├── Design de interiores
   │   ├── Arquitetura
   │   └── Lifestyle/Alto padrão
   │
   └── Propõe parceria de curadoria

2. Seleção de Imóveis
   ├── Influenciador escolhe imóveis do portfólio Pilar
   ├── Critérios:
   │   ├── Alinhamento com estética pessoal
   │   ├── Características arquitetônicas únicas
   │   └── Localizações premium
   │
   └── Exemplos atuais:
       ├── Lucila Zahran Turqueto (casadevalentina)
       ├── Fernanda Berendt (@CASA+)
       └── Nicole Gomes (revista Casa e Jardim)
```

---

#### **Fase 2: Publicação da Coleção**
```
3. Criação de Landing Page
   ├── URL estruturada: /colecao/{nome-influenciador}
   ├── Conteúdo:
   │   ├── Foto e bio do curador
   │   ├── Texto introdutório:
   │       └── "Conheça os imóveis favoritos de [NOME],
   │            referência em [ÁREA] no mundo digital"
   │   ├── Localização principal (ex: "São Paulo")
   │   └── Grid de imóveis selecionados
   │
   └── Aparece em homepage:
       └── Seção "Curadorias Assinadas" (carrossel com 3 curadores)

4. Promoção Cruzada
   ├── Pilar divulga:
   │   ├── Homepage (seção dedicada)
   │   ├── Instagram (@pilarhomes_)
   │   └── Email marketing
   │
   └── Influenciador divulga:
       ├── Redes sociais próprias
       ├── Blog/site pessoal
       └── Stories e posts patrocinados
```

---

#### **Fase 3: Engajamento**
```
5. Tráfego Qualificado
   ├── Seguidores do influenciador acessam:
   │   └── /colecao/{nome-influenciador}
   │
   ├── Exploram imóveis curados
   └── Seguem jornada de comprador (Fases 3-4)

6. Métricas e Retorno
   ├── Pilar acompanha:
   │   ├── Acessos à página da coleção
   │   ├── Taxa de conversão (leads gerados)
   │   └── Imóveis vendidos via curadoria
   │
   └── Influenciador recebe:
       ├── Exposição de marca
       ├── Posicionamento premium
       └── (Possivelmente) Comissão ou pagamento fixo
```

---

## 🎯 Principais CTAs por Stakeholder

### Para Compradores 🔵
| CTA | Localização | Destino | Objetivo |
|-----|-------------|---------|----------|
| **"Explorar imóveis"** | Hero (homepage) | /venda/imoveis/ | Iniciar busca |
| **"Quero comprar"** | Homepage (seção de propostas) | Formulário/Typeform | Cadastro de interesse |
| **"Exclusivos PilarHomes"** | Homepage, carrosséis | /venda/imoveis/?isExclusive=true | Acesso a exclusividade |
| **"Ver bairro"** | Cards de bairros | /bairros/{bairro} | Exploração geográfica |
| **"Adicionar a minha coleção"** | Cards de imóveis | /colecoes/minha-colecao | Salvar favoritos |
| **Coleções de Influenciadores** | Seção "Curadorias" | /colecao/{nome} | Inspiração curada |
| **"Off-Market"** | Homepage, carrossel | /off-market | Acesso a imóveis discretos |

### Para Vendedores 🟢
| CTA | Localização | Destino | Objetivo |
|-----|-------------|---------|----------|
| **"Quero vender"** | Homepage (seção de propostas) | Formulário/Typeform | Cadastro de propriedade |
| **"Anunciar meu Imóvel"** | Footer, links internos | /anunciar-imovel | Landing page de venda |
| **"Off-Market"** | Homepage, footer | /off-market | Venda discreta |
| **"Sobre a Pilar"** | Header, footer | /sobre-a-pilar | Conhecer empresa |
| **WhatsApp (11) 4040-3627** | Footer | WhatsApp direto | Contato imediato |
| **contato@pilarhomes.com.br** | Footer | Email | Contato formal |

### Para Corretores 🟡
| CTA | Localização | Destino | Objetivo |
|-----|-------------|---------|----------|
| **"Sou corretor"** | Homepage (seção de propostas) | Formulário/Typeform | Cadastro de interesse |
| **"Conheça a Rede Pilar"** | Footer | https://www.soupilar.com.br/ | Site da rede (externo) |
| **"Entrar"** | Header | Login/Área do corretor | Acesso à plataforma |
| **"Seja um Parceiro Pilar"** | Footer (título de seção) | Links de corretor | Navegação institucional |

---

## 🔄 Fluxos de Interação Críticos

### 🔍 **Fluxo de Busca de Imóveis**
```
Homepage
  ↓
Busca no Hero (Cidade + Bairro)
  ↓
/venda/imoveis/{cidade}/?regions={bairro}
  ↓
Aplicação de Filtros (Tipo, Exclusividade, POI)
  ↓
Visualização de Resultados (Grid de cards)
  ↓
Clique em Card de Imóvel
  ↓
/imovel/{codigo}/{slug}
  ↓
[Ação do Usuário]
  ├─→ Adicionar à Coleção → /colecoes/minha-colecao
  ├─→ Contatar Corretor → Formulário/WhatsApp
  └─→ Voltar à Busca → Navegação reversa
```

### 💾 **Fluxo de Coleções Compartilhadas**
```
Navegando Imóveis
  ↓
Clica "Adicionar a minha coleção" (em vários imóveis)
  ↓
Acessa "Minha Coleção" (/colecoes/minha-colecao)
  ↓
Revisa imóveis salvos
  ↓
[Opção A] Compartilha coleção
  ├─→ Gera link único
  └─→ Envia para familiares/parceiros
      ↓
      Destinatários acessam coleção compartilhada
      ↓
      Comentam/favoritam imóveis
      ↓
      Decisão colaborativa

[Opção B] Contata corretor
  └─→ Solicita visitas para imóveis da coleção
```

### 🤝 **Fluxo de Conversão (Lead)**
```
[Qualquer página do site]
  ↓
Usuário decide entrar em contato
  ↓
[Opção A - Formulário Web]
  ├─→ Clica CTA contextual ("Quero comprar", "Quero vender", etc.)
  ├─→ Preenche formulário/Typeform
  ├─→ Submete dados
  └─→ Confirmação de recebimento
      ↓
      Distribuição interna:
        ├─→ Se comprador: direcionado para corretor especialista do bairro
        ├─→ Se vendedor: direcionado para equipe de avaliação
        └─→ Se corretor: direcionado para RH/Parcerias

[Opção B - Contato Direto]
  ├─→ WhatsApp (11) 4040-3627
  └─→ Email contato@pilarhomes.com.br
      ↓
      Atendimento humano (Seg-Sex, 9h-18h)
      ↓
      Qualificação de lead
      ↓
      Encaminhamento para especialista

[Opção C - Login]
  └─→ Clica "Entrar" (header)
      ↓
      Acessa área personalizada
      ↓
      [Se novo usuário] Cadastro
      [Se usuário existente] Dashboard
```

---

## 📊 Hierarquia de Navegação

### **Navegação Primária** (Header)
```
┌─────────────────────────────────────────────────────┐
│ [Logo PilarHomes]                                   │
│                                                     │
│  [Comprar ▼]  [Vender ▼]  [Blog]  [Sobre a Pilar]│
│                                                     │
│                                    [Entrar]        │
└─────────────────────────────────────────────────────┘
```
- **Comprar** e **Vender**: Dropdowns (buttons com aria-expanded)
- **Blog**: Link externo (blog.pilarhomes.com.br) com UTM tracking
- **Sobre a Pilar**: Link interno (/sobre-a-pilar)
- **Entrar**: Login/área do usuário

### **Navegação Secundária** (Homepage Sections)
1. **Hero Section**: Busca principal + CTAs stakeholder
2. **Propostas de Valor**: 3 pilares + 3 CTAs (Quero comprar/vender/Sou corretor)
3. **Produtos Especializados**: Exclusivos, Coleções, Off-Market
4. **Nossas Regiões**: 6 macro-regiões (carrossel)
5. **Exclusivos PilarHomes**: Carrossel de 12+ imóveis
6. **Bairros em Destaque**: Carrossel de 8 bairros
7. **Curadorias Assinadas**: 3 influenciadores
8. **Depoimentos**: 4 testemunhos
9. **SEO Links**: 30+ links de cauda longa

### **Navegação Terciária** (Footer)
```
┌───────────────┬───────────────┬───────────────┬───────────────┐
│ Sobre nós     │ Seja Parceiro │ Comprar/Vender│ Fale Conosco  │
├───────────────┼───────────────┼───────────────┼───────────────┤
│ Sobre a Pilar │ Conheça a Rede│ Exclusivos    │ email         │
│               │ Pilar         │ Anunciar      │ whatsapp      │
│               │ Blog          │ Off-Market    │ horário       │
└───────────────┴───────────────┴───────────────┴───────────────┘

┌─────────────────────────────────────────────────────┐
│ [Transformando o Mercado Imobiliário]               │
│ Conectamos compradores e vendedores a corretores... │
│ [Sobre a Pilar]                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ [Política de Privacidade] [Termos de Uso] [Sitemap]│
│ [Instagram]                                         │
│ © 2025 Pilar. CRECI 39836-J. Todos os direitos...  │
└─────────────────────────────────────────────────────┘
```

---

## 🔑 Padrões de URL Identificados

### **Busca de Imóveis**
```
Padrão geral:
/venda/imoveis/{localizacao}/{tipo-imovel}?{filtros}

Exemplos:
1. Por macro-região:
   /venda/imoveis/sp-brasil?macroregions=São+Paulo

2. Por cidade:
   /venda/imoveis/sao-paulo-sp-brasil

3. Por bairro + tipo:
   /venda/imoveis/itaim-bibi-sao-paulo-sp-brasil/apartamento
   ?regions=Itaim+Bibi&cities=São+Paulo

4. Por exclusividade:
   /venda/imoveis/sao-paulo-sp-brasil?isExclusive=true&cities=São+Paulo

5. Por endereço (POI):
   /venda/imoveis/sp-brasil/Rua%20Oscar%20Freire,.../apartamento
   ?poiLocationLat=-23.5686704&poiLocationLng=-46.6626754
```

### **Páginas de Imóveis**
```
Padrão:
/imovel/{CODIGO}/{tipo-quartos-bairro-cidade}

Exemplos:
- /imovel/VA040/casa-de-condominio-4-quartos-campo-comprido-curitiba
- /imovel/HS27071/apartamento-3-quartos-itaim-bibi-sao-paulo
- /imovel/AMS046/casa-4-quartos-jardim-paulista-sao-paulo

Estrutura de código:
- VA040: Valsa Homes
- SB285: Sabiá Imóveis
- COC108: Costa Cesar Imóveis
- HS27071: Homesphere
- AMS046: Amenities
- GA082: Galleria de Imóveis
- CASAV037: Casa Valente
```

### **Coleções**
```
Padrão:
/colecao/{nome-curador} ou /colecoes/{tipo}

Exemplos:
- /colecao/casadevalentina
- /colecao/fernanda-berendt
- /colecao/nicole-gomes
- /colecoes/minha-colecao (usuário logado)
```

### **Páginas de Bairros**
```
Padrão:
/bairros/{nome-bairro}

Exemplo:
- /bairros/itaim-bibi

(Provavelmente template único reutilizado para 20+ bairros)
```

---

## 🎨 Elementos de UX por Stakeholder

### Para Compradores 🔵
**Elementos de Confiança**:
- ✅ Números de credibilidade: "R$ 3 bilhões negociados"
- ✅ Depoimentos de clientes (Marina, Silvia, Horácio, Adriana)
- ✅ Fotos dos corretores em cada imóvel
- ✅ Logos de imobiliárias parceiras

**Elementos de Curadoria**:
- ✅ Selo "Exclusivo" em imóveis
- ✅ Coleções de influenciadores (Lucila, Fernanda, Nicole)
- ✅ "Imóveis únicos que você só encontra aqui"

**Elementos de Facilidade**:
- ✅ Busca dupla (Cidade → Bairro) com combobox dependente
- ✅ Carrosséis em várias seções (regiões, bairros, imóveis)
- ✅ "Adicionar a minha coleção" (salvar favoritos)
- ✅ Links diretos por tipo de imóvel (Apartamento, Casa, Cobertura)

### Para Vendedores 🟢
**Elementos de Diferenciação**:
- ✅ "Atendimento sob medida" (proposta de valor)
- ✅ "Off-Market" (discrição para imóveis de alto valor)
- ✅ Depoimento de Silvia Berger (vendedora satisfeita)

**Elementos de Credibilidade**:
- ✅ CRECI 39836-J (rodapé)
- ✅ Horário de atendimento transparente (Seg-Sex, 9h-18h)
- ✅ Múltiplos canais de contato (email, WhatsApp)

### Para Corretores 🟡
**Elementos de Oportunidade**:
- ✅ "Mais de R$ 3 bilhões negociados" (volume de mercado)
- ✅ "Maior portfólio atualizado" (leads qualificados)
- ✅ Destaque individual em cada imóvel (foto + nome + logo)

**Elementos de Rede**:
- ✅ Múltiplas imobiliárias parceiras visíveis (8+ logos)
- ✅ Depoimentos de corretores bem-sucedidos
- ✅ Link "Conheça a Rede Pilar" (soupilar.com.br)

---

## 📈 Otimizações SEO Observadas

### **Long-Tail Keywords (Cauda Longa)**
A homepage possui 2 seções inteiras dedicadas a SEO:

#### **1. Tipos de imóvel por Bairro**
- 15 links estruturados:
  - "Apartamentos em Moema"
  - "Casas em Morumbi"
  - "Coberturas em Vila Madalena"
  - "Casas de condomínio em Alto da Boa Vista"

#### **2. Imóveis por Endereço e POI**
- 15 links estruturados:
  - "Rua Haddock Lobo"
  - "Apartamentos em Rua Oscar Freire"
  - "Imóveis próximos ao Parque do Ibirapuera"
  - "Imóveis próximos ao Clube Athletico Paulistano"

**Estratégia**: Capturar buscas específicas no Google:
- ✅ "apartamento moema"
- ✅ "casa jardim paulista"
- ✅ "cobertura vila mariana"
- ✅ "apartamento rua oscar freire"
- ✅ "imóvel próximo parque ibirapuera"

### **Breadcrumb Semântico em URLs**
```
/venda/imoveis/itaim-bibi-sao-paulo-sp-brasil/apartamento
           └─────┬─────┘ └──┬──┘ └┬┘ └──┬──┘ └────┬────┘
              bairro    cidade  UF  país    tipo
```

### **Sitemap XML**
- Link no footer: https://pilarhomes.com.br/sitemap/sitemap.xml
- Facilita indexação por motores de busca

---

## 🚀 Oportunidades de Melhoria (Insights)

### **1. Navegação**
⚠️ **Menus "Comprar" e "Vender" não abertos**: Os dropdowns não foram capturados no snapshot (buttons com aria-expanded). Sugestão:
- Revelar estrutura completa dos menus
- Adicionar megamenu com destaques visuais

### **2. Jornada do Usuário Logado**
⚠️ **Área "Entrar" não mapeada**: Não há informações sobre:
- Dashboard do comprador (coleções, histórico de buscas)
- Painel do corretor (publicação de imóveis, leads)
- Área do proprietário (status de anúncio)

Sugestão: Documentar jornadas pós-login separadamente

### **3. Mobile Experience**
⚠️ **Snapshot capturado em desktop**: Não há visibilidade sobre:
- Menu hamburger (mobile)
- Busca simplificada (mobile)
- CTAs em telas menores

Sugestão: Tirar snapshot em viewport mobile (375x667)

### **4. Formulários de Conversão**
⚠️ **CTAs levam a Typeform ou páginas não mapeadas**:
- "Quero comprar" → ?
- "Quero vender" → /anunciar-imovel (não visitada)
- "Sou corretor" → ?typeform=lead-broker (externo)

Sugestão: Mapear fluxos completos de formulários

### **5. Filtros Avançados**
⚠️ **Página de busca não visitada**: Faltam informações sobre:
- Filtros de preço (min/max)
- Filtros de área (m²)
- Filtros de quartos/suítes/vagas
- Ordenação (relevância, preço, data)

Sugestão: Navegar para /venda/imoveis/ e documentar filtros

---

## 📊 Métricas Sugeridas por Jornada

### **Comprador 🔵**
- **Topo de Funil**: Acessos à homepage, tempo médio na página
- **Meio de Funil**: 
  - Taxa de uso da busca (hero vs. cliques em regiões)
  - Páginas por sessão (navegação entre bairros/imóveis)
  - Taxa de adição à coleção
- **Fundo de Funil**: 
  - Taxa de conversão (formulário enviado ou contato)
  - Imóveis visualizados antes de conversão
  - Tempo até conversão (dias)

### **Vendedor 🟢**
- **Topo de Funil**: Cliques em "Quero vender" e "Off-Market"
- **Meio de Funil**: 
  - Taxa de preenchimento do formulário (/anunciar-imovel)
  - Visualizações de "Sobre a Pilar"
  - Leitura de depoimentos
- **Fundo de Funil**: 
  - Taxa de conversão (formulário enviado)
  - Taxa de fechamento de contrato
  - Tempo até publicação do imóvel

### **Corretor 🟡**
- **Topo de Funil**: Cliques em "Sou corretor" e "Conheça a Rede Pilar"
- **Meio de Funil**: 
  - Taxa de preenchimento do formulário de interesse
  - Taxa de acesso ao soupilar.com.br
- **Fundo de Funil**: 
  - Taxa de conversão (corretor onboarded)
  - Tempo até primeira publicação de imóvel
  - Número de imóveis publicados no primeiro mês

---

## 🎯 Conclusão

O **PilarHomes** possui uma arquitetura de informação bem estruturada com **foco em 3 stakeholders distintos**:

1. **Compradores de alto padrão** 🔵 - jornada orientada a curadoria, exclusividade e confiança
2. **Proprietários/Vendedores** 🟢 - jornada orientada a discrição, especialização e resultados
3. **Corretores/Imobiliárias** 🟡 - jornada orientada a oportunidade, rede e ferramentas

### **Forças**:
✅ Propostas de valor claras para cada stakeholder  
✅ CTAs específicos e bem posicionados  
✅ Curadoria de conteúdo (influenciadores, exclusivos, off-market)  
✅ Prova social (depoimentos, números, logos de parceiros)  
✅ SEO robusto (long-tail, URLs semânticas, sitemap)  
✅ Múltiplos pontos de entrada (busca, regiões, bairros, POIs)  

### **Áreas para Exploração**:
⚠️ Menus dropdown não mapeados  
⚠️ Jornadas pós-login não documentadas  
⚠️ Filtros avançados de busca não visitados  
⚠️ Formulários de conversão não detalhados  
⚠️ Experiência mobile não analisada  

---

**Data de Análise**: Janeiro 2025  
**Ferramenta**: Chrome DevTools MCP  
**Páginas Analisadas**: Homepage + 84 URLs mapeadas  
**Status**: ✅ Completo (Fase 1 - Sitemap e Jornadas Principais)
