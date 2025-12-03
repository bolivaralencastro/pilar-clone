<script setup lang="ts">
const props = defineProps<{
  loading?: boolean
}>()
</script>

<template>
  <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center gap-2">
          <div class="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-xl">P</span>
          </div>
          <span class="text-xl font-bold text-primary">Pilar Clone</span>
        </NuxtLink>
        
        <!-- Navigation -->
        <nav class="hidden md:flex items-center gap-6">
          <NuxtLink 
            to="/" 
            class="text-gray-600 hover:text-primary transition-colors font-medium"
          >
            Buscar Imóveis
          </NuxtLink>
          <NuxtLink 
            to="/sobre" 
            class="text-gray-600 hover:text-primary transition-colors font-medium"
          >
            Sobre
          </NuxtLink>
        </nav>
        
        <!-- Actions -->
        <div class="flex items-center gap-3">
          <button class="btn-secondary hidden sm:flex items-center gap-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
            Favoritos
          </button>
          
          <button class="btn-primary">
            Anunciar
          </button>
        </div>
      </div>
    </div>
    
    <!-- Loading bar -->
    <div 
      v-if="loading"
      class="absolute bottom-0 left-0 right-0 h-1 bg-gray-200 overflow-hidden"
    >
      <div class="h-full bg-accent animate-pulse w-full"></div>
    </div>
  </header>
</template>
