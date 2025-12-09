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
            <span class="text-text-primary">Briefing</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Documentação</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Briefing do Desafio</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Visão geral e requisitos do projeto de redesign e implementação de novas funcionalidades.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              
              <!-- Objetivo -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-4 text-text-primary">Objetivo</h3>
                <p class="text-secondary font-light leading-relaxed">
                  Projetar um fluxo intuitivo e eficiente para comparação de imóveis (seleção + exibição comparativa) em formato mobile, tablet ou desktop.
                </p>
              </div>

              <!-- Checklist: Seleção -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Checklist</span>
                <h3 class="text-2xl font-light mb-6 text-text-primary">Seleção de Imóveis</h3>
                
                <ul class="space-y-3">
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Permitir seleção de até 4 imóveis (via busca, detalhes ou favoritos).</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Exibir contador/indicador visual de itens selecionados.</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Mostrar aviso ao tentar selecionar mais de 5 imóveis.</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Facilitar a remoção de imóveis da seleção.</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Feedback visual claro e microinterações fluidas.</span>
                  </li>
                </ul>
              </div>

              <!-- Checklist: Comparação -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Checklist</span>
                <h3 class="text-2xl font-light mb-6 text-text-primary">Tela de Comparação</h3>
                
                <ul class="space-y-3">
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Exibição lado a lado para fácil comparação.</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Dados essenciais: Preço, Área, Quartos/Banheiros, Localização, Diferenciais.</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Opção de remover imóveis nesta tela.</span>
                  </li>
                  <li class="flex items-start gap-3 group">
                    <div class="w-5 h-5 rounded border border-subtle flex items-center justify-center mt-0.5 group-hover:border-action-primary transition-colors">
                      <div class="w-3 h-3 bg-action-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                    </div>
                    <span class="text-secondary font-light flex-1">Hierarquia visual clara (destacar diferenças/semelhanças).</span>
                  </li>
                </ul>
              </div>

              <!-- Critérios de Sucesso -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Critérios de Sucesso</h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div class="p-4 bg-surface-subtle rounded border border-subtle">
                    <strong class="block text-text-primary mb-2">Usabilidade</strong>
                    <span class="text-sm text-secondary font-light">Facilidade e clareza no fluxo.</span>
                  </div>
                  <div class="p-4 bg-surface-subtle rounded border border-subtle">
                    <strong class="block text-text-primary mb-2">Visual</strong>
                    <span class="text-sm text-secondary font-light">Estética "Luxury" e organização.</span>
                  </div>
                  <div class="p-4 bg-surface-subtle rounded border border-subtle">
                    <strong class="block text-text-primary mb-2">Funcionalidade</strong>
                    <span class="text-sm text-secondary font-light">Eficiência das interações.</span>
                  </div>
                </div>
              </div>

              <!-- Entrega -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-4 text-text-primary">Entrega</h3>
                <p class="text-secondary font-light leading-relaxed mb-6">
                  Protótipo interativo no Figma com fluxo completo.
                </p>
                <div class="flex flex-wrap gap-4">
                  <a 
                    href="https://www.figma.com/design/MJM59qaF0NVLdMDW1xgWQc/Pilar?node-id=0-1&t=Ya0taV96bP9jSYZg-1" 
                    target="_blank"
                    class="inline-flex items-center gap-3 px-6 py-3 bg-action-primary text-inverse text-sm font-medium uppercase tracking-widest hover:bg-action-primary/90 transition-colors rounded"
                  >
                    <i class="lni lni-figma"></i>
                    Acessar Figma
                  </a>
                  
                  <NuxtLink 
                    to="/prototipo" 
                    class="inline-flex items-center gap-3 px-6 py-3 bg-white border border-subtle text-text-primary text-sm font-medium uppercase tracking-widest hover:border-action-primary hover:text-action-primary transition-colors rounded"
                  >
                    <i class="lni lni-code"></i>
                    Protótipo Vue
                  </NuxtLink>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>




