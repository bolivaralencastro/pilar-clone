<script setup lang="ts">
import ContentCard from './ContentCard.vue'

interface Props {
  id?: string
  title?: string
  padding?: 'sm' | 'md' | 'lg'
  shadow?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  padding: 'lg',
  shadow: true
})
</script>

<template>
  <section :id="id">
    <ContentCard :padding="padding" :shadow="shadow" :scroll-anchor="true">
      <header v-if="title" class="mb-6">
        <h2 class="text-2xl font-light text-text-primary">{{ title }}</h2>
      </header>
      <slot />
    </ContentCard>
  </section>
</template>
