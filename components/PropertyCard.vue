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

const emit = defineEmits<{
  (e: 'add-to-compare', property: Property): void
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
  <article class="group cursor-pointer bg-surface-card transition-all duration-500 hover:shadow-xl">
    <!-- Imagem -->
    <div class="relative aspect-[4/3] overflow-hidden">
      <img 
        :src="mainImage" 
        :alt="property.title"
        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
        loading="lazy"
      />
      
      <!-- Badges -->
      <div class="absolute top-4 left-4 flex gap-2">
        <span class="px-3 py-1 bg-surface-base/90 backdrop-blur text-[10px] uppercase tracking-widest font-medium text-text-primary">
          {{ transactionLabel }}
        </span>
      </div>
      
      <!-- Actions Overlay -->
      <div class="absolute inset-0 bg-deep-brown/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
        <button 
          class="w-10 h-10 bg-off-white rounded-full flex items-center justify-center text-deep-brown hover:bg-deep-brown hover:text-off-white transition-colors duration-300"
          @click.stop="emit('add-to-compare', property)"
          title="Comparar"
        >
          <span class="text-lg">+</span>
        </button>
        <NuxtLink 
          :to="`/imovel/${property.slug}`"
          class="w-10 h-10 bg-off-white rounded-full flex items-center justify-center text-deep-brown hover:bg-deep-brown hover:text-off-white transition-colors duration-300"
          title="Ver Detalhes"
        >
          <span class="text-lg">→</span>
        </NuxtLink>
      </div>
    </div>
    
    <!-- Conteúdo -->
    <div class="p-6 space-y-4">
      <!-- Header -->
      <div class="flex justify-between items-start">
        <div>
          <span class="text-xs font-mono text-secondary uppercase tracking-widest block mb-1">
            {{ propertyTypeLabel }}
          </span>
          <h3 class="text-lg font-light text-text-primary leading-tight line-clamp-1 group-hover:text-action-primary transition-colors duration-300">
            {{ property.title }}
          </h3>
        </div>
      </div>

      <!-- Preço -->
      <div class="border-t border-border-subtle pt-4">
        <span class="text-xl font-medium text-text-primary block">
          {{ formatPrice(property.price) }}
          <span v-if="property.transactionType === 'rent'" class="text-sm font-light text-secondary">/mês</span>
        </span>
        <p class="text-sm text-secondary font-light mt-1">
          {{ property.address.region }}, {{ property.address.city }}
        </p>
      </div>
      
      <!-- Specs -->
      <div class="flex items-center gap-6 text-sm text-secondary font-light pt-2">
        <div class="flex items-center gap-2">
          <span>{{ formatArea(property.area) }}</span>
        </div>
        <div v-if="property.bedrooms" class="flex items-center gap-2">
          <span>{{ property.bedrooms }} qts</span>
        </div>
        <div v-if="property.parkingSpots" class="flex items-center gap-2">
          <span>{{ property.parkingSpots }} vgs</span>
        </div>
      </div>
    </div>
  </article>
</template>

