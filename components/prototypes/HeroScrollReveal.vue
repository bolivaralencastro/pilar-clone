<template>
  <section class="relative bg-surface-base py-24 md:py-32">
    <div class="container mx-auto px-6">
      <!-- Content -->
      <div class="flex flex-col items-center text-center max-w-4xl mx-auto">
        <!-- Tag -->
        <span class="text-xs tracking-[0.2em] uppercase text-text-secondary mb-6 border-t border-border-subtle pt-4">
          SÃO PAULO • CURITIBA
        </span>
        
        <!-- Title -->
        <h1 class="font-playfair text-4xl md:text-5xl lg:text-6xl text-text-primary mb-6 leading-tight">
          Curadoria de imóveis<br>de alto padrão
        </h1>
        
        <!-- Description -->
        <p class="text-text-secondary text-base md:text-lg max-w-lg mb-10 leading-relaxed">
          Atendimento personalizado e o maior portfólio de imóveis exclusivos em localização privilegiada.
        </p>
        
        <!-- Search Bar -->
        <div class="flex w-full max-w-md bg-white rounded-full shadow-lg border border-border-subtle overflow-hidden">
          <input 
            type="text" 
            placeholder="Buscar por bairro, cidade..." 
            class="flex-1 px-6 py-3 text-sm text-text-primary placeholder-text-secondary outline-none bg-transparent"
            @keyup.enter="router.push('/prototipo/resultados?tab=new')"
          >
          <button 
            type="button"
            class="px-6 py-3 bg-text-primary text-white text-xs font-bold tracking-wider uppercase hover:bg-accent-gold transition-colors"
            @click="router.push('/prototipo/resultados?tab=new')"
          >
            Buscar
          </button>
        </div>
      </div>
      
      <!-- Video -->
      <div class="mt-16 md:mt-20">
        <div class="relative rounded-2xl overflow-hidden shadow-2xl aspect-video max-w-5xl mx-auto">
          <video 
            autoplay 
            muted 
            loop 
            playsinline
            class="w-full h-full object-cover"
          >
            <source src="/video/hero-video.mp4" type="video/mp4">
          </video>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const router = useRouter()
</script>
