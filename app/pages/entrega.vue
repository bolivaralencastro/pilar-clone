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
            <span class="text-text-primary">Entrega</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 06</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Entrega</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Roadmap de desenvolvimento e próximos passos para evolução do produto.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Roadmap</h3>
                <div class="space-y-8 relative pl-8 border-l border-border-subtle">
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-text-primary">Q1 2024</h4>
                    <p class="text-secondary font-light text-sm">Lançamento do MVP com busca e comparador básico.</p>
                  </div>
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-secondary">Q2 2024</h4>
                    <p class="text-secondary font-light text-sm">Integração com CRM e agendamento de visitas online.</p>
                  </div>
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-secondary">Q3 2024</h4>
                    <p class="text-secondary font-light text-sm">Expansão para novos bairros e funcionalidade de tour virtual.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>



