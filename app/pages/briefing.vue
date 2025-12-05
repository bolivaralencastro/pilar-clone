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
            <span class="text-text-primary">Briefing</span>
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
              
              <!-- Context Section -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Contexto</h3>
                <p class="text-secondary font-light leading-relaxed">
                  Este projeto visa modernizar a experiência digital da Pilar Homes, alinhando-a com o posicionamento de luxo da marca. O foco principal é a implementação de um sistema de comparação de imóveis e a refatoração visual utilizando o novo Design System.
                </p>
              </div>

              <!-- Objectives Section -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Objetivos Principais</h3>
                <ul class="space-y-4">
                  <li class="flex items-start gap-4 group">
                    <span class="w-6 h-6 flex items-center justify-center rounded-full bg-surface-subtle text-xs font-mono text-secondary group-hover:bg-mat-stone group-hover:text-inverse transition-colors">01</span>
                    <span class="text-secondary font-light flex-1 pt-0.5">Implementar funcionalidade de comparação de imóveis (até 4 itens).</span>
                  </li>
                  <li class="flex items-start gap-4 group">
                    <span class="w-6 h-6 flex items-center justify-center rounded-full bg-surface-subtle text-xs font-mono text-secondary group-hover:bg-mat-stone group-hover:text-inverse transition-colors">02</span>
                    <span class="text-secondary font-light flex-1 pt-0.5">Refatorar a interface para refletir a estética "Luxury/Magazine".</span>
                  </li>
                  <li class="flex items-start gap-4 group">
                    <span class="w-6 h-6 flex items-center justify-center rounded-full bg-surface-subtle text-xs font-mono text-secondary group-hover:bg-mat-stone group-hover:text-inverse transition-colors">03</span>
                    <span class="text-secondary font-light flex-1 pt-0.5">Otimizar a performance e a experiência do usuário (UX).</span>
                  </li>
                  <li class="flex items-start gap-4 group">
                    <span class="w-6 h-6 flex items-center justify-center rounded-full bg-surface-subtle text-xs font-mono text-secondary group-hover:bg-mat-stone group-hover:text-inverse transition-colors">04</span>
                    <span class="text-secondary font-light flex-1 pt-0.5">Garantir responsividade e acessibilidade.</span>
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


