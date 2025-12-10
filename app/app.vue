<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
// Microsoft Clarity Analytics
useHead({
  script: [
    {
      innerHTML: `(function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      })(window, document, "clarity", "script", "ui6wgal6p5");`,
      type: 'text/javascript',
      tagPosition: 'head'
    }
  ]
})

const nuxtApp = useNuxtApp()
const router = useRouter()
const route = useRoute()
const loading = ref(false)

nuxtApp.hook('page:start', () => {
  loading.value = true
})

nuxtApp.hook('page:finish', () => {
  loading.value = false
})

// --- Keyboard Navigation & Shortcuts ---

const mainFlow = [
  '/briefing',
  '/programacao',
  '/pesquisa',
  '/estrategia',
  '/ideacao',
  '/ui-design',
  '/prototipo',
  '/entrega'
]

const subFlows: Record<string, string[]> = {
  '/pesquisa': [
    '/pesquisa',
    '/pesquisa/benchmarking',
    '/pesquisa/personas',
    '/pesquisa/jornadas'
  ]
}

const handleKeydown = (e: KeyboardEvent) => {
  // Ignore if typing in an input
  if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) return

  // Fullscreen (F)
  if (e.key.toLowerCase() === 'f') {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.error(`Error attempting to enable fullscreen: ${err.message}`)
      })
    } else {
      document.exitFullscreen()
    }
    return
  }

  const currentPath = route.path.replace(/\/$/, '') || '/'
  
  // 1. Identify current main section
  let mainIndex = mainFlow.indexOf(currentPath)
  let currentMain = currentPath
  
  console.log('Keydown:', e.key, 'CurrentPath:', currentPath, 'MainIndex:', mainIndex)

  // If not exact match, check if it's a sub-page (e.g. /pesquisa/personas is part of /pesquisa)
  if (mainIndex === -1) {
    const parent = mainFlow.find(p => currentPath.startsWith(p + '/'))
    if (parent) {
      mainIndex = mainFlow.indexOf(parent)
      currentMain = parent
    }
  }

  // 2. Main Navigation (Left/Right)
  if (e.key === 'ArrowRight') {
    if (mainIndex === -1) {
      // If on Home ('/'), go to first item
      if (currentPath === '/') router.push(mainFlow[0])
      return
    }
    if (mainIndex < mainFlow.length - 1) {
      router.push(mainFlow[mainIndex + 1])
    }
  } else if (e.key === 'ArrowLeft') {
    if (mainIndex === 0) {
      router.push('/')
      return
    }
    if (mainIndex > 0) {
      router.push(mainFlow[mainIndex - 1])
    }
  }

  // 3. Sub Navigation (Up/Down)
  if (currentMain && subFlows[currentMain]) {
    const subRoutes = subFlows[currentMain]
    const subIndex = subRoutes.indexOf(currentPath)
    
    if (e.key === 'ArrowDown') {
      if (subIndex !== -1 && subIndex < subRoutes.length - 1) {
        router.push(subRoutes[subIndex + 1])
      }
    } else if (e.key === 'ArrowUp') {
      if (subIndex > 0) {
        router.push(subRoutes[subIndex - 1])
      }
    }
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>
