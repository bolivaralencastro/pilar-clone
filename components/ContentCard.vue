<script setup lang="ts">
interface Props {
  variant?: 'default' | 'subtle' | 'highlight'
  padding?: 'sm' | 'md' | 'lg'
  shadow?: boolean
  scrollAnchor?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'default',
  padding: 'lg',
  shadow: false,
  scrollAnchor: false
})

const classes = computed(() => {
  const variants = {
    default: 'bg-surface-card border-subtle',
    subtle: 'bg-surface-subtle border-hairline',
    highlight: 'bg-surface-card border-strong border-l-4'
  }

  const paddings = {
    sm: 'p-6',
    md: 'p-8',
    lg: 'p-12'
  }

  return [
    'border rounded-lg',
    variants[props.variant],
    paddings[props.padding],
    props.shadow ? 'shadow-sm' : '',
    props.scrollAnchor ? 'scroll-mt-24' : ''
  ].filter(Boolean).join(' ')
})
</script>

<template>
  <div :class="classes">
    <slot />
  </div>
</template>
