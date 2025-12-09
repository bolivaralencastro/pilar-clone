<template>
  <section class="split-stage">
    
    <!-- PAINEL ESQUERDO -->
    <div class="left-panel">
      
      <!-- Título Misto (Top Left) -->
      <header class="top-brand">
        <span class="brand-sans">Coleção</span>
        <span class="brand-serif font-playfair">Assinada</span>
      </header>

      <!-- Menu de Curadoras -->
      <nav class="curator-menu">
        <div 
          v-for="(curator, index) in curators" 
          :key="curator.id"
          class="menu-item"
          :class="{ 'active': activeCurator === curator.id }"
          @mouseenter="updateDisplay(curator.id)"
        >
          <h3 class="curator-name">{{ curator.name }}</h3>
          <span class="curator-role">{{ curator.role }}</span>
        </div>
      </nav>

      <!-- Descrição (Bottom Left) -->
      <footer class="bottom-desc">
        Imóveis com alma, selecionados por quem entende que morar é um ato de expressão pessoal. 
        Explore as visões singulares de nossas especialistas.
      </footer>

    </div>

    <!-- WRAPPER CENTRAL -->
    <div class="center-wrapper">
      <!-- FOTO CENTRAL (CURADORA) - OVERLAY -->
      <div class="center-card">
        <div 
          v-for="curator in curators" 
          :key="`port-${curator.id}`"
          class="curator-portrait"
          :class="{ 'active': activeCurator === curator.id }"
          :style="{ backgroundImage: `url(${curator.portraitImage})` }"
        ></div>
      </div>
      
      <button 
        class="card-cta"
        @click="router.push('/prototipo/resultados?tab=new')"
      >
        Ver Imóveis
      </button>
    </div>

    <!-- PAINEL DIREITO (IMÓVEL) -->
    <div class="right-panel">
      <div 
        v-for="curator in curators" 
        :key="`prop-${curator.id}`"
        class="property-bg"
        :class="{ 'active': activeCurator === curator.id }"
        :style="{ backgroundImage: `url(${curator.propertyImage})` }"
      ></div>
    </div>

  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const router = useRouter()

interface Curator {
  id: string
  name: string
  role: string
  portraitImage: string
  propertyImage: string
}

const curators = ref<Curator[]>([
  {
    id: 'lucila',
    name: 'Lucila Zahran',
    role: 'Casa de Valentina',
    portraitImage: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop',
    propertyImage: 'https://images.unsplash.com/photo-1600607686527-6fb886090705?q=80&w=2700&auto=format&fit=crop'
  },
  {
    id: 'fernanda',
    name: 'Fernanda Berendt',
    role: 'CASA+',
    portraitImage: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=600&auto=format&fit=crop',
    propertyImage: 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=2574&auto=format&fit=crop'
  },
  {
    id: 'nicole',
    name: 'Nicole Gomes',
    role: 'Lighting Designer',
    portraitImage: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?q=80&w=600&auto=format&fit=crop',
    propertyImage: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=2670&auto=format&fit=crop'
  }
])

const activeCurator = ref('lucila')

const updateDisplay = (curatorId: string) => {
  activeCurator.value = curatorId
}
</script>

<style scoped>
/* --- CONTAINER GERAL (SPLIT) --- */
.split-stage {
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr; /* 50% - 50% */
  position: relative;
}

/* --- LADO ESQUERDO (TEXTO) --- */
.left-panel {
  background-color: var(--surface-subtle);
  padding: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  z-index: 2;
}

/* Título Topo Esquerdo (Misto) */
.top-brand {
  position: absolute;
  top: 60px;
  left: 60px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.brand-sans {
  font-size: 16px;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-weight: 300;
  color: var(--text-primary);
}

.brand-serif {
  font-family: 'Playfair Display', serif;
  font-size: 3rem;
  line-height: 0.9;
  font-style: italic;
  font-weight: 300;
  color: var(--text-secondary);
  opacity: 0.6;
}

/* Lista de Nomes (Esquerda Centro) */
.curator-menu {
  display: flex;
  flex-direction: column;
  gap: 30px;
  margin-top: 40px;
}

.menu-item {
  cursor: pointer;
  opacity: 0.5;
  transition: all 0.4s ease;
  position: relative;
  width: fit-content;
  padding-left: 0;
  border-left: 3px solid transparent;
}

.menu-item:hover,
.menu-item.active {
  opacity: 1;
  padding-left: 20px;
  border-left-color: var(--text-primary);
}

.curator-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2rem;
  color: var(--text-primary);
  margin-bottom: 5px;
}

.curator-role {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-tertiary);
  display: block;
}

/* Descrição Rodapé Esquerdo */
.bottom-desc {
  position: absolute;
  bottom: 60px;
  left: 60px;
  max-width: 300px;
  font-size: 11px;
  font-style: italic;
  color: var(--text-secondary);
  line-height: 1.6;
  border-top: 1px solid var(--border-subtle);
  padding-top: 15px;
}

/* --- LADO DIREITO (IMÓVEL) --- */
.right-panel {
  position: relative;
  overflow: hidden;
  background-color: #000;
}

