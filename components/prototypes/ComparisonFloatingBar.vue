<template>
  <Teleport to="body">
    <Transition 
      enter-active-class="transform transition duration-500 ease-out"
      enter-from-class="translate-y-full opacity-0"
      enter-to-class="translate-y-0 opacity-100"
      leave-active-class="transform transition duration-300 ease-in"
      leave-from-class="translate-y-0 opacity-100"
      leave-to-class="translate-y-full opacity-0"
    >
      <div 
        v-if="isVisible" 
        class="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 flex flex-col items-center gap-4 w-[90%] max-w-md md:w-auto"
      >
        <!-- The Bar - Glassmorphism Light -->
        <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 relative w-full md:w-auto justify-between md:justify-start">
          
          <!-- Botão Fechar (Cancelar Seleção) -->
          <button
            @click="$emit('cancel')"
            class="absolute -top-2 -right-2 w-6 h-6 bg-text-primary text-white rounded-full flex items-center justify-center shadow-md hover:bg-text-primary/90 hover:scale-110 transition-all duration-200 group"
            title="Cancelar seleção"
          >
            <i class="lni lni-close text-xs group-hover:rotate-90 transition-transform duration-200"></i>
          </button>

          <!-- Label -->
          <div class="flex flex-col">
            <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
            <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-tertiary mt-1">{{ selectedProperties.length }} Imóveis</span>
          </div>

          <!-- Avatars -->
          <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
            <!-- Empty Slots / Selected Items -->
            <template v-for="(item, index) in 4" :key="index">
              <div 
                v-if="selectedProperties[index]"
                class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative group cursor-pointer overflow-hidden bg-surface-offset shadow-md hover:shadow-lg transition-all hover:scale-105"
                @click="$emit('remove', selectedProperties[index].id)"
              >
                <img :src="selectedProperties[index].image" class="w-full h-full object-cover" />
                <!-- Hover Remove Icon -->
                <div class="absolute inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all">
                  <i class="lni lni-minus text-white text-xs md:text-lg"></i>
                </div>
              </div>
              <div 
                v-else
                class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-tertiary/40 shadow-inner"
              >
                <i class="lni lni-plus text-sm"></i>
              </div>
            </template>
          </div>

          <!-- Action Button -->
          <button 
            @click="$emit('compare')"
            class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium transition-all duration-300 ml-2 transform shadow-md"
            :class="selectedProperties.length >= 2 
              ? 'bg-text-primary text-white hover:bg-text-primary/90 hover:scale-105 hover:shadow-lg active:scale-95' 
              : 'bg-surface-offset/50 text-text-tertiary/50 cursor-not-allowed backdrop-blur-sm'"
            :disabled="selectedProperties.length < 2"
          >
            Comparar
          </button>

        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
interface Property {
  id: number
  image: string
  [key: string]: any
}

defineProps<{
  isVisible: boolean
  selectedProperties: Property[]
}>()

defineEmits<{
  (e: 'remove', id: number): void
  (e: 'compare'): void
  (e: 'cancel'): void
}>()
</script>
