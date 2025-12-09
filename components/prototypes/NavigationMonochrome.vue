<template>
  <section class="nav-monochrome">
    
    <!-- BACKGROUNDS -->
    <div class="bg-container">
      <div class="bg-image active"></div>
      <img 
        src="https://images.unsplash.com/photo-1600596542815-2a4d9f6facb8?q=80&w=2069" 
        class="bg-image" 
        id="bg-buy" 
        alt="Comprar"
      >
      <img 
        src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=2053" 
        class="bg-image" 
        id="bg-sell" 
        alt="Vender"
      >
      <img 
        src="https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2069" 
        class="bg-image" 
        id="bg-broker" 
        alt="Corretor"
      >
    </div>

    <!-- NAVEGAÇÃO -->
    <div class="nav-section">
      <ul class="nav-list">
        
        <li 
          class="nav-item" 
          data-bg="bg-buy"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <div class="nav-content">
            <span class="nav-num">01</span>
            <a href="#" class="nav-link" @click.prevent="router.push('/prototipo/resultados?tab=new')">Quero Comprar</a>
          </div>
          <span class="arrow-icon">→</span>
        </li>

        <li 
          class="nav-item" 
          data-bg="bg-sell"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <div class="nav-content">
            <span class="nav-num">02</span>
            <a href="#" class="nav-link">Quero Vender</a>
          </div>
          <span class="arrow-icon">→</span>
        </li>

        <li 
          class="nav-item" 
          data-bg="bg-broker"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <div class="nav-content">
            <span class="nav-num">03</span>
            <a href="#" class="nav-link">Sou Corretor</a>
          </div>
          <span class="arrow-icon">→</span>
        </li>

      </ul>
    </div>

    <!-- UI FLUTUANTE -->
    <div 
      ref="infoCard" 
      class="floating-details" 
      :class="{ visible: cardVisible }"
      :style="{ left: cardPosition.x + 'px', top: cardPosition.y + 'px' }"
    >
      <span class="detail-label">Pilar Homes</span>
      <span class="detail-stat">{{ currentStat }}</span>
      <p class="detail-desc">{{ currentDesc }}</p>
    </div>

  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const router = useRouter()

const cardVisible = ref(false)
const currentStat = ref('')
const currentDesc = ref('')
const cardPosition = ref({ x: 0, y: 0 })
const infoCard = ref<HTMLElement | null>(null)

const navData = {
  'bg-buy': {
    stat: 'Portfólio Off-Market',
    desc: 'Acesso exclusivo a coleções arquitetônicas que você não encontra nos portais comuns.'
  },
  'bg-sell': {
    stat: 'R$ 3 Bilhões Negociados',
    desc: 'Estratégia global e discrição absoluta. Conectamos sua propriedade aos compradores certos.'
  },
  'bg-broker': {
    stat: 'Carreira de Elite',
    desc: 'Infraestrutura, tecnologia e leads qualificados para corretores de alta performance.'
  }
}

const handleMouseMove = (e: MouseEvent) => {
  const xOffset = 30
  const yOffset = -50
  
  let xPos = e.clientX + xOffset
  if (xPos + 320 > window.innerWidth) {
    xPos = e.clientX - 350
  }
  
  cardPosition.value = {
    x: xPos,
    y: e.clientY + yOffset
  }
}

const handleMouseEnter = (e: Event) => {
  const target = e.currentTarget as HTMLElement
  const bgId = target.getAttribute('data-bg') as string
  
  // Atualizar backgrounds
  const bgImages = document.querySelectorAll('.bg-image')
  bgImages.forEach(img => img.classList.remove('active'))
  document.getElementById(bgId)?.classList.add('active')
  
  // Atualizar card info
  const data = navData[bgId as keyof typeof navData]
  currentStat.value = data.stat
  currentDesc.value = data.desc
  cardVisible.value = true
}

const handleMouseLeave = () => {
  cardVisible.value = false
}

onMounted(() => {
  document.addEventListener('mousemove', handleMouseMove)
})

onUnmounted(() => {
  document.removeEventListener('mousemove', handleMouseMove)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Italiana&family=Manrope:wght@300;400;500&display=swap');

/* --- CONFIGURAÇÕES VISUAIS --- */
.nav-monochrome {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-color: #F4F4F4;
  overflow: hidden;
}

/* --- 1. BACKGROUND DINÂMICO --- */
.bg-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
  background-color: #F4F4F4;
}

.bg-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transform: scale(1.1);
  transition: opacity 0.8s ease, transform 1.5s ease;
  filter: grayscale(100%) contrast(105%);
}

.bg-image.active {
  opacity: 0.12;
  transform: scale(1);
}

/* --- 2. NAVEGAÇÃO CENTRAL --- */
.nav-section {
  position: relative;
  z-index: 10;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 10vw;
}

.nav-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 2vh;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.nav-item {
  position: relative;
  padding: 25px 0;
  border-bottom: 1px solid #DDDDDD;
  transition: border-color 0.4s;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-item:last-child {
  border-bottom: none;
}

.nav-item:hover {
  border-bottom-color: #121212;
}

.nav-content {
  display: flex;
  align-items: center;
  width: 100%;
}

.nav-num {
  font-family: 'Manrope', sans-serif;
  font-size: 0.9rem;
  color: #666666;
  margin-right: 30px;
  font-weight: 500;
  transition: color 0.3s;
}

.nav-link {
  font-family: 'Italiana', serif;
  font-size: 4.5vw;
  line-height: 1;
  color: #121212;
  text-decoration: none;
  text-transform: uppercase;
  transition: padding-left 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.3s;
  display: block;
  opacity: 0.6;
}

.nav-item:hover .nav-link {
  opacity: 1;
  padding-left: 20px;
}

.nav-item:hover .nav-num {
  color: #121212;
}

.arrow-icon {
  font-size: 1.5rem;
  opacity: 0;
  transform: translateX(-15px);
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  color: #121212;
}

.nav-item:hover .arrow-icon {
  opacity: 1;
  transform: translateX(0);
}

/* --- 3. TOOLTIP / CARD FLUTUANTE --- */
.floating-details {
  position: fixed;
  width: 300px;
  background: #ffffff;
  padding: 30px;
  pointer-events: none;
  z-index: 20;
  opacity: 0;
  transform: scale(0.9);
  transition: opacity 0.3s, transform 0.15s linear;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.floating-details.visible {
  opacity: 1;
  transform: scale(1);
}

.detail-label {
  display: block;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #888;
  margin-bottom: 15px;
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 8px;
}

.detail-stat {
  display: block;
  font-family: 'Italiana', serif;
  font-size: 1.6rem;
  line-height: 1.2;
  color: #121212;
  margin-bottom: 12px;
}

.detail-desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #666666;
}

/* Responsividade */
@media (max-width: 1024px) {
  .nav-link {
    font-size: 6vw;
  }
}

@media (max-width: 768px) {
  .floating-details {
    position: fixed;
    bottom: 20px;
    left: 20px;
    right: 20px;
    width: auto;
    top: auto !important;
    transform: none !important;
    opacity: 0;
    transition: opacity 0.3s;
  }

  .floating-details.visible {
    opacity: 1;
  }

  .nav-link {
    font-size: 8vw;
  }

  .nav-section {
    padding: 60px 5vw;
  }

  .nav-item:last-child {
    border-bottom: none;
  }
}
</style>
