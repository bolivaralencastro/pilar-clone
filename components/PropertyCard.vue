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
  broker?: {
    name: string
    photo?: string
  }
}

const props = defineProps<{
  property: Property
}>()

const formatPrice = (price: number): string => {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(price)
}

const formatArea = (area: number): string => {
  return `${area} m²`
}

const mainImage = computed(() => {
  return props.property.images?.[0]?.url || '/placeholder.jpg'
})

const transactionLabel = computed(() => {
  return props.property.transactionType === 'sell' ? 'Venda' : 'Aluguel'
})

const propertyTypeLabel = computed(() => {
  const types: Record<string, string> = {
    apartment: 'Apartamento',
    house: 'Casa',
    penthouse: 'Cobertura',
    land: 'Terreno',
    commercial: 'Comercial'
  }
  return types[props.property.propertyType] || props.property.propertyType
})
</script>

<template>
  <article class="card overflow-hidden group cursor-pointer">
    <!-- Imagem -->
    <div class="relative aspect-[4/3] overflow-hidden">
      <img 
        :src="mainImage" 
        :alt="property.title"
        class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
        loading="lazy"
      />
      
      <!-- Badges -->
      <div class="absolute top-3 left-3 flex gap-2">
        <span 
          :class="property.transactionType === 'sell' ? 'badge-sale' : 'badge-rent'"
        >
          {{ transactionLabel }}
        </span>
        <span class="badge bg-white/90 text-gray-700">
          {{ propertyTypeLabel }}
        </span>
      </div>
      
      <!-- Favorito -->
      <button 
        class="absolute top-3 right-3 w-8 h-8 bg-white/90 rounded-full flex items-center justify-center
               hover:bg-white transition-colors"
        aria-label="Adicionar aos favoritos"
      >
        <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
        </svg>
      </button>
    </div>
    
    <!-- Conteúdo -->
    <div class="p-4">
      <!-- Preço -->
      <div class="mb-2">
        <span class="text-xl font-bold text-primary">
          {{ formatPrice(property.price) }}
        </span>
        <span v-if="property.transactionType === 'rent'" class="text-gray-500 text-sm">
          /mês
        </span>
      </div>
      
      <!-- Título -->
      <h3 class="font-semibold text-gray-900 mb-1 line-clamp-1">
        {{ property.title }}
      </h3>
      
      <!-- Localização -->
      <p class="text-gray-500 text-sm mb-3 line-clamp-1">
        {{ property.address.region }}, {{ property.address.city }}
      </p>
      
      <!-- Características -->
      <div class="flex items-center gap-4 text-sm text-gray-600 border-t border-gray-100 pt-3">
        <div class="flex items-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
          </svg>
          <span>{{ formatArea(property.area) }}</span>
        </div>
        
        <div v-if="property.bedrooms" class="flex items-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          <span>{{ property.bedrooms }} quarto{{ property.bedrooms > 1 ? 's' : '' }}</span>
        </div>
        
        <div v-if="property.parkingSpots" class="flex items-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
          <span>{{ property.parkingSpots }} vaga{{ property.parkingSpots > 1 ? 's' : '' }}</span>
        </div>
      </div>
    </div>
  </article>
</template>
