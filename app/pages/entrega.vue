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
            <span class="text-text-primary">Entrega</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 06</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Entrega</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Roadmap de desenvolvimento e próximos passos para evolução do produto.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              
              <!-- Deliverables -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Entregáveis do Projeto</h3>
                <div class="space-y-6">
                  <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-action-primary/10 flex items-center justify-center flex-shrink-0">
                      <i class="lni lni-files text-action-primary"></i>
                    </div>
                    <div>
                      <h4 class="font-medium text-text-primary mb-1">Documentação de Pesquisa</h4>
                      <p class="text-secondary font-light text-sm">Análise completa do site atual, benchmarking de concorrentes, estudo de personas e jornadas do usuário.</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-action-primary/10 flex items-center justify-center flex-shrink-0">
                      <i class="lni lni-bullhorn text-action-primary"></i>
                    </div>
                    <div>
                      <h4 class="font-medium text-text-primary mb-1">Estratégia de Produto</h4>
                      <p class="text-secondary font-light text-sm">Proposta de valor, estratégia de diferenciação e posicionamento premium da marca.</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-action-primary/10 flex items-center justify-center flex-shrink-0">
                      <i class="lni lni-grid-alt text-action-primary"></i>
                    </div>
                    <div>
                      <h4 class="font-medium text-text-primary mb-1">Sistema de Design</h4>
                      <p class="text-secondary font-light text-sm">Design system consolidado com paleta de cores, tipografia, componentes e padrões de UI.</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-action-primary/10 flex items-center justify-center flex-shrink-0">
                      <i class="lni lni-layers text-action-primary"></i>
                    </div>
                    <div>
                      <h4 class="font-medium text-text-primary mb-1">Protótipos de Alta Fidelidade</h4>
                      <p class="text-secondary font-light text-sm">4 páginas principais redesenhadas: Home, Resultados de Busca, Detalhe do Imóvel e Curadoria.</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-action-primary/10 flex items-center justify-center flex-shrink-0">
                      <i class="lni lni-code text-action-primary"></i>
                    </div>
                    <div>
                      <h4 class="font-medium text-text-primary mb-1">Implementação Técnica</h4>
                      <p class="text-secondary font-light text-sm">Protótipos funcionais desenvolvidos em Vue.js/Nuxt com design responsivo.</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Implementation Roadmap -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Roadmap de Implementação</h3>
                <p class="text-secondary font-light text-sm mb-8">Sugestão de faseamento para implementação dos designs propostos em ambiente de produção.</p>
                
                <div class="space-y-8 relative pl-8 border-l-2 border-subtle">
                  
                  <!-- Phase 1 -->
                  <div class="relative">
                    <span class="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-action-primary border-4 border-surface-card flex items-center justify-center">
                      <span class="text-white text-xs font-bold">1</span>
                    </span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-2 text-text-primary">Fase 1: Fundação</h4>
                    <p class="text-secondary font-light text-sm mb-3">Estabelecer as bases técnicas e de design</p>
                    <ul class="space-y-2 text-sm text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Implementar design system e componentes base</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Configurar nova estrutura de dados para curadoria</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Preparar API para novos recursos (comparação, IA)</span>
                      </li>
                    </ul>
                  </div>
                  
                  <!-- Phase 2 -->
                  <div class="relative">
                    <span class="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-mat-stone border-4 border-surface-card flex items-center justify-center">
                      <span class="text-white text-xs font-bold">2</span>
                    </span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-2 text-text-primary">Fase 2: Home e Navegação</h4>
                    <p class="text-secondary font-light text-sm mb-3">Implementar nova experiência inicial</p>
                    <ul class="space-y-2 text-sm text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Lançar nova home com hero imersivo e navegação simplificada</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Implementar carrosséis de curadoria por região</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Realizar testes A/B para validar melhorias</span>
                      </li>
                    </ul>
                  </div>
                  
                  <!-- Phase 3 -->
                  <div class="relative">
                    <span class="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-surface-subtle border-4 border-surface-card flex items-center justify-center">
                      <span class="text-text-primary text-xs font-bold">3</span>
                    </span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-2 text-secondary">Fase 3: Busca e Comparação</h4>
                    <p class="text-secondary font-light text-sm mb-3">Otimizar experiência de busca</p>
                    <ul class="space-y-2 text-sm text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Implementar nova página de resultados com filtros otimizados</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Integrar visualização em mapa sincronizada</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Lançar sistema de comparação com barra flutuante</span>
                      </li>
                    </ul>
                  </div>
                  
                  <!-- Phase 4 -->
                  <div class="relative">
                    <span class="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-surface-subtle border-4 border-surface-card flex items-center justify-center">
                      <span class="text-text-primary text-xs font-bold">4</span>
                    </span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-2 text-secondary">Fase 4: Detalhe e IA</h4>
                    <p class="text-secondary font-light text-sm mb-3">Enriquecer página de detalhes</p>
                    <ul class="space-y-2 text-sm text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Implementar galeria imersiva e hierarquia de informações</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Integrar análise de valor por IA</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Otimizar CTAs e fluxo de conversão</span>
                      </li>
                    </ul>
                  </div>
                  
                  <!-- Phase 5 -->
                  <div class="relative">
                    <span class="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-surface-subtle border-4 border-surface-card flex items-center justify-center">
                      <span class="text-text-primary text-xs font-bold">5</span>
                    </span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-2 text-secondary">Fase 5: Experiência Premium</h4>
                    <p class="text-secondary font-light text-sm mb-3">Consolidar posicionamento de marca</p>
                    <ul class="space-y-2 text-sm text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Lançar páginas de curadoria com experiência editorial</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Expandir coleções temáticas e exclusivas</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Medir impacto e iterar com base em dados</span>
                      </li>
                    </ul>
                  </div>
                  
                </div>
              </div>

              <!-- Next Steps -->
              <div class="bg-action-primary/5 border border-action-primary/20 rounded-lg p-8">
                <h3 class="text-xl font-light mb-4 text-text-primary">Próximos Passos</h3>
                <ul class="space-y-3 text-sm text-secondary font-light">
                  <li class="flex items-start gap-3">
                    <i class="lni lni-checkmark-circle text-action-primary mt-0.5"></i>
                    <span>Validar protótipos com testes de usabilidade</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <i class="lni lni-checkmark-circle text-action-primary mt-0.5"></i>
                    <span>Refinar design system com feedback da equipe de desenvolvimento</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <i class="lni lni-checkmark-circle text-action-primary mt-0.5"></i>
                    <span>Documentar especificações técnicas para implementação</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <i class="lni lni-checkmark-circle text-action-primary mt-0.5"></i>
                    <span>Estabelecer métricas de sucesso e KPIs para acompanhamento</span>
                  </li>
                </ul>
              </div>

            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>




