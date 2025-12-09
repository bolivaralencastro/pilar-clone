<template>
  <div class="hero-scroll-reveal-container" :class="{ 'is-mobile': isMobile }">
    <!-- 1. CAMADA DE FUNDO (Texto Fixo) -->
    <section class="hero-text-section" ref="heroTextRef">
      <span class="hero-tag">SÃO PAULO • CURITIBA</span>
      <h1>Curadoria de imóveis<br>de alto padrão</h1>
      <p class="hero-desc">Atendimento personalizado e o maior portfólio de imóveis exclusivos em localização privilegiada.</p>
      
      <form class="hero-search" @submit.prevent="handleSearch">
        <input 
          type="text" 
          placeholder="Buscar por bairro, cidade..." 
          v-model="searchQuery"
        >
        <button type="submit">BUSCAR</button>
      </form>
    </section>

    <!-- 2. ESPAÇADOR INVISÍVEL (Define o tempo de leitura antes do scroll) -->
    <div class="scroll-spacer"></div>

    <!-- 3. CAMADA DE FRENTE (Container do Vídeo com animação Sticky) -->
    <div class="video-container-wrapper" ref="videoWrapperRef">
      <div class="video-sticky-stage">
        <div class="video-frame" ref="videoFrameRef">
          <video 
            autoplay 
            muted 
            loop 
            playsinline
            class="w-full h-full object-cover"
          >
            <source src="/video/hero-video.mp4" type="video/mp4">
          </video>
          
          <div class="video-overlay-text" ref="videoTextRef">
            <h3 style="font-family: 'Playfair Display'; font-size: 2rem;">Experience Living</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, inject, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const searchQuery = ref('')

// Inject forceMobile from parent
const injectedForceMobile = inject<{ value: boolean }>('forceMobile', { value: false })
const isMobile = computed(() => injectedForceMobile.value)

const heroTextRef = ref<HTMLElement | null>(null)
const videoFrameRef = ref<HTMLElement | null>(null)
const videoTextRef = ref<HTMLElement | null>(null)
const videoWrapperRef = ref<HTMLElement | null>(null)

let scrollParent: HTMLElement | Window = window

const handleSearch = () => {
  router.push({ path: '/prototipo/resultados', query: { tab: 'new', q: searchQuery.value } })
}

const getScrollParent = (node: HTMLElement | null): HTMLElement | Window => {
  if (!node) return window
  
  const style = getComputedStyle(node)
  const overflowY = style.overflowY
  // Simplificado: se tem overflow auto/scroll, é o container de scroll
  if (overflowY === 'auto' || overflowY === 'scroll') {
    return node
  }
  
  return getScrollParent(node.parentElement)
}

const handleScroll = () => {
  if (!videoFrameRef.value || !heroTextRef.value) return

  // Garante que pegamos o scroll correto
  const scrollY = scrollParent === window 
    ? window.scrollY 
    : (scrollParent as HTMLElement).scrollTop
    
  const viewportHeight = scrollParent === window 
    ? window.innerHeight 
    : (scrollParent as HTMLElement).clientHeight
  
  // --- CÁLCULOS ---
  const expansionThreshold = viewportHeight * 0.8
  let progress = Math.min(scrollY / expansionThreshold, 1)
  if (progress < 0) progress = 0

  // FASE 1: Expansão (60% -> 96%) - mantém margem e border radius
  let newSize = 60 + (36 * progress) // 60 + 36 = 96%
  // Border radius vai de 20px para 8px (mantém arredondamento)
  let newRadius = 20 - (12 * progress) // 20 -> 8px

  // Texto do fundo some suavemente
  heroTextRef.value.style.opacity = String(Math.max(0, 1 - (progress * 1.5)))
  heroTextRef.value.style.transform = `translateY(-${progress * 50}px) scale(${1 - (progress * 0.05)})`

  // FASE 2: Diminuição e Blur (Quando o usuário continua descendo para a próxima section)
  const shrinkStart = viewportHeight * 1.0
  
  if (scrollY > shrinkStart) {
    let shrinkProgress = (scrollY - shrinkStart) / (viewportHeight * 1.2)
    shrinkProgress = Math.min(shrinkProgress, 1)
    if(shrinkProgress < 0) shrinkProgress = 0

    // Diminui de 96% para 65% progressivamente
    let shrinkSize = 96 - (31 * shrinkProgress) // 96 -> 65%
    let shrinkHeight = 96 - (36 * shrinkProgress) // 96vh -> 60vh
    // Border radius aumenta de 8px para 16px
    let shrinkRadius = 8 + (8 * shrinkProgress) // 8 -> 16px
    // Blur aumenta progressivamente
    let blurAmount = shrinkProgress * 12
    // Brightness diminui
    let brightness = 1 - (shrinkProgress * 0.35)

    videoFrameRef.value.style.width = `${shrinkSize}%`
    videoFrameRef.value.style.height = `${shrinkHeight}vh`
    videoFrameRef.value.style.borderRadius = `${shrinkRadius}px`
    videoFrameRef.value.style.filter = `blur(${blurAmount}px) brightness(${brightness})`
    videoFrameRef.value.style.transform = `scale(1)`
    
    if (videoTextRef.value) {
      videoTextRef.value.style.opacity = String(shrinkProgress)
      videoTextRef.value.style.transform = `translateY(${20 - (shrinkProgress * 20)}px)`
    }
  } else {
    // Fase 1: Aplicar expansão normal
    videoFrameRef.value.style.width = `${newSize}%`
    videoFrameRef.value.style.height = `${newSize}vh`
    videoFrameRef.value.style.borderRadius = `${newRadius}px`
    videoFrameRef.value.style.filter = `blur(0px) brightness(1)`
    videoFrameRef.value.style.transform = `scale(1)`
    
    if (videoTextRef.value) videoTextRef.value.style.opacity = '0'
  }
}

