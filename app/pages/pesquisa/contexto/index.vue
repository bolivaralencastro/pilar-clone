<script setup lang="ts">
useSeoMeta({
  title: 'Contexto & Negócio - Pilar Homes',
  description: 'Hub de análise de contexto de negócio e mercado da Pilar Homes.'
})
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
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Contexto</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        
        <!-- Intro -->
        <div class="mb-20 border-b border-border-subtle pb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 01</span>
          <h1 class="text-6xl md:text-7xl font-light tracking-tighter mb-8 text-text-primary">Contexto &<br/>Negócio</h1>
          <div class="w-16 h-1 bg-mat-stone mb-8"></div>
          <p class="text-secondary text-xl font-light leading-relaxed max-w-3xl">
            Análise aprofundada do contexto da Pilar como empresa, seu posicionamento no mercado imobiliário e as oportunidades identificadas.
          </p>
        </div>

        <!-- Sub-páginas Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <!-- Card: Sobre a Pilar -->
          <NuxtLink to="/pesquisa/contexto/pilar" class="group bg-surface-card border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all duration-500 p-8">
            <div class="flex items-start justify-between mb-6">
              <span class="text-xs font-mono text-action-primary uppercase tracking-widest">01</span>
              <span class="text-4xl group-hover:translate-x-2 transition-transform duration-300">→</span>
            </div>
            <h2 class="text-2xl font-light text-text-primary mb-4 group-hover:text-action-primary transition-colors">Sobre a Pilar</h2>
            <p class="text-secondary font-light leading-relaxed mb-6">
              Estrutura organizacional, fundadores, crescimento e modelo de negócio da Pilar como proptech de suporte ao corretor.
            </p>
            <div class="flex flex-wrap gap-2">
              <span class="text-xs px-3 py-1 bg-surface-subtle border border-border-subtle rounded-full rounded-lg">Organização</span>
              <span class="text-xs px-3 py-1 bg-surface-subtle border border-border-subtle rounded-full rounded-lg">Time</span>
              <span class="text-xs px-3 py-1 bg-surface-subtle border border-border-subtle rounded-full rounded-lg">Modelo</span>
            </div>
          </NuxtLink>

          <!-- Card: Mercado -->
          <NuxtLink to="/pesquisa/contexto/mercado" class="group bg-surface-card border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all duration-500 p-8">
            <div class="flex items-start justify-between mb-6">
              <span class="text-xs font-mono text-action-primary uppercase tracking-widest">02</span>
              <span class="text-4xl group-hover:translate-x-2 transition-transform duration-300">→</span>
            </div>
            <h2 class="text-2xl font-light text-text-primary mb-4 group-hover:text-action-primary transition-colors">Visão de Mercado</h2>
            <p class="text-secondary font-light leading-relaxed mb-6">
              Análise do mercado imobiliário de alto padrão, tendências, comportamento do consumidor e oportunidades identificadas.
            </p>
            <div class="flex flex-wrap gap-2">
              <span class="text-xs px-3 py-1 bg-surface-subtle border border-border-subtle rounded-full rounded-lg">Tendências</span>
              <span class="text-xs px-3 py-1 bg-surface-subtle border border-border-subtle rounded-full rounded-lg">Consumidor</span>
              <span class="text-xs px-3 py-1 bg-surface-subtle border border-border-subtle rounded-full rounded-lg">Oportunidades</span>
            </div>
          </NuxtLink>

        </div>

        <!-- Navigation -->
        <div class="mt-16 pt-8 border-t border-border-subtle flex justify-between items-center">
          <NuxtLink to="/pesquisa" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
            <span class="text-lg">←</span> Voltar para Discovery
          </NuxtLink>
        </div>

      </div>
    </main>
  </div>
</template>



