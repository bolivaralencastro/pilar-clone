<script setup lang="ts">
interface Props {
  to: string
}

const props = defineProps<Props>()
</script>

<template>
  <NuxtLink
    :to="props.to"
    class="block bg-surface-card p-8 border rounded-lg border-subtle hover:border-strong transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-action-primary/40"
  >
    <slot />
  </NuxtLink>
</template>
