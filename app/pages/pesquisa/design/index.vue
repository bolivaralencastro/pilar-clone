<script setup lang="ts">
useSeoMeta({
  title: 'Design & Referências - Pilar Homes',
  description: 'Consolidado da análise visual e padrões de interface.'
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
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Design</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        
        <!-- Intro -->
        <div class="mb-20 border-b border-border-subtle pb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 03</span>
          <h1 class="text-6xl md:text-7xl font-light tracking-tighter mb-8 text-text-primary">Design & Referências</h1>
          <p class="text-secondary text-xl font-light leading-relaxed max-w-3xl">
            Análise visual competitiva e identificação de padrões de interface que transmitam luxo, sofisticação e funcionalidade excepcional.
          </p>
        </div>

        <!-- Summary Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-20">
          <NuxtLink to="/pesquisa/benchmarking" class="group bg-surface-card p-10 border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">03.1</span>
            <h2 class="text-3xl font-light text-text-primary mb-4 group-hover:text-action-primary transition-colors">Benchmarking</h2>
            <p class="text-secondary font-light leading-relaxed mb-6">
              Análise detalhada de concorrentes diretos e indiretos, identificando melhores práticas e oportunidades de diferenciação.
            </p>
            <span class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary">
              Explorar <span class="text-lg">→</span>
            </span>
          </NuxtLink>

          <NuxtLink to="/pesquisa/ui-patterns" class="group bg-surface-card p-10 border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">03.2</span>
            <h2 class="text-3xl font-light text-text-primary mb-4 group-hover:text-action-primary transition-colors">UI Patterns</h2>
            <p class="text-secondary font-light leading-relaxed mb-6">
              Estudos de componentes, padrões de interação e soluções de interface para experiências premium.
            </p>
            <span class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary">
              Explorar <span class="text-lg">→</span>
            </span>
          </NuxtLink>
        </div>

        <!-- Key Insights -->
        <div class="mb-20">
          <h2 class="text-3xl font-light text-text-primary mb-8">Principais Insights</h2>
          
          <div class="space-y-6">
            <div class="bg-surface-card p-8 border rounded-lg-l-4 border-action-primary">
              <h3 class="text-lg font-medium text-text-primary mb-3">Minimalismo Sofisticado</h3>
              <p class="text-secondary font-light leading-relaxed">
                Interfaces de luxo privilegiam o minimalismo, com amplo uso de espaços em branco e tipografia elegante que transmite exclusividade.
              </p>
            </div>

            <div class="bg-surface-card p-8 border-l-4 border-border-strong rounded-lg">
              <h3 class="text-lg font-medium text-text-primary mb-3">Fotografia Premium</h3>
              <p class="text-secondary font-light leading-relaxed">
                A qualidade e apresentação das imagens são diferenciais críticos. Galerias imersivas e tours virtuais elevam a experiência.
              </p>
            </div>

            <div class="bg-surface-card p-8 border-l-4 border-border-strong rounded-lg">
              <h3 class="text-lg font-medium text-text-primary mb-3">Microinterações Fluidas</h3>
              <p class="text-secondary font-light leading-relaxed">
                Animações sutis e transições suaves contribuem para a percepção de qualidade e atenção aos detalhes.
              </p>
            </div>
          </div>
        </div>

        <!-- Navigation -->
        <div class="pt-8 border-t border-border-subtle flex justify-between items-center">
          <NuxtLink to="/pesquisa/usuario" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
            <span class="text-lg">←</span> Anterior: Usuário
          </NuxtLink>
          <NuxtLink to="/pesquisa" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors">
            Voltar para Discovery <span class="text-lg">→</span>
          </NuxtLink>
        </div>

      </div>
    </main>
  </div>
</template>





