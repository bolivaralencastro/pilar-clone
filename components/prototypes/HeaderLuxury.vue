<template>
  <header 
    class="w-full z-[200] py-6 bg-surface-base transition-all duration-300"
    :class="[ sticky ? 'sticky top-0' : 'relative' ]"
  >
    <div class="container mx-auto px-8 flex items-center justify-between">
      
      <!-- Left: Nav Links (Desktop) -->
      <nav v-if="!showMobileNav" class="hidden md:flex items-center gap-6 text-xs font-sans font-medium uppercase tracking-widest text-text-secondary">
        <button class="w-9 h-9 flex items-center justify-center hover:text-text-primary transition-colors" title="Buscar">
          <i class="lni lni-search text-base"></i>
        </button>
        <NuxtLink to="/prototipo/resultados?tab=new" class="hover:text-text-primary transition-colors">Comprar</NuxtLink>
        <a href="#" class="hover:text-text-primary transition-colors">Vender</a>
      </nav>

      <!-- Left: Mobile Menu Button (shown when forceMobile OR on small screens) -->
      <button 
        v-if="showMobileNav"
        class="w-10 h-10 flex items-center justify-center text-text-primary"
        @click="mobileMenuOpen = !mobileMenuOpen"
        :aria-expanded="mobileMenuOpen"
        aria-label="Menu"
      >
        <i v-if="!mobileMenuOpen" class="lni lni-menu text-xl"></i>
        <i v-else class="lni lni-close text-xl"></i>
      </button>

      <!-- Left: Mobile Menu Button (natural responsive) -->
      <button 
        v-if="!showMobileNav"
        class="md:hidden w-10 h-10 flex items-center justify-center text-text-primary"
        @click="mobileMenuOpen = !mobileMenuOpen"
        :aria-expanded="mobileMenuOpen"
        aria-label="Menu"
      >
        <i v-if="!mobileMenuOpen" class="lni lni-menu text-xl"></i>
        <i v-else class="lni lni-close text-xl"></i>
      </button>

      <!-- Right Actions -->
      <div class="flex items-center gap-8 text-xs font-sans font-medium uppercase tracking-widest text-text-secondary">
        <a v-if="!showMobileNav" href="#" class="hidden md:block hover:text-text-primary transition-colors">Magazine</a>
        <a href="#" class="hover:text-text-primary transition-colors">Entrar</a>
      </div>
    </div>

    <!-- Center: Logo -->
    <div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">
      <NuxtLink to="/prototipo/home?tab=new">
        <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-5 w-auto hover:opacity-80 transition-opacity cursor-pointer" />
      </NuxtLink>
    </div>

    <!-- Mobile Menu Overlay -->
    <Transition name="mobile-menu">
      <div 
        v-if="mobileMenuOpen" 
        class="fixed inset-0 top-[72px] bg-surface-base z-[199]"
        :class="{ 'md:hidden': !showMobileNav }"
      >
        <nav class="flex flex-col items-center justify-center h-full gap-8 text-center">
          <NuxtLink 
            to="/prototipo/resultados?tab=new" 
            class="text-2xl font-playfair text-text-primary hover:text-primary-600 transition-colors"
            @click="mobileMenuOpen = false"
          >
            Comprar
          </NuxtLink>
          <a 
            href="#" 
            class="text-2xl font-playfair text-text-primary hover:text-primary-600 transition-colors"
            @click="mobileMenuOpen = false"
          >
            Vender
          </a>
          <a 
            href="#" 
            class="text-2xl font-playfair text-text-primary hover:text-primary-600 transition-colors"
            @click="mobileMenuOpen = false"
          >
            Magazine
          </a>
          
          <div class="mt-8 pt-8 border-t border-border-subtle w-48">
            <button 
              class="flex items-center justify-center gap-3 w-full text-sm text-text-secondary uppercase tracking-widest"
              @click="mobileMenuOpen = false"
            >
              <i class="lni lni-search text-base"></i>
              Buscar
            </button>
          </div>
        </nav>
      </div>
    </Transition>
  </header>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// Header component - standalone luxury navigation
// Can be extended with props for variants (transparent, dark, etc.)
const props = defineProps<{
  sticky?: boolean
  forceMobile?: boolean
}>()

const mobileMenuOpen = ref(false)

// Show mobile menu when forceMobile is true
const showMobileNav = computed(() => props.forceMobile ?? false)
</script>

<style scoped>
/* Mobile menu transition */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
