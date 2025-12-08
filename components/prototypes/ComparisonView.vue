<template>
  <div class="w-full min-h-screen font-sans text-text-primary bg-surface-base">
    
    <div class="w-full">
      <!-- Topbar com ações -->
      <header class="sticky top-0 z-50 bg-surface-base/95 backdrop-blur-sm border-b border-border-subtle">
        <div class="max-w-[1280px] mx-auto px-4 md:px-8 py-3 flex items-center justify-between">
          <div class="flex items-center gap-4">
            <button @click="backToListing" class="flex items-center gap-2 text-xs uppercase tracking-widest text-text-secondary hover:text-text-primary transition-colors">
              <i class="lni lni-arrow-left"></i>
              Voltar
            </button>
            <div class="h-4 w-px bg-border-subtle"></div>
            <span class="text-xs uppercase tracking-widest text-text-tertiary">{{ selectedProperties.length }} imóveis</span>
          </div>
          
          <div class="flex items-center gap-3">
            <div class="h-4 w-px bg-border-subtle hidden md:block"></div>
            <button class="hidden md:flex border border-border-strong px-4 py-2 rounded text-xs uppercase tracking-widest font-medium text-text-primary hover:bg-surface-subtle transition-colors items-center gap-2" @click="saveComparison">
              <i class="lni lni-bookmark"></i>
              Salvar
            </button>
            <button class="bg-text-primary text-surface-base px-4 py-2 rounded text-xs uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors flex items-center gap-2" @click="contactConcierge">
              <i class="lni lni-comments-alt"></i>
              <span class="hidden md:inline">Falar com Concierge</span>
              <span class="md:hidden">Contato</span>
            </button>
          </div>
        </div>
      </header>

      <!-- Sticky header com nome e preço dos imóveis -->
      <div class="sticky top-[53px] z-40 bg-surface-base/95 backdrop-blur-sm border-b border-border-subtle">
        <div class="max-w-[1280px] mx-auto px-4 md:px-8 py-3">
          <!-- Usando pl-6 para compensar o padding interno dos cards (p-6) -->
          <div class="grid gap-4 pl-6" :style="gridStyle">
            <div class="hidden md:block"></div>
            <div v-for="prop in selectedProperties" :key="prop.id" class="flex items-center gap-3">
              <div class="w-10 h-10 rounded overflow-hidden flex-shrink-0 bg-surface-offset">
                <img 
                  :src="prop.image" 
                  :alt="prop.name"
                  class="w-full h-full object-cover"
                />
              </div>
              <div class="min-w-0">
                <div class="font-serif text-sm leading-tight text-text-primary truncate">{{ prop.name }}</div>
                <div class="text-xs font-medium text-text-secondary">{{ prop.price }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="max-w-[1280px] mx-auto px-4 md:px-8 py-6">
        <!-- Seções de Comparação -->
        <section class="space-y-4">
        <div v-for="section in sections" :key="section.id" class="bg-surface-card border border-border-subtle rounded-lg p-6">
          <div class="mb-6 border-b border-border-subtle pb-4">
            <h3 class="text-sm font-medium text-text-primary uppercase tracking-widest mb-1">{{ section.title }}</h3>
            <p class="text-xs text-text-tertiary font-light">{{ section.subtitle }}</p>
          </div>

          <div class="flex flex-col gap-2">
            <template v-for="row in section.rows" :key="row.key">
              <div 
                class="grid gap-4 items-center py-3 border-b border-dashed border-border-subtle last:border-0" 
                :style="gridStyle"
              >
                <div class="text-xs font-medium text-text-secondary uppercase tracking-wide">{{ row.label }}</div>
                
                <div 
                  v-for="prop in selectedProperties" 
                  :key="prop.id" 
                  class="text-sm font-light text-text-primary break-words pl-2"
                  :class="{ 'border-l-2 border-text-primary font-medium': isRowDifferent(row.key) }"
                >
                  {{ prop[row.key] || '—' }}
                </div>
              </div>
            </template>
          </div>
        </div>
      </section>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// --- Dados Mockados ---
// Em produção, isso viria de props ou store
const allProperties = [
  {
    id: "p1",
    name: "Cobertura Jardins",
    location: "Jardins, SP",
    price: "R$ 9.250.000",
    image: "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop",
    area: "420 m²",
    suites: "4 suítes",
    ceiling: "3,2 m",
    light: "Alta",
    security: "Portaria 24h, biometria",
    concierge: "Sim",
    schoolDistance: "8 min",
    walkability: "Alta",
    condoFee: "R$ 5.200",
    iptu: "R$ 1.800",
  },
  {
    id: "p2",
    name: "Residencial Dos Lagos",
    location: "Itaim Bibi, SP",
    price: "R$ 7.800.000",
    image: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=800&auto=format&fit=crop",
    area: "380 m²",
    suites: "4 suítes",
    ceiling: "2,8 m",
    light: "Média",
    security: "Portaria 24h",
    concierge: "Não",
    schoolDistance: "5 min",
    walkability: "Alta",
    condoFee: "R$ 4.000",
    iptu: "R$ 1.500",
  },
  {
    id: "p3",
    name: "Villa Toscana",
    location: "Vila Nova Conceição, SP",
    price: "R$ 6.950.000",
    image: "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=800&auto=format&fit=crop",
    area: "350 m²",
    suites: "3 suítes",
    ceiling: "3,0 m",
    light: "Alta",
    security: "Portaria 24h, ronda",
    concierge: "Sim",
    schoolDistance: "12 min",
    walkability: "Média",
    condoFee: "R$ 6.000",
    iptu: "R$ 2.100",
  }
]

const sections = [
  {
    id: "essence",
    title: "Essência",
    subtitle: "Fundamentos da propriedade.",
    rows: [
      { label: "Localização", key: "location" },
      { label: "Área privativa", key: "area" },
      { label: "Suítes", key: "suites" },
    ],
  },
  {
    id: "experience",
    title: "Experiência do espaço",
    subtitle: "Qualidade espacial, luz e sensação.",
    rows: [
      { label: "Pé-direito", key: "ceiling" },
      { label: "Iluminação natural", key: "light" },
    ],
  },
  {
    id: "amenities",
    title: "Comodidades & serviços",
    subtitle: "Serviços, segurança e facilidades.",
    rows: [
      { label: "Segurança", key: "security" },
      { label: "Concierge", key: "concierge" },
    ],
  },
  {
    id: "financial",
    title: "Visão financeira",
    subtitle: "Custos recorrentes estimados.",
    rows: [
      { label: "Condomínio", key: "condoFee" },
      { label: "IPTU (mensal)", key: "iptu" },
    ],
  },
]

// --- Estado ---
const selectedIds = ref(["p1", "p2", "p3"])
const showDifferencesOnly = ref(false)

// --- Computed ---
const selectedProperties = computed(() => {
  return allProperties.filter(p => selectedIds.value.includes(p.id))
})

// Calcula o grid dinamicamente baseado no número de colunas
const gridStyle = computed(() => {
  const count = selectedProperties.value.length
  return {
    gridTemplateColumns: `120px repeat(${count}, minmax(0, 1fr))`
  }
})

// --- Métodos ---

// Verifica se os valores de uma linha são diferentes entre os imóveis selecionados
const isRowDifferent = (key: string) => {
  if (selectedProperties.value.length < 2) return false
  const values = selectedProperties.value.map(p => (p as any)[key])
  const uniqueValues = new Set(values)
  return uniqueValues.size > 1
}

const backToListing = () => {
  // Emite evento ou navega de volta
  router.back()
}

const contactConcierge = () => {
  alert("Conectando com Concierge...")
}

const saveComparison = () => {
  alert("Comparação salva no perfil.")
}
</script>

<style scoped>
/* Ajustes finos se necessário, mas preferir Tailwind */
</style>