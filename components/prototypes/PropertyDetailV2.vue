<template>
  <div class="min-h-screen bg-surface-base font-sans text-text-primary">
    
    <!-- Header Luxury -->
    <HeaderLuxury />

    <!-- Hero Gallery -->
    <section class="relative h-[80vh] bg-surface-offset">
      <div class="absolute inset-0">
        <img 
          :src="currentImage" 
          :alt="property.name"
          class="w-full h-full object-cover"
        />
      </div>
      
      <!-- Gallery Controls -->
      <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex gap-2 z-10">
        <button 
          v-for="(img, index) in property.gallery" 
          :key="index"
          @click="currentImageIndex = index"
          class="w-16 h-16 rounded overflow-hidden border-2 transition-all"
          :class="currentImageIndex === index ? 'border-white scale-110' : 'border-white/50 opacity-70 hover:opacity-100'"
        >
          <img :src="img" :alt="`Imagem ${index + 1}`" class="w-full h-full object-cover" />
        </button>
      </div>

      <!-- Navigation Arrows -->
      <button 
        @click="previousImage"
        class="absolute left-8 top-1/2 -translate-y-1/2 w-12 h-12 bg-surface-card/90 backdrop-blur rounded-full flex items-center justify-center text-text-primary hover:bg-surface-card transition-all"
      >
        ←
      </button>
      <button 
        @click="nextImage"
        class="absolute right-8 top-1/2 -translate-y-1/2 w-12 h-12 bg-surface-card/90 backdrop-blur rounded-full flex items-center justify-center text-text-primary hover:bg-surface-card transition-all"
      >
        →
      </button>
    </section>

    <!-- Content -->
    <div class="max-w-7xl mx-auto px-6 md:px-12 py-16">
      
      <div class="grid lg:grid-cols-12 gap-12">
        
        <!-- Main Column -->
        <div class="lg:col-span-8 space-y-12">
          
          <!-- Header -->
          <header class="space-y-6 border-b border-border-subtle pb-8">
            <div class="flex items-start justify-between">
              <div class="space-y-2">
                <span class="text-xs uppercase tracking-[0.2em] text-text-tertiary">{{ property.ref }}</span>
                <h1 class="text-4xl md:text-5xl font-serif font-light text-text-primary">{{ property.name }}</h1>
                <p class="text-lg text-text-secondary">{{ property.neighborhood }}</p>
              </div>
              
              <div class="text-right">
                <div class="text-3xl font-light text-text-primary">{{ property.price }}</div>
                <div class="text-sm text-text-tertiary mt-1">{{ property.pricePerSqm }}</div>
              </div>
            </div>

            <!-- Quick Specs -->
            <div class="flex flex-wrap gap-6 pt-4">
              <div class="flex items-center gap-2">
                <span class="text-text-tertiary text-sm">Área:</span>
                <span class="font-medium">{{ property.area }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-text-tertiary text-sm">Suítes:</span>
                <span class="font-medium">{{ property.suites }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-text-tertiary text-sm">Vagas:</span>
                <span class="font-medium">{{ property.parking }}</span>
              </div>
            </div>
          </header>

          <!-- Description -->
          <section class="space-y-4">
            <h2 class="text-2xl font-light tracking-tight">Sobre o imóvel</h2>
            <div class="prose prose-sm max-w-none text-text-secondary leading-relaxed">
              <p>{{ property.description }}</p>
            </div>
          </section>

          <!-- Features -->
          <section class="space-y-6">
            <h2 class="text-2xl font-light tracking-tight">Características</h2>
            
            <div class="grid md:grid-cols-2 gap-8">
              <div v-for="category in features" :key="category.title" class="space-y-4">
                <h3 class="text-sm uppercase tracking-widest text-text-tertiary font-medium">{{ category.title }}</h3>
                <ul class="space-y-2">
                  <li v-for="item in category.items" :key="item" class="flex items-center gap-2 text-sm text-text-secondary">
                    <span class="w-1.5 h-1.5 bg-text-primary rounded-full"></span>
                    {{ item }}
                  </li>
                </ul>
              </div>
            </div>
          </section>

          <!-- Location -->
          <section class="space-y-6">
            <h2 class="text-2xl font-light tracking-tight">Localização</h2>
            <div class="aspect-video bg-surface-offset rounded-lg overflow-hidden">
              <div class="w-full h-full flex items-center justify-center text-text-tertiary">
                <span>Mapa interativo</span>
              </div>
            </div>
            <div class="grid md:grid-cols-3 gap-4 text-sm">
              <div>
                <span class="text-text-tertiary block mb-1">Walkability</span>
                <span class="font-medium">{{ property.walkability }}</span>
              </div>
              <div>
                <span class="text-text-tertiary block mb-1">Transporte</span>
                <span class="font-medium">{{ property.transit }}</span>
              </div>
              <div>
                <span class="text-text-tertiary block mb-1">Bike Score</span>
                <span class="font-medium">{{ property.bikeScore }}</span>
              </div>
            </div>
          </section>

        </div>

        <!-- Sidebar -->
        <aside class="lg:col-span-4 space-y-6">
          
          <!-- Sticky Container -->
          <div class="sticky top-24 space-y-6">
            
            <!-- Contact Card -->
            <div class="bg-surface-card border border-border-subtle rounded-lg p-6 space-y-6">
              <div class="flex items-center gap-4">
                <img 
                  :src="property.agent.avatar" 
                  :alt="property.agent.name"
                  class="w-16 h-16 rounded-full object-cover"
                />
                <div>
                  <h3 class="font-medium">{{ property.agent.name }}</h3>
                  <p class="text-sm text-text-tertiary">{{ property.agent.company }}</p>
                </div>
              </div>

              <div class="space-y-3">
                <button class="w-full bg-text-primary text-surface-base py-3 rounded text-sm uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors">
                  Agendar Visita
                </button>
                <button class="w-full border border-border-strong text-text-primary py-3 rounded text-sm uppercase tracking-widest font-medium hover:bg-surface-subtle transition-colors">
                  Fazer Proposta
                </button>
              </div>

              <div class="pt-4 border-t border-border-subtle space-y-2">
                <button class="w-full text-left text-sm text-text-secondary hover:text-text-primary transition-colors flex items-center justify-between">
                  <span>Enviar por e-mail</span>
                  <span>↗</span>
                </button>
                <button class="w-full text-left text-sm text-text-secondary hover:text-text-primary transition-colors flex items-center justify-between">
                  <span>Compartilhar</span>
                  <span>↗</span>
                </button>
              </div>
            </div>

            <!-- Financial Info -->
            <div class="bg-surface-card border border-border-subtle rounded-lg p-6 space-y-4">
              <h3 class="text-sm uppercase tracking-widest text-text-tertiary font-medium">Custos mensais</h3>
              <div class="space-y-3 text-sm">
                <div class="flex justify-between">
                  <span class="text-text-secondary">Condomínio</span>
                  <span class="font-medium">{{ property.condoFee }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-text-secondary">IPTU</span>
                  <span class="font-medium">{{ property.iptu }}</span>
                </div>
                <div class="flex justify-between pt-3 border-t border-border-subtle">
                  <span class="text-text-primary font-medium">Total estimado</span>
                  <span class="font-medium">{{ property.totalMonthly }}</span>
                </div>
              </div>
            </div>

          </div>

        </aside>

      </div>

    </div>

    <!-- Footer -->
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
                <h2 class="text-sm font-medium uppercase tracking-widest text-text-primary">Fluxo de Detalhe</h2>
                <p class="text-[10px] text-text-tertiary">Diagrama de conversão e imersão</p>
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
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import FlowchartViewer from '../FlowchartViewer.vue'
import MermaidRenderer from '../MermaidRenderer.vue'

const showFlowchart = ref(false)

const mermaidCode = `
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
`

const currentImageIndex = ref(0)

const property = ref({
  ref: 'LE4592',
  name: 'Cobertura Jardins',
  neighborhood: 'Jardins — São Paulo, SP',
  price: 'R$ 9.250.000',
  pricePerSqm: 'R$ 22.023/m²',
  area: '420 m²',
  suites: '4 suítes',
  parking: '4 vagas',
  description: 'Cobertura excepcional localizada em um dos endereços mais prestigiados de São Paulo. Com acabamentos premium e pé-direito duplo, oferece uma experiência de moradia incomparável. Vista panorâmica para o Parque do Ibirapuera e ambientes amplos com luz natural abundante.',
  walkability: 'Alta',
  transit: 'Excelente',
  bikeScore: '85/100',
  condoFee: 'R$ 5.200',
  iptu: 'R$ 1.800',
  totalMonthly: 'R$ 7.000',
  agent: {
    name: 'Laura Santos',
    company: 'Elite Realty',
    avatar: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop'
  },
  gallery: [
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2574&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=2574&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=2574&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2574&auto=format&fit=crop'
  ]
})

const features = ref([
  {
    title: 'Interiores',
    items: [
      'Pé-direito duplo',
      'Acabamento em mármore',
      'Piso em madeira nobre',
      'Closets em todas as suítes',
      'Cozinha gourmet integrada'
    ]
  },
  {
    title: 'Condomínio',
    items: [
      'Portaria 24h',
      'Segurança com biometria',
      'Piscina aquecida',
      'Academia completa',
      'Salão de festas'
    ]
  },
  {
    title: 'Localização',
    items: [
      'Vista para o Ibirapuera',
      'Próximo ao metrô',
      'Área comercial vibrante',
      'Escolas de excelência',
      'Restaurantes premiados'
    ]
  },
  {
    title: 'Sustentabilidade',
    items: [
      'Captação de água da chuva',
      'Painéis solares',
      'Sistema de aquecimento eficiente',
      'Ventilação cruzada',
      'Certificação LEED'
    ]
  }
])

const currentImage = computed(() => property.value.gallery[currentImageIndex.value])

const nextImage = () => {
  currentImageIndex.value = (currentImageIndex.value + 1) % property.value.gallery.length
}

const previousImage = () => {
  currentImageIndex.value = currentImageIndex.value === 0 
    ? property.value.gallery.length - 1 
    : currentImageIndex.value - 1
}
</script>

<style scoped>
.prose {
  @apply text-text-secondary;
}
</style>
