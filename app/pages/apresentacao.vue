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
  <div class="min-h-screen bg-deep-brown text-off-white selection:bg-soft-beige selection:text-deep-brown">
    <!-- Header -->
    <header class="bg-deep-brown border-b border-off-white/10">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto invert" />
          </NuxtLink>
          <div class="h-4 w-px bg-off-white/20"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-off-white/60 hover:text-off-white transition-colors">Home</NuxtLink>
            <span class="text-off-white/20">/</span>
            <span class="text-off-white">Apresentação</span>
          </nav>
        </div>
        <span class="text-xs font-mono text-off-white/60 tracking-widest">
          {{ String(currentSlide + 1).padStart(2, '0') }} / {{ String(slides.length).padStart(2, '0') }}
        </span>
      </div>
    </header>

    <!-- Main Slide -->
    <main class="py-16 min-h-screen flex items-center relative overflow-hidden">
      <!-- Background Element -->
      <div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-off-white/5 to-transparent pointer-events-none"></div>
      
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 w-full relative z-10">
        <template v-for="(slide, index) in slides" :key="slide.id">
          <div 
            v-if="currentSlide === index"
            class="slide-content grid grid-cols-1 lg:grid-cols-12 gap-12 items-center"
          >
            <!-- Left Column: Title -->
            <div class="lg:col-span-5 space-y-6">
              <div class="inline-block px-3 py-1 border border-action-primary/30 rounded-full text-[10px] uppercase tracking-[0.2em] text-action-primary mb-4">
                {{ slide.subtitle }}
              </div>
              <h1 class="text-6xl md:text-8xl font-light tracking-tighter text-off-white leading-[0.9]">
                {{ slide.title }}
              </h1>
              <div class="w-24 h-1 bg-action-primary mt-8"></div>
            </div>

            <!-- Right Column: Content -->
            <div class="lg:col-span-6 lg:col-start-7">
              <ul class="space-y-8">
                <li 
                  v-for="(point, i) in slide.content" 
                  :key="i"
                  class="flex items-start gap-6 group"
                >
                  <span class="text-action-primary font-mono text-sm mt-1 opacity-50 group-hover:opacity-100 transition-opacity">0{{ i + 1 }}</span>
                  <p class="text-xl md:text-2xl font-light text-off-white/80 leading-relaxed group-hover:text-off-white transition-colors duration-300">
                    {{ point }}
                  </p>
                </li>
              </ul>
            </div>
          </div>
        </template>
      </div>
    </main>

    <!-- Navigation -->
    <nav class="fixed bottom-0 left-0 right-0 bg-deep-brown/80 backdrop-blur-md border-t border-off-white/10">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 py-8">
        <div class="flex items-center justify-between">
          <!-- Progress Dots -->
          <div class="flex gap-3">
            <button 
              v-for="(slide, index) in slides" 
              :key="slide.id"
              :class="[
                'h-1 transition-all duration-500 rounded-full',
                currentSlide === index 
                  ? 'w-12 bg-action-primary' 
                  : 'w-2 bg-off-white/20 hover:bg-off-white/40'
              ]"
              @click="goToSlide(index)"
            />
          </div>

          <!-- Arrows -->
          <div class="flex gap-4">
            <button 
              :disabled="currentSlide === 0"
              :class="[
                'w-12 h-12 rounded-full border flex items-center justify-center transition-all duration-300',
                currentSlide === 0 
                  ? 'border-off-white/10 text-off-white/10 cursor-not-allowed' 
                  : 'border-off-white/20 text-off-white hover:border-action-primary hover:text-action-primary'
              ]"
              @click="prevSlide"
            >
              ←
            </button>
            <button 
              :disabled="currentSlide === slides.length - 1"
              :class="[
                'w-12 h-12 rounded-full border flex items-center justify-center transition-all duration-300',
                currentSlide === slides.length - 1 
                  ? 'border-off-white/10 text-off-white/10 cursor-not-allowed' 
                  : 'border-off-white/20 text-off-white hover:border-action-primary hover:text-action-primary'
              ]"
              @click="nextSlide"
            >
              →
            </button>
          </div>
        </div>
      </div>
    </nav>
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
