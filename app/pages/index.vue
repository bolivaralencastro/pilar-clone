<script setup lang="ts">
useSeoMeta({
  title: 'Pilar Homes - Desafio Técnico',
  description: 'Dashboard do desafio técnico Pilar Homes'
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

    <!-- Header Minimal -->
    <header class="bg-white border-b border-subtle relative z-50">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          <span class="text-xs font-mono text-secondary tracking-widest uppercase border-l border-subtle pl-4 mt-[6px]">por Bolívar Alencastro</span>
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
        
        <!-- Hero Section -->
        <div class="mb-16 pb-16">
          <span class="text-action-primary font-mono text-xs tracking-[0.3em] uppercase mb-6 block">Documentation & Process</span>
          <h1 class="text-6xl md:text-8xl font-light tracking-tighter mb-8 leading-[0.9]">
            Redesign <br/>
            <span class="text-secondary">&</span> Experience
          </h1>
          <div class="flex flex-col md:flex-row md:items-end justify-between gap-8">
            <p class="text-secondary font-light text-lg max-w-xl leading-relaxed">
              Uma jornada completa de design e engenharia para elevar a experiência digital da Pilar Homes. Do discovery à entrega final.
            </p>
          </div>
        </div>

        <!-- Navigation Grid (The Index) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-subtle border border-subtle rounded-lg overflow-hidden">
          
          <!-- Column 1: Context -->
          <div class="bg-white p-12 group hover:bg-surface-card transition-colors duration-500">
            <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-8 block">01. Contexto</span>
            <div class="space-y-8">
              <NuxtLink to="/briefing" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Briefing <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Entendimento do desafio e requisitos.</p>
              </NuxtLink>
              <NuxtLink to="/programacao" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Planejamento <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Cronograma e organização pessoal.</p>
              </NuxtLink>
            </div>
          </div>

          <!-- Column 2: Process -->
          <div class="bg-white p-12 group hover:bg-surface-card transition-colors duration-500">
            <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-8 block">02. Processo</span>
            <div class="space-y-8">
              <NuxtLink to="/pesquisa" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Discovery <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Pesquisa, personas e benchmarking.</p>
              </NuxtLink>
              <NuxtLink to="/estrategia" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Estratégia <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Definição de direção e objetivos.</p>
              </NuxtLink>
              <NuxtLink to="/ideacao" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Ideação <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Fluxos, wireframes e arquitetura.</p>
              </NuxtLink>
            </div>
          </div>

          <!-- Column 3: Output -->
          <div class="bg-white p-12 group hover:bg-surface-card transition-colors duration-500">
            <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-8 block">03. Entrega</span>
            <div class="space-y-8">
              <NuxtLink to="/ui-design" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">UI Design <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Design System e tokens visuais.</p>
              </NuxtLink>
              <NuxtLink to="/prototipo" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Protótipo <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Acesso às funcionalidades finais.</p>
              </NuxtLink>
              <NuxtLink to="/entrega" class="block group/item">
                <h3 class="text-2xl font-light mb-2 text-text-primary group-hover/item:text-action-primary transition-colors duration-300">Roadmap <span class="inline-block group-hover/item:translate-x-1 transition-transform duration-300">→</span></h3>
                <p class="text-sm text-secondary font-light">Próximos passos e evolução.</p>
              </NuxtLink>
            </div>
          </div>

        </div>

      </div>
    </main>
  </div>
</template>


