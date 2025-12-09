<template>
  <Teleport to="body">
    <!-- Floating Bar -->
    <Transition 
      enter-active-class="transform transition duration-500 ease-out"
      enter-from-class="translate-y-full opacity-0"
      enter-to-class="translate-y-0 opacity-100"
      leave-active-class="transform transition duration-300 ease-in"
      leave-from-class="translate-y-0 opacity-100"
      leave-to-class="translate-y-full opacity-0"
    >
      <div 
        v-if="isVisible && !isModalOpen" 
        class="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 flex flex-col items-center gap-2 w-[90%] max-w-md md:w-auto"
      >
        <!-- Tooltip de Limite Atingido -->
        <Transition
          enter-active-class="transition duration-300 ease-out"
          enter-from-class="opacity-0 translate-y-2 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
          leave-active-class="transition duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0 scale-100"
          leave-to-class="opacity-0 translate-y-2 scale-95"
        >
          <div 
            v-if="showLimitTooltip"
            class="bg-text-primary text-white text-xs px-4 py-2 rounded-full shadow-lg flex items-center gap-2 mb-1"
          >
            <i class="lni lni-information text-sm"></i>
            <span class="font-light">Limite de {{ MAX_ITEMS }} imóveis atingido</span>
          </div>
        </Transition>

        <!-- The Bar - Glassmorphism Light -->
        <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 relative w-full md:w-auto justify-between md:justify-start">
          
          <!-- Botão Fechar (Cancelar Seleção) -->
          <button
            @click="handleCancel"
            class="absolute -top-2 -right-2 w-6 h-6 bg-text-primary text-white rounded-full flex items-center justify-center shadow-md hover:bg-text-primary/90 hover:scale-110 transition-all duration-200 group"
            title="Cancelar seleção"
          >
            <i class="lni lni-close text-xs group-hover:rotate-90 transition-transform duration-200"></i>
          </button>

          <!-- Label -->
          <div class="flex flex-col">
            <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
            <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-secondary mt-1">
              {{ selectedProperties.length }} de {{ MAX_ITEMS }}
            </span>
          </div>

          <!-- Avatars -->
          <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
            <!-- Empty Slots / Selected Items -->
            <template v-for="(item, index) in MAX_ITEMS" :key="index">
              <div 
                v-if="selectedProperties[index]"
                class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative group cursor-pointer overflow-hidden bg-surface-offset shadow-md hover:shadow-lg transition-all hover:scale-105"
                @click="handleRemove(selectedProperties[index].id)"
              >
                <img :src="selectedProperties[index].image" class="w-full h-full object-cover" />
                <!-- Hover Remove Icon -->
                <div class="absolute inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all">
                  <i class="lni lni-minus text-white text-xs md:text-lg"></i>
                </div>
              </div>
              <div 
                v-else
                class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner transition-all"
                :class="{ 'border-dashed animate-pulse': isLimitReached }"
              >
                <i class="lni lni-plus text-sm"></i>
              </div>
            </template>
          </div>

          <!-- Action Button -->
          <button 
            @click="openModal"
            class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium transition-all duration-300 ml-2 transform shadow-md"
            :class="selectedProperties.length >= 2 
              ? 'bg-text-primary text-white hover:bg-text-primary/90 hover:scale-105 hover:shadow-lg active:scale-95' 
              : 'bg-surface-offset/50 text-text-secondary/50 cursor-not-allowed backdrop-blur-sm'"
            :disabled="selectedProperties.length < 2"
          >
            Comparar
          </button>

        </div>
      </div>
    </Transition>

    <!-- Comparison Modal/Dialog -->
    <Transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div 
        v-if="isModalOpen" 
        class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4 md:p-6 print:p-0"
      >
        <!-- Backdrop -->
        <div 
          class="absolute inset-0 bg-text-primary/60 backdrop-blur-sm transition-opacity duration-300 no-print"
          @click="closeModal"
        ></div>

        <!-- Modal Window -->
        <div class="relative bg-surface-card w-full h-full sm:h-[90vh] sm:rounded-2xl shadow-2xl flex flex-col overflow-hidden modal-animate max-w-[1400px] print:h-auto print:shadow-none">
          
          <!-- Modal Header -->
          <header class="flex-none h-16 bg-surface-card border-b border-border-subtle flex items-center justify-between px-4 sm:px-6 z-50 no-print">
            <div class="flex items-center gap-4">
              <div class="flex items-center gap-2 text-text-primary">
                <i class="lni lni-stats-up"></i>
                <h2 class="text-xs font-bold uppercase tracking-[0.15em]">Comparador</h2>
              </div>
            </div>

            <div class="flex items-center gap-2 sm:gap-3">
              <button 
                class="hidden md:flex border border-border-strong px-3 py-2 rounded-lg text-[10px] uppercase font-bold text-text-secondary hover:bg-surface-subtle hover:text-text-primary transition-all gap-2 items-center"
                @click="shareComparison"
              >
                <i class="lni lni-share"></i>
                <span class="hidden lg:inline">Compartilhar</span>
              </button>

              <button 
                class="hidden md:flex border border-border-strong px-3 py-2 rounded-lg text-[10px] uppercase font-bold text-text-secondary hover:bg-surface-subtle hover:text-text-primary transition-all gap-2 items-center"
                @click="printComparison"
              >
                <i class="lni lni-printer"></i>
                <span class="hidden lg:inline">Imprimir PDF</span>
              </button>
              
              <button 
                class="bg-text-primary text-text-inverse px-4 py-2 rounded-lg text-[10px] uppercase font-bold hover:bg-text-primary/90 transition-colors gap-2 flex items-center shadow-md"
                @click="contactConcierge"
              >
                <i class="lni lni-whatsapp"></i>
                <span class="hidden sm:inline">Concierge</span>
              </button>

              <div class="w-px h-6 bg-border-subtle mx-2"></div>

              <button 
                @click="closeModal"
                class="w-8 h-8 flex items-center justify-center rounded-full hover:bg-surface-subtle text-text-secondary hover:text-status-error transition-colors"
                title="Fechar (Esc)"
              >
                <i class="lni lni-close text-lg"></i>
              </button>
            </div>
          </header>

          <!-- Scrollable Content -->
          <main class="flex-1 overflow-auto relative custom-scrollbar bg-surface-card">
            <div class="inline-flex flex-col min-w-full">
              
              <!-- Properties Header Row -->
              <div class="sticky top-0 z-30 flex border-b border-border-subtle bg-surface-card/95 backdrop-blur shadow-sm print:bg-surface-card print:border-text-primary">
                
                <!-- Fixed Left Column -->
                <div class="sticky left-0 z-40 w-28 md:w-56 flex-none bg-surface-card border-r border-border-subtle p-3 md:p-6 flex flex-col justify-end pb-5 shadow-[4px_0_24px_rgba(0,0,0,0.04)] print:shadow-none print:border-r-0">
                  <span class="text-[10px] font-bold text-text-secondary uppercase tracking-widest hidden md:block">Propriedades</span>
                  <span class="text-[10px] font-bold text-text-secondary uppercase tracking-widest md:hidden">Imóveis</span>
                  <span class="text-xs text-text-primary font-bold mt-1 flex items-center gap-1">
                    {{ selectedProperties.length }} <span class="text-text-secondary font-normal">de {{ MAX_ITEMS }}</span>
                  </span>
                </div>

                <!-- Property Cards -->
                <div 
                  v-for="prop in selectedProperties" 
                  :key="prop.id"
                  class="w-60 md:w-80 flex-none p-4 md:p-5 bg-surface-card transition-colors relative group/col border-r border-transparent hover:border-border-subtle flex flex-col gap-4 print:w-auto print:flex-1 print:border-r print:border-border-subtle"
                >
                  <!-- Actions -->
                  <div class="absolute top-3 right-3 flex items-center gap-2 opacity-100 lg:opacity-0 lg:group-hover/col:opacity-100 transition-opacity duration-200 z-10 no-print">
                    <a 
                      :href="prop.url || '#'" 
                      target="_blank" 
                      title="Ver Detalhes"
                      class="w-8 h-8 flex items-center justify-center rounded-full bg-surface-subtle text-text-secondary hover:bg-text-primary hover:text-text-inverse transition-colors shadow-sm"
                    >
                      <i class="lni lni-arrow-right transform -rotate-45"></i>
                    </a>
                    <button 
                      @click="handleRemove(prop.id)"
                      title="Remover"
                      class="w-8 h-8 flex items-center justify-center rounded-full bg-surface-subtle text-text-secondary hover:bg-status-error/10 hover:text-status-error transition-colors shadow-sm"
                    >
                      <i class="lni lni-trash-can"></i>
                    </button>
                  </div>
                  
                  <!-- Info Card -->
                  <div class="flex items-center gap-3 md:gap-4 mt-2">
                    <a 
                      :href="prop.url || '#'" 
                      target="_blank" 
                      class="relative w-12 h-12 md:w-14 md:h-14 rounded-full overflow-hidden border border-border-subtle shadow-sm flex-shrink-0 group-hover/col:scale-105 transition-transform duration-300 print:w-10 print:h-10"
                    >
                      <img :src="prop.image" class="w-full h-full object-cover" />
                    </a>
                    <div class="min-w-0 flex-1">
                      <h3 class="font-serif text-sm font-medium truncate text-text-primary leading-tight">
                        <a :href="prop.url || '#'" target="_blank" class="hover:underline decoration-1 underline-offset-2">
                          {{ prop.name || prop.title || 'Imóvel' }}
                        </a>
                      </h3>
                      <p class="text-[10px] md:text-[11px] text-text-secondary font-bold uppercase tracking-wide mt-1">
                        {{ formatPrice(prop.price) }}
                      </p>
                    </div>
                  </div>
                </div>

                <!-- Add Property Card -->
                <div 
                  v-if="selectedProperties.length < MAX_ITEMS"
                  class="w-40 md:w-60 flex-none p-5 flex flex-col items-center justify-center border-r border-dashed border-border-subtle bg-surface-subtle/40 hover:bg-surface-subtle transition-colors cursor-pointer group/add no-print"
                  @click="handleAddProperty"
                >
                  <div class="w-10 h-10 md:w-12 md:h-12 rounded-full bg-surface-card border border-border-subtle flex items-center justify-center text-text-secondary group-hover/add:text-text-primary group-hover/add:border-text-primary transition-all mb-3 shadow-sm">
                    <i class="lni lni-plus"></i>
                  </div>
                  <span class="text-[10px] font-bold uppercase tracking-wider text-text-secondary group-hover/add:text-text-primary">Adicionar</span>
                </div>
              </div>

              <!-- Comparison Sections -->
              <div class="flex-1 pb-16 bg-surface-card">
                <div v-for="section in sections" :key="section.id">
                  
                  <!-- Section Header -->
                  <div 
                    @click="toggleSection(section.id)"
                    class="relative min-w-full bg-surface-subtle border-y border-border-subtle cursor-pointer hover:bg-surface-offset/30 transition-colors z-10 mt-[-1px] print:bg-surface-card print:border-text-primary print:border-t-2"
                  >
                    <div class="sticky left-0 px-3 md:px-6 py-2.5 flex items-center gap-2 md:gap-3 w-max">
                      <i 
                        class="lni lni-chevron-down text-[10px] text-text-secondary transition-transform duration-300 no-print"
                        :class="{ '-rotate-90': !expandedSections.includes(section.id) }"
                      ></i>
                      <span class="text-[10px] font-bold uppercase tracking-widest text-text-secondary print:text-text-primary">{{ section.title }}</span>
                    </div>
                  </div>

                  <!-- Section Rows -->
                  <template v-if="expandedSections.includes(section.id)">
                    <div 
                      v-for="row in section.rows" 
                      :key="row.key"
                      class="flex border-b border-border-hairline transition-colors h-16 group cursor-default print:h-auto print:py-2 print:border-border-subtle"
                    >
                      <!-- Row Label -->
                      <div class="sticky left-0 z-20 w-28 md:w-56 flex-none bg-surface-card/95 backdrop-blur-sm border-r border-border-subtle px-3 md:px-6 flex items-center shadow-[4px_0_24px_rgba(0,0,0,0.04)] group-hover:bg-action-primary/5 transition-colors print:shadow-none print:border-none print:bg-surface-card">
                        <div class="relative w-full pl-0 md:pl-2">
                          <span class="text-[10px] md:text-xs text-text-secondary font-medium group-hover:text-action-primary transition-colors block leading-tight print:text-text-primary">{{ row.label }}</span>
                        </div>
                      </div>

                      <!-- Data Cells -->
                      <div 
                        v-for="prop in selectedProperties" 
                        :key="prop.id"
                        class="w-60 md:w-80 flex-none px-4 md:px-5 flex items-center border-r border-border-hairline group-hover:bg-action-primary/5 transition-colors print:w-auto print:flex-1 print:border-0"
                      >
                        <span 
                          class="text-xs md:text-sm truncate w-full print:whitespace-normal"
                          :class="isRowDifferent(row.key) ? 'font-bold text-text-primary' : 'text-text-secondary font-light'"
                        >
                          <template v-if="row.key === 'security' || row.key === 'light'">
                            <span class="inline-flex items-center px-2 py-0.5 md:px-2.5 md:py-1 rounded text-[10px] md:text-xs font-medium bg-surface-subtle text-text-secondary border border-border-subtle whitespace-nowrap print:border-0 print:pl-0">
                              {{ getPropertyValue(prop, row.key) }}
                            </span>
                          </template>
                          <template v-else>
                            {{ getPropertyValue(prop, row.key) }}
                          </template>
                        </span>
                      </div>

                      <!-- Empty Space -->
                      <div 
                        v-if="selectedProperties.length < MAX_ITEMS"
                        class="w-40 md:w-60 flex-none bg-surface-subtle/10 border-r border-dashed border-border-subtle group-hover:bg-surface-subtle/30 transition-colors no-print"
                      ></div>
                    </div>
                  </template>
                </div>
              </div>

            </div>
          </main>

        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'

