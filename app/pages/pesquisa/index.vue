<script setup lang="ts">
import NavCard from '../../../components/NavCard.vue'

useSeoMeta({
  title: 'Discovery & Pesquisa - Pilar Homes',
  description: 'Hub de pesquisa e descoberta do projeto.'
})

const showMenu = ref(false)

const navigationLinks = [
  { title: 'Briefing', path: '/briefing' },
  { title: 'Planejamento', path: '/programacao' },
  { title: 'Discovery', path: '/pesquisa' },
  { title: 'Estratégia', path: '/estrategia' },
  { title: 'Ideação', path: '/ideacao' },
  { title: 'UI Design', path: '/ui-design' },
  { title: 'Protótipo', path: '/prototipo' },
  { title: 'Roadmap', path: '/entrega' }
]

const toggleMenu = () => {
  showMenu.value = !showMenu.value
}

const handleNavigation = () => {
  showMenu.value = false
}
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Background SVG -->
    <div class="fixed bottom-0 left-0 opacity-[0.02] pointer-events-none z-0 scale-[3] origin-bottom-left">
      <svg width="380" height="328" viewBox="0 0 380 328" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M95 0L0 163.917L95 327.834H285L380 163.917L285 0H95ZM252.274 307.033L34.4494 181.755L283.277 38.6387L252.274 307.033Z" fill="black"/>
      </svg>
    </div>

    <!-- Header -->
    <header class="bg-white border-b border-subtle relative z-50">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase mt-[6px]">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Discovery</span>
          </nav>
        </div>
        <!-- Menu Button with Dropdown -->
        <div class="relative">
          <button 
            @click="toggleMenu"
            class="flex items-center gap-2 text-xs font-mono text-action-primary tracking-widest uppercase mt-[6px] hover:text-text-primary transition-colors cursor-pointer"
          >
            <i class="lni lni-menu text-base"></i>
            <span>Menu</span>
          </button>
          
          <!-- Dropdown Menu -->
          <div 
            v-if="showMenu"
            class="absolute right-0 mt-3 w-56 bg-white border border-subtle rounded-lg shadow-xl z-[9999]"
          >
            <nav class="py-2">
              <NuxtLink
                v-for="link in navigationLinks"
                :key="link.path"
                :to="link.path"
                class="block px-4 py-2.5 text-sm font-light text-text-primary hover:bg-surface-subtle transition-colors cursor-pointer"
                @click="handleNavigation"
              >
                {{ link.title }}
              </NuxtLink>
            </nav>
          </div>
        </div>
      </div>
    </header>

    <main class="py-16 relative z-0">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <!-- Intro -->
        <div class="mb-20 border-b border-subtle pb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 01</span>
          <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Discovery</h1>
          <p class="text-secondary text-xl font-light leading-relaxed max-w-3xl">
            Uma imersão profunda no ecossistema da Pilar Homes. Estruturamos nossa pesquisa em três pilares fundamentais para garantir que a solução final seja viável, desejável e tecnicamente robusta.
          </p>
        </div>

        <!-- Clusters Grid -->
        <div class="grid grid-cols-1 gap-16">
          
          <!-- Cluster 1: Contexto & Negócio -->
          <section class="grid grid-cols-1 lg:grid-cols-12 gap-8 group">
            <div class="lg:col-span-4">
              <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Cluster 01</span>
              <h2 class="text-3xl font-light text-text-primary mb-4">Contexto & Negócio</h2>
              <p class="text-secondary font-light leading-relaxed mb-6">
                Entendimento da marca Pilar Homes, análise de mercado e alinhamento estratégico dos objetivos do negócio.
              </p>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-4">
              <NavCard to="/pesquisa/pilar">
                <h3 class="text-lg font-medium text-text-primary mb-2">Sobre a Pilar</h3>
                <p class="text-sm text-secondary font-light">História, valores e posicionamento de marca.</p>
              </NavCard>
              <NavCard to="/pesquisa/mercado">
                <h3 class="text-lg font-medium text-text-primary mb-2">Mercado</h3>
                <p class="text-sm text-secondary font-light">Tendências do setor imobiliário de alto padrão.</p>
              </NavCard>
            </div>
          </section>

          <div class="w-full h-px bg-primary/5"></div>

          <!-- Cluster 2: Usuário & Experiência -->
          <section class="grid grid-cols-1 lg:grid-cols-12 gap-8 group">
            <div class="lg:col-span-4">
              <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Cluster 02</span>
              <h2 class="text-3xl font-light text-text-primary mb-4">Usuário & Experiência</h2>
              <p class="text-secondary font-light leading-relaxed mb-6">
                Mapeamento das necessidades, dores e jornadas dos clientes para criar uma experiência centrada no usuário.
              </p>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-4">
              <NavCard to="/pesquisa/personas">
                <h3 class="text-lg font-medium text-text-primary mb-2">Personas</h3>
                <p class="text-sm text-secondary font-light">Arquétipos dos clientes ideais.</p>
              </NavCard>
              <NavCard to="/pesquisa/jornadas">
                <h3 class="text-lg font-medium text-text-primary mb-2">Jornadas</h3>
                <p class="text-sm text-secondary font-light">Mapeamento do fluxo atual vs. ideal.</p>
              </NavCard>
            </div>
          </section>

          <div class="w-full h-px bg-primary/5"></div>

          <!-- Cluster 3: Design & Referências -->
          <section class="grid grid-cols-1 lg:grid-cols-12 gap-8 group">
            <div class="lg:col-span-4">
              <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Cluster 03</span>
              <h2 class="text-3xl font-light text-text-primary mb-4">Design & Referências</h2>
              <p class="text-secondary font-light leading-relaxed mb-6">
                Análise visual competitiva e busca por padrões de interface que transmitam luxo e sofisticação.
              </p>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-4">
              <NavCard to="/pesquisa/benchmarking">
                <h3 class="text-lg font-medium text-text-primary mb-2">Benchmarking</h3>
                <p class="text-sm text-secondary font-light">Análise de concorrentes diretos e indiretos.</p>
              </NavCard>
              <NavCard to="/pesquisa/ui-patterns">
                <h3 class="text-lg font-medium text-text-primary mb-2">UI Patterns</h3>
                <p class="text-sm text-secondary font-light">Estudos de componentes e interações.</p>
              </NavCard>
            </div>
          </section>

        </div>
      </div>
    </main>
  </div>
</template>



