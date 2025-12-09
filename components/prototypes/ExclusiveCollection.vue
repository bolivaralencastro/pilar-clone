<template>
  <section class="w-full h-screen bg-surface-base p-4">
    <div class="luxury-container w-full h-full bg-pure-white rounded text-rich-black shadow-[0_30px_60px_-15px_rgba(0,0,0,0.15)] grid grid-cols-1 lg:grid-cols-[60%_40%] relative overflow-hidden">
    
    <!-- LADO ESQUERDO: VISUAL (Move com o hover no container) -->
    <div class="visual-side relative h-full overflow-hidden grid grid-cols-2 md:grid-cols-3 gap-5 p-5 bg-porcelain">
      
      <!-- Coluna 1 -->
      <div class="marquee-col col-1 flex flex-col gap-5 will-change-transform">
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600566753086-00f18cf6b3ea?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <!-- Duplicatas -->
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600566753086-00f18cf6b3ea?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
      </div>

      <!-- Coluna 2 -->
      <div class="marquee-col col-2 flex flex-col gap-5 will-change-transform -mt-[50px]">
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1613545325278-f24b0cae1224?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600573472592-401b489a3cdc?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <!-- Duplicatas -->
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1613545325278-f24b0cae1224?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600573472592-401b489a3cdc?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
      </div>

      <!-- Coluna 3 -->
      <div class="marquee-col col-3 flex flex-col gap-5 will-change-transform hidden md:flex">
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600607687644-c7171b42498f?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1598228723793-52759bba239c?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <!-- Duplicatas -->
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1600607687644-c7171b42498f?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
        <div class="card w-full rounded-sm overflow-hidden relative aspect-[3/4] bg-[#eee]">
          <img src="https://images.unsplash.com/photo-1598228723793-52759bba239c?q=80&w=600&fit=crop" alt="Home" class="w-full h-full object-cover block grayscale-[10%] transition-all duration-600 hover:grayscale-0 hover:scale-105">
        </div>
      </div>

    </div>

    <!-- LADO DIREITO: CONTEÚDO -->
    <div class="content-side p-12 lg:p-20 flex flex-col justify-center relative z-10 bg-pure-white">
      <div class="label font-mono text-xs uppercase tracking-[2px] text-mat-stone mb-8 flex items-center gap-4 font-semibold before:content-[''] before:w-[30px] before:h-[1px] before:bg-rich-black">
        Pilar Homes Collection
      </div>
      <h1 class="font-serif text-[clamp(2.5rem,3.5vw,4.5rem)] leading-[1.1] font-medium mb-8 text-rich-black">
        Curadoria <br>
        <span class="italic text-mat-stone block">Exclusiva.</span>
      </h1>
      <p class="text-[1.05rem] leading-[1.7] text-mat-stone max-w-[380px] mb-12 font-normal">
        Explore nossa seleção privada de imóveis de alto padrão. Arquitetura icônica, localizações privilegiadas e design atemporal.
      </p>
      
      <a href="#" class="cta-btn inline-flex items-center justify-between w-full max-w-[200px] py-4 text-rich-black no-underline font-mono text-sm uppercase font-semibold border-t border-b border-[#E5E5E5] transition-all duration-300 hover:border-rich-black hover:px-2.5">
        Ver Imóveis
        <span>+</span>
      </a>
    </div>

    </div>
  </section>
</template>

<script setup lang="ts">
// Component logic if needed
</script>

<style scoped>
.visual-side {
  /* Máscara suave */
  mask-image: linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%);
}

.marquee-col {
  /* ESTADO PADRÃO: PAUSADO */
  animation-play-state: paused;
}

/* 
   A MÁGICA ACONTECE AQUI:
   Quando o mouse passa no CONTAINER (.luxury-container), 
   as colunas (.marquee-col) começam a rodar.
*/
.luxury-container:hover .marquee-col {
  animation-play-state: running;
}

/* --- ANIMAÇÕES --- */
@keyframes scrollUp {
  0% { transform: translateY(0); }
  100% { transform: translateY(-50%); }
}

@keyframes scrollDown {
  0% { transform: translateY(-50%); }
  100% { transform: translateY(0); }
}

.col-1 { animation: scrollUp 35s linear infinite; }
.col-2 { animation: scrollDown 45s linear infinite; }
.col-3 { animation: scrollUp 40s linear infinite; }

/* --- RESPONSIVO --- */
@media (max-width: 1024px) {
  /* No mobile, removemos a pausa, pois não há "hover" */
  .marquee-col {
    animation-play-state: running;
  }
}
</style>
