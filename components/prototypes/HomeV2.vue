<template>
  <div class="font-sans text-text-primary min-h-screen bg-surface-base relative" :class="{ 'is-mobile': forceMobile }">
    
    <!-- Header (Not Fixed) -->
    <HeaderLuxury :sticky="false" :forceMobile="forceMobile" />

    <!-- Hero Scroll Reveal -->
    <HeroScrollReveal />

    <!-- Section 2: Editorial Horizontal Scroll -->
    <EditorialHorizontalScroll class="relative z-10" />

    <!-- Main Content -->
    <div class="relative z-20 bg-surface-base">

    <!-- Navigation Monochrome -->
    <div class="relative z-20 bg-surface-base">
      <NavigationMonochrome />
    </div>

    <!-- Regions -->
    <section class="regions-section py-20 md:pt-32 bg-surface-base text-text-primary overflow-hidden relative z-20">
      <div class="container mx-auto px-6">
        
        <!-- 1. EDITORIAL HEADER (Grid Assimétrico) -->
        <div class="regions-header grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-24 mb-16 items-end">
          
          <!-- Título (Lado Esquerdo) -->
          <div class="lg:col-span-6">
            <h2 class="text-sm md:text-base font-light tracking-[0.2em] leading-[1.1] text-text-primary uppercase">
              Nossas <br>
              <span class="text-5xl md:text-6xl text-text-secondary opacity-60 italic font-playfair normal-case">Regiões</span>
            </h2>
          </div>

          <!-- Descrição (Lado Direito - Offset) -->
          <div class="lg:col-span-5 lg:col-start-8">
            <p class="text-sm md:text-base text-text-secondary font-light leading-relaxed mb-8">
              Descubra bairros onde a arquitetura encontra o estilo de vida. Uma curadoria de localizações perfeitas para quem busca exclusividade e bem-estar.
            </p>
            <a href="#" class="inline-block text-xs font-bold uppercase tracking-[0.2em] border-b border-text-primary pb-1 hover:text-primary-600 hover:border-primary-600 transition-colors">
              Explorar todas as regiões
            </a>
          </div>
        </div>

        <!-- 2. CARROSSEL DE REGIÕES -->
        <div class="relative w-full">
          
          <!-- Scroll Container -->
          <div 
            ref="regionsCarousel"
            class="regions-carousel flex gap-6 overflow-x-auto hide-scrollbar pb-20 pr-16 -mr-6 md:-mr-24 pl-1 scroll-smooth"
          >
            
            <div v-for="(region, index) in regions" :key="index" class="region-card group min-w-[70vw] md:min-w-[25vw] cursor-pointer">
              <div class="aspect-[2/3] w-full bg-surface-offset overflow-hidden mb-4 relative" style="border-radius: 4px;">
                <img :src="region.image" class="w-full h-full object-cover img-zoom opacity-90 group-hover:opacity-100 transition-opacity" alt="Region Image">
                 <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                    <span class="bg-surface-card/90 backdrop-blur px-3 py-1 text-[9px] uppercase tracking-widest font-bold text-text-primary">{{ region.label }}</span>
                 </div>
              </div>
              
              <div class="flex justify-between items-center px-1">
                 <h3 class="text-lg font-light text-text-primary tracking-tight group-hover:text-primary-600 transition-colors">{{ region.name }}</h3>
                 <div class="text-text-secondary opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-300">
                    <AppIcon name="arrow-right" size="18" />
                 </div>
              </div>
            </div>

          </div>

        </div>

        <!-- Controles de navegação do carrossel -->
        <div class="carousel-controls mt-8 flex justify-end items-center">
          <div class="flex gap-2">
            <button 
              @click="scrollRegions('left')"
              class="w-10 h-10 border border-border-subtle rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors"
            >
              ←
            </button>
            <button 
              @click="scrollRegions('right')"
              class="w-10 h-10 border border-border-subtle rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors"
            >
              →
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- Section: Exclusive Collection -->
    <section class="py-20 bg-surface-base flex justify-center relative z-20">
      <ExclusiveCollection />
    </section>

    <!-- Curated Collections Split -->
    <div class="relative z-20 bg-surface-base">
      <CuratedCollectionsSplit />
    </div>

    <!-- Testimonials Refined -->
    <div class="relative z-20 bg-surface-base">
      <TestimonialsRefined />
    </div>

    <!-- Footer Luxury Component -->
    <div class="relative z-20 bg-surface-base">
      <FooterLuxury />
    </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { provide, computed } from 'vue'
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import CuratedCollectionsSplit from './CuratedCollectionsSplit.vue'
import TestimonialsRefined from './TestimonialsRefined.vue'
import NavigationMonochrome from './NavigationMonochrome.vue'
import ExclusiveCollection from './ExclusiveCollection.vue'
import HeroScrollReveal from './HeroScrollReveal.vue'
import EditorialHorizontalScroll from './EditorialHorizontalScroll.vue'

