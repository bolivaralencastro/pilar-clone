<template>
  <section class="w-full min-h-screen bg-surface-subtle pt-16 md:pt-20 pb-3 md:pb-4 flex flex-col">
    <div class="container mx-auto px-6 flex-1 flex flex-col">
    
    <!-- Título da Seção -->
    <div class="text-center mb-12">
      <h2 class="text-sm md:text-base font-light text-text-primary mb-2 uppercase tracking-[0.2em]">
        O que dizem <br>
        <span class="text-5xl md:text-6xl font-playfair italic text-text-secondary opacity-60 normal-case">nossos clientes</span>
      </h2>
    </div>
    
    <!-- Citação (Topo) -->
    <div class="flex-grow flex items-center justify-center max-w-4xl mx-auto text-center pb-8">
      <h2 
        class="font-playfair text-3xl md:text-4xl font-light italic leading-tight text-text-primary transition-all duration-500 ease-out relative"
        :class="{ 'opacity-100 translate-y-0': quoteVisible, 'opacity-0 translate-y-4': !quoteVisible }"
      >
        <span class="text-5xl md:text-6xl opacity-30 absolute -top-4 -left-8">“</span>
        {{ activeQuote }}
        <span class="text-5xl md:text-6xl opacity-30 absolute -bottom-8 -right-8">”</span>
      </h2>
    </div>

    <!-- Grid de Clientes (Baixo) - Largura total com cards pequenos distribuídos -->
    <div class="w-full flex justify-between items-end mt-auto">
        
        <div 
          v-for="(client, index) in clients" 
          :key="index"
          class="cursor-pointer flex flex-col gap-1.5 opacity-100 transition-all duration-400 ease-out w-32 md:w-40"
          :class="{ 
            'scale-110': activeIndex === index,
            'scale-100': activeIndex !== index
          }"
          @mouseenter="setTestimonial(index)"
        >
          <!-- Nome (Sans Serif - Menor) -->
          <h3 
            class="font-sans text-[9px] uppercase tracking-wide text-text-primary font-medium origin-left transition-all duration-400"
            :class="{ 'scale-110 font-semibold': activeIndex === index }"
          >
            {{ client.name }}
          </h3>
          
          <!-- Foto (Menor) -->
          <div class="w-full aspect-square overflow-hidden rounded relative" style="border-radius: 4px;">
            <img 
              :src="client.photo" 
              :alt="client.name"
              class="w-full h-full object-cover transition-all duration-500 ease-out grayscale"
              :class="{ 'grayscale-0 scale-105': activeIndex === index }"
            />
          </div>

          <!-- Footer (Info + Avatares - Compacto) -->
          <div class="flex justify-between items-end pt-1.5">
            <!-- Info Esquerda -->
            <div class="flex flex-col gap-0">
              <span class="text-[6px] uppercase text-text-tertiary tracking-widest">Atendimento</span>
              <span class="text-[9px] font-semibold text-text-primary">{{ client.broker }}</span>
              <span class="text-[8px] text-text-secondary">{{ client.agency }}</span>
            </div>

            <!-- Avatares Direita (Menores) -->
            <div class="flex items-center gap-0.5">
              <img 
                :src="client.brokerAvatar" 
                :alt="client.broker"
                class="w-4 h-4 rounded-full object-cover bg-surface-offset"
              />
              <div class="w-4 h-4 rounded-full bg-text-primary text-surface-base text-[6px] flex items-center justify-center font-bold">
                {{ client.agencyLogo }}
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Client {
  name: string
  photo: string
  broker: string
  agency: string
  brokerAvatar: string
  agencyLogo: string
  quote: string
}

const clients = ref<Client[]>([
  {
    name: 'Marina Sanvicente',
    photo: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop',
    broker: 'Renata Castro',
    agency: 'Oásis Urbanos',
    brokerAvatar: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=100&auto=format&fit=crop',
    agencyLogo: 'OU',
    quote: 'Com a ajuda da Renata, encontrei a cobertura dos meus sonhos. Foi tudo feito com leveza e sensibilidade única.'
  },
  {
    name: 'Silvia Berger',
    photo: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=600&auto=format&fit=crop',
    broker: 'Sabrina Lapyda',
    agency: 'Mosaic Homes',
    brokerAvatar: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=100&auto=format&fit=crop',
    agencyLogo: 'MH',
    quote: 'Sabrina mudou minha visão sobre corretores. Com foco e feedback constante, ela vendeu meu apartamento em tempo recorde.'
  },
  {
    name: 'Horácio Ferreira',
    photo: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=600&auto=format&fit=crop',
    broker: 'André Sarubbi',
    agency: 'Open Imóveis',
    brokerAvatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=100&auto=format&fit=crop',
    agencyLogo: 'OP',
    quote: 'Trabalhar com a Open Imóveis foi a melhor escolha! Profissionalismo e transparência para fechar um ótimo negócio.'
  },
  {
    name: 'Adriana Ribarolli',
    photo: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=600&auto=format&fit=crop',
    broker: 'Eduardo Pontes',
    agency: 'Pilar Exclusive',
    brokerAvatar: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=100&auto=format&fit=crop',
    agencyLogo: 'PE',
    quote: 'O Eduardo é um verdadeiro especialista na Vila Nova Conceição. Objetivo, dedicado e com conhecimento jurídico impecável.'
  }
])