.property-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 0.8s ease-in-out, transform 1.2s ease;
  transform: scale(1.1);
}

.property-bg.active {
  opacity: 1;
  transform: scale(1);
}

/* --- ELEMENTO CENTRAL (CURADORA) --- */
.center-wrapper {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 15px;
}

.center-card {
  position: relative;
  width: 280px;
  aspect-ratio: 2 / 3;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2);
  background-color: var(--surface-offset);
  border-radius: 4px;
}

.curator-portrait {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 0.5s ease, transform 0.8s ease;
  transform: scale(1.1);
  filter: grayscale(20%);
}

.curator-portrait.active {
  opacity: 1;
  transform: scale(1);
}

/* Link CTA abaixo do card central */
.card-cta {
  color: var(--text-primary);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 2px;
  border: none;
  border-bottom: 1px solid var(--text-primary);
  padding-bottom: 3px;
  background: transparent;
  cursor: pointer;
  opacity: 1;
  transition: opacity 0.3s;
}

.card-cta:hover {
  opacity: 0.7;
}

/* --- RESPONSIVO --- */
@media (max-width: 1024px) {
  .split-stage {
    grid-template-columns: 1fr;
    grid-template-rows: auto 350px;
    height: auto;
    min-height: 100vh;
  }

  .left-panel {
    padding: 40px 24px;
    min-height: 50vh;
  }

  .top-brand {
    position: relative;
    top: 0;
    left: 0;
    margin-bottom: 40px;
  }

  .bottom-desc {
    position: relative;
    bottom: 0;
    left: 0;
    margin-top: 40px;
  }

  .center-wrapper {
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    margin: -100px auto 40px auto;
    width: 200px;
  }

  .right-panel {
    height: 350px;
  }
}

@media (max-width: 768px) {
  .split-stage {
    grid-template-columns: 1fr;
    grid-template-rows: auto auto 280px;
    min-height: auto;
    height: auto;
  }

  .left-panel {
    padding: 32px 20px 24px;
    min-height: auto;
    order: 1;
  }

  .top-brand {
    margin-bottom: 20px;
    flex-direction: row;
    align-items: baseline;
    gap: 8px;
  }

  .brand-sans {
    font-size: 0.65rem;
    letter-spacing: 0.12em;
  }

  .brand-serif {
    font-size: 1.5rem;
  }

  .curator-menu {
    gap: 16px;
    margin-top: 16px;
  }

  .curator-name {
    font-size: 1.25rem;
  }

  .curator-role {
    font-size: 8px;
  }

  .menu-item {
    padding-left: 0;
    border-left-width: 2px;
  }

  .menu-item:hover,
  .menu-item.active {
    padding-left: 10px;
  }

  .bottom-desc {
    margin-top: 20px;
    font-size: 0.7rem;
    max-width: 100%;
    padding-top: 12px;
    line-height: 1.5;
  }

  .center-wrapper {
    order: 2;
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    margin: 0 auto;
    padding: 20px 0;
    width: 140px;
    align-items: center;
  }

  .center-card {
    width: 140px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
  }

  .card-cta {
    font-size: 8px;
    letter-spacing: 1px;
  }

  .right-panel {
    order: 3;
    height: 280px;
  }
}

/* Force mobile with .is-mobile class */
.is-mobile .split-stage {
  grid-template-columns: 1fr;
  grid-template-rows: auto auto 280px;
  min-height: auto;
  height: auto;
}

.is-mobile .left-panel {
  padding: 32px 20px 24px;
  min-height: auto;
  order: 1;
}

.is-mobile .top-brand {
  position: relative;
  top: 0;
  left: 0;
  margin-bottom: 20px;
  flex-direction: row;
  align-items: baseline;
  gap: 8px;
}

.is-mobile .brand-sans {
  font-size: 0.65rem;
  letter-spacing: 0.12em;
}

.is-mobile .brand-serif {
  font-size: 1.5rem;
}

.is-mobile .curator-menu {
  gap: 16px;
  margin-top: 16px;
}

.is-mobile .curator-name {
  font-size: 1.25rem;
}

.is-mobile .curator-role {
  font-size: 8px;
}

.is-mobile .menu-item {
  border-left-width: 2px;
}

.is-mobile .menu-item:hover,
.is-mobile .menu-item.active {
  padding-left: 10px;
}

.is-mobile .bottom-desc {
  position: relative;
  bottom: 0;
  left: 0;
  margin-top: 20px;
  font-size: 0.7rem;
  max-width: 100%;
  padding-top: 12px;
  line-height: 1.5;
}

.is-mobile .center-wrapper {
  order: 2;
  position: relative;
  top: auto;
  left: auto;
  transform: none;
  margin: 0 auto;
  padding: 20px 0;
  width: 140px;
  align-items: center;
}

.is-mobile .center-card {
  width: 140px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
}

.is-mobile .card-cta {
  font-size: 8px;
  letter-spacing: 1px;
}

.is-mobile .right-panel {
  order: 3;
  height: 280px;
}
</style>
