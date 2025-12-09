<template>
  <div class="font-sans text-text-primary min-h-screen overflow-x-hidden">
    
    <!-- Main Content (Curtain Effect) -->
    <div class="relative z-10 bg-surface-base shadow-2xl will-change-transform">
      <!-- Header -->
      <HeaderLuxury />

    <!-- Hero Editorial (Estilo SearchResultsV2) -->
    <header class="pt-20 pb-12 px-6 text-center max-w-4xl mx-auto bg-surface-base">
      
      <!-- Cidade (acima do título) -->
      <span class="block text-xs uppercase tracking-[0.2em] text-text-tertiary mb-4">São Paulo • Curitiba</span>
      
      <!-- Divider -->
      <div class="w-12 h-px bg-border-strong mx-auto mb-4"></div>
      
      <!-- Título Principal - Serif Display -->
      <h1 class="text-5xl md:text-6xl font-serif font-light text-text-primary mb-3 tracking-tight whitespace-nowrap">Curadoria de imóveis de alto padrão</h1>
      
      <!-- Descrição Elegante -->
      <p class="text-sm md:text-base font-light text-text-secondary leading-relaxed mb-6 max-w-2xl mx-auto">
        Atendimento personalizado e o maior portfólio de alto padrão em localização privilegiada
      </p>

      <!-- Search Bar Discreto -->
      <div class="max-w-xl mx-auto mt-8">
        <div class="relative bg-surface-card border border-border-subtle rounded-lg shadow-sm hover:shadow-md transition-all duration-300">
          <div class="flex items-center gap-3 p-3">
            <i class="lni lni-search text-text-tertiary text-base"></i>
            <input 
              type="text" 
              placeholder="Buscar por bairro, cidade ou tipo de imóvel..."
              class="w-full bg-transparent text-sm text-text-primary placeholder:text-text-tertiary focus:outline-none"
            />
            <button 
              @click="router.push('/prototipo/resultados?tab=new')"
              class="bg-text-primary text-surface-base px-5 py-2 rounded text-xs uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors flex-shrink-0"
            >
              Buscar
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- Hero Video Section -->
    <section class="h-[90vh] px-6 pb-6 bg-surface-base">
      <div class="container mx-auto h-full relative rounded-2xl overflow-hidden bg-gray-900">
        <!-- Video Background -->
        <video 
          autoplay 
          muted 
          loop 
          playsinline 
          class="w-full h-full object-cover"
        >
          <source src="/video/hero-video.mp4" type="video/mp4">
        </video>
      </div>
    </section>

    <!-- Section: Selected Properties -->
    <section class="py-16 bg-surface-base text-text-primary">
      <div class="container mx-auto px-6">
        <div class="mb-10 text-center">
          <h2 class="text-xs md:text-sm font-light mb-2 tracking-[0.2em] uppercase">Selecionados <br><span class="text-6xl md:text-7xl italic font-serif text-text-primary opacity-60 normal-case">para você</span></h2>
          <p class="text-text-secondary">A partir de imóveis que chamaram <br>sua atenção</p>
        </div>

        <!-- Horizontal Scroll Container -->
        <div 
          ref="selectedPropertiesCarousel"
          class="flex gap-6 overflow-x-auto pb-8 snap-x snap-mandatory hide-scrollbar scroll-smooth pl-1 pr-6 -mr-6"
        >
          <div v-for="property in highlightedProperties" :key="property.id" class="min-w-[320px] md:min-w-[380px] snap-start flex-shrink-0">
            <PropertyCardV2 
              :property="property" 
              imageHeight="medium" 
              :selectionMode="false"
              :isSelected="false"
            />
          </div>
        </div>
        
        <div class="mt-6 flex items-center justify-between">
          <button
            @click="router.push('/prototipo/resultados?tab=new')"
            class="text-xs font-bold uppercase tracking-[0.18em] text-text-secondary hover:text-text-primary flex items-center gap-2 transition-colors"
          >
            Ver todos os imóveis
            <span class="text-sm">↗</span>
          </button>
          
          <div class="flex gap-2">
            <button 
              @click="scrollSelectedProperties('left')"
              class="w-10 h-10 border border-border-subtle rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors"
            >
              ←
            </button>
            <button 
              @click="scrollSelectedProperties('right')"
              class="w-10 h-10 border border-border-subtle rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors"
            >
              →
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Navigation Monochrome -->
    <NavigationMonochrome />

    <!-- Regions -->
    <section class="py-20 md:pt-32 bg-surface-base text-text-primary overflow-hidden">
      <div class="container mx-auto px-6">
        
        <!-- 1. EDITORIAL HEADER (Grid Assimétrico) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-24 mb-16 items-end">
          
          <!-- Título (Lado Esquerdo) -->
          <div class="lg:col-span-6">
            <h2 class="text-base md:text-xl font-light tracking-tight leading-[1.1] text-text-primary uppercase">
              Nossas <br>
              <span class="text-4xl md:text-5xl text-text-secondary opacity-60 italic font-serif normal-case">Regiões</span>
            </h2>
          </div>

          <!-- Descrição (Lado Direito - Offset) -->
          <div class="lg:col-span-5 lg:col-start-8">
            <p class="text-sm md:text-base text-text-secondary font-light leading-relaxed mb-8">
              Descubra bairros onde a arquitetura encontra o estilo de vida. Uma curadoria de localizações perfeitas para quem busca exclusividade e bem-estar.
            </p>
            <a href="#" class="inline-block text-xs font-bold uppercase tracking-[0.2em] border-b border-text-primary pb-1 hover:text-primary-600 hover:border-primary-600 transition-colors">
              Explorar todas as regiões
            </a>
          </div>
        </div>

        <!-- 2. CARROSSEL DE REGIÕES -->
        <div class="relative w-full">
          
          <!-- Scroll Container -->
          <div 
            ref="regionsCarousel"
            class="flex gap-6 overflow-x-auto hide-scrollbar pb-20 pr-16 -mr-6 md:-mr-24 pl-1 scroll-smooth"
          >
            
            <div v-for="(region, index) in regions" :key="index" class="group min-w-[70vw] md:min-w-[25vw] cursor-pointer">
              <div class="aspect-[2/3] w-full bg-surface-offset overflow-hidden mb-4 relative" style="border-radius: 4px;">
                <img :src="region.image" class="w-full h-full object-cover img-zoom opacity-90 group-hover:opacity-100 transition-opacity" alt="Region Image">
                 <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                    <span class="bg-surface-card/90 backdrop-blur px-3 py-1 text-[9px] uppercase tracking-widest font-bold text-text-primary">{{ region.label }}</span>
                 </div>
              </div>
              
              <div class="flex justify-between items-center px-1">
                 <h3 class="text-lg font-light text-text-primary tracking-tight group-hover:text-primary-600 transition-colors">{{ region.name }}</h3>
                 <div class="text-text-secondary opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-300">
                    <AppIcon name="arrow-right" size="18" />
                 </div>
              </div>
            </div>

          </div>

        </div>

        <!-- Controles de navegação do carrossel -->
        <div class="mt-8 flex justify-end items-center">
          <div class="flex gap-2">
            <button 
              @click="scrollRegions('left')"
              class="w-10 h-10 border border-border-subtle rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors"
            >
              ←
            </button>
            <button 
              @click="scrollRegions('right')"
              class="w-10 h-10 border border-border-subtle rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors"
            >
              →
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- Exclusive Properties -->
    <section class="py-16 bg-surface-subtle text-text-primary">
      <div class="container mx-auto px-6">
        <div class="mb-10">
          <h2 class="text-base md:text-xl font-light tracking-tight uppercase">Exclusivos <br><span class="text-4xl md:text-5xl italic font-serif text-text-secondary opacity-60 normal-case">PilarHomes</span></h2>
          <p class="text-text-secondary mt-1">Imóveis únicos, listados apenas no PilarHomes.</p>
        </div>

        <div class="flex gap-6 overflow-x-auto pb-8 snap-x hide-scrollbar">
          <div v-for="i in 3" :key="i" class="min-w-[320px] md:min-w-[450px] snap-center">
            <div class="bg-surface-card border border-border-subtle rounded-lg overflow-hidden shadow-sm">
               
               <div class="h-64 bg-surface-offset relative"></div>
               
               <div class="p-5">
                 <div class="flex items-center gap-3 mb-4">
                    <div class="w-10 h-10 bg-text-tertiary/30 rounded-full"></div>
                    <div>
                      <div class="h-3 w-24 bg-text-tertiary/20 rounded mb-1"></div>
                      <div class="h-2 w-16 bg-text-tertiary/30 rounded"></div>
                    </div>
                 </div>
                 
                 <div class="space-y-2 border-t border-border-subtle pt-4">
                   <div class="flex justify-between">
                     <div class="h-6 w-28 bg-text-tertiary/20 rounded"></div>
                     <div class="h-3 w-10 bg-text-tertiary/30 rounded"></div>
                   </div>
                   <div class="h-3 w-full bg-text-tertiary/30 rounded"></div>
                   <div class="h-3 w-1/2 bg-text-tertiary/30 rounded"></div>
                 </div>
               </div>
            </div>
          </div>
        </div>
        
        <div class="mt-8 flex justify-between items-center">
             <button @click="router.push('/prototipo/resultados?tab=new')" class="border border-border-strong text-text-primary px-6 py-3 rounded text-sm hover:bg-surface-subtle transition-colors">Ver todos os imóveis ↗</button>
             <div class="flex gap-2">
               <button class="w-10 h-10 border border-border-strong rounded-full flex items-center justify-center text-text-secondary hover:bg-surface-subtle transition-colors">←</button>
               <button class="w-10 h-10 border border-border-strong rounded-full flex items-center justify-center text-text-primary hover:bg-surface-subtle transition-colors">→</button>
             </div>
        </div>
      </div>
    </section>

    <!-- Curated Collections Split -->
    <CuratedCollectionsSplit />

    <!-- Testimonials Refined -->
    <TestimonialsRefined />

    <!-- Footer Luxury Component -->
    <FooterLuxury />

    <!-- Flowchart Toggle -->
    <button 
      @click="showFlowchart = true"
      class="fixed bottom-6 right-6 z-40 w-12 h-12 bg-surface-base border border-border-subtle rounded-full flex items-center justify-center shadow-xl hover:bg-surface-subtle hover:scale-105 transition-all text-text-secondary group"
      title="Ver Fluxo"
    >
      <i class="lni lni-network text-xl group-hover:text-text-primary transition-colors"></i>
    </button>

    <!-- Flowchart Modal -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="showFlowchart" class="fixed inset-0 z-[60] bg-surface-base/95 backdrop-blur-sm flex flex-col">
          <!-- Header -->
          <div class="flex items-center justify-between px-6 py-4 border-b border-border-subtle bg-surface-base">
            <div class="flex items-center gap-3">
              <div class="w-8 h-8 bg-surface-offset rounded flex items-center justify-center">
                <i class="lni lni-network text-text-primary"></i>
              </div>
              <div>
                <h2 class="text-sm font-medium uppercase tracking-widest text-text-primary">Fluxo da Home</h2>
                <p class="text-[10px] text-text-tertiary">Diagrama de navegação e seções</p>
              </div>
            </div>
            <button 
              @click="showFlowchart = false" 
              class="w-10 h-10 flex items-center justify-center hover:bg-surface-offset rounded-full transition-colors text-text-secondary hover:text-text-primary"
            >
              <i class="lni lni-close text-lg"></i>
            </button>
          </div>
          <!-- Viewer -->
          <div class="flex-1 overflow-hidden relative bg-surface-offset/30">
             <FlowchartViewer>
               <MermaidRenderer :code="mermaidCode" />
             </FlowchartViewer>
          </div>
        </div>
      </Transition>
    </Teleport>
    </div>
  </div>