onMounted(() => {
  // Encontra o container de scroll (pode ser a janela ou um elemento pai)
  scrollParent = getScrollParent(heroTextRef.value)
  
  // Adiciona listener no container encontrado
  scrollParent.addEventListener('scroll', handleScroll)
  // Adiciona listener na janela também para garantir (resize, etc)
  window.addEventListener('resize', handleScroll)
  
  // Força uma verificação inicial após um breve delay para garantir renderização
  setTimeout(handleScroll, 100)
})

onUnmounted(() => {
  scrollParent.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', handleScroll)
})
</script>

<style scoped>
/* Variáveis locais para garantir isolamento */
.hero-scroll-reveal-container {
  --hero-bg: #F7F7F7;
  --hero-text: #1A1A1A;
  --hero-secondary: #666;
  --hero-gold: #C5A059;
  position: relative;
  width: 100%;
}

/* TEXTO FIXO */
.hero-text-section {
  position: absolute; /* Mudado de fixed - não funciona bem dentro de container com overflow */
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  z-index: 0; /* Camada inferior */
  padding: 0 20px;
  padding-bottom: 25vh; /* Move o conteúdo para cima, evitando ficar atrás do vídeo */
  background-color: transparent;
  will-change: transform, opacity;
  pointer-events: none; /* CRÍTICO: permite scroll através deste elemento */
}

/* Reabilitar pointer-events para elementos interativos dentro */
.hero-text-section form,
.hero-text-section button,
.hero-text-section input {
  pointer-events: auto;
}

.hero-tag {
  font-family: 'Manrope', sans-serif;
  font-size: 0.7rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--hero-secondary);
  margin-bottom: 1.5rem;
  border-top: 1px solid #ddd;
  padding-top: 1rem;
}

.hero-text-section h1 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 6vw, 4.5rem);
  font-weight: 400;
  color: var(--hero-text);
  margin-bottom: 1.5rem;
  line-height: 1.1;
  max-width: 900px;
}

.hero-desc {
  font-family: 'Manrope', sans-serif;
  font-size: 1rem;
  color: var(--hero-secondary);
  max-width: 500px;
  line-height: 1.6;
  margin-bottom: 3rem;
}

/* BUSCA */
.hero-search {
  display: flex;
  background: white;
  padding: 8px;
  border-radius: 50px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  width: 100%;
  max-width: 450px;
  border: 1px solid #eee;
}
.hero-search input {
  flex: 1; border: none; outline: none; padding: 0 20px;
  font-family: 'Manrope', sans-serif; font-size: 0.95rem;
  color: var(--hero-text);
}
.hero-search button {
  background: var(--hero-text); color: white; border: none;
  padding: 10px 24px; border-radius: 30px; font-size: 0.75rem;
  font-weight: 700; letter-spacing: 1px; cursor: pointer; transition: 0.3s;
}
.hero-search button:hover { background: var(--hero-gold); }

