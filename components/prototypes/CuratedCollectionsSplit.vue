<template>
  <section class="split-stage">
    
    <!-- PAINEL ESQUERDO -->
    <div class="left-panel">
      
      <!-- Título Misto (Top Left) -->
      <header class="top-brand">
        <span class="brand-sans">Coleção</span>
        <span class="brand-serif">Assinada</span>
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

    <!-- FOTO CENTRAL (CURADORA) - OVERLAY -->
    <div class="center-card">
      <div 
        v-for="curator in curators" 
        :key="`port-${curator.id}`"
        class="curator-portrait"
        :class="{ 'active': activeCurator === curator.id }"
        :style="{ backgroundImage: `url(${curator.portraitImage})` }"
      ></div>
      
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
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 3px;
  font-weight: 300;
  color: var(--text-primary);
}

.brand-serif {
  font-family: 'Playfair Display', serif;
  font-size: 4rem;
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
.center-card {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 280px;
  aspect-ratio: 2 / 3;
  z-index: 10;
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

/* Link CTA dentro do card central */
.card-cta {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  color: #fff;
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 2px;
  border: none;
  border-bottom: 1px solid #fff;
  padding-bottom: 3px;
  background: transparent;
  z-index: 2;
  mix-blend-mode: difference;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.3s 0.3s;
}

.center-card:hover .card-cta {
  opacity: 1;
}

/* --- RESPONSIVO --- */
@media (max-width: 1024px) {
  .split-stage {
    grid-template-columns: 1fr;
    grid-template-rows: auto 400px;
    height: auto;
    min-height: 100vh;
  }

  .left-panel {
    padding: 40px 20px;
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

  .center-card {
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    margin: -100px auto 40px auto;
    width: 200px;
  }

  .right-panel {
    height: 400px;
  }
}
</style>
