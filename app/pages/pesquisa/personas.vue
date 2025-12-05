<script setup lang="ts">
useSeoMeta({
  title: 'Personas - Pilar Homes',
  description: 'Arquétipos dos clientes ideais da Pilar Homes.'
})
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa/usuario" class="text-secondary hover:text-text-primary transition-colors">Usuário</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Personas</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <!-- Sidebar / Title -->
          <div class="lg:col-span-4">
            <div class="sticky top-32">
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Análise de Público</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Personas</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Identificação dos perfis comportamentais e necessidades dos usuários da plataforma Pilar Homes.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              <!-- Persona 1 -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <div class="flex items-center gap-4 mb-6">
                  <div class="w-16 h-16 bg-surface-subtle rounded-full flex items-center justify-center text-2xl">👨‍💼</div>
                  <div>
                    <h3 class="text-2xl font-light text-text-primary">O Investidor</h3>
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest">Perfil Analítico</span>
                  </div>
                </div>
                <p class="text-secondary font-light leading-relaxed mb-6">
                  Busca oportunidades de rentabilidade. Valoriza dados precisos, histórico de preços e potencial de valorização.
                </p>
                <ul class="space-y-2">
                  <li class="flex items-start gap-3 text-sm text-secondary">
                    <span class="text-action-primary mt-1">●</span>
                    Necessita de comparativos detalhados
                  </li>
                  <li class="flex items-start gap-3 text-sm text-secondary">
                    <span class="text-action-primary mt-1">●</span>
                    Prioriza localização e liquidez
                  </li>
                </ul>
              </div>

              <!-- Persona 2 -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <div class="flex items-center gap-4 mb-6">
                  <div class="w-16 h-16 bg-surface-subtle rounded-full flex items-center justify-center text-2xl">👩‍⚕️</div>
                  <div>
                    <h3 class="text-2xl font-light text-text-primary">A Compradora High-End</h3>
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest">Perfil Emocional/Estético</span>
                  </div>
                </div>
                <p class="text-secondary font-light leading-relaxed mb-6">
                  Busca exclusividade e qualidade de vida. Valoriza a apresentação visual, arquitetura e acabamentos.
                </p>
                <ul class="space-y-2">
                  <li class="flex items-start gap-3 text-sm text-secondary">
                    <span class="text-action-primary mt-1">●</span>
                    Necessita de fotos de alta qualidade e tours virtuais
                  </li>
                  <li class="flex items-start gap-3 text-sm text-secondary">
                    <span class="text-action-primary mt-1">●</span>
                    Prioriza design e conforto
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>




