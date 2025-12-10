export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const clarityId = config.public.clarityId as string

  if (clarityId) {
    try {
      // Inject Clarity script directly
      const script = document.createElement('script')
      script.type = 'text/javascript'
      script.innerHTML = `
        (function(c,l,a,r,i,t,y){
          c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
          t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
          y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", "${clarityId}");
      `
      document.head.appendChild(script)
      console.log('✅ Microsoft Clarity initialized with ID:', clarityId)
    } catch (error) {
      console.error('❌ Failed to initialize Microsoft Clarity:', error)
    }
  } else {
    console.warn('⚠️ Microsoft Clarity ID not configured')
  }
})
