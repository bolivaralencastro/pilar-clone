<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-primary/10"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Comparador</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <!-- Title Section -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
          <div>
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Ferramentas</span>
            <h1 class="text-5xl font-light tracking-tighter text-text-primary">Comparar Imóveis</h1>
          </div>
          <div class="flex items-center gap-4">
            <span class="text-sm font-mono text-secondary tracking-widest uppercase">
              Selecionados: {{ store.count }}/4
            </span>
          </div>
        </div>

        <!-- Warning -->
        <div v-if="store.warning" class="mb-8 p-4 bg-action-primary/10 border border-action-primary/30 text-text-primary rounded-lg flex items-center justify-between">
          <span class="text-sm font-light">{{ store.warning }}</span>
          <button class="text-xs font-medium uppercase tracking-widest hover:text-action-primary transition-colors" @click="store.clearWarning()">ok</button>
        </div>

        <!-- Empty State -->
        <div v-if="store.count === 0" class="py-24 border border-dashed border-border-subtle rounded-lg text-center">
          <p class="text-xl font-light text-secondary mb-4">Nenhum imóvel selecionado</p>
          <NuxtLink to="/" class="btn-primary inline-flex">
            Explorar Imóveis
          </NuxtLink>
        </div>

        <!-- Grid -->
        <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8">
          <div v-for="item in store.items" :key="item.id" class="group relative bg-surface-card border rounded-lg border-border-subtle hover:border-action-primary/30 transition-all duration-500 hover:shadow-lg">
            <!-- Image Placeholder (if available in item, otherwise generic) -->
            <div class="aspect-[4/3] bg-surface-subtle relative overflow-hidden">
              <img v-if="item.image" :src="item.image" :alt="item.title" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div v-else class="w-full h-full flex items-center justify-center text-secondary/50 font-light">Sem Imagem</div>
              
              <button 
                class="absolute top-4 right-4 w-8 h-8 bg-surface-card/90 backdrop-blur flex items-center justify-center rounded-full text-primary hover:bg-mat-stone hover:text-surface-base transition-colors duration-300"
                @click="store.remove(item.id)"
                title="Remover"
              >
                ×
              </button>
            </div>

            <div class="p-6 space-y-6">
              <h2 class="text-xl font-light leading-tight min-h-[3.5rem] text-text-primary">{{ item.title }}</h2>
              
              <div class="space-y-4 pt-4 border-t border-border-subtle">
                <div class="flex justify-between items-baseline">
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Preço</span>
                  <span class="font-medium text-lg text-text-primary">{{ formatPrice(item.price) }}</span>
                </div>
                <div class="flex justify-between items-baseline">
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Área</span>
                  <span class="font-light text-text-primary">{{ item.area }} m²</span>
                </div>
                <div class="flex justify-between items-baseline">
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Quartos</span>
                  <span class="font-light text-text-primary">{{ item.bedrooms }}</span>
                </div>
                <div class="flex justify-between items-baseline">
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Banheiros</span>
                  <span class="font-light text-text-primary">{{ item.bathrooms }}</span>
                </div>
                <div class="flex justify-between items-baseline">
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Local</span>
                  <span class="font-light text-right truncate ml-4 text-text-primary">{{ item.region }}, {{ item.city }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useCompareStore } from '~~/stores/compare'
const store = useCompareStore()

function formatPrice(value?: number) {
  if (!value) return '—'
  return `R$ ${value.toLocaleString('pt-BR')}`
}
</script>


