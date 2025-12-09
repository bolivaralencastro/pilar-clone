<template>
  <header 
    class="w-full z-[200] py-6 bg-surface-base transition-all duration-300"
    :class="[ sticky ? 'sticky top-0' : 'relative' ]"
  >
    <div class="container mx-auto px-8 flex items-center justify-between">
      
      <!-- Left: Nav Links -->
      <nav class="hidden md:flex items-center gap-6 text-xs font-sans font-medium uppercase tracking-widest text-text-secondary">
        <button class="w-9 h-9 flex items-center justify-center hover:text-text-primary transition-colors" title="Buscar">
          <i class="lni lni-search text-base"></i>
        </button>
        <NuxtLink to="/prototipo/resultados?tab=new" class="hover:text-text-primary transition-colors">Comprar</NuxtLink>
        <a href="#" class="hover:text-text-primary transition-colors">Vender</a>
      </nav>

      <!-- Right Actions -->
      <div class="flex items-center gap-8 text-xs font-sans font-medium uppercase tracking-widest text-text-secondary">
        <a href="#" class="hidden md:block hover:text-text-primary transition-colors">Magazine</a>
        <a href="#" class="hover:text-text-primary transition-colors">Entrar</a>
      </div>
    </div>

    <!-- Center: Logo -->
    <div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">
      <NuxtLink to="/prototipo/home?tab=new">
        <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-5 w-auto hover:opacity-80 transition-opacity cursor-pointer" />
      </NuxtLink>
    </div>
  </header>
</template>

<script setup lang="ts">
// Header component - standalone luxury navigation
// Can be extended with props for variants (transparent, dark, etc.)
defineProps({
  sticky: {
    type: Boolean,
    default: true
  }
})
</script>
