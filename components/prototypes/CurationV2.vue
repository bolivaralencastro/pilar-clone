<template>
  <div class="font-sans text-text-primary min-h-screen bg-surface-base">
    
    <!-- Header -->
    <HeaderLuxury />

    <div class="relative">
      <!-- HERO EDITORIAL -->
      <header class="pt-20 pb-12 px-6 text-center max-w-4xl mx-auto">
      
      <!-- Título Principal -->
      <h1 class="text-5xl md:text-6xl font-serif font-light text-text-primary mb-3 tracking-tight">Curadoria</h1>
      
      <!-- Subtítulo -->
      <span class="block text-xs uppercase tracking-[0.2em] text-text-tertiary mb-8">Suas Coleções</span>
      
      <!-- Descrição Elegante -->
      <p class="text-sm md:text-base font-light text-text-secondary leading-relaxed mb-6 max-w-2xl mx-auto">
        Organize, compare e compartilhe seus imóveis favoritos<br>em coleções personalizadas.
      </p>

      <!-- Contagem de imóveis -->
      <span class="text-xs uppercase tracking-[0.15em] text-text-tertiary">{{ currentCollectionProperties.length }} imóveis salvos</span>

    </header>

    <!-- CONTROL BAR (Sticky) -->
    <div class="sticky top-0 z-40 bg-surface-base border-t border-b border-border-subtle">
      <div class="container mx-auto px-6 h-14 flex justify-between items-center text-[10px] uppercase tracking-[0.15em] font-medium text-text-primary">
        
        <!-- Lado Esquerdo: Filtros, Ordenação e Collections Tabs -->
        <div class="flex items-center gap-6">
          <button 
            @click="showFilters = true"
            class="flex items-center gap-2 hover:text-text-secondary transition-colors"
          >
            <i class="lni lni-funnel text-xs"></i>
            <span>Filtrar</span>
          </button>
          
          <div class="h-4 w-px bg-border-subtle"></div>

          <button class="flex items-center gap-2 hover:text-text-secondary transition-colors group">
            <i class="lni lni-sort-amount-dsc text-xs"></i>
            <span>Ordenar</span>
            <i class="lni lni-chevron-down text-[8px] group-hover:rotate-180 transition-transform"></i>
          </button>

          <div class="h-4 w-px bg-border-subtle"></div>

          <div class="flex items-center gap-2 overflow-x-auto pb-2 md:pb-0">
          <button 
            v-for="collection in collections" 
            :key="collection.id"
            @click="activeCollection = collection.id"
            class="px-2.5 py-1 text-[10px] border rounded-full transition-colors whitespace-nowrap uppercase tracking-[0.15em] font-medium"
            :class="activeCollection === collection.id 
              ? 'bg-text-primary text-surface-base border-text-primary hover:bg-text-primary/90' 
              : 'text-text-secondary border-border-subtle hover:border-text-primary hover:bg-surface-subtle hover:text-text-primary'"
          >
            {{ collection.name }} <span class="opacity-60">({{ collection.count }})</span>
          </button>
          </div>
        </div>

        <!-- Lado Direito: Comparar + Mapa -->
        <div class="flex items-center gap-6">
          <button 
            @click="toggleComparisonMode"
            class="flex items-center gap-2 transition-all duration-300"
            :class="isComparisonMode 
              ? 'text-text-primary font-medium scale-105' 
              : 'hover:text-text-secondary hover:scale-105'"
          >
            <span>Comparar</span>
            
            <!-- Badge contador com animação -->
            <span 
              v-if="selectedProperties.length > 0" 
              class="bg-text-primary text-surface-base text-[9px] w-4 h-4 rounded-full flex items-center justify-center transition-transform duration-200"
              :class="selectedProperties.length > 0 ? 'scale-100' : 'scale-0'"
            >
              {{ selectedProperties.length }}
            </span>
          </button>
          
          <div class="h-4 w-px bg-border-subtle"></div>

          <button 
            @click="viewMode = viewMode === 'grid' ? 'map' : 'grid'"
            class="flex items-center gap-2 hover:text-text-secondary transition-colors"
          >
            <span>{{ viewMode === 'grid' ? 'Ver Mapa' : 'Ver Grid' }}</span>
            <i :class="viewMode === 'grid' ? 'lni-map' : 'lni-grid-alt'" class="lni text-xs"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Main Content -->
    <main class="container mx-auto px-6 pb-16 mt-12">

      <!-- Empty State -->
      <div v-if="currentCollectionProperties.length === 0" class="py-32 text-center">
        <div class="w-20 h-20 mx-auto rounded-full bg-surface-offset flex items-center justify-center mb-6">
          <i class="lni lni-heart text-3xl text-text-tertiary"></i>
        </div>
        <h3 class="text-2xl font-light text-text-primary mb-2">Nenhum imóvel salvo ainda</h3>
        <p class="text-text-secondary mb-8 max-w-md mx-auto">
          Comece a explorar nosso portfólio e salve seus imóveis favoritos para criar sua coleção privada.
        </p>
        <button 
          @click="router.push('/prototipo/resultados?tab=new')"
          class="px-6 py-3 bg-text-primary text-surface-base rounded text-sm uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors"
        >
          Explorar Imóveis
        </button>
      </div>

      <!-- Editorial Grid View -->
      <div v-if="viewMode === 'grid'" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="property in currentCollectionProperties" 
          :key="property.id"
          class="col-span-1"
        >
          <PropertyCardV2 
            :property="property" 
            imageHeight="medium" 
            :selectionMode="isComparisonMode"
            :isSelected="selectedProperties.some(p => p.id === property.id)"
            :isSaved="true"
            @toggle-selection="handleSelection"
          />
        </div>
      </div>

      <!-- Map View -->
      <div v-else class="flex gap-6 items-start relative">
        <!-- Sidebar with Cards (scroll com a página) -->
        <div class="w-full md:w-[420px] space-y-4 pb-16">
          <div 
            v-for="property in currentCollectionProperties" 
            :key="property.id" 
            class="bg-surface-card rounded-lg overflow-hidden flex shadow-sm border border-border-subtle group hover:shadow-md transition-all relative"
            :class="{
              'cursor-pointer': !isComparisonMode,
              'ring-2 ring-text-primary': isComparisonMode && selectedProperties.some(p => p.id === property.id)
            }"
            @click="isComparisonMode ? handleSelection(property) : null"
          >
            <!-- Selection Checkbox (Comparison Mode) -->
            <div 
              v-if="isComparisonMode"
              class="absolute top-2 left-2 z-10"
            >
              <div 
                class="w-5 h-5 rounded border-2 flex items-center justify-center transition-all"
                :class="selectedProperties.some(p => p.id === property.id) 
                  ? 'bg-text-primary border-text-primary' 
                  : 'bg-white border-border-strong'"
              >
                <i 
                  v-if="selectedProperties.some(p => p.id === property.id)"
                  class="lni lni-checkmark text-white text-xs font-bold"
                ></i>
              </div>
            </div>

            <!-- Image -->
            <div class="w-32 h-32 bg-surface-offset flex-shrink-0 overflow-hidden relative">
              <img 
                v-if="!imageErrors.has(property.id)"
                :src="property.image" 
                :alt="property.name"
                class="w-full h-full object-cover"
                @error="handleImageError(property.id)"
              />
              <div 
                v-else 
                class="w-full h-full flex flex-col items-center justify-center bg-surface-offset text-text-tertiary"
              >
                <i class="lni lni-image text-xl mb-1 opacity-30"></i>
              </div>
              <!-- Favorite Badge -->
              <div class="absolute top-2 right-2">
                <div class="w-6 h-6 bg-white/90 backdrop-blur rounded-full flex items-center justify-center">
                  <i class="lni lni-heart text-red-500 text-xs" style="font-weight: 900;"></i>
                </div>
              </div>
            </div>
            <!-- Content -->
            <div class="p-3 flex-1 flex flex-col justify-between">
              <div>
                <p class="text-[9px] uppercase tracking-widest text-text-tertiary">{{ property.neighborhood }}</p>
                <h3 class="font-serif font-semibold text-sm text-text-primary leading-tight mt-1">{{ property.name }}</h3>
              </div>
              <div class="space-y-1">
                <p class="font-bold text-sm text-text-primary">{{ property.price }}</p>
                <p class="font-mono text-[10px] text-text-secondary">{{ property.specs }}</p>
                <!-- Agent Info -->
                <div class="flex items-center gap-2 pt-1 border-t border-border-subtle/50 mt-2">
                  <div class="w-5 h-5 rounded-full bg-surface-offset flex items-center justify-center flex-shrink-0">
                    <i class="lni lni-user text-[8px] text-text-tertiary"></i>
                  </div>
                  <div class="flex-1 min-w-0">
                    <p class="text-[9px] text-text-secondary truncate">{{ property.agent.name }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>        <!-- Map Placeholder (Sticky) -->
        <div class="hidden md:block flex-1 sticky top-[80px] h-[calc(100vh-104px)] z-10">
          <div class="w-full h-full bg-surface-offset rounded-lg flex items-center justify-center border border-border-subtle">
            <div class="text-center">
              <div class="w-16 h-16 bg-surface-card rounded-full flex items-center justify-center mx-auto mb-4 border border-border-subtle">
                <i class="lni lni-map-marker text-2xl text-text-tertiary"></i>
              </div>
              <p class="text-text-tertiary text-sm">Mapa interativo</p>
              <p class="text-text-tertiary/60 text-xs mt-1">Placeholder para integração</p>
            </div>
          </div>
        </div>
      </div>

    </main>
    </div>

    <!-- Footer -->
    <FooterLuxury />

    <!-- FILTERS PANEL -->
    <FiltersPanel 
      v-model="showFilters"
      @apply="handleApplyFilters"
      @clear="handleClearFilters"
    />

    <!-- COMPARISON FLOATING BAR -->
    <ComparisonFloatingBar 
      :is-visible="isComparisonMode"
      :selected-properties="selectedProperties"
      @remove="removeSelection"
      @compare="navigateToCompare"
      @cancel="toggleComparisonMode"
    />

  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import PropertyCardV2 from './PropertyCardV2.vue'
import ComparisonFloatingBar from './ComparisonFloatingBar.vue'
import FiltersPanel from './FiltersPanel.vue'

const router = useRouter()

const activeCollection = ref('all')
const viewMode = ref<'grid' | 'map'>('grid')
const isComparisonMode = ref(false)
const imageErrors = ref<Set<number>>(new Set())
const showFilters = ref(false)

const handleImageError = (id: number) => {
  imageErrors.value.add(id)
}

const selectedProperties = ref<Property[]>([])

const collections = ref([
  { id: 'all', name: 'Todos', count: 8 },
  { id: 'favorites', name: 'Favoritos', count: 3 },
  { id: 'visiting', name: 'Para Visitar', count: 2 },
  { id: 'offers', name: 'Propostas', count: 1 }
])

const properties = ref([
  {
    id: 1,
    ref: 'LE4592',
    name: 'Cobertura Jardins',
    neighborhood: 'Jardins — São Paulo, SP',
    price: 'R$ 9.250.000',
    specs: '420m² / 4 Suítes',
    area: 420,
    image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'favorites', 'visiting'],
    agent: { name: 'M. Costa', company: 'PilarHomes' },
    layout: 'featured' as const
  },
  {
    id: 2,
    ref: 'LE4593',
    name: 'Residencial Dos Lagos',
    neighborhood: 'Itaim Bibi — São Paulo, SP',
    price: 'R$ 7.800.000',
    specs: '380m² / 4 Suítes',
    area: 380,
    image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'favorites'],
    agent: { name: 'A. Silva', company: 'PilarHomes' },
    layout: 'half' as const
  },
  {
    id: 3,
    ref: 'LE4594',
    name: 'Villa Toscana',
    neighborhood: 'Vila Nova Conceição — São Paulo, SP',
    price: 'R$ 6.950.000',
    specs: '350m² / 3 Suítes',
    area: 350,
    image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'visiting'],
    agent: { name: 'L. Santos', company: 'PilarHomes' },
    layout: 'third' as const
  },
  {
    id: 4,
    ref: 'LE4595',
    name: 'Edifício Atlântica',
    neighborhood: 'Morumbi — São Paulo, SP',
    price: 'R$ 8.750.000',
    specs: '480m² / 5 Suítes',
    area: 480,
    image: 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'favorites', 'offers'],
    agent: { name: 'R. Oliveira', company: 'PilarHomes' },
    layout: 'half' as const
  },
  {
    id: 5,
    ref: 'LE4596',
    name: 'Loft Higienópolis',
    neighborhood: 'Higienópolis — São Paulo, SP',
    price: 'R$ 4.200.000',
    specs: '220m² / 2 Suítes',
    area: 220,
    image: 'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=800&auto=format&fit=crop',
    collections: ['all'],
    agent: { name: 'C. Pereira', company: 'PilarHomes' },
    layout: 'third' as const
  },
  {
    id: 6,
    ref: 'LE4597',
    name: 'Penthouse Faria Lima',
    neighborhood: 'Itaim Bibi — São Paulo, SP',
    price: 'R$ 12.500.000',
    specs: '550m² / 5 Suítes',
    area: 550,
    image: 'https://images.unsplash.com/photo-1600585154526-990dced4db0d?q=80&w=800&auto=format&fit=crop',
    collections: ['all'],
    agent: { name: 'F. Mendes', company: 'PilarHomes' },
    layout: 'featured' as const
  },
  {
    id: 7,
    ref: 'LE4598',
    name: 'Casa de Vila Pinheiros',
    neighborhood: 'Pinheiros — São Paulo, SP',
    price: 'R$ 5.800.000',
    specs: '320m² / 4 Suítes',
    area: 320,
    image: 'https://images.unsplash.com/photo-1600047509358-9dc75507daeb?q=80&w=800&auto=format&fit=crop',
    collections: ['all'],
    agent: { name: 'J. Almeida', company: 'PilarHomes' },
    layout: 'half' as const
  },
  {
    id: 8,
    ref: 'LE4599',
    name: 'Apartamento Moema',
    neighborhood: 'Moema — São Paulo, SP',
    price: 'R$ 3.900.000',
    specs: '180m² / 3 Suítes',
    area: 180,
    image: 'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?q=80&w=800&auto=format&fit=crop',
    collections: ['all'],
    agent: { name: 'P. Costa', company: 'PilarHomes' },
    layout: 'third' as const
  }
])

