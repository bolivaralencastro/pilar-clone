// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  // Ensure auto-import of components from the `components/` directory
  components: [
    {
      path: '~/../components',
      pathPrefix: false
    }
  ],

  vite: {
    server: {
      hmr: {
        port: 24689
      }
    }
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt'
  ],

  app: {
    head: {
      title: 'Pilar Clone - Busca de Imóveis',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Clone do sistema de busca de imóveis Pilar Homes' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;1,400&family=Roboto:wght@300;400;500;700&display=swap' },
        { rel: 'stylesheet', href: 'https://cdn.lineicons.com/4.0/lineicons.css' }
      ]
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },

  loading: {
    color: '#D5500B',
    height: '2px',
    throttle: 0,
    continuous: true
  },
  // https://nuxt.com/docs/api/configuration/nuxt-config
  // Trigger restart
  runtimeConfig: {
    pilarApiUrl: process.env.PILAR_API_URL || 'https://pilarhomes.com.br',
    public: {
      googleMapsKey: process.env.NUXT_PUBLIC_GOOGLE_MAPS_KEY || '',
      clarityId: process.env.NUXT_PUBLIC_CLARITY_ID || ''
    }
  },

  tailwindcss: {
    cssPath: './assets/css/main.css'
  }
})
