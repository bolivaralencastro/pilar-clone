<template>
  <section class="horizontal-scroll-container" ref="sectionRef">
    <div class="sticky-wrapper">
      <div class="horizontal-track" ref="trackRef">
        
        <!-- SLIDE 1: Padrão (Texto Esq / Imagem Vertical Dir) -->
        <div class="editorial-slide slide-layout-1">
          <div class="slide-content">
            <div class="text-block">
              <span class="meta-tag">São Paulo — Jardins</span>
              <h2 class="display-title">Refúgio<br>Urbano</h2>
              <p class="desc-text">O equilíbrio perfeito entre a arquitetura brutalista e o conforto orgânico em 420m².</p>
              <button class="link-btn" @click="router.push('/prototipo/imovel?tab=new')">Explorar Imóvel</button>
            </div>
            <div class="image-block vertical">
              <img src="https://images.unsplash.com/photo-1600607686527-6fb886090705?q=80&w=2000&auto=format&fit=crop" alt="Jardins">
            </div>
          </div>
        </div>

        <!-- SLIDE 2: Invertido (Imagem Horizontal Esq / Texto Dir) -->
        <div class="editorial-slide slide-layout-2">
          <div class="slide-content">
            <div class="image-block horizontal">
              <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2000&auto=format&fit=crop" alt="Curitiba">
            </div>
            <div class="text-block align-right">
              <span class="meta-tag">Curitiba — Batel</span>
              <h2 class="display-title">Glass<br>House</h2>
              <p class="desc-text">Projetada ao redor da luz. Paredes de vidro integram o jardim ao living principal.</p>
              <button class="link-btn" @click="router.push('/prototipo/imovel?tab=new')">Explorar Imóvel</button>
            </div>
          </div>
        </div>

        <!-- SLIDE 3: Villa Toscana (Panorâmica Topo / Texto Baixo) -->
        <div class="editorial-slide slide-layout-3">
          <div class="slide-content">
            <div class="text-block align-bottom">
              <span class="meta-tag">Vila Nova — SP</span>
              <h2 class="display-title">Villa<br>Toscana</h2>
              <p class="desc-text">Acabamentos importados e design assinado. Um ícone de sofisticação.</p>
              <button class="link-btn" @click="router.push('/prototipo/imovel?tab=new')">Explorar Imóvel</button>
            </div>
            <div class="image-block panoramic">
              <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=2000&auto=format&fit=crop" alt="Villa Toscana">
            </div>
          </div>
        </div>

        <!-- SLIDE 4: Layout 1 Variação -->
        <div class="editorial-slide slide-layout-1">
          <div class="slide-content">
            <div class="text-block">
              <span class="meta-tag">Itaim Bibi — SP</span>
              <h2 class="display-title">Penthouse<br>Lumière</h2>
              <p class="desc-text">Vista panorâmica de 360° e terraço privativo com piscina de borda infinita.</p>
              <button class="link-btn" @click="router.push('/prototipo/imovel?tab=new')">Explorar Imóvel</button>
            </div>
            <div class="image-block vertical">
              <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2000&auto=format&fit=crop" alt="Penthouse">
            </div>
          </div>
        </div>

        <!-- Espaço final para respiro -->
        <div class="editorial-slide spacer"></div>

      </div>
      
      <!-- Barra de Progresso -->
      <div class="progress-bar-container">
        <div class="progress-fill" :style="{ width: `${progress * 100}%` }"></div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const sectionRef = ref<HTMLElement | null>(null)
const trackRef = ref<HTMLElement | null>(null)
const progress = ref(0)
let scrollTarget: HTMLElement | Window = window

const findScrollableParent = (el: HTMLElement | null): HTMLElement | null => {
  let node: HTMLElement | null = el
  while (node && node !== document.body) {
    const style = getComputedStyle(node)
    const isScrollable = /(auto|scroll)/.test(style.overflowY)
    if (isScrollable) return node
    node = node.parentElement
  }
  return null
}

const getOffsetTop = (el: HTMLElement, ancestor: HTMLElement | null) => {
  let offset = 0
  let node: HTMLElement | null = el
  while (node && node !== ancestor) {
    offset += node.offsetTop
    node = node.offsetParent as HTMLElement | null
  }
  return offset
}

const updateScroll = () => {
  if (!sectionRef.value || !trackRef.value) return

  const isWindow = scrollTarget === window
  const viewportHeight = isWindow
    ? window.innerHeight
    : (scrollTarget as HTMLElement).clientHeight

  const sectionOffset = isWindow
    ? sectionRef.value.getBoundingClientRect().top + window.scrollY
    : getOffsetTop(sectionRef.value, scrollTarget as HTMLElement)

  const currentScroll = isWindow
    ? window.scrollY
    : (scrollTarget as HTMLElement).scrollTop

  const scrolledDistance = currentScroll - sectionOffset
  const sectionHeight = sectionRef.value.offsetHeight
  const scrollableDistance = sectionHeight - viewportHeight

  let currentProgress = scrollableDistance > 0 ? scrolledDistance / scrollableDistance : 0
  if (currentProgress < 0) currentProgress = 0
  if (currentProgress > 1) currentProgress = 1

  progress.value = currentProgress

  const maxTranslate = trackRef.value.scrollWidth - (isWindow ? window.innerWidth : (scrollTarget as HTMLElement).clientWidth)
  if (maxTranslate <= 0) return
  const currentTranslate = maxTranslate * currentProgress

  trackRef.value.style.transform = `translateX(-${currentTranslate}px)`
}

