<script setup lang="ts">
import { ref, computed } from 'vue'
import AppIcon from './AppIcon.vue'

const props = defineProps<{
  src?: string
  alt?: string
}>()

const scale = ref(1)
const translateX = ref(0)
const translateY = ref(0)
const isDragging = ref(false)
const startX = ref(0)
const startY = ref(0)

const containerStyle = computed(() => ({
  transform: `translate(${translateX.value}px, ${translateY.value}px) scale(${scale.value})`,
  transition: isDragging.value ? 'none' : 'transform 0.1s ease-out',
  cursor: isDragging.value ? 'grabbing' : 'grab'
}))

const zoomIn = () => {
  scale.value = Math.min(scale.value + 0.2, 5)
}

const zoomOut = () => {
  scale.value = Math.max(scale.value - 0.2, 0.5)
}

const reset = () => {
  scale.value = 1
  translateX.value = 0
  translateY.value = 0
}

const onMouseDown = (e: MouseEvent) => {
  isDragging.value = true
  startX.value = e.clientX - translateX.value
  startY.value = e.clientY - translateY.value
}

const onMouseMove = (e: MouseEvent) => {
  if (!isDragging.value) return
  e.preventDefault()
  translateX.value = e.clientX - startX.value
  translateY.value = e.clientY - startY.value
}

const onMouseUp = () => {
  isDragging.value = false
}

const onWheel = (e: WheelEvent) => {
  if (e.ctrlKey) {
    e.preventDefault()
    const delta = e.deltaY > 0 ? -0.1 : 0.1
    scale.value = Math.min(Math.max(scale.value + delta, 0.5), 5)
  }
}
</script>

<template>
  <div class="relative w-full h-full overflow-hidden flex flex-col dotted-bg">
    <!-- Controls -->
    <div class="absolute bottom-6 right-6 z-10 flex flex-col gap-2 bg-white p-2 rounded-lg shadow-lg border border-subtle">
      <button @click="zoomIn" class="w-8 h-8 flex items-center justify-center rounded hover:bg-surface-card text-secondary hover:text-text-primary transition-colors" title="Zoom In">
        <AppIcon name="lni-plus" />
      </button>
      <button @click="zoomOut" class="w-8 h-8 flex items-center justify-center rounded hover:bg-surface-card text-secondary hover:text-text-primary transition-colors" title="Zoom Out">
        <AppIcon name="lni-minus" />
      </button>
      <div class="h-px w-full bg-subtle my-1"></div>
      <button @click="reset" class="w-8 h-8 flex items-center justify-center rounded hover:bg-surface-card text-secondary hover:text-text-primary transition-colors" title="Reset View">
        <AppIcon name="lni-reload" />
      </button>
    </div>

    <!-- Viewport -->
    <div 
      class="flex-1 w-full h-full flex items-center justify-center overflow-hidden"
      @mousedown="onMouseDown"
      @mousemove="onMouseMove"
      @mouseup="onMouseUp"
      @mouseleave="onMouseUp"
      @wheel="onWheel"
    >
      <div :style="containerStyle" class="origin-center flex items-center justify-center">
        <slot>
          <img 
            v-if="props.src"
            :src="props.src" 
            :alt="props.alt || 'Flowchart'" 
            class="max-w-none pointer-events-none select-none block" 
            draggable="false" 
            style="min-width: 800px; min-height: 600px;"
          />
        </slot>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dotted-bg {
  background-color: #FAFAFA;
  background-image: radial-gradient(#E4E4E7 1px, transparent 1px);
  background-size: 24px 24px;
}
</style>
