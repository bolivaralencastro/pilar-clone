<script setup lang="ts">
import AppIcon from '../../../components/AppIcon.vue'
import FlowchartViewer from '../../../components/FlowchartViewer.vue'
import MermaidRenderer from '../../../components/MermaidRenderer.vue'
import HomeV2 from '../../../components/prototypes/HomeV2.vue'
import SearchResultsV2 from '../../../components/prototypes/SearchResultsV2.vue'
import PropertyDetailV2 from '../../../components/prototypes/PropertyDetailV2.vue'
import CurationV2 from '../../../components/prototypes/CurationV2.vue'

const route = useRoute()
const router = useRouter()

const slug = route.params.slug as string

// Configuration for each prototype page
const prototypes = {
  home: {
    title: 'Home',
    description: 'Página inicial com nova proposta de valor e navegação simplificada.',
    newUrl: '/',
    oldUrl: 'https://www.pilarhomes.com.br/',
    mermaidCode: `
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
`,
    features: [
      'Hero section imersiva',
      'Busca simplificada',
      'Curadoria em destaque'
    ]
  },
  resultados: {
    title: 'Resultados de Busca',
    description: 'Listagem de imóveis com filtros avançados e visualização em mapa.',
    newUrl: '/?search=true',
    oldUrl: 'https://pilarhomes.com.br/venda/imoveis/sao-paulo-sp-brasil',
    mermaidCode: `
flowchart TD
    %% --- CAMADA DE NAVEGAÇÃO ---
    subgraph Navigation ["📍 Navegação & Páginas"]
        direction TB
        Home["🏠 Pág 01: Home<br/>(Porta de Entrada)"]
        Results["📋 Pág 02: Resultados<br/>(Busca & Mapa)"]
        Curation["✨ Pág 04: Curadoria<br/>(Coleções Temáticas)"]
        Details["💎 Pág 03: Detalhe (Single)<br/>(Imersão Total)"]

        %% Fluxo de navegação básica
        Home --> Results & Curation
        Results -.->|Clica no Card| Details
        Curation -.->|Clica no Card| Details
    end

    %% --- CAMADA DE PERSISTÊNCIA (BARRA FLUTUANTE) ---
    subgraph PersistentUI ["⚓ Barra Flutuante de Comparação"]
        direction TB
        %% Ações de adicionar à comparação vindas de várias origens
        ActionAdd["🖱️ Ação: Selecionar Card<br/>(Checkbox ou Botão)"]
        
        Results --> ActionAdd
        Curation --> ActionAdd
        Details --> ActionAdd
        
        ActionAdd --> FloatingBar["🚧 Barra Flutuante Ativa<br/>(Persiste no rodapé/topo)"]
        
        %% Lógica de Estado da Barra
        FloatingBar --> CheckState{"Qtd. Selecionada?"}
        
        CheckState -- "< 2 Imóveis" --> KeepBrowsing["👀 Botão 'Comparar' Inativo<br/>User continua navegando"]
        CheckState -- ">= 2 Imóveis" --> ReadyState["✅ Botão 'Comparar' Ativo"]
        
        %% O loop de persistência: volta para a navegação visualmente
        KeepBrowsing -.->|Barra permanece visível| Navigation
        ReadyState -.->|Barra permanece visível| Navigation
    end

    %% --- FLUXO DE EXECUÇÃO (COMPARAR) ---
    subgraph CompareFlow ["Tela de Comparação"]
        ReadyState -->|Clicou Comparar| ManualView["📊 Tabela Side-by-Side<br/>(Página de Comparação)"]
        ManualView --> Insights["💡 Insights de IA<br/>sobre a seleção"]
        ManualView --> Actions["⚡ Ações Finais:<br/>Agendar, Ofertar"]
    end

    %% --- FLUXO DE IA (EXCLUSIVO SINGLE PAGE) ---
    subgraph AIFlow ["Fluxo IA (Exclusivo Single-Page)"]
        direction TB
        Details -->|Botão 'Analisar Valor'| Analyze["🤖 Processar Análise IA"]
        Analyze --> AutoView["📈 Popup IA:<br/>Preço, Similares, Fatores"]
        
        %% Integração: Da IA para a Barra Flutuante
        AutoView -->|Botão 'Add à Comparação'| FloatingBar
    end

    %% --- ESTILIZAÇÃO ---
    classDef nav fill:#f1faee,stroke:#1d3557,stroke-width:2px,color:#1d3557,rx:5,ry:5
    classDef bar fill:#cdb4db,stroke:#5c2a9d,stroke-width:2px,color:#333,rx:10,ry:10
    classDef action fill:#bde0fe,stroke:#457b9d,stroke-width:1px,color:#1d3557,rx:5,ry:5
    classDef manual fill:#e9c46a,stroke:#d4a373,stroke-width:1px,color:#333,rx:5,ry:5
    classDef ai fill:#a2d2ff,stroke:#023e8a,stroke-width:1px,color:#1d3557,rx:5,ry:5
    classDef decision fill:#ffafcc,stroke:#e63946,stroke-width:1px,color:#333,rx:5,ry:5

    %% Aplicação das Classes
    class Home,Results,Curation,Details nav
    class FloatingBar,KeepBrowsing,ReadyState bar
    class ActionAdd action
    class ManualView,Insights,Actions manual
    class Analyze,AutoView ai
    class CheckState decision
`,
    features: [
      'Filtros laterais',
      'Visualização em mapa',
      'Cards informativos'
    ]
  },
  imovel: {
    title: 'Detalhe do Imóvel',
    description: 'Página de detalhes com foco na experiência visual e informações estruturadas.',
    newUrl: '/imovel/exemplo',
    oldUrl: 'https://pilarhomes.com.br/imovel/CA16821/cobertura-4-quartos-vila-romana-sao-paulo',
    mermaidCode: `
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
        AIAnalysis[Análise de Valor IA]
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
`,
    features: [
      'Galeria imersiva',
      'Informações técnicas claras',
      'Call to action contextual'
    ]
  },
  curadoria: {
    title: 'Curadoria (Imóveis Salvos)',
    description: 'Área exclusiva para o cliente gerenciar seus imóveis favoritos, com uma experiência de "coleção privada".',
    newUrl: '/curadoria',
    oldUrl: 'https://pilarhomes.com.br/venda/imoveis/sao-paulo-sp-brasil',
    mermaidCode: `
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
`,
    features: [
      'Visualização em galeria',
      'Notas pessoais',
      'Compartilhamento elegante'
    ]
  }
}