interface Property {
  id: number | string
  image: string
  name?: string
  title?: string
  price?: number | string
  url?: string
  area?: string
  suites?: string
  ceiling?: string
  light?: string
  security?: string
  concierge?: string
  condoFee?: string
  iptu?: string
  location?: string
  [key: string]: any
}

const props = defineProps<{
  isVisible: boolean
  selectedProperties: Property[]
}>()

const emit = defineEmits<{
  (e: 'remove', id: number | string): void
  (e: 'compare'): void
  (e: 'cancel'): void
  (e: 'add'): void
}>()

// Constants
const MAX_ITEMS = 4

// State
const isModalOpen = ref(false)
const expandedSections = ref(['essence', 'details', 'costs', 'amenities'])
const showLimitTooltip = ref(false)
let tooltipTimeout: ReturnType<typeof setTimeout> | null = null

// Computed
const isLimitReached = computed(() => props.selectedProperties.length >= MAX_ITEMS)

// Watch para mostrar tooltip quando limite é atingido
watch(() => props.selectedProperties.length, (newLen, oldLen) => {
  if (newLen >= MAX_ITEMS && oldLen < MAX_ITEMS) {
    showLimitTooltip.value = true
    // Auto-hide after 3 seconds
    if (tooltipTimeout) clearTimeout(tooltipTimeout)
    tooltipTimeout = setTimeout(() => {
      showLimitTooltip.value = false
    }, 3000)
  }
})

