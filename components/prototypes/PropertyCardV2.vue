<template>
  <div 
    class="group cursor-pointer flex flex-col relative p-16"
    @click="handleClick"
  >
    <!-- Selection Overlay/Border -->
    <div 
      v-if="selectionMode"
      class="absolute inset-0 z-20 rounded border-2 transition-colors pointer-events-none"
      :class="[
        isSelected 
          ? 'border-transparent bg-text-primary/5' 
          : isDisabled 
            ? 'border-transparent opacity-60' 
            : 'border-transparent hover:border-text-primary/30'
      ]"
    ></div>

    <!-- Image Container -->
    <div class="relative overflow-hidden rounded bg-surface-offset" :class="imageHeightClass">
      <img 
        v-if="!imageError"
        :src="property.image" 
        :alt="property.name" 
        class="w-full h-full object-cover img-zoom" 
        @error="imageError = true"
      />
      
      <!-- Empty State (Fallback) -->
      <div 
        v-else 
        class="w-full h-full flex flex-col items-center justify-center bg-surface-offset text-text-tertiary"
      >
        <i class="lni lni-image text-2xl mb-2 opacity-30"></i>
        <span class="text-[9px] uppercase tracking-widest opacity-40">Imagem indisponível</span>
      </div>

      <!-- Selection Checkbox (Visible in Selection Mode) -->
      <div 
        v-if="selectionMode"
        class="absolute top-3 left-3 z-30 transition-transform duration-200"
      >
        <div 
          class="w-6 h-6 rounded-full border flex items-center justify-center transition-colors shadow-sm"
          :class="[
            isSelected 
              ? 'bg-text-primary border-text-primary text-surface-base' 
              : isDisabled 
                ? 'bg-surface-offset/60 border-border-subtle text-transparent cursor-not-allowed opacity-50' 
                : 'bg-surface-card/90 border-border-subtle text-transparent hover:border-text-primary'
          ]"
        >
          <i class="lni lni-checkmark text-xs font-bold"></i>
        </div>
      </div>
      
      <!-- Hover Actions (aparecem apenas no hover e se não estiver em modo seleção) -->
      <div v-if="!selectionMode" class="absolute top-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
        <!-- Salvar -->
        <button 
          class="w-9 h-9 bg-surface-card/90 backdrop-blur-sm rounded-full flex items-center justify-center transition-colors"
          :class="isSaved ? 'text-red-500 hover:text-red-600' : 'text-text-secondary hover:text-text-primary hover:bg-surface-card'"
          title="Salvar"
          @click.stop
        >
          <i class="lni lni-heart text-base" :style="isSaved ? 'font-weight: 900;' : ''"></i>
        </button>
      </div>
    </div>
    
    <!-- Content -->
    <div class="pt-4">
      <!-- Meta Row -->
      <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
        <span class="text-text-tertiary">{{ property.neighborhood }}</span>
        <span class="text-text-tertiary/60">{{ property.ref }}</span>
      </div>
      
      <!-- Property Name -->
      <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
        {{ property.name }}
      </h3>
      
      <!-- Specs -->
      <p class="font-mono text-xs text-text-secondary mt-1">{{ property.specs }}</p>
      
      <!-- Footer -->
      <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
        <span class="font-bold text-sm text-text-primary">{{ property.price }}</span>
        
        <!-- Agent Avatar -->
        <div class="flex items-center gap-2">
          <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
            <span class="text-text-tertiary text-[9px] font-medium">
              {{ property.agent.name.charAt(0) }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Property {
  id: number
  name: string
  neighborhood: string
  ref: string
  price: string
  specs: string
  image: string
  agent: { name: string; company: string }
  layout: 'featured' | 'half' | 'third'
}

interface Props {
  property: Property
  imageHeight?: 'tall' | 'medium' | 'short'
  selectionMode?: boolean
  isSelected?: boolean
  isDisabled?: boolean
  isSaved?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  imageHeight: 'medium',
  selectionMode: false,
  isSelected: false,
  isDisabled: false,
  isSaved: false
})

const emit = defineEmits(['click', 'toggle-selection'])

const imageError = ref(false)

const handleClick = () => {
  if (props.selectionMode) {
    // Se está desabilitado e não está selecionado, não faz nada
    if (props.isDisabled && !props.isSelected) {
      return
    }
    emit('toggle-selection', props.property)
  } else {
    emit('click')
  }
}

// Map image height prop to CSS classes
const imageHeightClass = computed(() => {
  const heights: Record<string, string> = {
    tall: 'h-[320px] md:h-[400px]',
    medium: 'h-[280px] md:h-[340px]',
    short: 'h-[240px] md:h-[280px]'
  }
  return heights[props.imageHeight] || heights.medium
})
</script>

<style scoped>
/* Micro-interação de Zoom suave */
.img-zoom { 
  transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); 
}
.group:hover .img-zoom { 
  transform: scale(1.05); 
}
</style>
