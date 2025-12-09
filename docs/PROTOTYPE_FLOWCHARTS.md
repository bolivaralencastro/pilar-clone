# Fluxogramas de Navegação - Protótipo PilarHomes

Este documento detalha os fluxos de navegação e interação das principais páginas do protótipo: Home, Resultados (Busca), Curadoria e Detalhe do Imóvel (Single Page).

## 1. Home (Página Inicial)
**Arquivo:** `components/prototypes/HomeV2.vue`

A Home serve como o ponto central de entrada, direcionando o usuário para fluxos de compra, venda ou exploração de coleções.

```mermaid
flowchart TD
    %% Nós Principais
    Start((Início)) --> Home[HomeV2.vue<br/>Landing Page]
    
    %% Seções da Home
    subgraph Hero [Hero Section]
        SearchInput[Barra de Busca]
        VideoBg[Vídeo Background]
    end
    
    subgraph Sections [Seções de Conteúdo]
        Selected[Selecionados para Você<br/>Carrossel]
        NavMono[Navegação Monocromática]
        Regions[Regiões<br/>Carrossel]
        Exclusive[Exclusivos PilarHomes]
        Collections[Coleções Curadas]
    end
    
    %% Conexões Internas
    Home --> Hero
    Home --> Sections
    
    %% Ações de Navegação
    SearchInput -->|Enter/Click| ResultsPage[SearchResultsV2.vue<br/>Resultados de Busca]
    
    Selected -->|Click Card| PropertyDetail[PropertyDetailV2.vue<br/>Detalhe do Imóvel]
    Selected -->|Ver Todos| ResultsPage
    
    NavMono -->|Quero Comprar| ResultsPage
    NavMono -->|Quero Vender| SellerForm[Formulário de Venda]
    NavMono -->|Sou Corretor| BrokerForm[Cadastro de Corretor]
    
    Regions -->|Click Região| ResultsPageFiltered[Resultados Filtrados<br/>por Região]
    
    Exclusive -->|Click Card| PropertyDetail
    Exclusive -->|Ver Todos| ResultsPage
    
    Collections -->|Click Coleção| CurationPage[CurationV2.vue<br/>Página de Curadoria]
    
    %% Estilização
    classDef page fill:#f9f,stroke:#333,stroke-width:2px;
    classDef component fill:#e1f5fe,stroke:#0277bd,stroke-width:1px;
    classDef action fill:#fff9c4,stroke:#fbc02d,stroke-width:1px;
    
    class Home,ResultsPage,PropertyDetail,CurationPage page;
    class SearchInput,Selected,NavMono,Regions,Exclusive,Collections component;
```

## 2. Resultados de Busca & Curadoria
**Arquivos:** `SearchResultsV2.vue` e `CurationV2.vue`

Estas páginas compartilham estruturas similares de listagem, mas com propósitos diferentes (exploração vs. coleções temáticas).

```mermaid
flowchart TD
    %% Estados Iniciais
    subgraph Pages [Páginas de Listagem]
        Results[SearchResultsV2.vue<br/>Busca Geral]
        Curation[CurationV2.vue<br/>Curadoria/Coleções]
    end

    %% Componentes de Controle
    subgraph Controls [Barra de Controle Sticky]
        Filters[Painel de Filtros]
        Sort[Ordenação]
        ViewToggle[Alternar Mapa/Grid]
        CompareToggle[Modo Comparação]
    end

    %% Componentes de Interface
    subgraph UI [Interface Principal]
        Grid[Grid de Cards]
        Map[Mapa Interativo]
        FloatBar[ComparisonFloatingBar.vue<br/>Barra Flutuante]
    end

    %% Fluxo Resultados
    Results --> Controls
    Results --> Grid
    
    %% Fluxo Curadoria
    Curation --> Controls
    Curation --> Grid
    Curation -->|Tabs| SwitchCollection[Trocar Coleção]

    %% Interações
    ViewToggle -->|Click| Map
    CompareToggle -->|Ativar| SelectionMode[Modo de Seleção Ativo]
    
    SelectionMode -->|Selecionar Imóveis| FloatBar
    FloatBar -->|Click Comparar| ComparePage[ComparisonView.vue<br/>Comparador Side-by-Side]
    
    Grid -->|Click Card| Detail[PropertyDetailV2.vue<br/>Detalhe do Imóvel]
    Map -->|Click Pin| Detail

    %% Estilização
    classDef page fill:#f9f,stroke:#333,stroke-width:2px;
    classDef ui fill:#e1f5fe,stroke:#0277bd,stroke-width:1px;
    classDef logic fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px;

    class Results,Curation,ComparePage,Detail page;
    class Grid,Map,FloatBar,Filters ui;
    class SelectionMode logic;
```

