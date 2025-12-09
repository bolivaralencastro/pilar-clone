<template>
  <div class="min-h-screen bg-surface-base flex items-center justify-center">
    <div class="text-center max-w-md mx-auto px-6">
      <div class="w-20 h-20 bg-surface-subtle rounded-full flex items-center justify-center mx-auto mb-6">
        <i class="lni lni-stats-up text-3xl text-text-secondary"></i>
      </div>
      <h1 class="text-2xl font-serif font-light text-text-primary mb-3">Comparador de Imóveis</h1>
      <p class="text-text-secondary font-light mb-6">
        O comparador agora abre diretamente como um modal na página de resultados. 
        Selecione imóveis para comparar na busca.
      </p>
      <NuxtLink 
        to="/prototipo/resultados?tab=new"
        class="inline-flex items-center gap-2 px-6 py-3 bg-text-primary text-white rounded text-sm uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors"
      >
        <i class="lni lni-arrow-left"></i>
        Ir para Resultados
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
// Página de fallback - o comparador agora é um modal no ComparisonFloatingBar
// Esta página existe para redirecionamento de links antigos
</script>