const props = defineProps<{
  forceMobile?: boolean
}>()

// Provide forceMobile to all child components
provide('forceMobile', computed(() => props.forceMobile ?? false))

const router = useRouter()

const regionsCarousel = ref<HTMLElement | null>(null)

const scrollRegions = (direction: 'left' | 'right') => {
  if (!regionsCarousel.value) return
  
  const scrollAmount = 400
  const currentScroll = regionsCarousel.value.scrollLeft
  
  if (direction === 'left') {
    regionsCarousel.value.scrollTo({
      left: currentScroll - scrollAmount,
      behavior: 'smooth'
    })
  } else {
    regionsCarousel.value.scrollTo({
      left: currentScroll + scrollAmount,
      behavior: 'smooth'
    })
  }
}

const regions = ref([
  { name: 'São Paulo', image: '/images/sao-paulo.jpeg', label: 'Capital' },
  { name: 'Curitiba', image: '/images/curitiba.png', label: 'Sul' },
  { name: 'Boa Vista', image: '/images/boa vista.jpeg', label: 'Campo' },
  { name: 'Alphaville', image: '/images/alphaville.jpeg', label: 'Grande SP' }
])
</script>

<style scoped>
  /* Custom scrollbar hiding for clean UI */
  .hide-scrollbar::-webkit-scrollbar {
    display: none;
  }
  .hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  
  /* Micro-interação de Zoom suave do DS */
  .img-zoom { transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); }
  .group:hover .img-zoom { transform: scale(1.05); }

  /* ======== MOBILE RESPONSIVENESS ======== */
  @media (max-width: 768px) {
    /* Regions Section - Complete Mobile Layout */
    .regions-section {
      padding: 32px 0;
    }

    .regions-section .container {
      padding: 0 16px;
    }

    /* Header - Compact stacked Layout */
    .regions-header {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 20px;
    }

    .regions-header h2 {
      font-size: 0.6rem;
      letter-spacing: 0.12em;
    }

    .regions-header h2 span {
      font-size: 1.5rem;
    }

    .regions-header p {
      font-size: 0.75rem;
      line-height: 1.5;
      margin-bottom: 8px;
    }

    .regions-header a {
      font-size: 0.6rem;
    }

    /* Carousel - Compact cards with 2:3 ratio */
    .regions-carousel {
      gap: 10px;
      padding-bottom: 8px;
      padding-right: 16px;
      margin-right: -16px;
      padding-left: 0;
      scroll-snap-type: x mandatory;
    }

    /* Cards in carousel - Much smaller with 2:3 aspect ratio */
    .region-card {
      min-width: 35vw;
      scroll-snap-align: start;
    }

    .region-card .aspect-\[2\/3\] {
      aspect-ratio: 2/3;
    }

    .region-card h3 {
      font-size: 0.75rem;
      margin-top: 6px;
    }

    .region-card .absolute {
      top: 6px;
      right: 6px;
    }

    .region-card .absolute span {
      font-size: 6px;
      padding: 2px 6px;
    }

    /* Navigation controls - Inline arrows like Section 2 */
    .carousel-controls {
      margin-top: 16px;
      justify-content: center;
    }

    .carousel-controls button {
      width: 36px;
      height: 36px;
      font-size: 0.9rem;
    }
  }

  /* Force mobile when .is-mobile class present */
  .is-mobile .regions-section {
    padding: 32px 0;
  }

  .is-mobile .regions-section .container {
    padding: 0 16px;
  }

  .is-mobile .regions-header {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 20px;
  }

  .is-mobile .regions-header h2 {
    font-size: 0.6rem;
    letter-spacing: 0.12em;
  }

  .is-mobile .regions-header h2 span {
    font-size: 1.5rem;
  }

  .is-mobile .regions-header p {
    font-size: 0.75rem;
    line-height: 1.5;
    margin-bottom: 8px;
  }

  .is-mobile .regions-header a {
    font-size: 0.6rem;
  }

  .is-mobile .regions-carousel {
    gap: 10px;
    padding-bottom: 8px;
    padding-right: 16px;
    margin-right: -16px;
    padding-left: 0;
    scroll-snap-type: x mandatory;
  }

  .is-mobile .region-card {
    min-width: 35vw;
    scroll-snap-align: start;
  }

  .is-mobile .region-card .aspect-\[2\/3\] {
    aspect-ratio: 2/3;
  }

  .is-mobile .region-card h3 {
    font-size: 0.75rem;
    margin-top: 6px;
  }

  .is-mobile .carousel-controls {
    margin-top: 16px;
    justify-content: center;
  }

  .is-mobile .carousel-controls button {
    width: 36px;
    height: 36px;
    font-size: 0.9rem;
  }
</style>