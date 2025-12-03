<script setup lang="ts">
interface Property {
  id: string
  slug: string
  title: string
  transactionType: 'sell' | 'rent'
  propertyType: string
  price: number
  area: number
  bedrooms: number
  suites: number
  parkingSpots: number
  address: {
    city: string
    region: string
    street?: string
  }
  images: Array<{ url: string }>
}

interface ApiResponse {
  properties: Property[]
  pagination: {
    page: number
    perPage: number
    total: number
    totalPages: number
  }
}

// Estado
const properties = ref<Property[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const currentPage = ref(1)
const totalPages = ref(1)
const totalProperties = ref(0)
const currentFilters = ref<Record<string, string | number>>({
  transactionType: 'sell'
})

// SEO
useSeoMeta({
  title: 'Buscar Imóveis | Pilar Clone',
  description: 'Encontre apartamentos, casas, coberturas e terrenos para comprar ou alugar.'
})

// Buscar imóveis
const fetchProperties = async (filters: Record<string, string | number> = {}) => {
  loading.value = true
  error.value = null
  
  try {
    const query = new URLSearchParams()
    
    // Adicionar filtros
    Object.entries({ ...currentFilters.value, ...filters }).forEach(([key, value]) => {
      if (value) {
        query.append(key, String(value))
      }
    })
    
    query.append('page', String(currentPage.value))
    query.append('perPage', '12')
    
    const response = await $fetch<ApiResponse>(`/api/properties?${query.toString()}`)
    
    if (response.error) {
      throw new Error(response.message || 'Erro ao buscar imóveis')
    }
    
    properties.value = response.properties || []
    totalPages.value = response.pagination?.totalPages || 1
    totalProperties.value = response.pagination?.total || 0
    
  } catch (err) {
    console.error('Error:', err)
    error.value = 'Não foi possível carregar os imóveis. Tente novamente.'
    properties.value = []
  } finally {
    loading.value = false
  }
}

// Aplicar filtros
const handleFilter = (filters: Record<string, string | number>) => {
  currentFilters.value = { ...currentFilters.value, ...filters }
  currentPage.value = 1
  fetchProperties(filters)
}

// Paginação
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    fetchProperties()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
    fetchProperties()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

// Carregar ao montar
onMounted(() => {
  fetchProperties()
})
</script>

<template>
  <div class="bg-gray-50 min-h-screen">
    <!-- Hero Section -->
    <section class="bg-primary text-white py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl md:text-4xl font-bold mb-2">
          Encontre seu imóvel ideal
        </h1>
        <p class="text-gray-400 mb-8">
          Mais de {{ totalProperties.toLocaleString() }} imóveis disponíveis
        </p>
        
        <!-- Filtros -->
        <SearchFilters @filter="handleFilter" />
      </div>
    </section>
    
    <!-- Resultados -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Header dos Resultados -->
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-xl font-semibold text-gray-900">
          <span v-if="loading">Buscando...</span>
          <span v-else-if="error">Erro</span>
          <span v-else>
            {{ totalProperties.toLocaleString() }} imóveis encontrados
          </span>
        </h2>
        
        <div class="text-sm text-gray-500">
          Página {{ currentPage }} de {{ totalPages }}
        </div>
      </div>
      
      <!-- Loading State -->
      <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="n in 6" 
          :key="n" 
          class="bg-white rounded-xl border border-gray-200 overflow-hidden animate-pulse"
        >
          <div class="aspect-[4/3] bg-gray-200"></div>
          <div class="p-4 space-y-3">
            <div class="h-6 bg-gray-200 rounded w-3/4"></div>
            <div class="h-4 bg-gray-200 rounded w-1/2"></div>
            <div class="h-4 bg-gray-200 rounded w-full"></div>
          </div>
        </div>
      </div>
      
      <!-- Error State -->
      <div v-else-if="error" class="text-center py-12">
        <div class="text-red-500 mb-4">
          <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
        <p class="text-gray-600 mb-4">{{ error }}</p>
        <button @click="fetchProperties()" class="btn-primary">
          Tentar novamente
        </button>
      </div>
      
      <!-- Empty State -->
      <div v-else-if="properties.length === 0" class="text-center py-12">
        <div class="text-gray-400 mb-4">
          <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
        </div>
        <p class="text-gray-600">Nenhum imóvel encontrado com esses filtros.</p>
      </div>
      
      <!-- Grid de Imóveis -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PropertyCard 
          v-for="property in properties" 
          :key="property.id" 
          :property="property"
        />
      </div>
      
      <!-- Paginação -->
      <div v-if="!loading && properties.length > 0" class="flex items-center justify-center gap-4 mt-8">
        <button 
          @click="prevPage" 
          :disabled="currentPage === 1"
          class="btn-secondary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          ← Anterior
        </button>
        
        <span class="text-gray-600">
          Página {{ currentPage }} de {{ totalPages }}
        </span>
        
        <button 
          @click="nextPage" 
          :disabled="currentPage === totalPages"
          class="btn-secondary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Próxima →
        </button>
      </div>
    </section>
  </div>
</template>
