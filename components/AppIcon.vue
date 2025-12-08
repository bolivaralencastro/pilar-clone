<script setup lang="ts">
const props = defineProps<{
  name: string
}>()

const computedClass = computed(() => {
  if (props.name && props.name.includes('lni ')) {
    return props.name
  }
  return `lni ${props.name}`
})
</script>

<template>
  <i :class="computedClass"></i>
</template>