const activeIndex = ref(0)
const activeQuote = ref(clients.value[0].quote)
const quoteVisible = ref(true)

const setTestimonial = (index: number) => {
  if (index === activeIndex.value) return
  
  activeIndex.value = index
  quoteVisible.value = false
  
  setTimeout(() => {
    activeQuote.value = clients.value[index].quote
    quoteVisible.value = true
  }, 300)
}
</script>

<style scoped>
/* Transições suaves customizadas */
.duration-400 {
  transition-duration: 400ms;
}

/* ======== MOBILE RESPONSIVENESS ======== */
@media (max-width: 768px) {
  /* Mobile: sempre colorido */
  .grayscale {
    filter: grayscale(0%);
  }

  section.w-full.min-h-screen {
    min-height: auto;
    padding: 40px 0 24px;
  }

  .container {
    padding-left: 20px;
    padding-right: 20px;
  }

  /* Título ajustado */
  .text-center.mb-12 {
    margin-bottom: 20px;
  }

  .text-center.mb-12 h2 {
    font-size: 0.7rem;
  }

  .text-center.mb-12 h2 span {
    font-size: 1.75rem;
  }

  /* Quote container */
  .flex-grow.flex.items-center {
    padding: 20px 0;
    min-height: auto;
  }

  .font-playfair.text-3xl {
    font-size: 1.1rem;
    padding: 0 24px;
    line-height: 1.5;
  }

  .font-playfair.text-3xl span.absolute {
    display: none;
  }

  /* Client cards - horizontal scroll */
  .w-full.flex.justify-between {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    gap: 12px;
    padding-bottom: 12px;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    justify-content: flex-start;
  }

  .w-full.flex.justify-between::-webkit-scrollbar {
    display: none;
  }

  /* Individual client card */
  .cursor-pointer.flex.flex-col {
    min-width: 120px;
    width: 120px;
    flex-shrink: 0;
    scroll-snap-align: start;
  }

  /* Client name */
  .font-sans.text-\[9px\] {
    font-size: 7px;
  }

  /* Photo container */
  .w-full.aspect-square {
    border-radius: 4px;
  }

  /* Footer info text */
  .text-\[6px\] {
    font-size: 5px;
  }

  .text-\[9px\] {
    font-size: 7px;
  }

  .text-\[8px\] {
    font-size: 6px;
  }

  /* Avatars */
  .w-4.h-4 {
    width: 10px;
    height: 10px;
  }

  .w-32.md\:w-40 {
    width: 120px;
  }
}

/* Force mobile with .is-mobile class */
.is-mobile .grayscale {
  filter: grayscale(0%);
}

.is-mobile section.w-full.min-h-screen {
  min-height: auto;
  padding: 40px 0 24px;
}

.is-mobile .container {
  padding-left: 20px;
  padding-right: 20px;
}

.is-mobile .text-center.mb-12 {
  margin-bottom: 20px;
}

.is-mobile .flex-grow.flex.items-center {
  padding: 20px 0;
  min-height: auto;
}

.is-mobile .font-playfair.text-3xl {
  font-size: 1.1rem;
  padding: 0 24px;
  line-height: 1.5;
}

.is-mobile .font-playfair.text-3xl span.absolute {
  display: none;
}

.is-mobile .w-full.flex.justify-between {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  gap: 12px;
  padding-bottom: 12px;
  -webkit-overflow-scrolling: touch;
  scroll-snap-type: x mandatory;
  justify-content: flex-start;
}

.is-mobile .w-full.flex.justify-between::-webkit-scrollbar {
  display: none;
}

.is-mobile .cursor-pointer.flex.flex-col {
  min-width: 120px;
  width: 120px;
  flex-shrink: 0;
  scroll-snap-align: start;
}

.is-mobile .w-4.h-4 {
  width: 10px;
  height: 10px;
}
</style>