const currentPrototype = computed(() => prototypes[slug as keyof typeof prototypes])

// State
const activeTab = ref<'current' | 'flowchart' | 'new'>('current')
const viewMode = ref<'desktop' | 'mobile'>('desktop')
const isFullscreen = ref(false)
const showInfo = ref(false)
const showHeader = ref(true)

// Initialize tab from URL
const initTab = Array.isArray(route.query.tab) ? route.query.tab[0] : route.query.tab
if (initTab && ['current', 'flowchart', 'new'].includes(initTab)) {
  activeTab.value = initTab as 'current' | 'flowchart' | 'new'
}

// Initialize viewMode from URL
const initView = Array.isArray(route.query.view) ? route.query.view[0] : route.query.view
if (initView && ['desktop', 'mobile'].includes(initView)) {
  viewMode.value = initView as 'desktop' | 'mobile'
}

// Helper to update URL with current state
const updateUrl = () => {
  router.replace({ 
    query: { 
      ...route.query, 
      tab: activeTab.value,
      view: viewMode.value
    } 
  })
}

// Watchers
watch(activeTab, (newTab) => {
  if (newTab === 'flowchart') {
    viewMode.value = 'desktop'
  }
  
  // Update URL to make state shareable
  updateUrl()
})

// Watch viewMode changes
watch(viewMode, () => {
  updateUrl()
})