// Comparison sections configuration
const sections = [
  {
    id: 'essence',
    title: 'Essência',
    rows: [
      { label: 'Localização', key: 'location' },
      { label: 'Área Privativa', key: 'area' },
      { label: 'Suítes', key: 'suites' },
      { label: 'Valor de Venda', key: 'price' }
    ]
  },
  {
    id: 'details',
    title: 'Detalhes Técnicos',
    rows: [
      { label: 'Pé-direito', key: 'ceiling' },
      { label: 'Iluminação Natural', key: 'light' }
    ]
  },
  {
    id: 'costs',
    title: 'Custos',
    rows: [
      { label: 'Condomínio', key: 'condoFee' },
      { label: 'IPTU (mensal)', key: 'iptu' }
    ]
  },
  {
    id: 'amenities',
    title: 'Comodidades',
    rows: [
      { label: 'Segurança', key: 'security' },
      { label: 'Concierge', key: 'concierge' }
    ]
  }
]

// Methods
const openModal = () => {
  if (props.selectedProperties.length >= 2) {
    isModalOpen.value = true
    document.body.style.overflow = 'hidden'
    emit('compare')
  }
}

const closeModal = () => {
  isModalOpen.value = false
  document.body.style.overflow = ''
}

const handleRemove = (id: number | string) => {
  emit('remove', id)
  if (props.selectedProperties.length <= 1) {
    closeModal()
  }
}

