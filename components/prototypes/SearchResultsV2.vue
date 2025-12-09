<template>
  <div class="font-sans text-text-primary min-h-screen bg-surface-base">
    
    <!-- Header -->
    <HeaderLuxury :sticky="false" />

    <div class="relative">
      <!-- HERO EDITORIAL (Estilo Aman Resorts) -->
      <header class="pt-20 pb-12 px-6 text-center max-w-4xl mx-auto">
      
      <!-- Bairro (Título Principal - Serif Display) -->
      <h1 class="text-5xl md:text-6xl font-serif font-light text-text-primary mb-3 tracking-tight">Jardins</h1>
      
      <!-- Cidade (Pequeno abaixo) -->
      <span class="block text-xs uppercase tracking-[0.2em] text-text-tertiary mb-8">São Paulo</span>
      
      <!-- Descrição Elegante -->
      <p class="text-sm md:text-base font-light text-text-secondary leading-relaxed mb-6 max-w-2xl mx-auto">
        Um refúgio de sofisticação onde a arquitetura clássica encontra a modernidade. 
        Ruas arborizadas, alta gastronomia e as boutiques mais exclusivas definem 
        o estilo de vida inconfundível desta região icônica.
      </p>

      <!-- Contagem de imóveis -->
      <span class="text-xs uppercase tracking-[0.15em] text-text-tertiary">127 imóveis encontrados</span>

    </header>

    <!-- CONTROL BAR (Sticky) -->
    <div class="sticky top-0 z-40 bg-surface-base border-t border-b border-border-subtle">
      <div class="container mx-auto px-6 h-14 flex justify-between items-center text-[10px] uppercase tracking-[0.15em] font-medium text-text-primary">
        
        <!-- Lado Esquerdo: Filtros, Ordenação e Busca -->
        <div class="flex items-center gap-4 md:gap-6 overflow-x-auto hide-scrollbar max-w-[60%] md:max-w-none">
          <button 
            @click="showFilters = true"
            class="flex items-center gap-2 hover:text-text-secondary transition-colors whitespace-nowrap"
          >
            <i class="lni lni-funnel text-xs"></i>
            <span>Filtrar</span>
          </button>
          
          <div class="h-4 w-px bg-border-subtle flex-shrink-0"></div>

          <button class="flex items-center gap-2 hover:text-text-secondary transition-colors group whitespace-nowrap">
            <i class="lni lni-sort-amount-dsc text-xs"></i>
            <span class="hidden sm:inline">Ordenar</span>
            <i class="lni lni-chevron-down text-[8px] group-hover:rotate-180 transition-transform"></i>
          </button>

          <div class="h-4 w-px bg-border-subtle flex-shrink-0 hidden md:block"></div>

          <!-- Busca inline (Desktop) -->
          <div class="relative hidden md:block">
            <input 
              type="text" 
              v-model="searchQuery"
              placeholder="Buscar..."
              class="w-48 bg-transparent border-b border-border-subtle py-1 text-xs lowercase tracking-normal font-light focus:outline-none focus:border-text-primary transition-colors placeholder:text-text-tertiary placeholder:italic"
            />
            <div class="absolute right-0 top-1/2 -translate-y-1/2 text-text-tertiary/50">
              <i class="lni lni-search text-[10px]"></i>
            </div>
          </div>

          <!-- Busca Mobile Toggle -->
          <button 
            class="md:hidden flex items-center gap-2 hover:text-text-secondary transition-colors"
            @click="showMobileSearch = !showMobileSearch"
          >
            <i class="lni lni-search text-xs"></i>
          </button>
        </div>

        <!-- Lado Direito: Comparar + Mapa -->
        <div class="flex items-center gap-4 md:gap-6 flex-shrink-0">
          <button 
            @click="toggleComparisonMode"
            class="flex items-center gap-2 transition-all duration-300 whitespace-nowrap"
            :class="isComparisonMode 
              ? 'text-text-primary font-medium scale-105' 
              : 'hover:text-text-secondary hover:scale-105'"
          >
            <span class="hidden sm:inline">Comparar</span>
            <span class="sm:hidden"><i class="lni lni-layers text-xs"></i></span>
            
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
            class="flex items-center gap-2 hover:text-text-secondary transition-colors whitespace-nowrap"
          >
            <span class="hidden sm:inline">{{ viewMode === 'grid' ? 'Ver Mapa' : 'Ver Grid' }}</span>
            <span class="sm:hidden">{{ viewMode === 'grid' ? 'Mapa' : 'Grid' }}</span>
            <i :class="viewMode === 'grid' ? 'lni-map' : 'lni-grid-alt'" class="lni text-xs"></i>
          </button>
        </div>

      </div>
      
      <!-- Mobile Search Bar (Expandable) -->
      <div v-if="showMobileSearch" class="md:hidden px-6 py-3 border-t border-border-subtle bg-surface-base animate-fade-in">
        <div class="relative">
          <input 
            type="text" 
            v-model="searchQuery"
            placeholder="Buscar por bairro, condomínio..."
            class="w-full bg-surface-offset rounded px-3 py-2 text-xs text-text-primary focus:outline-none border border-transparent focus:border-border-strong"
            autoFocus
          />
          <i class="lni lni-search absolute right-3 top-1/2 -translate-y-1/2 text-text-tertiary text-xs"></i>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <main class="container mx-auto px-6 pb-16 mt-6">
      
      <!-- Editorial Grid View -->
      <div v-if="viewMode === 'grid'" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="property in properties" 
          :key="property.id" 
          class="col-span-1"
        >
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
      <div v-else class="flex flex-col md:flex-row gap-6 items-start relative h-[calc(100vh-140px)] md:h-auto">
        <!-- Sidebar with Cards (scroll com a página) -->
        <div class="hidden md:block w-full md:w-[420px] space-y-4 pb-16">
          <div 
            v-for="property in properties" 
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
        </div>
        
        <!-- Map Placeholder (Sticky) -->
        <div class="block flex-1 sticky top-[80px] h-full md:h-[calc(100vh-104px)] z-10 w-full">
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

      <!-- Load More -->
      <div v-if="viewMode === 'grid'" class="mt-12 flex justify-center">
        <button class="border border-border-strong px-8 py-4 rounded text-sm hover:bg-surface-subtle hover:text-text-primary transition-colors text-text-secondary">
          Carregar mais imóveis
        </button>
      </div>

    </main>
    </div>

    <!-- Footer -->
    <FooterLuxury />

    <!-- COMPARISON FLOATING BAR -->
    <ComparisonFloatingBar 
      :is-visible="isComparisonMode"
      :selected-properties="selectedProperties"
      @remove="removeSelection"
      @compare="navigateToCompare"
      @cancel="toggleComparisonMode"
    />

    <!-- FILTERS PANEL -->
    <FiltersPanel 
      v-model="showFilters"
      @apply="handleApplyFilters"
      @clear="handleClearFilters"
    />

  </div>
