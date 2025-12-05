<script setup lang="ts">
useSeoMeta({
  title: 'Discovery & Pesquisa - Pilar Homes',
  description: 'Hub de pesquisa e descoberta do projeto.'
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
          <div class="h-4 w-px bg-border-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Discovery</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <!-- Intro -->
        <div class="mb-20 border-b border-border-subtle pb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 01</span>
          <h1 class="text-6xl md:text-7xl font-light tracking-tighter mb-8 text-text-primary">Discovery</h1>
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
              <NuxtLink to="/pesquisa/contexto" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors">
                Explorar Contexto <span class="text-lg">→</span>
              </NuxtLink>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-4">
              <NuxtLink to="/pesquisa/contexto/pilar" class="bg-surface-card p-8 border rounded-lg border-border-subtle hover:border-border-strong transition-colors">
                <h3 class="text-lg font-medium text-text-primary mb-2">Sobre a Pilar</h3>
                <p class="text-sm text-secondary font-light">História, valores e posicionamento de marca.</p>
              </NuxtLink>
              <NuxtLink to="/pesquisa/contexto/mercado" class="bg-surface-card p-8 border rounded-lg border-border-subtle hover:border-border-strong transition-colors">
                <h3 class="text-lg font-medium text-text-primary mb-2">Mercado</h3>
                <p class="text-sm text-secondary font-light">Tendências do setor imobiliário de alto padrão.</p>
              </NuxtLink>
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
              <NuxtLink to="/pesquisa/usuario" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors">
                Explorar Usuário <span class="text-lg">→</span>
              </NuxtLink>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-4">
              <NuxtLink to="/pesquisa/personas" class="bg-surface-card p-8 border rounded-lg border-border-subtle hover:border-border-strong transition-colors">
                <h3 class="text-lg font-medium text-text-primary mb-2">Personas</h3>
                <p class="text-sm text-secondary font-light">Arquétipos dos clientes ideais.</p>
              </NuxtLink>
              <NuxtLink to="/pesquisa/jornadas" class="bg-surface-card p-8 border rounded-lg border-border-subtle hover:border-border-strong transition-colors">
                <h3 class="text-lg font-medium text-text-primary mb-2">Jornadas</h3>
                <p class="text-sm text-secondary font-light">Mapeamento do fluxo atual vs. ideal.</p>
              </NuxtLink>
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
              <NuxtLink to="/pesquisa/design" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors">
                Explorar Design <span class="text-lg">→</span>
              </NuxtLink>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-4">
              <NuxtLink to="/pesquisa/benchmarking" class="bg-surface-card p-8 border rounded-lg border-border-subtle hover:border-border-strong transition-colors">
                <h3 class="text-lg font-medium text-text-primary mb-2">Benchmarking</h3>
                <p class="text-sm text-secondary font-light">Análise de concorrentes diretos e indiretos.</p>
              </NuxtLink>
              <NuxtLink to="/pesquisa/ui-patterns" class="bg-surface-card p-8 border rounded-lg border-border-subtle hover:border-border-strong transition-colors">
                <h3 class="text-lg font-medium text-text-primary mb-2">UI Patterns</h3>
                <p class="text-sm text-secondary font-light">Estudos de componentes e interações.</p>
              </NuxtLink>
            </div>
          </section>

        </div>
      </div>
    </main>
  </div>
</template>


