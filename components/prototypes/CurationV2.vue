<template>
  <div class="min-h-screen bg-surface-base font-sans text-text-primary">
    
    <!-- Header Luxury -->
    <HeaderLuxury />

    <!-- Hero Section -->
    <section class="pt-20 pb-12 px-6 text-center max-w-4xl mx-auto bg-surface-base">
      <span class="block text-xs uppercase tracking-[0.2em] text-text-tertiary mb-4">Minha Coleção Privada</span>
      
      <div class="w-12 h-px bg-border-strong mx-auto mb-4"></div>
      
      <h1 class="text-5xl md:text-6xl font-serif font-light text-text-primary mb-3 tracking-tight">Curadoria Pessoal</h1>
      
      <p class="text-sm md:text-base font-light text-text-secondary leading-relaxed mb-6 max-w-2xl mx-auto">
        Seus imóveis favoritos organizados em coleções exclusivas. Gerencie, compare e compartilhe suas escolhas.
      </p>
    </section>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 md:px-12 py-16">
      
      <!-- Filters & Actions Bar -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 mb-12 pb-8 border-b border-border-subtle">
        
        <!-- Left: Collections Tabs -->
        <div class="flex items-center gap-2 overflow-x-auto pb-2 md:pb-0">
          <button 
            v-for="collection in collections" 
            :key="collection.id"
            @click="activeCollection = collection.id"
            class="px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all"
            :class="activeCollection === collection.id 
              ? 'bg-text-primary text-surface-base' 
              : 'text-text-secondary hover:text-text-primary hover:bg-surface-subtle'"
          >
            {{ collection.name }} <span class="opacity-60">({{ collection.count }})</span>
          </button>
        </div>

        <!-- Right: Actions -->
        <div class="flex items-center gap-3">
          <button 
            v-if="selectedProperties.length > 0"
            @click="compareSelected"
            class="px-4 py-2 bg-text-primary text-surface-base rounded text-xs uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors flex items-center gap-2"
          >
            <i class="lni lni-layers"></i>
            Comparar ({{ selectedProperties.length }})
          </button>
          
          <button class="px-4 py-2 border border-border-strong text-text-primary rounded text-xs uppercase tracking-widest font-medium hover:bg-surface-subtle transition-colors flex items-center gap-2">
            <i class="lni lni-share-alt"></i>
            Compartilhar
          </button>

          <!-- Map Toggle -->
          <button 
            @click="viewMode = viewMode === 'grid' ? 'map' : 'grid'"
            class="px-4 py-2 border border-border-strong text-text-primary rounded text-xs uppercase tracking-widest font-medium hover:bg-surface-subtle transition-colors flex items-center gap-2"
            :class="viewMode === 'map' ? 'bg-text-primary text-surface-base' : ''"
          >
            <i class="lni lni-map"></i>
            Mapa
          </button>
        </div>
      </div>

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

      <!-- Grid View -->
      <div v-if="viewMode === 'grid'" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="property in currentCollectionProperties" 
          :key="property.id"
          class="col-span-1 relative"
        >
          <!-- Favorite Button (Always Active) - sobreposto ao card -->
          <button 
            class="absolute top-4 right-4 z-20 w-9 h-9 bg-white/90 backdrop-blur rounded-full flex items-center justify-center hover:bg-white transition-all shadow-sm"
            @click.stop
          >
            <i class="lni lni-heart text-red-500 text-lg" style="font-weight: 900;"></i>
          </button>

          <PropertyCardV2 
            :property="property" 
            imageHeight="medium" 
            :selectionMode="isComparisonMode"
            :isSelected="selectedProperties.some(p => p.id === property.id)"
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
            class="bg-surface-card rounded-lg overflow-hidden flex shadow-sm border border-border-subtle group cursor-pointer hover:shadow-md transition-shadow"
            @click="viewProperty(property.id)"
          >
            <!-- Image -->
            <div class="w-32 h-32 bg-surface-offset flex-shrink-0 overflow-hidden relative">
              <img 
                :src="property.image" 
                :alt="property.name"
                class="w-full h-full object-cover"
              />
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
              <div>
                <p class="font-bold text-sm text-text-primary">{{ property.price }}</p>
                <p class="font-mono text-[10px] text-text-secondary">{{ property.specs }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Map Placeholder (Sticky) -->
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

      <!-- Collection Stats -->
      <div v-if="currentCollectionProperties.length > 0" class="mt-16 pt-8 border-t border-border-subtle">
        <div class="grid md:grid-cols-4 gap-6 text-center">
          <div class="space-y-2">
            <div class="text-3xl font-light text-text-primary">{{ currentCollectionProperties.length }}</div>
            <div class="text-xs uppercase tracking-widest text-text-tertiary">Imóveis Salvos</div>
          </div>
          <div class="space-y-2">
            <div class="text-3xl font-light text-text-primary">{{ averagePrice }}</div>
            <div class="text-xs uppercase tracking-widest text-text-tertiary">Preço Médio</div>
          </div>
          <div class="space-y-2">
            <div class="text-3xl font-light text-text-primary">{{ totalArea }}</div>
            <div class="text-xs uppercase tracking-widest text-text-tertiary">Área Total</div>
          </div>
          <div class="space-y-2">
            <div class="text-3xl font-light text-text-primary">{{ neighborhoods }}</div>
            <div class="text-xs uppercase tracking-widest text-text-tertiary">Bairros</div>
          </div>
        </div>
      </div>

    </div>

    <!-- Footer -->
    <FooterLuxury />

  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import PropertyCardV2 from './PropertyCardV2.vue'

const router = useRouter()

const activeCollection = ref('all')
const viewMode = ref<'grid' | 'map'>('grid')
const isComparisonMode = ref(false)

// Estrutura similar ao SearchResultsV2
interface Property {
  id: string
  name: string
  neighborhood: string
  ref: string
  price: string
  specs: string
  image: string
  area: number
  collections: string[]
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
    id: 'p1',
    ref: 'LE4592',
    name: 'Cobertura Jardins',
    neighborhood: 'Jardins — São Paulo, SP',
    price: 'R$ 9.250.000',
    specs: '420m² / 4 Suítes',
    area: 420,
    image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'favorites', 'visiting']
  },
  {
    id: 'p2',
    ref: 'LE4593',
    name: 'Residencial Dos Lagos',
    neighborhood: 'Itaim Bibi — São Paulo, SP',
    price: 'R$ 7.800.000',
    specs: '380m² / 4 Suítes',
    area: 380,
    image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'favorites']
  },
  {
    id: 'p3',
    ref: 'LE4594',
    name: 'Villa Toscana',
    neighborhood: 'Vila Nova Conceição — São Paulo, SP',
    price: 'R$ 6.950.000',
    specs: '350m² / 3 Suítes',
    area: 350,
    image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'visiting']
  },
  {
    id: 'p4',
    ref: 'LE4595',
    name: 'Edifício Atlântica',
    neighborhood: 'Morumbi — São Paulo, SP',
    price: 'R$ 8.750.000',
    specs: '480m² / 5 Suítes',
    area: 480,
    image: 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=800&auto=format&fit=crop',
    collections: ['all', 'favorites', 'offers']
  },
  {
    id: 'p5',
    ref: 'LE4596',
    name: 'Loft Higienópolis',
    neighborhood: 'Higienópolis — São Paulo, SP',
    price: 'R$ 4.200.000',
    specs: '220m² / 2 Suítes',
    area: 220,
    image: 'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=800&auto=format&fit=crop',
    collections: ['all']
  },
  {
    id: 'p6',
    ref: 'LE4597',
    name: 'Penthouse Faria Lima',
    neighborhood: 'Itaim Bibi — São Paulo, SP',
    price: 'R$ 12.500.000',
    specs: '550m² / 5 Suítes',
    area: 550,
    image: 'https://images.unsplash.com/photo-1600585154526-990dced4db0d?q=80&w=800&auto=format&fit=crop',
    collections: ['all']
  },
  {
    id: 'p7',
    ref: 'LE4598',
    name: 'Casa de Vila Pinheiros',
    neighborhood: 'Pinheiros — São Paulo, SP',
    price: 'R$ 5.800.000',
    specs: '320m² / 4 Suítes',
    area: 320,
    image: 'https://images.unsplash.com/photo-1600047509358-9dc75507daeb?q=80&w=800&auto=format&fit=crop',
    collections: ['all']
  },
  {
    id: 'p8',
    ref: 'LE4599',
    name: 'Apartamento Moema',
    neighborhood: 'Moema — São Paulo, SP',
    price: 'R$ 3.900.000',
    specs: '180m² / 3 Suítes',
    area: 180,
    image: 'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?q=80&w=800&auto=format&fit=crop',
    collections: ['all']
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
    if (selectedProperties.value.length < 3) {
      selectedProperties.value.push(property)
    }
  }
}

const removeSelection = (id: string) => {
  const index = selectedProperties.value.findIndex(p => p.id === id)
  if (index >= 0) {
    selectedProperties.value.splice(index, 1)
  }
}

const compareSelected = () => {
  router.push('/prototipo/compare?tab=new')
}

const viewProperty = (id: string) => {
  router.push('/prototipo/imovel?tab=new')
}

const removeFromCollection = (id: string) => {
  // Remove property from collection logic
  console.log('Removing property:', id)
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
