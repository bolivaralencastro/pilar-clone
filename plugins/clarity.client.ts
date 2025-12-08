import { init } from '@microsoft/clarity'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const clarityId = config.public.clarityId as string

  if (clarityId) {
    try {
      init(clarityId)
      console.log('Microsoft Clarity initialized')
    } catch (error) {
      console.error('Failed to initialize Microsoft Clarity:', error)
    }
  }
})
