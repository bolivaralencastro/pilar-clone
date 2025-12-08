<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import mermaid from 'mermaid'

const props = defineProps<{
  code: string
}>()

const containerRef = ref<HTMLElement | null>(null)
const svgContent = ref('')

const renderChart = async () => {
  if (!props.code) return
  
  try {
    mermaid.initialize({ 
      startOnLoad: false,
      theme: 'base',
      themeVariables: {
        primaryColor: '#f1faee',
        primaryTextColor: '#1d3557',
        primaryBorderColor: '#1d3557',
        lineColor: '#1d3557',
        secondaryColor: '#cdb4db',
        tertiaryColor: '#fff',
        fontFamily: 'Inter, sans-serif'
      }
    })
    
    const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`
    const { svg } = await mermaid.render(id, props.code)
    svgContent.value = svg
  } catch (error) {
    console.error('Mermaid rendering failed:', error)
    svgContent.value = '<div class="text-red-500 p-4">Erro ao renderizar fluxograma</div>'
  }
}

onMounted(() => {
  renderChart()
})

watch(() => props.code, () => {
  renderChart()
})
</script>

<template>
  <div ref="containerRef" class="mermaid-container" v-html="svgContent"></div>
</template>

<style>
.mermaid-container svg {
  max-width: none !important;
  height: auto;
}
</style>
