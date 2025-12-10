<script setup lang="ts">
useSeoMeta({
  title: 'Benchmarking Global - Pilar Homes',
  description: 'Análise de referências globais em luxo e design.'
})

interface Competitor {
  name: string
  segment: string
  country: string
  flag: string
  url: string
  image: string
  summary: string
  strengths: string[]
  opportunities: string[]
}

interface Segment {
  name: string
  icon: string
  competitors: Competitor[]
}

const segments: Segment[] = [
  {
    name: 'Real Estate',
    icon: '',
    competitors: [
      {
        name: 'Douglas Elliman',
        segment: 'Real Estate',
        country: 'EUA',
        flag: '🇺🇸',
        url: 'https://www.elliman.com',
        image: '/images/Logos/Douglas-Elliman-logo.jpg',
        summary: 'Uma das maiores redes dos EUA em imóveis premium, forte em NY, Miami e LA.',
        strengths: ['Conteúdo editorial forte', 'Navegação clean', 'Fotografia impecável'],
        opportunities: ['Filtros pouco avançados', 'Experiência mobile']
      },
      {
        name: 'The Agency',
        segment: 'Real Estate',
        country: 'EUA',
        flag: '🇺🇸',
        url: 'https://www.theagencyre.com',
        image: '/images/Logos/The-Agency-logo.png',
        summary: 'Marca de luxo com storytelling aspiracional e produção audiovisual de altíssimo nível.',
        strengths: ['Branding excepcional', 'Vídeos high-end', 'Experiência inspiracional'],
        opportunities: ['Menos dados estruturados', 'Foco na emoção vs função']
      },
      {
        name: 'Knight Frank',
        segment: 'Real Estate',
        country: 'Reino Unido',
        flag: '🇬🇧',
        url: 'https://www.knightfrank.co.uk',
        image: '/images/Logos/Knight-Frank-logo.png',
        summary: 'Potência global em imóveis premium e ultra-prime.',
        strengths: ['Relatórios de mercado impecáveis', 'Organização exemplar'],
        opportunities: ['Design mais tradicional', 'Pode parecer "frio"']
      }
    ]
  },
  {
    name: 'Moda & Luxo',
    icon: '',
    competitors: [
      {
        name: 'Hermès',
        segment: 'Moda',
        country: 'França',
        flag: '🇫🇷',
        url: 'https://www.hermes.com',
        image: '/images/Logos/Hermes-logo.png',
        summary: 'Referência absoluta em luxo atemporal, artesania e exclusividade.',
        strengths: ['Design minimalista', 'Storytelling rico', 'Fotografia impecável'],
        opportunities: ['E-commerce limitado propositalmente']
      },
      {
        name: 'Loro Piana',
        segment: 'Moda',
        country: 'Itália',
        flag: '🇮🇹',
        url: 'https://www.loropiana.com',
        image: '/images/Logos/Loro-Piana-logo.png',
        summary: 'Luxo discreto e qualidade suprema em tecidos nobres.',
        strengths: ['Elegância sutil', 'Foco em materiais', 'UX refinada'],
        opportunities: ['Navegação pode ser mais fluida']
      }
    ]
  },
  {
    name: 'Automotivo',
    icon: '',
    competitors: [
      {
        name: 'Rolls-Royce',
        segment: 'Automotivo',
        country: 'Reino Unido',
        flag: '🇬🇧',
        url: 'https://www.rolls-roycemotorcars.com',
        image: '/images/Logos/Rolls-Royce-logo.png',
        summary: 'Epítome do luxo automotivo com experiência digital imersiva.',
        strengths: ['Experiência imersiva', 'Configurador 3D', 'Branding majestoso'],
        opportunities: ['Carregamento pesado em conexões lentas']
      },
      {
        name: 'Bentley',
        segment: 'Automotivo',
        country: 'Reino Unido',
        flag: '🇬🇧',
        url: 'https://www.bentleymotors.com',
        image: '/images/Logos/Bentley-Motors-logo.png',
        summary: 'Luxo britânico com forte ênfase em personalização.',
        strengths: ['Configurador detalhado', 'Conteúdo editorial', 'Navegação clara'],
        opportunities: ['Design pode ser mais ousado']
      }
    ]
  },
  {
    name: 'Hotelaria & Turismo',
    icon: '',
    competitors: [
      {
        name: 'Aman Resorts',
        segment: 'Hotelaria',
        country: 'Global',
        flag: '🌍',
        url: 'https://www.aman.com',
        image: '/images/Logos/Aman-Resorts-logo.png',
        summary: 'Referência em hospitalidade de ultra-luxo e design minimalista.',
        strengths: ['Fotografia excepcional', 'Minimalismo', 'Atmosfera zen'],
        opportunities: ['Informações práticas poderiam ser mais acessíveis']
      },
      {
        name: 'Four Seasons',
        segment: 'Hotelaria',
        country: 'Canadá',
        flag: '🇨🇦',
        url: 'https://www.fourseasons.com',
        image: '/images/Logos/Four-Seasons-logo.jpg',
        summary: 'Líder global em hospitalidade de luxo com UX exemplar.',
        strengths: ['Sistema de reservas fluido', 'Conteúdo rico', 'UX impecável'],
        opportunities: ['Visual poderia ser mais aspiracional']
      }
    ]
  },
  {
    name: 'Design & Interiores',
    icon: '',
    competitors: [
      {
        name: 'B&B Italia',
        segment: 'Design',
        country: 'Itália',
        flag: '🇮🇹',
        url: 'https://www.bebitalia.com',
        image: '/images/Logos/BB-Italia-logo.webp',
        summary: 'Design italiano contemporâneo de alto padrão.',
        strengths: ['Catálogo visual forte', 'Filtros eficientes', 'Inspiração'],
        opportunities: ['Poderia ter mais storytelling']
      },
      {
        name: 'Minotti',
        segment: 'Design',
        country: 'Itália',
        flag: '🇮🇹',
        url: 'https://www.minotti.com',
        image: '/images/Logos/Minotti-logo.png',
        summary: 'Mobiliário de luxo com estética atemporal.',
        strengths: ['Design clean', 'Fotografia profissional', 'Elegância'],
        opportunities: ['E-commerce limitado']
      }
    ]
  },
  {
    name: 'Bebidas',
    icon: '',
    competitors: [
      {
        name: 'Hennessy',
        segment: 'Bebidas',
        country: 'França',
        flag: '🇫🇷',
        url: 'https://www.hennessy.com',
        image: '/images/Logos/Hennessy-logo.png',
        summary: 'Maison de cognac mais prestigiada do mundo, referência em luxo, herança e colaborações culturais icônicas.',
        strengths: ['Storytelling cultural excepcional', 'Colaborações com ícones (LeBron, Tems)', 'Experiência imersiva de marca'],
        opportunities: ['Age-gate pode prejudicar UX inicial', 'Navegação poderia ser mais direta']
      }
    ]
  }
]

