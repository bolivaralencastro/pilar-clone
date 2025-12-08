<template>
  <div class="font-sans text-text-primary min-h-screen overflow-x-hidden">
    
    <!-- Main Content (Curtain Effect) -->
    <div class="relative z-10 bg-surface-base shadow-2xl will-change-transform">
      <!-- Header -->
      <HeaderLuxury />

    <!-- Hero Section -->
    <section class="h-[90vh] p-6 bg-surface-base">
      <div class="relative w-full h-full rounded-2xl overflow-hidden flex flex-col items-center justify-center bg-gray-900 text-white">
        <!-- Video Background -->
        <div class="absolute inset-0 z-0">
          <video 
            autoplay 
            muted 
            loop 
            playsinline 
            class="w-full h-full object-cover"
          >
            <source src="/video/hero-video.mp4" type="video/mp4">
          </video>
          <!-- Overlay for readability -->
          <div class="absolute inset-0 bg-gradient-to-b from-black/30 via-black/20 to-black/80"></div>
        </div>

        <div class="relative z-10 w-full max-w-4xl text-center space-y-8">
          <h1 class="text-4xl md:text-6xl font-light tracking-tight leading-tight">
            O endereço dos melhores endereços.<br>
            Agora em Curitiba.
          </h1>
        </div>
      </div>
    </section>

    <!-- Section: Selected Properties -->
    <section class="py-16 bg-surface-base text-text-primary">
      <div class="container mx-auto px-6">
        <div class="mb-10">
          <h2 class="text-3xl font-light mb-2 tracking-tight">Selecionados para você</h2>
          <p class="text-text-secondary">A partir de imóveis que chamaram sua atenção</p>
        </div>

        <!-- Horizontal Scroll Container -->
        <div class="flex gap-6 overflow-x-auto pb-8 snap-x hide-scrollbar">
          <div v-for="i in 4" :key="i" class="min-w-[300px] md:min-w-[400px] snap-center">
            <div class="bg-surface-card rounded-lg overflow-hidden h-full flex flex-col shadow-sm border border-border-subtle group cursor-pointer">
              <!-- Image Placeholder -->
              <div class="h-64 bg-surface-offset w-full relative">
                <div class="absolute top-4 right-4 w-8 h-8 bg-surface-card/90 backdrop-blur rounded-full flex items-center justify-center text-text-primary shadow-sm">★</div>
                <div class="absolute bottom-4 left-4 flex items-center gap-2">
                  <div class="w-8 h-8 bg-text-tertiary/20 rounded-full"></div>
                  <div class="text-xs">
                    <div class="w-16 h-2 bg-text-tertiary/30 mb-1 rounded"></div>
                    <div class="w-10 h-2 bg-text-tertiary/20 rounded"></div>
                  </div>
                </div>
              </div>
              <!-- Content -->
              <div class="p-4 space-y-2">
                <div class="flex justify-between items-center">
                  <div class="h-6 w-32 bg-text-tertiary/30 rounded"></div> <!-- Price -->
                  <div class="h-3 w-12 bg-text-tertiary/20 rounded"></div> <!-- Code -->
                </div>
                <div class="h-4 w-3/4 bg-text-tertiary/30 rounded"></div> <!-- Features -->
                <div class="h-3 w-1/2 bg-text-tertiary/20 rounded"></div> <!-- Location -->
              </div>
            </div>
          </div>
        </div>
        
        <div class="mt-8 flex justify-center">
             <button class="border border-border-strong px-6 py-3 rounded text-sm hover:bg-surface-subtle hover:text-text-primary transition-colors text-text-secondary">Ver todos</button>
        </div>
      </div>
    </section>

    <!-- Value Proposition -->
    <section class="py-16 bg-surface-subtle text-text-primary border-t border-border-subtle">
      <div class="container mx-auto px-6 grid md:grid-cols-3 gap-10">
        <div class="space-y-4">
          <h3 class="text-2xl font-light tracking-tight">Liderança no alto padrão</h3>
          <div class="h-px w-full bg-border-strong"></div>
          <p class="text-text-secondary leading-relaxed">Mais de R$ 3 bilhões negociados nos últimos 12 meses.</p>
        </div>
        <div class="space-y-4">
          <h3 class="text-2xl font-light tracking-tight">Atendimento sob medida</h3>
          <div class="h-px w-full bg-border-strong"></div>
          <p class="text-text-secondary leading-relaxed">Conexão direta com corretores especialistas nos melhores endereços.</p>
        </div>
        <div class="space-y-4">
          <h3 class="text-2xl font-light tracking-tight">O maior portfólio atualizado</h3>
          <div class="h-px w-full bg-border-strong"></div>
          <p class="text-text-secondary leading-relaxed">Mais opções e imóveis que você só encontra aqui.</p>
        </div>
      </div>
    </section>

    <!-- Navigation Cards (Tabs) -->
    <section class="py-12 bg-surface-base">
      <div class="container mx-auto px-6">
        <div class="flex gap-8 mb-8 border-b border-border-subtle pb-4 text-text-secondary">
          <button class="text-text-primary font-medium border-b-2 border-text-primary pb-4 -mb-4.5">Quero comprar</button>
          <button class="hover:text-text-primary transition-colors">Quero vender</button>
          <button class="hover:text-text-primary transition-colors">Sou corretor</button>
        </div>
        
        <div class="grid md:grid-cols-3 gap-6">
          <div v-for="(card, index) in navCards" :key="index" class="relative h-64 rounded-lg overflow-hidden group cursor-pointer bg-surface-card border border-border-subtle shadow-sm">
            <div class="absolute inset-0 bg-surface-offset group-hover:bg-surface-subtle transition-colors"></div>
            <div class="absolute bottom-0 left-0 p-6 w-full bg-gradient-to-t from-surface-card/90 to-transparent">
              <h3 class="text-xl text-text-primary font-medium flex items-center justify-between">
                {{ card.title }}
                <span class="text-lg">↗</span>
              </h3>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Regions -->
    <section class="py-20 md:pt-32 bg-surface-base text-text-primary overflow-hidden">
      <div class="container mx-auto px-6">
        
        <!-- 1. EDITORIAL HEADER (Grid Assimétrico) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-24 mb-16 items-end">
          
          <!-- Título (Lado Esquerdo) -->
          <div class="lg:col-span-6">
            <h2 class="text-5xl md:text-7xl font-light tracking-tighter leading-[1.1] text-text-primary">
              Nossas <br>
              <span class="text-text-secondary opacity-60 italic font-serif">Regiões</span>
            </h2>
          </div>

          <!-- Descrição (Lado Direito - Offset) -->
          <div class="lg:col-span-5 lg:col-start-8">
            <p class="text-sm md:text-base text-text-secondary font-light leading-relaxed mb-8">
              Descubra bairros onde a arquitetura encontra o estilo de vida. Uma curadoria de localizações perfeitas para quem busca exclusividade e bem-estar.
            </p>
            <a href="#" class="inline-block text-xs font-bold uppercase tracking-[0.2em] border-b border-text-primary pb-1 hover:text-primary-600 hover:border-primary-600 transition-colors">
              Explorar todas as regiões
            </a>
          </div>
        </div>

        <!-- 2. CARROSSEL DE REGIÕES -->
        <div class="relative w-full">
          
          <!-- Scroll Container -->
          <div class="flex gap-6 overflow-x-auto hide-scrollbar pb-20 pr-16 -mr-6 md:-mr-24 pl-1">
            
            <div v-for="(region, index) in regions" :key="index" class="group min-w-[85vw] md:min-w-[30vw] cursor-pointer">
              <div class="aspect-[2/3] w-full bg-surface-offset overflow-hidden rounded-sm mb-4 relative">
                <img :src="region.image" class="w-full h-full object-cover img-zoom opacity-90 group-hover:opacity-100 transition-opacity" alt="Region Image">
                 <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                    <span class="bg-surface-card/90 backdrop-blur px-3 py-1 text-[9px] uppercase tracking-widest font-bold text-text-primary">{{ region.label }}</span>
                 </div>
              </div>
              
              <div class="flex justify-between items-center px-1">
                 <h3 class="text-lg font-light text-text-primary tracking-tight group-hover:text-primary-600 transition-colors">{{ region.name }}</h3>
                 <div class="text-text-secondary opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-300">
                    <AppIcon name="arrow-right" size="18" />
                 </div>
              </div>
            </div>

          </div>

          <!-- BOTÃO DE NAVEGAÇÃO FLUTUANTE (Floating Nav) -->
          <div class="absolute top-1/2 -translate-y-1/2 right-4 md:right-8 z-20 pointer-events-none md:pointer-events-auto">
             <div class="flex items-center">
                <button class="w-16 h-16 md:w-20 md:h-20 bg-surface-card rounded-full shadow-2xl flex items-center justify-center hover:scale-105 transition-transform border border-border-subtle group cursor-pointer">
                   <div class="flex gap-4 text-text-primary">
                      <AppIcon name="arrow-right" size="24" />
                   </div>
                </button>
             </div>
          </div>

        </div>

      </div>
    </section>

    <!-- Exclusive Properties -->
    <section class="py-16 bg-surface-subtle text-text-primary">
      <div class="container mx-auto px-6">
        <div class="mb-10">
          <h2 class="text-3xl font-light tracking-tight">Exclusivos PilarHomes</h2>
          <p class="text-text-secondary mt-1">Imóveis únicos, listados apenas no PilarHomes.</p>
        </div>

        <div class="flex gap-6 overflow-x-auto pb-8 snap-x hide-scrollbar">
          <div v-for="i in 3" :key="i" class="min-w-[320px] md:min-w-[450px] snap-center">
            <div class="bg-surface-card border border-border-subtle rounded-lg overflow-hidden shadow-sm">
               
               <div class="h-64 bg-surface-offset relative"></div>
               
               <div class="p-5">
                 <div class="flex items-center gap-3 mb-4">
                    <div class="w-10 h-10 bg-text-tertiary/30 rounded-full"></div>
                    <div>
                      <div class="h-3 w-24 bg-text-tertiary/20 rounded mb-1"></div>
                      <div class="h-2 w-16 bg-text-tertiary/30 rounded"></div>
                    </div>
                 </div>
                 
                 <div class="space-y-2 border-t border-border-subtle pt-4">
                   <div class="flex justify-between">
                     <div class="h-6 w-28 bg-text-tertiary/20 rounded"></div>
                     <div class="h-3 w-10 bg-text-tertiary/30 rounded"></div>
                   </div>
                   <div class="h-3 w-full bg-text-tertiary/30 rounded"></div>
                   <div class="h-3 w-1/2 bg-text-tertiary/30 rounded"></div>
                 </div>
               </div>
            </div>
          </div>
        </div>
        
        <div class="mt-8 flex justify-between items-center">
             <button class="border border-border-strong text-text-primary px-6 py-3 rounded text-sm hover:bg-surface-subtle transition-colors">Ver todos os imóveis ↗</button>
             <div class="flex gap-2">
               <button class="w-10 h-10 border border-border-strong rounded-full flex items-center justify-center text-text-secondary hover:bg-surface-subtle transition-colors">←</button>
               <button class="w-10 h-10 border border-border-strong rounded-full flex items-center justify-center text-text-primary hover:bg-surface-subtle transition-colors">→</button>
             </div>
        </div>
      </div>
    </section>

    <!-- Curated Collections -->
    <section class="py-16 bg-surface-base">
      <div class="container mx-auto px-6">
         <div class="mb-10">
            <h2 class="text-3xl text-text-primary font-light mb-2 tracking-tight">Curadorias Assinadas</h2>
            <p class="text-text-secondary">Imóveis selecionados por referências do design, arquitetura e lifestyle.</p>
         </div>
         
         <div class="grid md:grid-cols-3 gap-6">
           <div v-for="curator in curators" :key="curator.name" class="bg-surface-card p-8 rounded-lg hover:bg-surface-subtle transition-colors cursor-pointer group border border-border-subtle shadow-sm">
             <div class="text-xs font-bold tracking-widest text-text-tertiary uppercase mb-6">Coleção</div>
             <div class="flex items-center gap-4 mb-6">
               <div class="w-16 h-16 rounded-full bg-surface-offset"></div>
               <h3 class="text-xl font-light text-text-primary">{{ curator.name }}</h3>
             </div>
             <p class="text-text-secondary mb-8 min-h-[80px]">{{ curator.desc }}</p>
             <div class="flex justify-between items-center text-sm font-medium text-text-primary">
               <span class="bg-surface-base px-2 py-1 rounded border border-border-subtle">São Paulo</span>
               <span class="group-hover:translate-x-1 transition-transform">↗</span>
             </div>
           </div>
         </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="py-16 bg-surface-base border-t border-border-subtle">
      <div class="container mx-auto px-6">
        <h2 class="text-3xl text-text-primary font-light mb-10 tracking-tight">O que dizem nossos clientes</h2>
        
        <div class="flex gap-6 overflow-x-auto pb-8 hide-scrollbar">
           <div v-for="i in 4" :key="i" class="min-w-[300px] md:min-w-[350px]">
             <div class="relative h-[300px] bg-surface-offset mb-6 rounded-lg overflow-hidden">
                <!-- Quote Badge -->
                <div class="absolute bottom-4 right-4 bg-surface-card p-4 shadow-lg max-w-[200px] rounded">
                   <div class="h-4 w-32 bg-text-primary/10 rounded"></div>
                </div>
             </div>
             <p class="text-xs text-text-tertiary mb-2 uppercase tracking-wide">Depoimento</p>
             <p class="text-text-secondary text-sm leading-relaxed mb-6">
               "Encontramos o imóvel dos sonhos com um atendimento impecável. Profissionalismo e dedicação definem a experiência."
             </p>
             <div class="flex items-center gap-3">
               <div class="w-10 h-10 rounded-full bg-surface-offset"></div>
               <div>
                 <div class="h-3 w-24 bg-text-primary/20 rounded mb-1"></div>
                 <div class="h-2 w-16 bg-text-tertiary/30 rounded"></div>
               </div>
             </div>
           </div>
        </div>
      </div>
    </section>

    <!-- Footer Luxury Component -->
    <FooterLuxury />
    </div>
  </div>
