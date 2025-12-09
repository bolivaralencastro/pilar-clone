import Clarity from '@microsoft/clarity'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const clarityId = config.public.clarityId as string

  if (clarityId) {
    try {
      Clarity.init(clarityId)
      console.log('Microsoft Clarity initialized with ID:', clarityId)
    } catch (error) {
      console.error('Failed to initialize Microsoft Clarity:', error)
    }
  } else {
    console.warn('Microsoft Clarity ID not configured')
  }
})