const activeSegment = ref(0)

const showMenu = ref(false)

const navigationLinks = [
  { title: 'Briefing', path: '/briefing' },
  { title: 'Planejamento', path: '/programacao' },
  { title: 'Discovery', path: '/pesquisa' },
  { title: 'Estratégia', path: '/estrategia' },
  { title: 'Ideação', path: '/ideacao' },
  { title: 'UI Design', path: '/ui-design' },
  { title: 'Protótipo', path: '/prototipo' },
  { title: 'Roadmap', path: '/entrega' }
]

const toggleMenu = () => {
  showMenu.value = !showMenu.value
}

const handleNavigation = () => {
  showMenu.value = false
}
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-subtle relative z-50">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase mt-[6px]">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Benchmarking</span>
          </nav>
        </div>
        <!-- Menu Button with Dropdown -->
        <div class="relative">
          <button 
            @click="toggleMenu"
            class="flex items-center gap-2 text-xs font-mono text-action-primary tracking-widest uppercase mt-[6px] hover:text-text-primary transition-colors cursor-pointer"
          >
            <i class="lni lni-menu text-base"></i>
            <span>Menu</span>
          </button>
          
          <!-- Dropdown Menu -->
          <div 
            v-if="showMenu"
            class="absolute right-0 mt-3 w-56 bg-white border border-subtle rounded-lg shadow-xl z-[9999]"
          >
            <nav class="py-2">
              <NuxtLink
                v-for="link in navigationLinks"
                :key="link.path"
                :to="link.path"
                class="block px-4 py-2.5 text-sm font-light text-text-primary hover:bg-surface-subtle transition-colors cursor-pointer"
                @click="handleNavigation"
              >
                {{ link.title }}
              </NuxtLink>
            </nav>
          </div>
        </div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        
        <!-- Intro -->
        <div class="mb-16">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 03 · Design & Referências</span>
          <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Benchmarking de Luxo</h1>
          <p class="text-secondary text-xl font-light leading-relaxed max-w-3xl">
            Análise de marcas de luxo em diversos segmentos. Identificamos padrões de UX, storytelling e oportunidades de diferenciação para a Pilar Homes.
          </p>
        </div>

        <!-- Segment Tabs -->
        <div class="flex flex-wrap gap-2 mb-12">
          <button
            v-for="(segment, index) in segments"
            :key="segment.name"
            @click="activeSegment = index"
            class="px-4 py-2 text-xs font-mono uppercase tracking-widest transition-all duration-300 rounded-lg flex items-center gap-2 border"
            :class="activeSegment === index 
              ? 'bg-white text-action-primary border-action-primary' 
              : 'bg-surface-card text-secondary hover:text-text-primary border-subtle hover:border-strong'"
          >
            <span>{{ segment.name }}</span>
          </button>
        </div>

        <!-- Competitors Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <TransitionGroup name="fade">
            <div 
              v-for="competitor in segments[activeSegment].competitors" 
              :key="competitor.name"
              class="bg-surface-card border rounded-lg border-subtle hover:border-strong transition-all duration-500 overflow-hidden group"
            >
              <!-- Cover Image -->
              <a
                :href="competitor.url"
                target="_blank"
                rel="noopener noreferrer"
                class="block relative"
              >
                <div
                  class="w-full h-40 bg-white border-b border-subtle overflow-hidden group-hover:scale-105 transition-transform duration-700 flex items-center justify-center"
                >
                  <img
                    :src="competitor.image"
                    :alt="competitor.name"
                    class="max-h-16 max-w-[80%] object-contain p-2"
                  />
                </div>
              </a>

              <!-- Content -->
              <div class="p-5">
                <!-- Header -->
                <div class="mb-3">
                  <div class="flex items-center gap-2 mb-1">
                    <span class="text-lg">{{ competitor.flag }}</span>
                    <h3 class="text-lg font-light text-text-primary">{{ competitor.name }}</h3>
                  </div>
                  <a 
                    :href="competitor.url" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="text-xs text-action-primary hover:underline font-mono"
                  >
                    {{ competitor.url.replace('https://www.', '').replace('https://', '') }} ↗
                  </a>
                </div>

                <!-- Summary -->
                <p class="text-sm text-secondary font-light mb-4 leading-relaxed">
                  {{ competitor.summary }}
                </p>

                <!-- Strengths & Opportunities -->
                <div class="grid grid-cols-2 gap-3 text-xs">
                  <div>
                    <span class="font-mono text-[10px] text-action-primary uppercase tracking-widest block mb-2">Pontos Fortes</span>
                    <ul class="space-y-1">
                      <li v-for="strength in competitor.strengths.slice(0, 2)" :key="strength" class="text-secondary">
                        • {{ strength }}
                      </li>
                    </ul>
                  </div>
                  <div>
                    <span class="font-mono text-[10px] text-secondary uppercase tracking-widest block mb-2">Oportunidades</span>
                    <ul class="space-y-1">
                      <li v-for="opportunity in competitor.opportunities.slice(0, 2)" :key="opportunity" class="text-secondary">
                        • {{ opportunity }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </TransitionGroup>
        </div>

        <!-- Navigation -->
        <div class="pt-8 border-t border-subtle flex justify-between items-center mt-12">
          <NuxtLink to="/pesquisa" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
            <span class="text-lg">←</span> Voltar para Discovery
          </NuxtLink>
        </div>

      </div>
    </main>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Navigation spacing */
.navigation-back {
  margin-top: 3rem;
}
</style>

