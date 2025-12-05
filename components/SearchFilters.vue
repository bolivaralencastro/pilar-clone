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
  <div class="bg-surface-card border border-border-subtle p-8 shadow-sm">
    <!-- Toggle Venda/Aluguel -->
    <div class="flex gap-8 mb-8 border-b border-border-subtle pb-4">
      <button
        @click="filters.transactionType = 'sell'"
        :class="[
          'text-sm font-medium uppercase tracking-widest transition-colors pb-4 -mb-4 border-b-2',
          filters.transactionType === 'sell' 
            ? 'border-action-primary text-action-primary' 
            : 'border-transparent text-secondary hover:text-action-primary'
        ]"
      >
        Comprar
      </button>
      <button
        @click="filters.transactionType = 'rent'"
        :class="[
          'text-sm font-medium uppercase tracking-widest transition-colors pb-4 -mb-4 border-b-2',
          filters.transactionType === 'rent' 
            ? 'border-action-primary text-action-primary' 
            : 'border-transparent text-secondary hover:text-action-primary'
        ]"
      >
        Alugar
      </button>
    </div>
    
    <!-- Grid de Filtros -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Cidade -->
      <div class="group">
        <label class="block text-xs font-mono text-secondary uppercase tracking-widest mb-2">Localização</label>
        <input
          v-model="filters.city"
          type="text"
          placeholder="Cidade ou bairro"
          class="w-full border-b border-border-subtle py-2 text-text-primary placeholder-secondary/50 focus:outline-none focus:border-action-primary transition-colors bg-transparent"
        />
      </div>
      
      <!-- Tipo de Imóvel -->
      <div class="group">
        <label class="block text-xs font-mono text-secondary uppercase tracking-widest mb-2">Tipo</label>
        <select 
          v-model="filters.propertyType" 
          class="w-full border-b border-border-subtle py-2 text-text-primary focus:outline-none focus:border-action-primary transition-colors bg-transparent appearance-none cursor-pointer"
        >
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
      <div class="group">
        <label class="block text-xs font-mono text-secondary uppercase tracking-widest mb-2">Dormitórios</label>
        <select 
          v-model="filters.bedrooms" 
          class="w-full border-b border-border-subtle py-2 text-text-primary focus:outline-none focus:border-action-primary transition-colors bg-transparent appearance-none cursor-pointer"
        >
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
      <div class="group">
        <label class="block text-xs font-mono text-secondary uppercase tracking-widest mb-2">Faixa de Preço</label>
        <div class="flex gap-4">
          <input
            v-model="filters.minPrice"
            type="number"
            placeholder="Min"
            class="w-1/2 border-b border-border-subtle py-2 text-text-primary placeholder-secondary/50 focus:outline-none focus:border-action-primary transition-colors bg-transparent"
          />
          <input
            v-model="filters.maxPrice"
            type="number"
            placeholder="Max"
            class="w-1/2 border-b border-border-subtle py-2 text-text-primary placeholder-secondary/50 focus:outline-none focus:border-action-primary transition-colors bg-transparent"
          />
        </div>
      </div>
    </div>
    
    <!-- Botão Buscar -->
    <button
      @click="applyFilters"
      class="w-full btn-primary py-4 flex items-center justify-center gap-3 group"
    >
      <span class="text-sm font-medium uppercase tracking-widest">Buscar Imóveis</span>
      <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
              d="M17 8l4 4m0 0l-4 4m4-4H3" />
      </svg>
    </button>
  </div>
</template>


