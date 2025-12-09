<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const translateX = ref(0)
const translateY = ref(0)

const handleScroll = () => {
  if (import.meta.client) {
    const scrollY = window.scrollY
    const windowHeight = window.innerHeight
    const documentHeight = document.documentElement.scrollHeight
    const maxScroll = documentHeight - windowHeight
    
    if (maxScroll > 0) {
      const scrollPercentage = scrollY / maxScroll
      // Movimento diagonal:
      // X: move para a direita (0 a 200px)
      // Y: move para cima (0 a -200px)
      translateX.value = scrollPercentage * 200
      translateY.value = scrollPercentage * -200
    }
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  // Trigger once on mount to set initial state
  handleScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <div 
    class="fixed bottom-0 left-0 opacity-[0.02] pointer-events-none z-0 origin-center will-change-transform"
    :style="{ transform: `scale(3) translate(${translateX}px, ${translateY}px)` }"
  >
    <svg width="380" height="328" viewBox="0 0 380 328" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M95 0L0 163.917L95 327.834H285L380 163.917L285 0H95ZM252.274 307.033L34.4494 181.755L283.277 38.6387L252.274 307.033Z" fill="black"/>
    </svg>
  </div>
</template>
