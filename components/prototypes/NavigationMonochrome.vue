<template>
  <section class="nav-monochrome" :class="{ 'is-mobile': isMobile }">
    
    <!-- BACKGROUNDS -->
    <div class="bg-container">
      <div class="bg-image"></div>
      <img 
        src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2069" 
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
    <div class="nav-section container mx-auto px-6">
      <ul class="nav-list">
        
        <li 
          class="nav-item" 
          data-bg="bg-buy"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <span class="nav-num">01</span>
          <a href="#" class="nav-link font-playfair" @click.prevent="router.push('/prototipo/resultados?tab=new')">Quero Comprar</a>
          <span class="arrow-icon">→</span>
          <!-- Mobile inline details -->
          <div class="mobile-details">
            <span class="detail-stat">{{ navData['bg-buy'].stat }}</span>
            <p class="detail-desc">{{ navData['bg-buy'].desc }}</p>
          </div>
        </li>

        <li 
          class="nav-item" 
          data-bg="bg-sell"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <span class="nav-num">02</span>
          <a href="#" class="nav-link font-playfair">Quero Vender</a>
          <span class="arrow-icon">→</span>
          <!-- Mobile inline details -->
          <div class="mobile-details">
            <span class="detail-stat">{{ navData['bg-sell'].stat }}</span>
            <p class="detail-desc">{{ navData['bg-sell'].desc }}</p>
          </div>
        </li>

        <li 
          class="nav-item" 
          data-bg="bg-broker"
          @mouseenter="handleMouseEnter"
          @mouseleave="handleMouseLeave"
        >
          <span class="nav-num">03</span>
          <a href="#" class="nav-link font-playfair">Sou Corretor</a>
          <span class="arrow-icon">→</span>
          <!-- Mobile inline details -->
          <div class="mobile-details">
            <span class="detail-stat">{{ navData['bg-broker'].stat }}</span>
            <p class="detail-desc">{{ navData['bg-broker'].desc }}</p>
          </div>
        </li>

      </ul>
    </div>

    <!-- UI FLUTUANTE (Desktop only) -->
    <Teleport to="body">
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
    </Teleport>

  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, inject, computed } from 'vue'

const router = useRouter()

// Inject forceMobile from parent
const injectedForceMobile = inject<{ value: boolean }>('forceMobile', { value: false })
const isMobile = computed(() => injectedForceMobile.value)

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
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500&display=swap');

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
  opacity: 0.06;
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
  padding-top: 80px;
  padding-bottom: 80px;
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
  border-bottom: 1px solid rgba(18, 18, 18, 0.1);
  transition: border-color 0.4s;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
}

.nav-item:last-child {
  border-bottom: none;
}

.nav-item:hover {
  border-bottom-color: #121212;
}

.nav-num {
  font-family: 'Manrope', sans-serif;
  font-size: 0.9rem;
  color: #666666;
  font-weight: 500;
  transition: color 0.3s;
  justify-self: start;
}

.nav-link {
  font-family: "Playfair Display", serif;
  font-size: 4.5vw;
  line-height: 1;
  color: #121212;
  text-decoration: none;
  text-transform: uppercase;
  transition: padding-left 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.3s;
  display: block;
  opacity: 0.6;
  justify-self: center;
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
  justify-self: end;
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
  z-index: 9999;
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
  font-family: "Playfair Display", serif;
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

/* Mobile inline details - hidden by default */
.mobile-details {
  display: none;
}

@media (max-width: 768px) {
  /* Hide floating tooltip on mobile */
  .floating-details {
    display: none !important;
  }

  /* Show inline details on mobile */
  .mobile-details {
    display: block;
    grid-column: 1 / -1;
    padding-top: 12px;
    padding-left: 28px;
    border-top: none;
  }

  .mobile-details .detail-stat {
    font-family: "Playfair Display", serif;
    font-size: 1rem;
    line-height: 1.3;
    color: #121212;
    margin-bottom: 6px;
    display: block;
  }

  .mobile-details .detail-desc {
    font-size: 0.8rem;
    line-height: 1.5;
    color: #666666;
    margin: 0;
  }

  .nav-section {
    padding-top: 48px;
    padding-bottom: 48px;
    min-height: auto;
    padding-left: 16px;
    padding-right: 16px;
  }

  .nav-item {
    padding: 20px 0;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
  }

  .nav-num {
    font-size: 0.7rem;
    min-width: 20px;
  }

  .nav-link {
    font-size: 1.5rem;
    justify-self: start;
    opacity: 1;
    flex: 1;
    text-transform: none;
  }

  .arrow-icon {
    font-size: 1rem;
    opacity: 0.4;
    transform: translateX(0);
  }

  .nav-item:last-child {
    border-bottom: none;
  }

  .nav-list {
    gap: 0;
  }
}

/* Support for .is-mobile class (forced mobile mode) */
.is-mobile .floating-details {
  display: none !important;
}

.is-mobile .mobile-details {
  display: block;
  grid-column: 1 / -1;
  padding-top: 12px;
  padding-left: 28px;
  border-top: none;
}

.is-mobile .mobile-details .detail-stat {
  font-family: "Playfair Display", serif;
  font-size: 1rem;
  line-height: 1.3;
  color: #121212;
  margin-bottom: 6px;
  display: block;
}

.is-mobile .mobile-details .detail-desc {
  font-size: 0.8rem;
  line-height: 1.5;
  color: #666666;
  margin: 0;
}

.is-mobile .nav-section {
  padding-top: 48px;
  padding-bottom: 48px;
  min-height: auto;
  padding-left: 16px;
  padding-right: 16px;
}

.is-mobile .nav-item {
  padding: 20px 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.is-mobile .nav-num {
  font-size: 0.7rem;
  min-width: 20px;
}

.is-mobile .nav-link {
  font-size: 1.5rem;
  justify-self: start;
  opacity: 1;
  flex: 1;
  text-transform: none;
}

.is-mobile .arrow-icon {
  font-size: 1rem;
  opacity: 0.4;
  transform: translateX(0);
}

.is-mobile .nav-item:last-child {
  border-bottom: none;
}

.is-mobile .nav-list {
  gap: 0;
}
</style>
