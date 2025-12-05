<script setup lang="ts">
useSeoMeta({
  title: 'Jornadas do Usuário - Pilar Homes',
  description: 'Mapeamento das jornadas e pontos de contato dos usuários.'
})
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa/usuario" class="text-secondary hover:text-text-primary transition-colors">Usuário</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Jornadas</span>
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
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fluxos de Usuário</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Jornadas</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Mapeamento dos pontos de contato e fricção na experiência atual de busca e comparação de imóveis.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              <!-- Journey 1 -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Jornada de Comparação (Atual)</h3>
                
                <div class="relative pl-8 border-l border-subtle space-y-8">
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-text-primary">Busca</h4>
                    <p class="text-secondary font-light text-sm">Usuário realiza busca com filtros básicos.</p>
                  </div>
                  
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-text-primary">Seleção</h4>
                    <p class="text-secondary font-light text-sm">Abre múltiplos imóveis em novas abas do navegador.</p>
                  </div>

                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-red-500 border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-red-600">Fricção</h4>
                    <p class="text-secondary font-light text-sm">Alterna entre abas para comparar preços e m², perdendo contexto.</p>
                  </div>
                </div>
              </div>

              <!-- Journey 2 -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Jornada Proposta (To-Be)</h3>
                
                <div class="relative pl-8 border-l border-strong space-y-8">
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-text-primary">Busca</h4>
                    <p class="text-secondary font-light text-sm">Usuário realiza busca e visualiza cards.</p>
                  </div>
                  
                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-text-primary">Seleção Rápida</h4>
                    <p class="text-secondary font-light text-sm">Clica em "Adicionar ao Comparador" diretamente no card.</p>
                  </div>

                  <div class="relative">
                    <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-action-primary border-4 border-surface-card"></span>
                    <h4 class="text-sm font-bold uppercase tracking-widest mb-1 text-action-primary">Comparação</h4>
                    <p class="text-secondary font-light text-sm">Visualiza até 4 imóveis lado a lado em uma única tela.</p>
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