const handleCancel = () => {
  closeModal()
  emit('cancel')
}

const handleAddProperty = () => {
  closeModal()
  emit('add')
}

const toggleSection = (sectionId: string) => {
  const index = expandedSections.value.indexOf(sectionId)
  if (index > -1) {
    expandedSections.value.splice(index, 1)
  } else {
    expandedSections.value.push(sectionId)
  }
}

const isRowDifferent = (key: string): boolean => {
  if (props.selectedProperties.length < 2) return false
  const values = props.selectedProperties.map(p => getPropertyValue(p, key))
  return new Set(values).size > 1
}

const getPropertyValue = (prop: Property, key: string): string => {
  const value = prop[key]
  if (value === undefined || value === null) return '—'
  if (key === 'price' && typeof value === 'number') {
    return formatPrice(value)
  }
  return String(value)
}

const formatPrice = (price: number | string | undefined): string => {
  if (price === undefined || price === null) return '—'
  if (typeof price === 'string') return price
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    maximumFractionDigits: 0
  }).format(price)
}

const shareComparison = () => {
  // Copy link to clipboard
  navigator.clipboard?.writeText(window.location.href)
  alert('Link copiado para a área de transferência!')
}

const printComparison = () => {
  window.print()
}

const contactConcierge = () => {
  // Open WhatsApp or contact form
  alert('Conectando com Concierge...')
}

// Keyboard shortcuts
const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === 'Escape' && isModalOpen.value) {
    closeModal()
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeydown)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Premium Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

/* Modal Animation */
@keyframes modalIn {
  from {
    opacity: 0;
    transform: scale(0.98) translateY(10px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
.modal-animate {
  animation: modalIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

/* Print Styles */
@media print {
  .no-print {
    display: none !important;
  }
  .custom-scrollbar {
    overflow: visible !important;
  }
  .sticky {
    position: static !important;
  }
  * {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
}
</style>