</template>

<script setup lang="ts">
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import PropertyCardV2 from './PropertyCardV2.vue'
import CuratedCollectionsSplit from './CuratedCollectionsSplit.vue'
import TestimonialsRefined from './TestimonialsRefined.vue'
import NavigationMonochrome from './NavigationMonochrome.vue'
import FlowchartViewer from '../FlowchartViewer.vue'
import MermaidRenderer from '../MermaidRenderer.vue'

const showFlowchart = ref(false)

const mermaidCode = `
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
`

const router = useRouter()

const selectedPropertiesCarousel = ref<HTMLElement | null>(null)
const regionsCarousel = ref<HTMLElement | null>(null)

const scrollSelectedProperties = (direction: 'left' | 'right') => {
  if (!selectedPropertiesCarousel.value) return
  
  const scrollAmount = 400 // Largura aproximada do card + gap
  const currentScroll = selectedPropertiesCarousel.value.scrollLeft
  
  if (direction === 'left') {
    selectedPropertiesCarousel.value.scrollTo({
      left: currentScroll - scrollAmount,
      behavior: 'smooth'
    })
  } else {
    selectedPropertiesCarousel.value.scrollTo({
      left: currentScroll + scrollAmount,
      behavior: 'smooth'
    })
  }
}

const scrollRegions = (direction: 'left' | 'right') => {
  if (!regionsCarousel.value) return
  
  const scrollAmount = 400
  const currentScroll = regionsCarousel.value.scrollLeft
  
  if (direction === 'left') {
    regionsCarousel.value.scrollTo({
      left: currentScroll - scrollAmount,
      behavior: 'smooth'
    })
  } else {
    regionsCarousel.value.scrollTo({
      left: currentScroll + scrollAmount,
      behavior: 'smooth'
    })
  }
}