onMounted(() => {
  // Suporta tanto scroll global quanto dentro do viewer (overflow auto)
  const found = findScrollableParent(sectionRef.value)
  if (found) {
    scrollTarget = found
    found.addEventListener('scroll', updateScroll, { passive: true })
  } else {
    scrollTarget = window
    window.addEventListener('scroll', updateScroll, { passive: true })
  }
  window.addEventListener('resize', updateScroll)
  updateScroll()
})

onUnmounted(() => {
  if (scrollTarget instanceof HTMLElement) {
    scrollTarget.removeEventListener('scroll', updateScroll)
  } else {
    window.removeEventListener('scroll', updateScroll)
  }
  window.removeEventListener('resize', updateScroll)
})
</script>

<style scoped>
/* Configurações da Section */
.horizontal-scroll-container {
  height: 350vh;
  position: relative;
  background-color: var(--surface-subtle, #F2F2F2);
  color: var(--text-primary, #1A1A1A);
}

.sticky-wrapper {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.horizontal-track {
  display: flex;
  height: 100%;
  width: max-content;
  will-change: transform;
}

/* --- SLIDES GERAIS --- */
.editorial-slide {
  width: 85vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  padding: 0 4vw;
  box-sizing: border-box;
}

.editorial-slide.spacer {
  width: 10vw;
}

.slide-content {
  width: 100%;
  max-width: 1400px;
  height: 80vh;
  position: relative;
}

/* --- TEXTOS --- */
.text-block {
  position: absolute;
  z-index: 2;
  max-width: 380px;
}

.meta-tag {
  display: inline-block;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--text-secondary, #666);
  margin-bottom: 1.5rem;
  border-bottom: 1px solid var(--border-subtle, #ccc);
  padding-bottom: 5px;
}

.display-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3rem, 5vw, 4.5rem);
  line-height: 0.95;
  font-weight: 300;
  margin: 0 0 1.5rem 0;
  color: var(--text-primary, #1A1A1A);
}

.desc-text {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary, #555);
  margin-bottom: 2rem;
}

.link-btn {
  text-decoration: none;
  color: var(--text-primary, #1A1A1A);
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 2px;
  border: none;
  border-bottom: 1px solid var(--text-primary, #1A1A1A);
  padding: 0 0 4px 0;
  background: transparent;
  cursor: pointer;
  transition: opacity 0.3s;
}

.link-btn:hover {
  opacity: 0.6;
}

/* --- IMAGENS --- */
.image-block {
  position: absolute;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.08);
  border-radius: 4px;
}

.image-block img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 1.2s cubic-bezier(0.2, 1, 0.3, 1);
  display: block;
}

.editorial-slide:hover .image-block img {
  transform: scale(1.05);
}

/* --- LAYOUTS ESPECÍFICOS --- */

/* LAYOUT 1: Texto Esq / Imagem Vertical Dir */
.slide-layout-1 .text-block {
  left: 0;
  top: 25%;
}

.slide-layout-1 .image-block.vertical {
  right: 0;
  top: 0;
  width: 60%;
  height: 90%;
}

/* LAYOUT 2: Imagem Horizontal Esq / Texto Dir */
.slide-layout-2 .image-block.horizontal {
  left: 0;
  top: 10%;
  width: 55%;
  height: 70%;
}

.slide-layout-2 .text-block.align-right {
  right: 5%;
  bottom: 25%;
  text-align: left;
}

/* LAYOUT 3: Panorâmica Topo / Texto Baixo */
.slide-layout-3 .image-block.panoramic {
  right: 0;
  top: 5%;
  width: 70%;
  height: 60%;
}

.slide-layout-3 .text-block.align-bottom {
  left: 5%;
  bottom: 10%;
}

/* Barra de Progresso */
.progress-bar-container {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: rgba(0, 0, 0, 0.05);
}

.progress-fill {
  height: 100%;
  background: var(--text-primary, #1A1A1A);
  transition: width 0.1s linear;
}

/* Responsivo */
@media (max-width: 768px) {
  .editorial-slide {
    width: 95vw;
    padding: 0 2vw;
  }

  .display-title {
    font-size: clamp(2rem, 8vw, 3rem);
  }

  .text-block {
    max-width: 280px;
  }

  .slide-layout-1 .image-block.vertical,
  .slide-layout-2 .image-block.horizontal,
  .slide-layout-3 .image-block.panoramic {
    width: 70%;
  }
}
</style>
