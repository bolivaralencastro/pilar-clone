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
            <span class="text-text-primary">Protótipo</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 05</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Protótipo</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Navegue pelas funcionalidades implementadas no protótipo de alta fidelidade.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="grid grid-cols-1 gap-8">
              <NuxtLink to="/" class="group block">
                <div class="bg-surface-card border rounded-lg border-border-subtle p-8 transition-all duration-500 hover:border-action-primary/30 hover:shadow-xl relative overflow-hidden">
                  <div class="absolute top-0 left-0 w-1 h-full bg-mat-stone transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500"></div>
                  
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Funcionalidade 01</span>
                  <h3 class="text-2xl font-light mb-4 text-text-primary group-hover:translate-x-2 transition-transform duration-300">Busca de Imóveis</h3>
                  <p class="text-secondary font-light leading-relaxed group-hover:text-text-primary transition-colors">
                    Listagem principal com filtros avançados e visualização em cards imersivos.
                  </p>
                  
                  <div class="mt-8 flex items-center gap-2 text-sm font-medium uppercase tracking-widest opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-2 group-hover:translate-y-0 text-action-primary">
                    Acessar <span class="text-lg">→</span>
                  </div>
                </div>
              </NuxtLink>

              <NuxtLink to="/compare" class="group block">
                <div class="bg-surface-card border rounded-lg border-border-subtle p-8 transition-all duration-500 hover:border-action-primary/30 hover:shadow-xl relative overflow-hidden">
                  <div class="absolute top-0 left-0 w-1 h-full bg-mat-stone transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500"></div>
                  
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest mb-4 block">Funcionalidade 02</span>
                  <h3 class="text-2xl font-light mb-4 text-text-primary group-hover:translate-x-2 transition-transform duration-300">Comparador</h3>
                  <p class="text-secondary font-light leading-relaxed group-hover:text-text-primary transition-colors">
                    Ferramenta de comparação lado a lado para análise detalhada de especificações.
                  </p>
                  
                  <div class="mt-8 flex items-center gap-2 text-sm font-medium uppercase tracking-widest opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-2 group-hover:translate-y-0 text-action-primary">
                    Acessar <span class="text-lg">→</span>
                  </div>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>



