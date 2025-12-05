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
          <div class="h-4 w-px bg-border-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Estratégia</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 02</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Estratégia</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Alinhamento de objetivos de negócio e necessidades do usuário para definir a direção do produto.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Definição Estratégica</h3>
                <p class="text-secondary font-light leading-relaxed mb-6">
                  O foco principal é reduzir a fricção no processo de comparação de imóveis, transformando uma experiência fragmentada em um fluxo contínuo e visual.
                </p>
                <ul class="space-y-4">
                  <li class="flex items-start gap-3">
                    <span class="w-1.5 h-1.5 rounded-full bg-mat-stone mt-2"></span>
                    <span class="text-secondary font-light">Centralização da informação</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <span class="w-1.5 h-1.5 rounded-full bg-mat-stone mt-2"></span>
                    <span class="text-secondary font-light">Comparação visual lado a lado</span>
                  </li>
                  <li class="flex items-start gap-3">
                    <span class="w-1.5 h-1.5 rounded-full bg-mat-stone mt-2"></span>
                    <span class="text-secondary font-light">Design minimalista para foco no conteúdo</span>
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



