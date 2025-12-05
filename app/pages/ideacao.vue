<script setup lang="ts">
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-primary/10"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Ideação</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <!-- Sidebar / Title -->
          <div class="lg:col-span-4">
            <div class="sticky top-32">
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 03</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Ideação</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Exploração de soluções, fluxos de navegação e definição das funcionalidades chave.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Funcionalidades Chave</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Core Feature</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Comparador Lado a Lado</h4>
                    <p class="text-secondary font-light text-sm">Visualização simultânea de até 4 imóveis com destaque para diferenças.</p>
                  </div>
                  <div class="p-6 bg-surface-subtle">
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-2 block">Discovery</span>
                    <h4 class="text-lg font-medium mb-2 text-text-primary">Filtros Inteligentes</h4>
                    <p class="text-secondary font-light text-sm">Sistema de filtragem rápido e contextual sem recarregamento de página.</p>
                  </div>
                </div>
              </div>

              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Fluxos e Wireframes</h3>
                <p class="text-secondary font-light leading-relaxed">
                  O fluxo foi desenhado para ser linear mas flexível, permitindo que o usuário entre no funil de comparação a partir de qualquer ponto da listagem.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>