/* ESPAÇADOR */
.scroll-spacer {
  height: 50vh; /* Altura reduzida para menos gap entre texto e vídeo */
  position: relative;
  z-index: 5;
  pointer-events: none; 
  background: transparent;
}

/* VÍDEO WRAPPER */
.video-container-wrapper {
  position: relative;
  z-index: 10; /* Superior ao texto */
  width: 100%;
  height: 200vh; /* Altura para controlar duração da animação */
  background: transparent;
}

.video-sticky-stage {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  pointer-events: none; /* Permite scroll através dele se necessário, mas aqui queremos que ele ocupe espaço */
}

.video-frame {
  width: 60%; /* Largura Inicial */
  height: 60vh; /* Altura Inicial */
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 20px 50px rgba(0,0,0,0.2);
  transform-origin: center center;
  will-change: width, height, transform, filter, border-radius;
}

.video-frame img, .video-frame video {
  width: 100%; height: 100%; object-fit: cover; display: block;
}

.video-overlay-text {
  position: absolute; bottom: 40px; left: 40px; color: white;
  opacity: 0; transform: translateY(20px); transition: 0.5s;
  z-index: 2;
}

/* ======== MOBILE RESPONSIVE ======== */
/* Applied via media query OR .is-mobile class from parent */
@media (max-width: 768px) {
  .hero-text-section {
    padding: 0 16px;
    justify-content: flex-start;
    padding-top: 15vh;
    padding-bottom: 35vh; /* Compensa o vídeo no mobile */
  }

  .hero-tag {
    font-size: 0.6rem;
    letter-spacing: 2px;
    margin-bottom: 1rem;
  }

  .hero-text-section h1 {
    font-size: clamp(1.75rem, 8vw, 2.5rem);
    margin-bottom: 1rem;
    max-width: 100%;
  }

  .hero-desc {
    font-size: 0.9rem;
    max-width: 100%;
    margin-bottom: 2rem;
    padding: 0 8px;
  }

  .hero-search {
    flex-direction: column;
    border-radius: 12px;
    padding: 12px;
    max-width: 100%;
    gap: 8px;
  }

  .hero-search input {
    padding: 12px 16px;
    font-size: 1rem;
    text-align: center;
  }

  .hero-search button {
    width: 100%;
    padding: 14px 24px;
    border-radius: 8px;
  }

  .scroll-spacer {
    height: 30vh;
  }

  .video-container-wrapper {
    height: 150vh;
  }

  .video-frame {
    width: 90%;
    height: 50vh;
    border-radius: 12px;
  }

  .video-overlay-text {
    bottom: 20px;
    left: 20px;
  }

  .video-overlay-text h3 {
    font-size: 1.25rem !important;
  }
}

/* Force mobile styles when .is-mobile class is present */
.is-mobile .hero-text-section {
  padding: 0 16px;
  justify-content: flex-start;
  padding-top: 25vh;
}

.is-mobile .hero-tag {
  font-size: 0.6rem;
  letter-spacing: 2px;
  margin-bottom: 1rem;
}

.is-mobile .hero-text-section h1 {
  font-size: 1.75rem;
  margin-bottom: 1rem;
  max-width: 100%;
}

.is-mobile .hero-desc {
  font-size: 0.9rem;
  max-width: 100%;
  margin-bottom: 2rem;
  padding: 0 8px;
}

.is-mobile .hero-search {
  flex-direction: column;
  border-radius: 12px;
  padding: 12px;
  max-width: 100%;
  gap: 8px;
}

.is-mobile .hero-search input {
  padding: 12px 16px;
  font-size: 1rem;
  text-align: center;
}

.is-mobile .hero-search button {
  width: 100%;
  padding: 14px 24px;
  border-radius: 8px;
}

.is-mobile .scroll-spacer {
  height: 30vh;
}

.is-mobile .video-container-wrapper {
  height: 150vh;
}

.is-mobile .video-frame {
  width: 90%;
  height: 50vh;
  border-radius: 12px;
}

.is-mobile .video-overlay-text {
  bottom: 20px;
  left: 20px;
}

.is-mobile .video-overlay-text h3 {
  font-size: 1.25rem !important;
}
</style>
