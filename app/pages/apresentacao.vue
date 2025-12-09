<script setup lang="ts">
definePageMeta({
  layout: 'presentation'
})

const slides = [
  {
    id: 1,
    title: 'Descoberta',
    subtitle: 'Fase de Pesquisa',
    content: [
      'Análise de HAR files para entender a API existente',
      'OSINT consolidado sobre stack técnica e arquitetura',
      'Mapeamento de jornadas de usuário',
      'Extração do design system (cores, tipografia, componentes)'
    ],
    phase: 'discover'
  },
  {
    id: 2,
    title: 'Definição',
    subtitle: 'Síntese dos Insights',
    content: [
      'Problema identificado: usuários comparam imóveis em abas separadas',
      'Oportunidade: funcionalidade nativa de comparação',
      'Requisitos: máximo 4 imóveis, lado a lado, fácil remoção',
      'Critérios de sucesso: reduzir fricção na decisão de compra'
    ],
    phase: 'define'
  },
  {
    id: 3,
    title: 'Desenvolvimento',
    subtitle: 'Prototipação',
    content: [
      'Store Pinia para estado de comparação',
      'Componente PropertyCard com botão de adicionar',
      'Página /compare com grid responsivo',
      'Integração com API existente da Pilar'
    ],
    phase: 'develop'
  },
  {
    id: 4,
    title: 'Entrega',
    subtitle: 'Validação',
    content: [
      'Protótipo funcional em Nuxt 4',
      'Código limpo e tipado com TypeScript',
      'Documentação do processo Double Diamond',
      'Pronto para testes com usuários reais'
    ],
    phase: 'deliver'
  }
]

const currentSlide = ref(0)

const nextSlide = () => {
  if (currentSlide.value < slides.length - 1) {
    currentSlide.value++
  }
}

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--
  }
}

const goToSlide = (index: number) => {
  currentSlide.value = index
}
</script>

<template>
  <div class="min-h-screen bg-off-white text-rich-black selection:bg-brand-orange selection:text-white relative">
    <!-- Background SVG -->
    <TheBackgroundLogo />

    <!-- Header -->
    <header class="bg-off-white border-b border-chromium relative z-10">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-chromium"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase mt-[6px]">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Apresentação</span>
          </nav>
        </div>
        
        <div class="flex items-center gap-4 mt-[6px]">
          <!-- Previous Arrow -->
          <button 
            :disabled="currentSlide === 0"
            :class="[
              'text-2xl transition-all duration-300',
              currentSlide === 0 
                ? 'text-platinum cursor-not-allowed' 
                : 'text-secondary hover:text-text-primary'
            ]"
            @click="prevSlide"
          >
            ←
          </button>

          <span class="text-xs font-mono text-secondary tracking-widest">
            {{ String(currentSlide + 1).padStart(2, '0') }} / {{ String(slides.length).padStart(2, '0') }}
          </span>

          <!-- Next Arrow -->
          <button 
            :disabled="currentSlide === slides.length - 1"
            :class="[
              'text-2xl transition-all duration-300',
              currentSlide === slides.length - 1 
                ? 'text-platinum cursor-not-allowed' 
                : 'text-secondary hover:text-text-primary'
            ]"
            @click="nextSlide"
          >
            →
          </button>
        </div>
      </div>
    </header>

    <!-- Main Slide -->
    <main class="py-16 min-h-screen flex items-center relative overflow-hidden">
      <!-- Background Element -->
      <div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-chromium/30 to-transparent pointer-events-none"></div>
      
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 w-full relative z-10">
        <template v-for="(slide, index) in slides" :key="slide.id">
          <div 
            v-if="currentSlide === index"
            class="slide-content grid grid-cols-1 lg:grid-cols-12 gap-12 items-center"
          >
            <!-- Left Column: Title -->
            <div class="lg:col-span-5">
              <span class="text-[10px] uppercase tracking-[0.2em] text-secondary mb-4 block">
                {{ slide.subtitle }}
              </span>
              <h1 class="text-6xl md:text-8xl font-light tracking-tighter text-text-primary leading-[0.9]">
                {{ slide.title }}
              </h1>
            </div>

            <!-- Right Column: Content -->
            <div class="lg:col-span-6 lg:col-start-7">
              <ul class="space-y-8">
                <li 
                  v-for="(point, i) in slide.content" 
                  :key="i"
                  class="flex items-start gap-6 group"
                >
                  <span class="text-secondary font-mono text-sm mt-1 group-hover:text-text-primary transition-colors">0{{ i + 1 }}</span>
                  <p class="text-xl md:text-2xl font-light text-secondary leading-relaxed group-hover:text-text-primary transition-colors duration-300">
                    {{ point }}
                  </p>
                </li>
              </ul>
            </div>
          </div>
        </template>
      </div>
    </main>
  </div>
</template>

<style scoped>
.slide-content {
  animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
