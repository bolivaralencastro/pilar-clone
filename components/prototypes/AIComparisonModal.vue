<template>
  <div v-if="isOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4">
    <!-- Backdrop -->
    <div 
      class="absolute inset-0 bg-black/70 backdrop-blur-sm transition-opacity" 
      @click="closeModal"
    ></div>
    
    <!-- Modal Content -->
    <div 
      class="relative bg-surface-base rounded-lg border border-border-subtle w-full max-w-2xl max-h-[80vh] overflow-hidden shadow-2xl"
    >
      <!-- Header -->
      <div class="flex items-center justify-between p-6 border-b border-border-subtle">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-full bg-brand-primary/10 flex items-center justify-center">
            <i class="lni lni-ai text-brand-primary text-lg"></i>
          </div>
          <h2 class="text-lg font-semibold text-text-primary">Assistente de Compra</h2>
        </div>
        <button 
          @click="closeModal"
          class="p-1 rounded-full hover:bg-surface-subtle transition-colors"
        >
          <i class="lni lni-close text-text-secondary"></i>
        </button>
      </div>

      <!-- Content -->
      <div class="p-6 overflow-y-auto max-h-[calc(80vh-140px)]">
        <!-- Loading State -->
        <div v-if="isLoading" class="flex flex-col items-center py-8">
          <div class="w-12 h-12 border-4 border-brand-primary border-t-transparent rounded-full animate-spin mb-4"></div>
          <p class="text-text-secondary mb-6">Analisando imóveis selecionados...</p>
          <div class="w-full bg-surface-subtle rounded-full h-2">
            <div class="bg-brand-primary h-2 rounded-full animate-pulse" 
                 :style="{ width: progress + '%' }"></div>
          </div>
          <div class="mt-4 text-xs text-text-secondary">
            {{ loadingMessage }}
          </div>
        </div>

        <!-- Resultado -->
        <div v-else-if="result">
          <div class="flex items-start gap-3 mb-6">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-brand-primary to-brand-secondary flex items-center justify-center">
              <i class="lni lni-ai text-white text-lg"></i>
            </div>
            <div>
              <h3 class="font-medium text-text-primary mb-2">Recomendação da IA</h3>
              <div class="text-sm text-text-secondary">
                <div v-for="(line, index) in result.analysis" :key="index" class="mb-2 last:mb-0">
                  {{ line }}
                </div>
              </div>
            </div>
          </div>
          
          <div class="border-t border-border-subtle pt-6">
            <h4 class="font-medium text-text-primary mb-4">Resumo Comparativo</h4>
            <div class="space-y-3">
              <div 
                v-for="(item, index) in result.properties" 
                :key="index" 
                class="p-4 rounded-lg border"
                :class="item.isRecommended ? 'border-green-500 bg-green-50/30' : 'border-border-subtle bg-surface-subtle'"
              >
                <div class="flex justify-between items-start">
                  <div>
                    <h5 class="font-medium text-text-primary">{{ item.name }}</h5>
                    <p class="text-xs text-text-secondary mt-1">{{ item.summary }}</p>
                  </div>
                  <div v-if="item.isRecommended" class="bg-green-500/10 text-green-600 px-2 py-1 rounded text-xs font-medium">
                    Recomendado
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

interface Property {
  id: string
  name: string
  location: string
  price: string
  area: string
  suites: string
  ceiling: string
  light: string
  security: string
  concierge: string
  schoolDistance: string
  walkability: string
  condoFee: string
  iptu: string
}

interface ModalResult {
  analysis: string[]
  properties: Array<{
    name: string
    summary: string
    isRecommended: boolean
  }>
}

const props = defineProps<{
  isOpen: boolean
  properties: Property[]
}>()

const emit = defineEmits<{
  close: []
}>()

const isLoading = ref(false)
const progress = ref(0)
const result = ref<ModalResult | null>(null)
const loadingMessage = ref("")

const closeModal = () => {
  emit('close')
  isLoading.value = false
  progress.value = 0
  result.value = null
}

// Função para simular a IA
const simulateAIAnalysis = () => {
  isLoading.value = true
  progress.value = 0
  result.value = null

  const messages = [
    "Analisando características dos imóveis...",
    "Comparando localizações e valores...",
    "Avaliando custos-benefício...",
    "Considerando critérios de valorização...",
    "Finalizando recomendação..."
  ]

  let currentMessageIndex = 0
  const interval = setInterval(() => {
    progress.value += 20
    loadingMessage.value = messages[currentMessageIndex]
    currentMessageIndex++

    if (progress.value >= 100) {
      clearInterval(interval)
      setTimeout(() => {
        generateMockResult()
      }, 500)
    }
  }, 800)
}

const generateMockResult = () => {
  // Dados mockados para a análise
  result.value = {
    analysis: [
      `Após análise detalhada, o ${props.properties[0].name} se destaca por oferecer o melhor equilíbrio entre localização, área útil e valorização potencial.`,
      `O imóvel apresenta características que atendem diretamente às suas preferências de pé-direito elevado e iluminação natural.`,
      `Apesar de ter um valor ligeiramente superior, o custo-benefício é superior devido à localização privilegiada e comodidades exclusivas.`,
      `A combinação de segurança, conforto e proximidade a centros educacionais o torna ideal para sua família.`
    ],
    properties: props.properties.map((prop, index) => ({
      name: prop.name,
      summary: `${prop.area} | ${prop.suites} | ${prop.location} | ${prop.price}`,
      isRecommended: index === 0 // Primeiro imóvel é o recomendado
    }))
  }

  isLoading.value = false
}

// Observa quando o modal abre para iniciar a simulação
watch(() => props.isOpen, (newValue) => {
  if (newValue) {
    nextTick(() => {
      simulateAIAnalysis()
    })
  } else {
    isLoading.value = false
    progress.value = 0
    result.value = null
  }
})
</script>