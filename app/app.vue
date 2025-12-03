<template>
  <div class="min-h-screen flex flex-col">
    <AppHeader :loading="loading" />
    <main class="flex-1">
      <NuxtPage />
    </main>
    <AppFooter />
  </div>
</template>

<script setup lang="ts">
const nuxtApp = useNuxtApp()
const loading = ref(false)

nuxtApp.hook('page:start', () => {
  loading.value = true
})

nuxtApp.hook('page:finish', () => {
  loading.value = false
})
</script>
