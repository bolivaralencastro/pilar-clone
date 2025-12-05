<script setup lang="ts">
useSeoMeta({
  title: 'Usuário & Experiência - Pilar Homes',
  description: 'Consolidado da pesquisa de usuários e mapeamento de jornadas.'
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
            <span class="text-text-primary">Usuário</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        
        <!-- Intro -->
        <div class="mb-20 border-b border-border-subtle pb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 02</span>
          <h1 class="text-6xl md:text-7xl font-light tracking-tighter mb-8 text-text-primary">Usuário & Experiência</h1>
          <p class="text-secondary text-xl font-light leading-relaxed max-w-3xl">
            Compreensão profunda dos usuários, suas necessidades, dores e jornadas para criar experiências verdadeiramente centradas no cliente.
          </p>
        </div>

        <!-- Summary Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-20">
          <NuxtLink to="/pesquisa/personas" class="group bg-surface-card p-10 border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">02.1</span>
            <h2 class="text-3xl font-light text-text-primary mb-4 group-hover:text-action-primary transition-colors">Personas</h2>
            <p class="text-secondary font-light leading-relaxed mb-6">
              Arquétipos detalhados dos clientes ideais, incluindo perfis demográficos, comportamentais e necessidades.
            </p>
            <span class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary">
              Explorar <span class="text-lg">→</span>
            </span>
          </NuxtLink>

          <NuxtLink to="/pesquisa/jornadas" class="group bg-surface-card p-10 border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">02.2</span>
            <h2 class="text-3xl font-light text-text-primary mb-4 group-hover:text-action-primary transition-colors">Jornadas</h2>
            <p class="text-secondary font-light leading-relaxed mb-6">
              Mapeamento detalhado das jornadas atuais e ideais, identificando pontos de contato e oportunidades.
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
              <h3 class="text-lg font-medium text-text-primary mb-3">Busca por Experiências</h3>
              <p class="text-secondary font-light leading-relaxed">
                Usuários de alto padrão não buscam apenas imóveis, mas experiências de vida. O contexto e lifestyle são tão importantes quanto as características físicas.
              </p>
            </div>

            <div class="bg-surface-card p-8 border-l-4 border-border-strong rounded-lg">
              <h3 class="text-lg font-medium text-text-primary mb-3">Jornada Complexa</h3>
              <p class="text-secondary font-light leading-relaxed">
                A decisão de compra envolve múltiplos stakeholders, pesquisa extensa e comparações detalhadas, demandando ferramentas que facilitem este processo.
              </p>
            </div>

            <div class="bg-surface-card p-8 border-l-4 border-border-strong rounded-lg">
              <h3 class="text-lg font-medium text-text-primary mb-3">Confiança e Transparência</h3>
              <p class="text-secondary font-light leading-relaxed">
                Informação completa, transparente e facilmente acessível é fundamental para estabelecer confiança e facilitar a tomada de decisão.
              </p>
            </div>
          </div>
        </div>

        <!-- Navigation -->
        <div class="pt-8 border-t border-border-subtle flex justify-between items-center">
          <NuxtLink to="/pesquisa/contexto" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
            <span class="text-lg">←</span> Anterior: Contexto
          </NuxtLink>
          <NuxtLink to="/pesquisa/design" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-action-primary hover:text-text-primary transition-colors">
            Próximo: Design <span class="text-lg">→</span>
          </NuxtLink>
        </div>

      </div>
    </main>
  </div>
</template>