const highlightedProperties = ref([
  {
    id: 1,
    name: 'Cobertura Jardins',
    neighborhood: 'Jardins — SP',
    ref: 'LE4592',
    price: 'R$ 9.250.000',
    specs: '420m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Laura S.', company: 'Elite Realty' }
  },
  {
    id: 2,
    name: 'Residencial Dos Lagos',
    neighborhood: 'Itaim Bibi — SP',
    ref: 'LE4593',
    price: 'R$ 7.800.000',
    specs: '380m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Sofia B.', company: 'Elite Realty' }
  },
  {
    id: 3,
    name: 'Villa Toscana',
    neighborhood: 'Vila Nova Conceição — SP',
    ref: 'LE4594',
    price: 'R$ 6.950.000',
    specs: '350m² / 3 Suítes',
    image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Alice R.', company: 'Elite Realty' }
  },
  {
    id: 4,
    name: 'Edifício Atlântica',
    neighborhood: 'Morumbi — SP',
    ref: 'LE4595',
    price: 'R$ 8.750.000',
    specs: '480m² / 5 Suítes',
    image: 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Isabella V.', company: 'Elite Realty' }
  }
])

const navCards = ref([
  { title: 'Exclusivos PilarHomes' },
  { title: 'Coleções Compartilhadas' },
  { title: 'Off-Market' }
]);

const regions = ref([
  { name: 'São Paulo', image: '/images/sao-paulo.jpeg', label: 'Capital' },
  { name: 'Curitiba', image: '/images/curitiba.png', label: 'Sul' },
  { name: 'Boa Vista', image: '/images/boa vista.jpeg', label: 'Campo' },
  { name: 'Alphaville', image: '/images/alphaville.jpeg', label: 'Grande SP' }
])
</script>

<style scoped>
  /* Custom scrollbar hiding for clean UI */
  .hide-scrollbar::-webkit-scrollbar {
    display: none;
  }
  .hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  
  /* Micro-interação de Zoom suave do DS */
  .img-zoom { transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); }
  .group:hover .img-zoom { transform: scale(1.05); }
</style>