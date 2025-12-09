<template>
  <footer class="bg-[#121212] text-[#F9F9F9] font-sans flex flex-col justify-between pb-10">
    
    <!-- 1. SEO & REGIONS (Horizontal Accordion) -->
    <div class="w-full border-t border-white/10 border-b border-white/10 px-6 md:px-16">
      
      <!-- Header Line - Always visible at top -->
      <div class="flex flex-wrap items-center justify-center gap-8 md:gap-12 py-8 border-b border-white/10">
        <div v-for="(group, groupIndex) in seoGroups" :key="groupIndex" class="flex flex-wrap items-center gap-3 md:gap-6">
          <!-- Label -->
          <span class="text-xs uppercase tracking-[0.2em] font-light text-white/40 whitespace-nowrap">
            {{ group.label }}
          </span>

          <!-- Tabs -->
          <div class="flex items-center gap-4 md:gap-6">
            <button 
              v-for="(tab, tabIndex) in group.tabs" 
              :key="tabIndex"
              @click="toggleTab(groupIndex, tabIndex)"
              class="flex items-center gap-2 text-xs uppercase tracking-[0.2em] transition-colors duration-300 focus:outline-none group whitespace-nowrap"
              :class="isTabActive(groupIndex, tabIndex) ? 'text-white font-medium' : 'text-white/50 hover:text-white font-normal'"
            >
              <span>{{ tab.name }}</span>
              <!-- Icon -->
              <span 
                class="text-lg leading-none transform transition-transform duration-300" 
                :class="isTabActive(groupIndex, tabIndex) ? 'text-white' : 'text-white/30 group-hover:text-white'"
              >
                {{ isTabActive(groupIndex, tabIndex) ? '×' : '+' }}
              </span>
            </button>
          </div>
        </div>
      </div>

      <!-- Content Area - Opens below the header line -->
      <div 
        class="overflow-hidden transition-all duration-500 ease-in-out"
        :style="{ maxHeight: activeState ? '800px' : '0px', opacity: activeState ? '1' : '0' }"
      >
        <div v-if="activeState" class="grid grid-cols-1 md:grid-cols-4 gap-y-8 gap-x-8 py-12 animate-fade-in">
          <div v-for="(contentGroup, i) in getActiveTabContent(activeState.group)" :key="i" class="space-y-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-white/40">{{ contentGroup.subtitle }}</h4>
            <div class="flex flex-col gap-2">
              <a 
                v-for="(link, j) in contentGroup.items" 
                :key="j" 
                href="#" 
                class="text-sm text-gray-400 hover:text-white transition-colors hover:translate-x-1 duration-300 block"
              >
                {{ link }}
              </a>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- 2. MAIN FOOTER CONTENT -->
    <div class="flex-grow flex flex-col items-center justify-center py-24 px-6 md:px-16 space-y-16">
      
      <!-- Navigation Grid -->
      <div class="w-full grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-8 max-w-[1400px] mx-auto">
        
        <!-- Coluna 1 -->
        <div class="space-y-6">
          <h4 class="text-xs font-bold uppercase tracking-widest text-white/50 mb-8">A Maison</h4>
          <ul class="space-y-3 text-sm font-light">
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Sobre a Pilar</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Carreiras & Parceiros</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Conheça a Rede</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Editorial & Blog</a></li>
          </ul>
        </div>

        <!-- Coluna 2 -->
        <div class="space-y-6">
          <h4 class="text-xs font-bold uppercase tracking-widest text-white/50 mb-8">Serviços</h4>
          <ul class="space-y-3 text-sm font-light">
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Comprar Imóvel</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Vender Imóvel</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Private Broker</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Avaliação de Patrimônio</a></li>
          </ul>
        </div>

        <!-- Coluna 3 -->
        <div class="space-y-6">
          <h4 class="text-xs font-bold uppercase tracking-widest text-white/50 mb-8">Legal</h4>
          <ul class="space-y-3 text-sm font-light">
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Termos de Uso</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Política de Privacidade</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">Cookies</a></li>
            <li><a href="#" class="hover:underline decoration-white/30 underline-offset-4">CRECI 39836-J</a></li>
          </ul>
        </div>

        <!-- Coluna 4: Newsletter & Social -->
        <div class="space-y-8">
          <h4 class="text-xs font-bold uppercase tracking-widest text-white/50 mb-4">Newsletter</h4>
          <div class="relative group max-w-xs">
            <input 
              type="email" 
              placeholder="Cadastre seu e-mail" 
              class="w-full bg-transparent border-b border-white/30 py-2 text-sm focus:outline-none focus:border-white transition-colors text-white placeholder-white/30"
            >
            <button class="absolute right-0 bottom-2 text-xs uppercase tracking-widest hover:text-gray-300 text-white/70">
              Assinar
            </button>
          </div>
          
          <div class="pt-4 flex gap-6">
             <a href="#" class="text-white/60 hover:text-white transition-colors text-xs tracking-widest">INSTAGRAM</a>
             <a href="#" class="text-white/60 hover:text-white transition-colors text-xs tracking-widest">LINKEDIN</a>
          </div>
        </div>

      </div>

      <!-- LOGO (Estilo Chanel/LV - Grande destaque) -->
      <div class="w-full flex justify-center border-t border-white/10 pt-16">
        <img 
          src="/images/logo-pilar.svg" 
          alt="Pilar Homes" 
          class="h-8 md:h-14 w-auto brightness-0 invert opacity-90 hover:opacity-100 transition-opacity duration-500" 
        />
      </div>

    </div>

    <!-- 3. BOTTOM BAR -->
    <div class="w-full px-6 md:px-16 flex flex-col md:flex-row justify-between items-center text-[10px] uppercase tracking-widest text-white/30 pt-8 border-t border-white/5">
      <div class="flex items-center gap-4 mb-4 md:mb-0">
        <span class="hover:text-white cursor-pointer transition-colors">Brasil - Português</span>
        <span class="w-px h-3 bg-white/20"></span>
        <span>R. Amauri, 255 - Jd. Europa</span>
      </div>
      <div>
        © 2025 Pilar Homes. All rights reserved.
      </div>
    </div>

  </footer>
