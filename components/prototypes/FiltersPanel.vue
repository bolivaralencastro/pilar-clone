<template>
  <!-- FILTERS PANEL (Painel Flutuante) -->
  <Teleport to="body">
    <Transition name="fade">
      <div 
        v-if="modelValue" 
        class="fixed inset-0 z-50 flex items-stretch justify-end p-4"
      >
        <!-- Backdrop -->
        <div 
          class="absolute inset-0 bg-text-primary/40 backdrop-blur-sm"
          @click="close"
        ></div>
        
        <!-- Panel -->
        <div class="relative w-full max-w-md bg-surface-base rounded-lg shadow-2xl overflow-hidden flex flex-col animate-slide-in-right">
          
          <!-- Header do Painel -->
          <div class="flex items-center justify-between px-6 py-5 border-b border-border-subtle">
            <h2 class="text-lg font-light tracking-tight text-text-primary">Filtros</h2>
            <button 
              @click="close"
              class="w-8 h-8 flex items-center justify-center text-text-tertiary hover:text-text-primary transition-colors"
            >
              <i class="lni lni-close text-lg"></i>
            </button>
          </div>

          <!-- Conteúdo Scrollável -->
          <div class="flex-1 overflow-y-auto px-6 py-6 space-y-8">
            
            <!-- BAIRROS -->
            <div class="space-y-4">
              <button 
                @click="toggleSection('bairros')"
                class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
              >
                <span>Bairros</span>
                <i 
                  :class="openSections.includes('bairros') ? 'lni-chevron-up' : 'lni-chevron-down'"
                  class="lni text-xs text-text-tertiary transition-transform"
                ></i>
              </button>
              
              <div v-if="openSections.includes('bairros')" class="space-y-3">
                <label 
                  v-for="bairro in ['Jardins', 'Itaim Bibi', 'Vila Nova Conceição', 'Moema', 'Pinheiros', 'Higienópolis']"
                  :key="bairro"
                  class="flex items-center gap-3 cursor-pointer group"
                >
                  <input 
                    type="checkbox" 
                    class="w-4 h-4 rounded border-border-strong text-text-primary focus:ring-2 focus:ring-text-primary/20"
                  />
                  <span class="text-sm text-text-secondary group-hover:text-text-primary transition-colors">
                    {{ bairro }}
                  </span>
                </label>
              </div>
            </div>

            <!-- ÁREA ÚTIL -->
            <div class="space-y-4">
              <button 
                @click="toggleSection('area')"
                class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
              >
                <span>Área Útil (m²)</span>
                <i 
                  :class="openSections.includes('area') ? 'lni-chevron-up' : 'lni-chevron-down'"
                  class="lni text-xs text-text-tertiary transition-transform"
                ></i>
              </button>
              
              <div v-if="openSections.includes('area')" class="flex gap-3">
                <input 
                  type="number" 
                  placeholder="Mín"
                  class="flex-1 px-3 py-2 text-sm border border-border-subtle rounded bg-surface-base text-text-primary focus:outline-none focus:border-text-primary transition-colors"
                />
                <input 
                  type="number" 
                  placeholder="Máx"
                  class="flex-1 px-3 py-2 text-sm border border-border-subtle rounded bg-surface-base text-text-primary focus:outline-none focus:border-text-primary transition-colors"
                />
              </div>
            </div>

            <!-- VALOR DE VENDA -->
            <div class="space-y-4">
              <button 
                @click="toggleSection('valor')"
                class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
              >
                <span>Valor de Venda</span>
                <i 
                  :class="openSections.includes('valor') ? 'lni-chevron-up' : 'lni-chevron-down'"
                  class="lni text-xs text-text-tertiary transition-transform"
                ></i>
              </button>
              
              <div v-if="openSections.includes('valor')" class="flex gap-3">
                <input 
                  type="text" 
                  placeholder="R$ Mín"
                  class="flex-1 px-3 py-2 text-sm border border-border-subtle rounded bg-surface-base text-text-primary focus:outline-none focus:border-text-primary transition-colors"
                />
                <input 
                  type="text" 
                  placeholder="R$ Máx"
                  class="flex-1 px-3 py-2 text-sm border border-border-subtle rounded bg-surface-base text-text-primary focus:outline-none focus:border-text-primary transition-colors"
                />
              </div>
            </div>

            <!-- TIPO DE IMÓVEL -->
            <div class="space-y-4">
              <button 
                @click="toggleSection('tipo')"
                class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
              >
                <span>Tipo de Imóvel</span>
                <i 
                  :class="openSections.includes('tipo') ? 'lni-chevron-up' : 'lni-chevron-down'"
                  class="lni text-xs text-text-tertiary transition-transform"
                ></i>
              </button>
              
              <div v-if="openSections.includes('tipo')" class="space-y-3">
                <label 
                  v-for="tipo in ['Apartamento', 'Cobertura', 'Casa', 'Loft', 'Terreno']"
                  :key="tipo"
                  class="flex items-center gap-3 cursor-pointer group"
                >
                  <input 
                    type="checkbox" 
                    class="w-4 h-4 rounded border-border-strong text-text-primary focus:ring-2 focus:ring-text-primary/20"
                  />
                  <span class="text-sm text-text-secondary group-hover:text-text-primary transition-colors">
                    {{ tipo }}
                  </span>
                </label>
              </div>
            </div>

            <!-- CÔMODOS -->
            <div class="space-y-4">
              <button 
                @click="toggleSection('comodos')"
                class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
              >
                <span>Cômodos</span>
                <i 
                  :class="openSections.includes('comodos') ? 'lni-chevron-up' : 'lni-chevron-down'"
                  class="lni text-xs text-text-tertiary transition-transform"
                ></i>
              </button>
              
              <div v-if="openSections.includes('comodos')" class="space-y-5">
                <!-- Quartos -->
                <div>
                  <p class="text-xs uppercase tracking-widest text-text-tertiary mb-2">Quartos</p>
                  <div class="flex gap-2">
                    <button 
                      v-for="n in [1, 2, 3, 4, 5]"
                      :key="'quarto-' + n"
                      class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors text-text-secondary"
                    >
                      {{ n }}+
                    </button>
                  </div>
                </div>

                <!-- Suítes -->
                <div>
                  <p class="text-xs uppercase tracking-widest text-text-tertiary mb-2">Suítes</p>
                  <div class="flex gap-2">
                    <button 
                      v-for="n in [1, 2, 3, 4, 5]"
                      :key="'suite-' + n"
                      class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors text-text-secondary"
                    >
                      {{ n }}+
                    </button>
                  </div>
                </div>

                <!-- Vagas -->
                <div>
                  <p class="text-xs uppercase tracking-widest text-text-tertiary mb-2">Vagas</p>
                  <div class="flex gap-2">
                    <button 
                      v-for="n in [1, 2, 3, 4, 5]"
                      :key="'vaga-' + n"
                      class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors text-text-secondary"
                    >
                      {{ n }}+
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- MAIS FILTROS -->
            <div class="space-y-4">
              <button 
                @click="toggleSection('mais')"
                class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
              >
                <span>Mais Filtros</span>
                <i 
                  :class="openSections.includes('mais') ? 'lni-chevron-up' : 'lni-chevron-down'"
                  class="lni text-xs text-text-tertiary transition-transform"
                ></i>
              </button>
              
              <div v-if="openSections.includes('mais')" class="space-y-3">
                <label 
                  v-for="filtro in [
                    'Aceita Permuta',
                    'Condomínio Fechado',
                    'Varanda/Sacada',
                    'Área de Lazer',
                    'Piscina',
                    'Academia',
                    'Portaria 24h',
                    'Mobiliado'
                  ]"
                  :key="filtro"
                  class="flex items-center gap-3 cursor-pointer group"
                >
                  <input 
                    type="checkbox" 
                    class="w-4 h-4 rounded border-border-strong text-text-primary focus:ring-2 focus:ring-text-primary/20"
                  />
                  <span class="text-sm text-text-secondary group-hover:text-text-primary transition-colors">
                    {{ filtro }}
                  </span>
                </label>
              </div>
            </div>

          </div>

          <!-- Footer do Painel -->
          <div class="px-6 py-5 border-t border-border-subtle bg-surface-base flex items-center justify-between gap-4">
            <button 
              @click="clearFilters"
              class="text-xs uppercase tracking-widest text-text-tertiary hover:text-text-primary transition-colors underline underline-offset-4"
            >
              Limpar Tudo
            </button>
            <button 
              @click="applyFilters"
              class="flex-1 bg-text-primary text-surface-base py-3 text-xs uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors rounded"
            >
              Filtrar
            </button>
          </div>

        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Props
const props = defineProps<{
  modelValue: boolean
}>()

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: boolean]
  'apply': []
  'clear': []
}>()

// State
const openSections = ref<string[]>(['bairros'])

// Methods
const close = () => {
  emit('update:modelValue', false)
}

const toggleSection = (section: string) => {
  if (openSections.value.includes(section)) {
    openSections.value = openSections.value.filter(s => s !== section)
  } else {
    openSections.value.push(section)
  }
}

const applyFilters = () => {
  emit('apply')
  close()
}

const clearFilters = () => {
  emit('clear')
}
</script>

<style scoped>
/* Animação do painel de filtros */
.animate-slide-in-right {
  animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Transição fade para backdrop */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active .animate-slide-in-right {
  animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-leave-active .animate-slide-in-right {
  animation: slideOutRight 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes slideOutRight {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%);
    opacity: 0;
  }
}
</style>
