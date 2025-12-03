<script setup lang="ts">
const emit = defineEmits<{
  (e: 'filter', filters: Record<string, string | number>): void
}>()

const filters = reactive({
  transactionType: 'sell',
  propertyType: '',
  city: '',
  minPrice: '',
  maxPrice: '',
  bedrooms: ''
})

const propertyTypes = [
  { value: '', label: 'Todos os tipos' },
  { value: 'apartment', label: 'Apartamento' },
  { value: 'house', label: 'Casa' },
  { value: 'penthouse', label: 'Cobertura' },
  { value: 'land', label: 'Terreno' },
  { value: 'commercial', label: 'Comercial' }
]

const bedroomOptions = [
  { value: '', label: 'Quartos' },
  { value: '1', label: '1 quarto' },
  { value: '2', label: '2 quartos' },
  { value: '3', label: '3 quartos' },
  { value: '4', label: '4+ quartos' }
]

const applyFilters = () => {
  const activeFilters: Record<string, string | number> = {}
  
  Object.entries(filters).forEach(([key, value]) => {
    if (value) {
      activeFilters[key] = value
    }
  })
  
  emit('filter', activeFilters)
}

// Aplicar filtros quando transactionType mudar
watch(() => filters.transactionType, () => {
  applyFilters()
})
</script>

<template>
  <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
    <!-- Toggle Venda/Aluguel -->
    <div class="flex gap-2 mb-4">
      <button
        @click="filters.transactionType = 'sell'"
        :class="[
          'flex-1 py-2 px-4 rounded-lg font-medium transition-colors',
          filters.transactionType === 'sell' 
            ? 'bg-primary text-white' 
            : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
        ]"
      >
        Comprar
      </button>
      <button
        @click="filters.transactionType = 'rent'"
        :class="[
          'flex-1 py-2 px-4 rounded-lg font-medium transition-colors',
          filters.transactionType === 'rent' 
            ? 'bg-primary text-white' 
            : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
        ]"
      >
        Alugar
      </button>
    </div>
    
    <!-- Grid de Filtros -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3 mb-4">
      <!-- Cidade -->
      <div>
        <input
          v-model="filters.city"
          type="text"
          placeholder="Cidade ou bairro"
          class="input"
        />
      </div>
      
      <!-- Tipo de Imóvel -->
      <div>
        <select v-model="filters.propertyType" class="select">
          <option 
            v-for="type in propertyTypes" 
            :key="type.value" 
            :value="type.value"
          >
            {{ type.label }}
          </option>
        </select>
      </div>
      
      <!-- Quartos -->
      <div>
        <select v-model="filters.bedrooms" class="select">
          <option 
            v-for="opt in bedroomOptions" 
            :key="opt.value" 
            :value="opt.value"
          >
            {{ opt.label }}
          </option>
        </select>
      </div>
      
      <!-- Preço -->
      <div class="flex gap-2">
        <input
          v-model="filters.minPrice"
          type="number"
          placeholder="Min"
          class="input w-1/2"
        />
        <input
          v-model="filters.maxPrice"
          type="number"
          placeholder="Max"
          class="input w-1/2"
        />
      </div>
    </div>
    
    <!-- Botão Buscar -->
    <button
      @click="applyFilters"
      class="w-full btn-primary py-3 flex items-center justify-center gap-2"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
      Buscar Imóveis
    </button>
  </div>
</template>
