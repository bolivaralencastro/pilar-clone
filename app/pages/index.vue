<script setup lang="ts">
useSeoMeta({
  title: 'Pilar Homes - Desafio Técnico',
  description: 'Dashboard do desafio técnico Pilar Homes'
})
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header Minimal -->
    <header class="bg-white border-b border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          <span class="text-xs font-mono text-secondary tracking-widest uppercase border-l border-subtle pl-4">Desafio Técnico</span>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16 relative z-10">
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
            <NuxtLink to="/apresentacao" class="group flex items-center gap-3 text-primary hover:text-action-primary transition-colors duration-300">
              <span class="uppercase tracking-widest text-xs font-medium">Iniciar Apresentação</span>
              <span class="text-lg group-hover:translate-x-1 transition-transform">→</span>
            </NuxtLink>
          </div>
        </div>

        <!-- Navigation Grid (The Index) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-subtle border border-subtle rounded-lg">
          
          <!-- Column 1: Context -->
          <div class="bg-surface-base p-12 group hover:bg-surface-card transition-colors duration-500">
            <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-8 block">01. Contexto</span>
            <div class="space-y-8">
              <NuxtLink to="/briefing" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Briefing</h3>
                <p class="text-sm text-secondary font-light">Entendimento do desafio e requisitos.</p>
              </NuxtLink>
              <NuxtLink to="/programacao" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Planejamento</h3>
                <p class="text-sm text-secondary font-light">Cronograma e organização pessoal.</p>
              </NuxtLink>
            </div>
          </div>

          <!-- Column 2: Process -->
          <div class="bg-surface-base p-12 group hover:bg-surface-card transition-colors duration-500">
            <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-8 block">02. Processo</span>
            <div class="space-y-8">
              <NuxtLink to="/pesquisa" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Discovery</h3>
                <p class="text-sm text-secondary font-light">Pesquisa, personas e benchmarking.</p>
              </NuxtLink>
              <NuxtLink to="/estrategia" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Estratégia</h3>
                <p class="text-sm text-secondary font-light">Definição de direção e objetivos.</p>
              </NuxtLink>
              <NuxtLink to="/ideacao" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Ideação</h3>
                <p class="text-sm text-secondary font-light">Fluxos, wireframes e arquitetura.</p>
              </NuxtLink>
            </div>
          </div>

          <!-- Column 3: Output -->
          <div class="bg-surface-base p-12 group hover:bg-surface-card transition-colors duration-500">
            <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-8 block">03. Entrega</span>
            <div class="space-y-8">
              <NuxtLink to="/ui-design" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">UI Design</h3>
                <p class="text-sm text-secondary font-light">Design System e tokens visuais.</p>
              </NuxtLink>
              <NuxtLink to="/prototipo" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Protótipo</h3>
                <p class="text-sm text-secondary font-light">Acesso às funcionalidades finais.</p>
              </NuxtLink>
              <NuxtLink to="/entrega" class="block group/item">
                <h3 class="text-2xl font-light mb-2 group-hover/item:text-text-primary transition-colors">Roadmap</h3>
                <p class="text-sm text-secondary font-light">Próximos passos e evolução.</p>
              </NuxtLink>
            </div>
          </div>

        </div>

      </div>
    </main>
  </div>
</template>