## 3. Detalhe do Imóvel (Single Page)
**Arquivo:** `PropertyDetailV2.vue`

Página de imersão total no imóvel, com foco em conversão e análise.

```mermaid
flowchart TD
    %% Página Principal
    Detail[PropertyDetailV2.vue<br/>Detalhe do Imóvel]
    
    %% Seções
    subgraph Content [Conteúdo Rico]
        Gallery[Galeria Fullscreen]
        Info[Informações Principais]
        Specs[Características & Comodidades]
        MapSection[Localização]
    end
    
    %% Ações Flutuantes / Header
    subgraph Actions [Ações de Conversão]
        Contact[Contatar Concierge]
        Schedule[Agendar Visita]
        Share[Compartilhar]
        Save[Salvar/Favoritar]
    end
    
    %% Fluxos Avançados
    subgraph Advanced [Fluxos Avançados]
        AIAnalysis[Análise de Valor (IA)]
        AddToCompare[Adicionar à Comparação]
    end

    %% Conexões
    Detail --> Content
    Detail --> Actions
    
    %% Interações
    Gallery -->|Navegar| ViewImages[Visualizar Fotos]
    
    Contact -->|Click| WhatsApp[WhatsApp / Chat]
    Schedule -->|Click| CalendarModal[Modal de Agendamento]
    
    AddToCompare -->|Click| FloatBar[ComparisonFloatingBar.vue]
    FloatBar -->|Comparar| ComparePage[ComparisonView.vue]
    
    AIAnalysis -->|Click| AIModal[Modal de Insights de Preço]

    %% Estilização
    classDef page fill:#f9f,stroke:#333,stroke-width:2px;
    classDef section fill:#fff3e0,stroke:#ef6c00,stroke-width:1px;
    classDef external fill:#eceff1,stroke:#455a64,stroke-width:1px;

    class Detail,ComparePage page;
    class Gallery,Info,Specs,MapSection section;
    class WhatsApp,CalendarModal,AIModal external;
```

## 4. Fluxo Global de Comparação
**Arquivo:** `ComparisonView.vue`

O fluxo de comparação conecta diferentes pontos da jornada do usuário.

```mermaid
flowchart LR
    %% Origens
    Results[Resultados] -->|Selecionar| Bar[Barra Flutuante]
    Curation[Curadoria] -->|Selecionar| Bar
    Detail[Detalhe] -->|Adicionar| Bar
    
    %% Barra
    Bar -->|Validar (>1)| CompareBtn[Botão Comparar]
    
    %% Página de Comparação
    CompareBtn --> View[ComparisonView.vue]
    
    subgraph CompareUI [Interface de Comparação]
        Header[Header Sticky]
        Accordion[Seções Expansíveis]
        DiffHighlight[Highlight de Diferenças]
    end
    
    View --> CompareUI
    
    %% Saídas
    CompareUI -->|Salvar| UserProfile[Perfil do Usuário]
    CompareUI -->|Concierge| Contact[Contato]
    CompareUI -->|Voltar| Previous[Página Anterior]

    %% Estilização
    classDef flow fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef ui fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px;

    class Results,Curation,Detail,View flow;
    class Bar,CompareUI ui;
```
