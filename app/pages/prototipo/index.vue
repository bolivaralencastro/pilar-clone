<script setup lang="ts">
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
    <TheBackgroundLogo />

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
            <span class="text-text-primary">Protótipo</span>
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
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <!-- Sidebar / Title -->
          <div class="lg:col-span-4">
            <div class="sticky top-32">
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 05</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Protótipo</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Navegue pelas funcionalidades implementadas no protótipo de alta fidelidade.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="grid grid-cols-1 gap-8">
              
              <!-- Home -->
              <div class="group block">
                <div class="bg-surface-card border rounded-lg border-subtle p-8 transition-all duration-500 hover:border-action-primary/30 hover:shadow-xl relative overflow-hidden">
                  <div class="absolute top-0 left-0 w-1 h-full bg-mat-stone transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500"></div>
                  
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Página 01</span>
                  <h3 class="text-2xl font-light mb-4 text-text-primary group-hover:translate-x-2 transition-transform duration-300">Home</h3>
                  <p class="text-secondary font-light leading-relaxed group-hover:text-text-primary transition-colors">
                    A nova porta de entrada da Pilar Homes. Foco em curadoria, storytelling e acesso rápido aos imóveis mais exclusivos.
                  </p>
                  
                  <div class="mt-8 flex items-center gap-6 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-2 group-hover:translate-y-0">
                    <a href="https://www.pilarhomes.com.br/" target="_blank" class="text-xs font-mono uppercase tracking-widest text-secondary hover:text-action-primary transition-colors flex items-center gap-2">
                      Versão Atual <i class="lni lni-arrow-right-circle"></i>
                    </a>
                    <NuxtLink to="/prototipo/home" class="text-xs font-mono uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors flex items-center gap-2">
                      Nova Versão <span class="text-lg">→</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>

              <!-- Resultados -->
              <div class="group block">
                <div class="bg-surface-card border rounded-lg border-subtle p-8 transition-all duration-500 hover:border-action-primary/30 hover:shadow-xl relative overflow-hidden">
                  <div class="absolute top-0 left-0 w-1 h-full bg-mat-stone transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500"></div>
                  
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Página 02</span>
                  <h3 class="text-2xl font-light mb-4 text-text-primary group-hover:translate-x-2 transition-transform duration-300">Resultados de Busca</h3>
                  <p class="text-secondary font-light leading-relaxed group-hover:text-text-primary transition-colors">
                    Experiência de busca refinada com filtros inteligentes, mapa interativo e cards que valorizam a fotografia.
                  </p>
                  
                  <div class="mt-8 flex items-center gap-6 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-2 group-hover:translate-y-0">
                    <a href="https://pilarhomes.com.br/venda/imoveis/sao-paulo-sp-brasil" target="_blank" class="text-xs font-mono uppercase tracking-widest text-secondary hover:text-action-primary transition-colors flex items-center gap-2">
                      Versão Atual <i class="lni lni-arrow-right-circle"></i>
                    </a>
                    <NuxtLink to="/prototipo/resultados" class="text-xs font-mono uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors flex items-center gap-2">
                      Nova Versão <span class="text-lg">→</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>

              <!-- Imóvel -->
              <div class="group block">
                <div class="bg-surface-card border rounded-lg border-subtle p-8 transition-all duration-500 hover:border-action-primary/30 hover:shadow-xl relative overflow-hidden">
                  <div class="absolute top-0 left-0 w-1 h-full bg-mat-stone transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500"></div>
                  
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Página 03</span>
                  <h3 class="text-2xl font-light mb-4 text-text-primary group-hover:translate-x-2 transition-transform duration-300">Detalhe do Imóvel</h3>
                  <p class="text-secondary font-light leading-relaxed group-hover:text-text-primary transition-colors">
                    Imersão total. Uma página desenhada para contar a história de cada propriedade com elegância e clareza técnica.
                  </p>
                  
                  <div class="mt-8 flex items-center gap-6 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-2 group-hover:translate-y-0">
                    <a href="https://pilarhomes.com.br/imovel/CA16821/cobertura-4-quartos-vila-romana-sao-paulo" target="_blank" class="text-xs font-mono uppercase tracking-widest text-secondary hover:text-action-primary transition-colors flex items-center gap-2">
                      Versão Atual <i class="lni lni-arrow-right-circle"></i>
                    </a>
                    <NuxtLink to="/prototipo/imovel" class="text-xs font-mono uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors flex items-center gap-2">
                      Nova Versão <span class="text-lg">→</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>

              <!-- Curadoria -->
              <div class="group block">
                <div class="bg-surface-card border rounded-lg border-subtle p-8 transition-all duration-500 hover:border-action-primary/30 hover:shadow-xl relative overflow-hidden">
                  <div class="absolute top-0 left-0 w-1 h-full bg-mat-stone transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500"></div>
                  
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Página 04</span>
                  <h3 class="text-2xl font-light mb-4 text-text-primary group-hover:translate-x-2 transition-transform duration-300">Curadoria</h3>
                  <p class="text-secondary font-light leading-relaxed group-hover:text-text-primary transition-colors">
                    Coleções exclusivas e seleções temáticas que elevam a percepção de valor do portfólio.
                  </p>
                  
                  <div class="mt-8 flex items-center gap-6 opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-2 group-hover:translate-y-0">
                    <a href="https://pilarhomes.com.br/venda/imoveis/sao-paulo-sp-brasil" target="_blank" class="text-xs font-mono uppercase tracking-widest text-secondary hover:text-action-primary transition-colors flex items-center gap-2">
                      Versão Atual <i class="lni lni-arrow-right-circle"></i>
                    </a>
                    <NuxtLink to="/prototipo/curadoria" class="text-xs font-mono uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors flex items-center gap-2">
                      Nova Versão <span class="text-lg">→</span>
                    </NuxtLink>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