</template>

<script setup lang="ts">
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import PropertyCardV2 from './PropertyCardV2.vue'
import ComparisonFloatingBar from './ComparisonFloatingBar.vue'
import FiltersPanel from './FiltersPanel.vue'

// Types
interface Property {
  id: number
  name: string
  neighborhood: string
  ref: string
  price: string
  specs: string
  image: string
  agent: { name: string; company: string }
}

// Row configuration type
// Define os tipos de linha disponíveis para o grid editorial
type RowType = 'single' | 'two-col' | 'three-col' | 'four-col'
type ImageHeight = 'tall' | 'medium' | 'short'

interface GridRow {
  type: RowType        // Tipo de layout da linha
  count: number        // Quantidade de cards na linha
  imageHeight: ImageHeight  // Altura das imagens (todas iguais na linha)
}

// State
const viewMode = ref<'grid' | 'map'>('grid')
const searchQuery = ref('')
const showFilters = ref(false)
const showMobileSearch = ref(false)
const imageErrors = ref<Set<number>>(new Set())

const handleImageError = (id: number) => {
  imageErrors.value.add(id)
}

// Comparison State
const isComparisonMode = ref(false)
const selectedProperties = ref<Property[]>([])

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

const router = useRouter()
const navigateToCompare = async () => {
  await navigateTo('/compare')
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

// ============================================
// CONFIGURAÇÃO DO GRID EDITORIAL
// ============================================
// Defina aqui a sequência de linhas e seus formatos.
// Cada linha terá cards com dimensões idênticas.
// 
// Tipos disponíveis:
// - 'single': 1 card full-width (destaque máximo)
// - 'two-col': 2 cards lado a lado (50% cada)
// - 'three-col': 3 cards lado a lado (33% cada)
// - 'four-col': 4 cards lado a lado (25% cada)
//
// Alturas de imagem:
// - 'tall': 400px (para destaques)
// - 'medium': 340px (padrão)
// - 'short': 280px (para grids densos)
// ============================================

const gridRows = ref<GridRow[]>([
  { type: 'two-col', count: 2, imageHeight: 'tall' },
  { type: 'three-col', count: 3, imageHeight: 'medium' },
  { type: 'two-col', count: 2, imageHeight: 'medium' },
  { type: 'three-col', count: 3, imageHeight: 'medium' },
  { type: 'two-col', count: 2, imageHeight: 'tall' },
])

// Calcula o índice inicial de cada linha
const getRowStartIndex = (rowIndex: number): number => {
  let start = 0
  for (let i = 0; i < rowIndex; i++) {
    start += gridRows.value[i].count
  }
  return start
}

// Retorna os imóveis para uma linha específica
const getPropertiesForRow = (rowIndex: number): Property[] => {
  const start = getRowStartIndex(rowIndex)
  const count = gridRows.value[rowIndex].count
  return properties.value.slice(start, start + count)
}

// Mock data for properties (sem layout, agora controlado pelas rows)
const properties = ref<Property[]>([
  // === LINHA 1: 2 colunas ===
  {
    id: 1,
    name: 'Casa Del Sol',
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
  // === LINHA 2: 3 colunas ===
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
  },
  {
    id: 5,
    name: 'Quinta da Baroneza',
    neighborhood: 'Higienópolis — SP',
    ref: 'LE4596',
    price: 'R$ 6.500.000',
    specs: '320m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600210491892-03d54cc0d578?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Maria Clara N.', company: 'Elite Realty' }
  },
  // === LINHA 3: 2 colunas ===
  {
    id: 6,
    name: 'Haras da Prata',
    neighborhood: 'Perdizes — SP',
    ref: 'LE4597',
    price: 'R$ 8.900.000',
    specs: '520m² / 5 Suítes',
    image: 'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Beatriz F.', company: 'Elite Realty' }
  },
  {
    id: 7,
    name: 'Palazzo di Fiori',
    neighborhood: 'Pinheiros — SP',
    ref: 'LE4598',
    price: 'R$ 7.300.000',
    specs: '400m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600585154526-990dced4db0d?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Maria Eduarda C.', company: 'Elite Realty' }
  },
  // === LINHA 4: 3 colunas ===
  {
    id: 8,
    name: 'Mansão Imperial',
    neighborhood: 'Alto de Pinheiros — SP',
    ref: 'LE4599',
    price: 'R$ 9.500.000',
    specs: '600m² / 6 Suítes',
    image: 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Giovanna D.', company: 'Elite Realty' }
  },
  {
    id: 9,
    name: 'Solar das Palmeiras',
    neighborhood: 'Moema — SP',
    ref: 'LE4600',
    price: 'R$ 9.100.000',
    specs: '450m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Valentina L.', company: 'Elite Realty' }
  },
  {
    id: 10,
    name: 'Fazenda Boa Vista',
    neighborhood: 'Vila Mariana — SP',
    ref: 'LE4601',
    price: 'R$ 12.800.000',
    specs: '850m² / 6 Suítes',
    image: 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Helena E.', company: 'Elite Realty' }
  },
  // === LINHA 5: 2 colunas ===
  {
    id: 11,
    name: 'Porto Feliz Resort',
    neighborhood: 'Brooklin — SP',
    ref: 'LE4602',
    price: 'R$ 7.650.000',
    specs: '390m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Ana M.', company: 'Elite Realty' }
  },
  {
    id: 12,
    name: 'Vivendas do Parque',
    neighborhood: 'Cidade Jardim — SP',
    ref: 'LE4603',
    price: 'R$ 8.500.000',
    specs: '520m² / 5 Suítes',
    image: 'https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Manuela P.', company: 'Elite Realty' }
  }
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
.img-zoom { 
  transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); 
}
.group:hover .img-zoom { 
  transform: scale(1.05); 
}
</style>