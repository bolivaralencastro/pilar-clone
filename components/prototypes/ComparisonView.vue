<template>
  <div class="w-full min-h-screen font-sans text-text-primary bg-surface-base flex justify-center p-4 pb-24">
    
    <div class="w-full max-w-[1120px]">
      <!-- Topbar -->
      <header class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 mb-12">
        <div class="flex items-center gap-4">
          <button @click="backToListing" class="flex items-center gap-2 text-xs uppercase tracking-widest text-text-secondary hover:text-text-primary transition-colors">
            <i class="lni lni-arrow-left"></i>
            Voltar
          </button>
          <div class="h-4 w-px bg-border-subtle"></div>
          <span class="text-xs uppercase tracking-widest text-text-tertiary">{{ selectedProperties.length }} imóveis em comparação</span>
        </div>
        <div class="w-10 h-10 rounded-full border border-border-subtle flex items-center justify-center text-xs font-serif italic text-text-primary">
          PH
        </div>
      </header>

      <!-- Hero Section -->
      <section class="bg-surface-card border border-border-subtle rounded-lg p-6 md:p-8 shadow-sm mb-6">
        <div class="mb-8">
          <h1 class="text-2xl md:text-3xl font-serif font-light tracking-tight text-text-primary mb-2">Comparação curada</h1>
          <p class="text-sm font-light text-text-secondary leading-relaxed max-w-2xl">
            Uma visão clara das diferenças que realmente importam entre os imóveis selecionados.
          </p>
        </div>
        
        <!-- Header Row (Imóveis) -->
        <div class="grid gap-4" :style="gridStyle">
          <div class="hidden md:block"></div> <!-- Canto vazio -->
          
          <div v-for="prop in selectedProperties" :key="prop.id" class="bg-surface-offset/50 rounded border border-border-subtle p-4 flex flex-col gap-2">
            <div class="font-serif text-lg leading-tight text-text-primary">{{ prop.name }}</div>
            <div class="text-[10px] uppercase tracking-widest text-text-tertiary">{{ prop.location }}</div>
            <div class="font-medium text-sm text-text-primary mt-1">{{ prop.price }}</div>
          </div>
        </div>
      </section>

      <!-- Toolbar -->
      <section class="flex flex-col md:flex-row justify-between items-center gap-4 mb-6">
        <div class="flex items-center gap-6">
          <label class="flex items-center gap-2 text-xs text-text-secondary cursor-pointer select-none hover:text-text-primary transition-colors">
            <input type="checkbox" v-model="showDifferencesOnly" class="accent-text-primary w-3 h-3" />
            Mostrar apenas diferenças
          </label>
          <span class="px-2 py-1 rounded-full border border-border-subtle text-[10px] uppercase tracking-widest text-text-tertiary bg-surface-card">
            Comparação privada
          </span>
        </div>
        <button class="text-xs uppercase tracking-widest text-text-secondary hover:text-text-primary transition-colors flex items-center gap-2" @click="showConciergeHint">
          <i class="lni lni-question-circle"></i>
          O que muda realmente?
        </button>
      </section>

      <!-- Seções de Comparação -->
      <section class="space-y-6">
        <div v-for="section in sections" :key="section.id" class="bg-surface-card border border-border-subtle rounded-lg p-6">
          <div class="mb-6 border-b border-border-subtle pb-4">
            <h3 class="text-sm font-medium text-text-primary uppercase tracking-widest mb-1">{{ section.title }}</h3>
            <p class="text-xs text-text-tertiary font-light">{{ section.subtitle }}</p>
          </div>

          <div class="flex flex-col gap-2">
            <template v-for="row in section.rows" :key="row.key">
              <!-- Renderiza apenas se não estiver filtrando diferenças OU se houver diferença -->
              <div 
                v-if="!showDifferencesOnly || isRowDifferent(row.key)" 
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

      <!-- Actions Footer -->
      <section class="mt-12 flex flex-col md:flex-row justify-between items-center gap-6">
        <div class="flex gap-4">
          <button class="bg-text-primary text-surface-base px-6 py-3 rounded text-xs uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors" @click="contactConcierge">
            Falar com um concierge
          </button>
          <button class="border border-border-strong px-6 py-3 rounded text-xs uppercase tracking-widest font-medium text-text-primary hover:bg-surface-subtle transition-colors" @click="saveComparison">
            Salvar comparação
          </button>
        </div>
        <div class="text-[10px] text-text-tertiary max-w-xs text-center md:text-right leading-relaxed">
          Esta visão é uma simulação. Na interface final, este fluxo conecta ao CRM e agenda visitas.
        </div>
      </section>
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
    gridTemplateColumns: `140px repeat(${count}, minmax(0, 1fr))`
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

const showConciergeHint = () => {
  alert("O Concierge explicaria aqui: 'A cobertura tem custo fixo 30% maior, mas oferece o dobro de área externa.'")
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