// Watch URL changes (back/forward navigation)
watch(() => route.query, (newQuery) => {
  const tab = Array.isArray(newQuery.tab) ? newQuery.tab[0] : newQuery.tab
  if (tab && ['current', 'flowchart', 'new'].includes(tab) && tab !== activeTab.value) {
    activeTab.value = tab as 'current' | 'flowchart' | 'new'
  }
  
  const view = Array.isArray(newQuery.view) ? newQuery.view[0] : newQuery.view
  if (view && ['desktop', 'mobile'].includes(view) && view !== viewMode.value) {
    viewMode.value = view as 'desktop' | 'mobile'
  }
}, { deep: true })

// Actions
const toggleFullscreen = () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen()
    isFullscreen.value = true
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen()
      isFullscreen.value = false
    }
  }
}

const toggleHeader = () => {
  showHeader.value = !showHeader.value
}

const handleKeydown = (e: KeyboardEvent) => {
  // Ignore if typing in an input
  if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) return

  if (e.key.toLowerCase() === 'h') {
    toggleHeader()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})

// Ensure we have a valid slug
if (!currentPrototype.value) {
  router.push('/prototipo')
}
</script>

<template>
  <div class="h-screen flex flex-col bg-porcelain overflow-hidden relative">
    <!-- Floating Header Toggle (Hover Area) -->
    <div 
      v-if="!showHeader"
      class="absolute top-0 right-0 z-50 w-32 h-32 flex items-start justify-end p-4 group"
    >
      <button 
        @click="showHeader = true"
        class="w-10 h-10 rounded-lg bg-white border border-subtle shadow-lg flex items-center justify-center text-secondary hover:text-text-primary transition-all duration-300 opacity-0 group-hover:opacity-100 transform -translate-y-2 group-hover:translate-y-0"
        title="Mostrar Menu (H)"
      >
        <AppIcon name="lni-menu" />
      </button>
    </div>

    <!-- Header -->
    <header v-if="showHeader" class="h-16 bg-white border-b border-subtle flex items-center justify-between px-6 shrink-0 z-20 relative">
      <!-- Left: Back & Title -->
      <div class="flex items-center gap-6">
        <NuxtLink to="/prototipo" class="w-8 h-8 flex items-center justify-center rounded-full hover:bg-surface-card transition-colors text-secondary hover:text-text-primary">
          <AppIcon name="lni-arrow-left" />
        </NuxtLink>
        
        <div class="h-8 w-px bg-subtle"></div>
        
        <div>
          <h1 class="text-sm font-medium text-text-primary">{{ currentPrototype?.title }}</h1>
          <span class="text-[10px] font-mono text-secondary uppercase tracking-widest">Protótipo de Alta Fidelidade</span>
        </div>
      </div>

      <!-- Center: Version Tabs -->
      <div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">
        <div class="bg-surface-subtle p-1.5 rounded-lg border border-border-subtle flex items-center gap-1.5">
          <button 
            @click="activeTab = 'current'"
            class="px-5 py-2 rounded-md text-xs font-semibold transition-all duration-200 uppercase tracking-wider"
            :class="activeTab === 'current' ? 'bg-text-primary text-white shadow-md' : 'text-text-secondary hover:text-text-primary hover:bg-surface-card'"
          >
            Versão Atual
          </button>
          <button 
            @click="activeTab = 'flowchart'"
            class="px-5 py-2 rounded-md text-xs font-semibold transition-all duration-200 uppercase tracking-wider"
            :class="activeTab === 'flowchart' ? 'bg-text-primary text-white shadow-md' : 'text-text-secondary hover:text-text-primary hover:bg-surface-card'"
          >
            Fluxograma
          </button>
          <button 
            @click="activeTab = 'new'"
            class="px-5 py-2 rounded-md text-xs font-semibold transition-all duration-200 uppercase tracking-wider"
            :class="activeTab === 'new' ? 'bg-text-primary text-white shadow-md' : 'text-text-secondary hover:text-text-primary hover:bg-surface-card'"
          >
            Nova Proposta
          </button>
        </div>
      </div>

      <!-- Right: Controls -->
      <div class="flex items-center gap-2">
        <!-- View Mode -->
        <div class="flex items-center bg-surface-card rounded-lg border border-subtle p-1 mr-2">
          <button 
            @click="viewMode = 'desktop'"
            class="w-8 h-8 rounded flex items-center justify-center transition-all"
            :class="viewMode === 'desktop' ? 'bg-white text-text-primary shadow-sm' : 'text-secondary hover:text-text-primary'"
            title="Desktop View"
          >
            <AppIcon name="lni-display" />
          </button>
          <button 
            @click="viewMode = 'mobile'"
            :disabled="activeTab === 'flowchart'"
            class="w-8 h-8 rounded flex items-center justify-center transition-all"
            :class="[
              viewMode === 'mobile' ? 'bg-white text-text-primary shadow-sm' : 'text-secondary hover:text-text-primary',
              activeTab === 'flowchart' ? 'opacity-50 cursor-not-allowed' : ''
            ]"
            title="Mobile View"
          >
            <AppIcon name="lni-mobile" />
          </button>
        </div>

        <div class="h-8 w-px bg-subtle mx-2"></div>

        <!-- Actions -->
        <button 
          @click="toggleHeader"
          class="w-10 h-10 rounded-lg border border-subtle hover:bg-surface-card flex items-center justify-center text-secondary hover:text-text-primary transition-colors"
          title="Esconder Menu (H)"
        >
          <AppIcon name="lni-layout" />
        </button>

        <button 
          @click="toggleFullscreen"
          class="w-10 h-10 rounded-lg border border-subtle hover:bg-surface-card flex items-center justify-center text-secondary hover:text-text-primary transition-colors"
          :title="isFullscreen ? 'Sair da Tela Cheia' : 'Tela Cheia'"
        >
          <AppIcon :name="isFullscreen ? 'lni-exit' : 'lni-full-screen'" />
        </button>
        
        <button 
          @click="showInfo = !showInfo"
          class="w-10 h-10 rounded-lg border border-subtle hover:bg-surface-card flex items-center justify-center transition-colors"
          :class="showInfo ? 'bg-action-primary text-white border-action-primary' : 'text-secondary hover:text-text-primary'"
          title="Informações do Design"
        >
          <AppIcon name="lni-information" />
        </button>
      </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 relative z-10 bg-mat-stone/5 flex items-center justify-center overflow-hidden">
      
      <!-- Prototype Container -->
      <div 
        class="bg-white shadow-2xl transition-all duration-500 relative"
        :class="[
          viewMode === 'mobile' ? 'w-[375px] h-[calc(100%-48px)] max-h-[812px] rounded-[40px] border-[8px] border-text-primary overflow-hidden' : 'w-full h-full border-none overflow-hidden'
        ]"
      >
        <!-- Iframe for Content (Current Version) -->
        <iframe 
          v-if="activeTab === 'current' && currentPrototype"
          :src="currentPrototype.oldUrl"
          class="w-full h-full bg-white"
          :class="{ 'rounded-[32px]': viewMode === 'mobile' }"
          frameborder="0"
        ></iframe>

        <!-- Flowchart Viewer (Mermaid) -->
        <FlowchartViewer
          v-else-if="activeTab === 'flowchart' && currentPrototype && currentPrototype.mermaidCode"
          class="w-full h-full bg-white"
          :class="{ 'rounded-[32px]': viewMode === 'mobile' }"
        >
          <MermaidRenderer :code="currentPrototype.mermaidCode" />
        </FlowchartViewer>

        <!-- Flowchart Viewer (Image Fallback) -->
        <FlowchartViewer
          v-else-if="activeTab === 'flowchart' && currentPrototype"
          :src="currentPrototype.flowchartUrl || '/images/logo-pilar.svg'"
          class="w-full h-full bg-white"
          :class="{ 'rounded-[32px]': viewMode === 'mobile' }"
        />

        <!-- New Version (Home) -->
        <div v-else-if="activeTab === 'new' && slug === 'home'" class="w-full h-full overflow-y-auto overflow-x-hidden bg-white" :class="[viewMode === 'mobile' ? 'rounded-[32px] force-mobile' : '', ]">
           <HomeV2 :forceMobile="viewMode === 'mobile'" />
        </div>

        <!-- New Version (Search Results) -->
        <div v-else-if="activeTab === 'new' && slug === 'resultados'" class="w-full h-full overflow-y-auto bg-white" :class="[viewMode === 'mobile' ? 'rounded-[32px] force-mobile' : '']">
           <SearchResultsV2 :forceMobile="viewMode === 'mobile'" />
        </div>

        <!-- New Version (Property Detail) -->
        <div v-else-if="activeTab === 'new' && slug === 'imovel'" class="w-full h-full overflow-y-auto bg-white" :class="[viewMode === 'mobile' ? 'rounded-[32px] force-mobile' : '']">
           <PropertyDetailV2 :forceMobile="viewMode === 'mobile'" />
        </div>

        <!-- New Version (Curation) -->
        <div v-else-if="activeTab === 'new' && slug === 'curadoria'" class="w-full h-full overflow-y-auto bg-white" :class="[viewMode === 'mobile' ? 'rounded-[32px] force-mobile' : '']">
           <CurationV2 :forceMobile="viewMode === 'mobile'" />
        </div>

        <!-- Empty State (New Version) -->
        <div v-else class="w-full h-full flex flex-col items-center justify-center bg-white p-8 text-center">
          <div class="w-16 h-16 rounded-full bg-surface-card flex items-center justify-center mb-6">
            <AppIcon name="lni-construction" class="text-3xl text-action-primary" />
          </div>
          <h3 class="text-xl font-light text-text-primary mb-2">Em Desenvolvimento</h3>
          <p class="text-secondary font-light max-w-md">
            O protótipo de alta fidelidade para esta página está sendo construído. Em breve você poderá navegar pela nova experiência.
          </p>
        </div>
      </div>

      <!-- Info Panel (Floating) -->
      <Transition name="slide-right">
        <div v-if="showInfo" class="absolute right-0 top-0 h-full w-96 bg-white border-l border-subtle shadow-xl z-30 p-8 overflow-y-auto">
          <div class="flex items-center justify-between mb-8">
            <h2 class="text-lg font-light text-text-primary">Sobre o Design</h2>
            <button @click="showInfo = false" class="text-secondary hover:text-text-primary">
              <AppIcon name="lni-close" />
            </button>
          </div>

          <div class="space-y-8">
            <div>
              <span class="text-xs font-mono text-action-primary uppercase tracking-widest block mb-2">Contexto</span>
              <p class="text-secondary font-light leading-relaxed text-sm">
                {{ currentPrototype?.description }}
              </p>
            </div>

            <div>
              <span class="text-xs font-mono text-action-primary uppercase tracking-widest block mb-2">Melhorias Chave</span>
              <ul class="space-y-3">
                <li v-for="feature in currentPrototype?.features" :key="feature" class="flex items-start gap-3 text-sm text-secondary font-light">
                  <AppIcon name="lni-checkmark-circle" class="mt-0.5 text-action-primary shrink-0" />
                  <span>{{ feature }}</span>
                </li>
              </ul>
            </div>

            <div class="p-4 bg-surface-card rounded-lg border border-subtle">
              <span class="text-xs font-mono text-secondary uppercase tracking-widest block mb-2">Status</span>
              <div class="flex items-center gap-2">
                <div class="w-2 h-2 rounded-full bg-amber-500"></div>
                <span class="text-sm font-medium text-text-primary">Em Construção</span>
              </div>
            </div>
          </div>
        </div>
      </Transition>

    </main>
  </div>
</template>

<style scoped>
.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.3s ease;
}

.slide-right-enter-from,
.slide-right-leave-to {
  transform: translateX(100%);
}
</style>