</template>

<script setup lang="ts">
// --- Estado do Accordion ---
const activeState = ref<{ group: number, tab: number } | null>(null);

const toggleTab = (groupIndex: number, tabIndex: number) => {
  if (activeState.value && activeState.value.group === groupIndex && activeState.value.tab === tabIndex) {
    activeState.value = null; // Close if clicking active
  } else {
    activeState.value = { group: groupIndex, tab: tabIndex }; // Open new
  }
};

const isTabActive = (groupIndex: number, tabIndex: number) => {
  return activeState.value?.group === groupIndex && activeState.value?.tab === tabIndex;
};

const isGroupActive = (groupIndex: number) => {
  return activeState.value?.group === groupIndex;
};

const getActiveTabContent = (groupIndex: number) => {
  if (!activeState.value || activeState.value.group !== groupIndex) return [];
  return seoGroups.value[groupIndex].tabs[activeState.value.tab].groups;
};

// --- Dados Mockados (SEO Links) ---
const seoGroups = ref([
  {
    label: 'Imóvel por Bairro',
    tabs: [
      {
        name: 'São Paulo',
        groups: [
          {
            subtitle: 'Apartamentos por bairro',
            items: ['Apartamentos em Moema', 'Apartamentos em Cidade Jardim', 'Apartamentos em Perdizes', 'Apartamentos em Vila Mariana', 'Apartamentos em Higienópolis']
          },
          {
            subtitle: 'Casas por bairro',
            items: ['Casas em Morumbi', 'Casas em Cidade Jardim', 'Casas em Alto da Boa Vista', 'Casas em Vila Mariana', 'Casas em Vila Madalena']
          },
          {
            subtitle: 'Coberturas por bairro',
            items: ['Coberturas em Vila Madalena', 'Coberturas em Vila Olímpia', 'Coberturas em Vila Mariana', 'Coberturas em Alto da Boa Vista', 'Coberturas em Moema']
          },
          {
            subtitle: 'Casas de condomínio por bairro',
            items: ['Casas de condomínio em Alto da Boa Vista', 'Casas de condomínio em Morumbi', 'Casas de condomínio em Jardim Guedala', 'Casas de condomínio em Brooklin', 'Casas de condomínio em Campo Belo']
          }
        ]
      },
      {
        name: 'Curitiba',
        groups: [
          {
            subtitle: 'Apartamentos por bairro',
            items: ['Apartamentos em Batel', 'Apartamentos em Água Verde', 'Apartamentos em Ecoville', 'Apartamentos em Bigorrilho', 'Apartamentos em Mossunguê']
          },
          {
            subtitle: 'Casas de condomínio por bairro',
            items: ['Casas de condomínio em Campo Comprido', 'Casas de condomínio em Santa Felicidade', 'Casas de condomínio em São Braz', 'Casas de condomínio em Uberaba', 'Casas de condomínio em Santa Cândida']
          },
          {
            subtitle: 'Casas por bairro',
            items: ['Casas em Santa Felicidade', 'Casas em Ecoville', 'Casas em Centro', 'Casas em Vista Alegre', 'Casas em Mercês']
          },
          {
            subtitle: 'Coberturas por bairro',
            items: ['Coberturas em Água Verde', 'Coberturas em Batel', 'Coberturas em Bigorrilho', 'Coberturas em Ecoville', 'Coberturas em Juvevê']
          }
        ]
      }
    ]
  },
  {
    label: 'Imóvel por Endereço e Ponto de interesse',
    tabs: [
      {
        name: 'São Paulo',
        groups: [
          {
            subtitle: 'Imóveis próximos a ruas',
            items: ['Rua Haddock Lobo', 'Rua Bela Cintra', 'Avenida Juriti', 'Rua Joaquim Antunes', 'Rua Tucumã']
          },
          {
            subtitle: 'Apartamentos próximos às ruas',
            items: ['Apartamentos em Rua Oscar Freire', 'Apartamentos em Rua Haddock Lobo', 'Apartamentos em Rua Bela Cintra', 'Apartamentos em Rua Pernambuco', 'Apartamentos em Rua Venezuela']
          },
          {
            subtitle: 'Casas próximas às ruas',
            items: ['Casas em Rua Estados Unidos', 'Casas em Rua Tabapuã', 'Casas em Rua Pernambuco', 'Casas em Rua Curitiba', 'Casas em Rua Sergipe']
          },
          {
            subtitle: 'Imóveis próximos a pontos de interesse',
            items: ['Imóveis próximos à Praça Pereira Coutinho', 'Imóveis próximos ao Parque do Ibirapuera', 'Imóveis próximos ao Clube Athletico Paulistano', 'Imóveis próximos ao Parque do Povo', 'Imóveis próximos ao Parque Villa-Lobos']
          }
        ]
      },
      {
        name: 'Curitiba',
        groups: [
          {
            subtitle: 'Imóveis próximos a ruas',
            items: ['Rua Brigadeiro Franco', 'Rua Prof. Pedro Viriato Parigot de Souza', 'Av. Visconde de Guarapuava', 'Rua Dep. Heitor Alencar Furtado', 'Rua José Izidoro Biazetto']
          },
          {
            subtitle: 'Apartamentos próximos às ruas',
            items: ['Apartamentos em Rua Prof. Pedro Viriato Parigot de Souza', 'Apartamentos em Rua Guilherme Pugsley', 'Apartamentos em Rua José Izidoro Biazetto', 'Apartamentos em Rua Martim Afonso', 'Apartamentos em Rua Mariano Torres']
          },
          {
            subtitle: 'Casas de condomínio próximas às ruas',
            items: ['Casas de condomínio em Rua Luiz Tramontin', 'Casas de condomínio em Rua Luiz Zilli', 'Casas de condomínio em Rua Hermenegildo Luca', 'Casas de condomínio em Rua José Benedito Cottolengo', 'Casas de condomínio em Rua Tobias de Macedo Júnior']
          },
          {
            subtitle: 'Imóveis próximos a pontos de interesse',
            items: ['Imóveis próximos ao Jardim Botânico', 'Imóveis próximos ao Parque Barigui', 'Imóveis próximos ao Parque Tanguá', 'Imóveis próximos ao Parque Tingui', 'Imóveis próximos ao Pátio Batel']
          }
        ]
      }
    ]
  }
]);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&display=swap');

.font-serif {
  font-family: 'Playfair Display', serif;
}

.font-sans {
  font-family: 'Inter', sans-serif;
}

/* Transições suaves extras */
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>