<script setup lang="ts">
useSeoMeta({
  title: 'UI Patterns - Pilar Homes',
  description: 'Estudos de componentes e padrões de interface para experiências premium.'
})
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa/design" class="text-secondary hover:text-text-primary transition-colors">Design</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">UI Patterns</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          <!-- Sidebar -->
          <aside class="lg:col-span-4 sticky top-32 h-fit">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 03.2</span>
            <h1 class="text-4xl md:text-5xl font-light tracking-tighter mb-8 text-text-primary">UI Patterns</h1>
            <div class="w-12 h-1 bg-mat-stone mb-8"></div>
            
            <nav class="space-y-4 border-l border-subtle pl-6">
              <a href="#navegacao" class="block text-sm font-medium text-primary hover:text-action-primary transition-colors">Navegação</a>
              <a href="#cards" class="block text-sm font-light text-secondary hover:text-text-primary transition-colors">Cards</a>
              <a href="#filtros" class="block text-sm font-light text-secondary hover:text-text-primary transition-colors">Filtros</a>
              <a href="#galerias" class="block text-sm font-light text-secondary hover:text-text-primary transition-colors">Galerias</a>
            </nav>
          </aside>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6 space-y-8">
            
            <!-- Section: Navegação -->
            <section id="navegacao" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Padrões de Navegação</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline rounded-lg mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed mb-6">
                  A navegação em sites de imóveis de luxo deve ser intuitiva, discreta e permitir que o conteúdo visual seja protagonista.
                </p>
              </div>

              <div class="space-y-6">
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Menu Minimalista</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Navegação principal com poucos itens, hierarquia clara e suporte para mega-menus quando necessário.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Minimalismo</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Hierarquia</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Breadcrumbs Contextuais</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Navegação secundária que ajuda o usuário a entender sua posição e voltar facilmente.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Contexto</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">UX</span>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Cards -->
            <section id="cards" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Cards de Propriedades</h2>
              
              <div class="space-y-6">
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Imagem Dominante</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Cards com proporção 16:9 ou 4:3 onde a imagem é o elemento principal, com overlays sutis de informação.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Visual First</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Overlay</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Informação Hierárquica</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Título do imóvel, preço destacado, localização e atributos principais em ordem de importância.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Tipografia</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Hierarquia</span>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Filtros -->
            <section id="filtros" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Sistemas de Filtros</h2>
              
              <div class="space-y-6">
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Filtros Avançados</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Sidebar persistente ou modal com múltiplos critérios: localização, preço, características, amenidades.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Filtros</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Busca</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Tags Ativas</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Visualização clara dos filtros aplicados com possibilidade de remoção individual.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Tags</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Feedback</span>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Galerias -->
            <section id="galerias" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Galerias de Imagens</h2>
              
              <div class="space-y-6">
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Lightbox Premium</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Visualização em tela cheia com navegação fluida, zoom de alta qualidade e informações contextuais.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Lightbox</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Zoom</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Grid Responsivo</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Layouts em grid que se adaptam ao tamanho da tela mantendo proporções elegantes.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Grid</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Responsive</span>
                  </div>
                </div>
              </div>
            </section>

            <!-- Navigation -->
            <div class="pt-8 border-t border-subtle flex justify-between items-center">
              <NuxtLink to="/pesquisa/design" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
                <span class="text-lg">←</span> Voltar para Design
              </NuxtLink>
            </div>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>