</template>

<script setup lang="ts">
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'

const navCards = ref([
  { title: 'Exclusivos PilarHomes' },
  { title: 'Coleções Compartilhadas' },
  { title: 'Off-Market' }
]);

const regions = ref([
  { name: 'São Paulo', image: 'https://images.unsplash.com/photo-1534234828563-02511c7590ac?q=80&w=2574&auto=format&fit=crop', label: 'Capital' },
  { name: 'Curitiba', image: 'https://images.unsplash.com/photo-1635352726330-22c662660ae3?q=80&w=2574&auto=format&fit=crop', label: 'Sul' },
  { name: 'Boa Vista', image: 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=2574&auto=format&fit=crop', label: 'Campo' },
  { name: 'Alphaville', image: 'https://images.unsplash.com/photo-1566958769312-82a9b2b2dcab?q=80&w=2572&auto=format&fit=crop', label: 'Grande SP' }
]);

const curators = ref([
  { name: 'Lucila Zahran Turqueto', desc: 'Conheça os imóveis favoritos de Lucila Zahran Turqueto, referência em decoração no mundo digital.' },
  { name: 'Fernanda Berendt', desc: 'Conheça os imóveis favoritos da criadora do @CASA+, referência em design de interiores.' },
  { name: 'Nicole Gomes', desc: 'Conheça os imóveis favoritos da colunista da revista Casa e Jardim.' }
]);
</script>

<style scoped>
  /* Custom scrollbar hiding for clean UI */
  .hide-scrollbar::-webkit-scrollbar {
    display: none;
  }
  .hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  
  /* Micro-interação de Zoom suave do DS */
  .img-zoom { transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); }
  .group:hover .img-zoom { transform: scale(1.05); }
</style>