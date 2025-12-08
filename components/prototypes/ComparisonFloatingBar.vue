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
        class="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 flex flex-col items-center gap-4"
      >
        <!-- The Bar -->
        <div class="bg-[#0f172b] text-white rounded-full shadow-2xl flex items-center py-2 pl-6 pr-3 gap-6 border border-white/10">
          
          <!-- Label -->
          <div class="flex flex-col">
            <span class="font-serif italic text-lg leading-none">Sua Seleção</span>
            <span class="text-[9px] uppercase tracking-widest text-gray-400 mt-1">{{ selectedProperties.length }} Imóveis</span>
          </div>

          <!-- Avatars -->
          <div class="flex items-center -space-x-3 pl-4">
            <!-- Empty Slots / Selected Items -->
            <template v-for="(item, index) in 3" :key="index">
              <div 
                v-if="selectedProperties[index]"
                class="w-12 h-12 rounded-full border-2 border-[#0f172b] relative group cursor-pointer overflow-hidden bg-surface-offset"
                @click="$emit('remove', selectedProperties[index].id)"
              >
                <img :src="selectedProperties[index].image" class="w-full h-full object-cover" />
                <!-- Hover Remove Icon -->
                <div class="absolute inset-0 bg-black/50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                  <i class="lni lni-minus text-white"></i>
                </div>
              </div>
              <div 
                v-else
                class="w-12 h-12 rounded-full border-2 border-[#0f172b] bg-white/5 flex items-center justify-center text-white/20"
              >
                <i class="lni lni-plus"></i>
              </div>
            </template>
          </div>

          <!-- Action Button -->
          <button 
            @click="$emit('compare')"
            class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium transition-all duration-300 ml-2 transform"
            :class="selectedProperties.length >= 2 ? 'bg-white text-[#0f172b] hover:bg-gray-100 hover:scale-105 hover:shadow-[0_0_15px_rgba(255,255,255,0.3)] active:scale-95' : 'bg-white/10 text-white/30 cursor-not-allowed'"
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
}>()
</script>