const currentCollectionProperties = computed(() => {
  return properties.value.filter(p => p.collections.includes(activeCollection.value))
})

const averagePrice = computed(() => {
  if (currentCollectionProperties.value.length === 0) return 'R$ 0'
  const total = currentCollectionProperties.value.reduce((sum, p) => {
    const price = parseFloat(p.price.replace(/[^\d,]/g, '').replace(',', '.'))
    return sum + price
  }, 0)
  const avg = total / currentCollectionProperties.value.length
  return `R$ ${(avg / 1000000).toFixed(1)}M`
})

const totalArea = computed(() => {
  const total = currentCollectionProperties.value.reduce((sum, p) => sum + p.area, 0)
  return `${total}m²`
})

const neighborhoods = computed(() => {
  const unique = new Set(currentCollectionProperties.value.map(p => p.neighborhood.split('—')[0].trim()))
  return unique.size
})

const toggleComparisonMode = () => {
  isComparisonMode.value = !isComparisonMode.value
  if (!isComparisonMode.value) {
    selectedProperties.value = []
  }
}

const handleSelection = (property: Property) => {
  const index = selectedProperties.value.findIndex(p => p.id === property.id)
  if (index >= 0) {
    selectedProperties.value.splice(index, 1)
  } else {
    if (selectedProperties.value.length < 4) {
      selectedProperties.value.push(property)
    }
  }
}

const removeSelection = (id: number) => {
  const index = selectedProperties.value.findIndex(p => p.id === id)
  if (index >= 0) {
    selectedProperties.value.splice(index, 1)
  }
}

const navigateToCompare = async () => {
  await navigateTo('/prototipo/compare?tab=new')
}

// Handlers para o painel de filtros
const handleApplyFilters = () => {
  // Lógica de aplicação de filtros
  console.log('Filtros aplicados')
}

const handleClearFilters = () => {
  // Lógica de limpeza de filtros
  console.log('Filtros limpos')
}
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
.img-zoom { 
  transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); 
}
.group:hover .img-zoom { 
  transform: scale(1.05); 
}
</style>
