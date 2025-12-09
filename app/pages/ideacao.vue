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
            <span class="text-text-primary">Ideação</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 03</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Ideação</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Exploração de soluções, fluxos de navegação e definição das funcionalidades chave com base na análise de oportunidades identificadas na fase de discovery.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Funcionalidades Chave</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Core Feature</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Comparador Lado a Lado</h4>
                    <p class="text-secondary font-light text-sm">Visualização simultânea de até 4 imóveis com destaque para diferenças, permitindo tomada de decisão mais informada.</p>
                  </div>
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Discovery</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Filtros Inteligentes</h4>
                    <p class="text-secondary font-light text-sm">Sistema de filtragem avançado com busca contextual sem recarregamento de página para experiência fluida.</p>
                  </div>
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">UX Enhancement</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Barra de Comparação Flutuante</h4>
                    <p class="text-secondary font-light text-sm">Componente persistente que permite adicionar imóveis à comparação de qualquer página, com visualização em tempo real.</p>
                  </div>
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">AI Integration</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Análise de Valor por IA</h4>
                    <p class="text-secondary font-light text-sm">Ferramenta de análise automatizada que fornece insights sobre o valor do imóvel com base em dados de mercado.</p>
                  </div>
                </div>
              </div>

              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Fluxos e Wireframes</h3>
                <p class="text-secondary font-light leading-relaxed mb-6">
                  O fluxo foi desenhado para ser linear mas flexível, permitindo que o usuário entre no funil de comparação a partir de qualquer ponto da listagem, com persistência do estado de comparação entre diferentes páginas.
                </p>
                
                <div class="space-y-6">
                  <div>
                    <h4 class="text-lg font-medium mb-3 text-text-primary">Fluxo Principal</h4>
                    <ul class="space-y-2 text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Início em qualquer página de listagem ou detalhe de imóvel</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Selecão de imóveis para comparação via checkbox ou botão</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Barra flutuante mostra itens selecionados e ativa modo comparação</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Navegação contínua mantendo o estado da comparação</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Visualização side-by-side quando dois ou mais imóveis são selecionados</span>
                      </li>
                    </ul>
                  </div>
                  
                  <div>
                    <h4 class="text-lg font-medium mb-3 text-text-primary">Fluxos Alternativos</h4>
                    <ul class="space-y-2 text-secondary font-light">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Recomendação de imóveis similares com base na comparação</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Análise de valor por IA em páginas de imóvel individual</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span>Compartilhamento de seleções de comparação</span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>

              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Estratégia de Implementação</h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Fase 1</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Core Features</h4>
                    <p class="text-secondary font-light text-sm">Implementação do comparador básico e da barra flutuante com persistência de estado.</p>
                  </div>
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Fase 2</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">AI Enhancement</h4>
                    <p class="text-secondary font-light text-sm">Integração da análise de valor por IA e recomendações inteligentes.</p>
                  </div>
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Fase 3</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">User Experience</h4>
                    <p class="text-secondary font-light text-sm">Refinamento da experiência com base em testes de usabilidade e feedback.</p>
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




