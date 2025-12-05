<script setup lang="ts">
useSeoMeta({
  title: 'Benchmarking Global - Pilar Homes',
  description: 'Análise de referências globais em imobiliárias de luxo.'
})

interface Competitor {
  name: string
  country: string
  flag: string
  url: string
  image: string
  summary: string
  strengths: string[]
  opportunities: string[]
}

interface Region {
  name: string
  competitors: Competitor[]
}

const regions: Region[] = [
  {
    name: 'América do Norte',
    competitors: [
      {
        name: 'Douglas Elliman',
        country: 'EUA',
        flag: '🇺🇸',
        url: 'https://www.elliman.com',
        image: '/images/benchmarking/douglas-elliman.png',
        summary: 'Uma das maiores redes dos EUA em imóveis premium, forte em NY, Miami e LA.',
        strengths: ['Conteúdo editorial forte', 'Navegação clean', 'Fotografia impecável', 'Credibilidade'],
        opportunities: ['Filtros pouco avançados', 'Experiência mobile pode melhorar']
      },
      {
        name: 'The Agency',
        country: 'EUA',
        flag: '🇺🇸',
        url: 'https://www.theagencyre.com',
        image: '/images/benchmarking/the-agency.png',
        summary: 'Marca de luxo com storytelling aspiracional e produção audiovisual de altíssimo nível.',
        strengths: ['Branding excepcional', 'Vídeos high-end', 'Experiência inspiracional'],
        opportunities: ['Menos dados estruturados', 'Foco maior na emoção do que na função']
      },
      {
        name: 'Compass',
        country: 'EUA',
        flag: '🇺🇸',
        url: 'https://www.compass.com',
        image: '/images/benchmarking/compass.png',
        summary: 'Maior case de tecnologia aplicada ao mercado imobiliário premium.',
        strengths: ['UX fluida', 'Busca inteligente', 'CRM para corretores', 'Dados integrados'],
        opportunities: ['Visual não tão aspiracional quanto concorrentes de luxo puro']
      },
      {
        name: 'Hammond International Properties',
        country: 'Canadá',
        flag: '🇨🇦',
        url: 'https://hammondinternationalproperties.com',
        image: '/images/benchmarking/hammond.png',
        summary: 'Marca de luxo extremo, forte em Toronto.',
        strengths: ['Narrativa forte', 'Fotografias muito refinadas'],
        opportunities: ['Layout menos funcional', 'Prioriza emoção sobre busca']
      }
    ]
  },
  {
    name: 'Europa',
    competitors: [
      {
        name: 'Knight Frank',
        country: 'Reino Unido',
        flag: '🇬🇧',
        url: 'https://www.knightfrank.co.uk',
        image: '/images/benchmarking/knight-frank.png',
        summary: 'Potência global em imóveis premium e ultra-prime.',
        strengths: ['Relatórios de mercado impecáveis', 'Organização exemplar'],
        opportunities: ['Design mais tradicional', 'Pode parecer "frio" para padrões modernos']
      },
      {
        name: 'Savills',
        country: 'Reino Unido',
        flag: '🇬🇧',
        url: 'https://www.savills.co.uk',
        image: '/images/benchmarking/savills.png',
        summary: 'Rede global com força em pesquisa e inteligência de mercado.',
        strengths: ['Autoridade', 'Dados confiáveis', 'Clareza na navegação'],
        opportunities: ['Pouca emoção visual', 'Parece mais corporate']
      },
      {
        name: 'Barnes International Realty',
        country: 'França',
        flag: '🇫🇷',
        url: 'https://www.barnes-international.com',
        image: '/images/benchmarking/barnes.png',
        summary: 'Marca de luxo clássico, forte em Paris, Riviera Francesa, Genebra.',
        strengths: ['Elegância', 'Simplicidade', 'Consistência fotográfica'],
        opportunities: ['UX pouco interativa', 'Busca poderia ser mais intuitiva']
      },
      {
        name: 'Daniel Féau',
        country: 'França',
        flag: '🇫🇷',
        url: 'https://www.danielfeau.com',
        image: '/images/benchmarking/daniel-feau.png',
        summary: 'Especialista absoluto no mercado prime parisiense.',
        strengths: ['Refinamento visual', 'Informação profunda sobre bairros'],
        opportunities: ['Pouca escalabilidade de UX', 'Foco restrito']
      },
      {
        name: 'Engel & Völkers',
        country: 'Alemanha',
        flag: '🇩🇪',
        url: 'https://www.engelvoelkers.com',
        image: '/images/benchmarking/engel-volkers.png',
        summary: 'Uma das maiores redes globais, mix de premium e mainstream.',
        strengths: ['Escopo mundial', 'Estrutura robusta', 'Layout eficiente'],
        opportunities: ['Visual datado', 'Páginas longas e às vezes pesadas']
      },
      {
        name: 'Lionard Luxury Real Estate',
        country: 'Itália',
        flag: '🇮🇹',
        url: 'https://www.lionard.com',
        image: '/images/benchmarking/lionard.png',
        summary: 'Especialista em vilas italianas, castelos e propriedades históricas.',
        strengths: ['Fotografia cinematográfica', 'Storytelling de propriedade único'],
        opportunities: ['Muito visual', 'Poucos dados estruturados']
      },
      {
        name: 'Lucas Fox',
        country: 'Espanha',
        flag: '🇪🇸',
        url: 'https://www.lucasfox.com',
        image: '/images/benchmarking/lucas-fox.png',
        summary: 'Principal imobiliária de luxo da Espanha.',
        strengths: ['UI moderna', 'Experiência clara e leve'],
        opportunities: ['Alguns fluxos dependem de verificações (cloudflare)', 'Atrito na navegação']
      },
      {
        name: 'Lisbon Estates',
        country: 'Portugal',
        flag: '🇵🇹',
        url: 'https://www.lisbonestates.com',
        image: '/images/benchmarking/lisbon-estates.png',
        summary: 'Boutique premium com forte presença no mercado português.',
        strengths: ['Estética moderna', 'Boas descrições'],
        opportunities: ['Filtro limitado', 'Pouca profundidade de dados']
      },
      {
        name: 'Kalinka Ecosystem',
        country: 'Rússia',
        flag: '🇷🇺',
        url: 'https://kalinka-realty.com',
        image: '/images/benchmarking/kalinka.png',
        summary: 'Rede premium de Moscou com foco em ultra-luxo.',
        strengths: ['Curadoria e exclusividade'],
        opportunities: ['Site frequentemente inacessível', 'Tecnologia fraca']
      }
    ]
  },
  {
    name: 'Ásia & Oriente Médio',
    competitors: [
      {
        name: 'Metropolitan Premium Properties',
        country: 'Emirados Árabes',
        flag: '🇦🇪',
        url: 'https://metropolitan.realestate',
        image: '/images/benchmarking/metropolitan.png',
        summary: 'Especialista em Dubai, foco em novos lançamentos e investimento estrangeiro.',
        strengths: ['Muito conteúdo', 'Dados de ROI e plantas baixas', 'CTAs fortes'],
        opportunities: ['Visual carregado', 'Excesso de informações']
      },
      {
        name: 'India Sotheby\'s International Realty',
        country: 'Índia',
        flag: '🇮🇳',
        url: 'https://www.indiasothebysrealty.com',
        image: '/images/benchmarking/india-sothebys.png',
        summary: 'Marca premium fortíssima em Delhi e Mumbai.',
        strengths: ['Forte reputação global', 'Foco em HNWI e UHNW'],
        opportunities: ['Site pesado', 'Navegação lenta']
      },
      {
        name: 'Savills China',
        country: 'China',
        flag: '🇨🇳',
        url: 'https://www.savills.com.cn',
        image: '/images/benchmarking/savills-china.png',
        summary: 'Mais institucional; forte em comercial e consultoria.',
        strengths: ['Autoridade e dados robustos'],
        opportunities: ['Pouca oferta residencial', 'Não serve bem como inspiração de UX']
      },
      {
        name: 'Ken Corporation',
        country: 'Japão',
        flag: '🇯🇵',
        url: 'https://www.kencorp.com',
        image: '/images/benchmarking/ken-corporation.png',
        summary: 'Especialista em imóveis premium e expatriados em Tóquio.',
        strengths: ['Foco claro', 'Excelente reputação'],
        opportunities: ['Site muito antigo', 'Baixa inspiração visual']
      }
    ]
  },
  {
    name: 'Oceania',
    competitors: [
      {
        name: 'Schmith Estate Agents',
        country: 'Austrália',
        flag: '🇦🇺',
        url: 'https://schmith.com.au',
        image: '/images/benchmarking/schmith.png',
        summary: 'Agência boutique moderna, com forte apelo visual.',
        strengths: ['UI clean', 'Imagens grandes', 'Fluxo simples'],
        opportunities: ['Páginas inconsistentes entre si', 'Alguns elementos escondidos']
      }
    ]
  },
  {
    name: 'América Latina',
    competitors: [
      {
        name: 'Bossa Nova Sotheby\'s International Realty',
        country: 'Brasil',
        flag: '🇧🇷',
        url: 'https://www.bossanovasir.com.br',
        image: '/images/benchmarking/bossa-nova-sothebys.png',
        summary: 'Principal marca premium no Brasil, afiliada à Sotheby\'s.',
        strengths: ['Repertório de luxo', 'Boa curadoria', 'Credibilidade altíssima'],
        opportunities: ['UI irregular', 'Dificuldade para encontrar imóveis específicos']
      }
    ]
  }
]

const activeRegion = ref(0)
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa/design" class="text-secondary hover:text-text-primary transition-colors">Design</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Benchmarking</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        
        <!-- Intro -->
        <div class="mb-16 border-b border-subtle pb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 03 · Design & Referências</span>
          <h1 class="text-5xl md:text-6xl font-light tracking-tighter mb-8 text-text-primary">Benchmarking Global</h1>
          <p class="text-secondary text-xl font-light leading-relaxed max-w-3xl">
            Análise de 19 imobiliárias de luxo em 5 continentes. Identificamos padrões de UX, pontos fortes e oportunidades de diferenciação para a Pilar Homes.
          </p>
        </div>

        <!-- Region Tabs -->
        <div class="flex flex-wrap gap-2 mb-12">
          <button
            v-for="(region, index) in regions"
            :key="region.name"
            @click="activeRegion = index"
            class="px-4 py-2 text-xs font-mono uppercase tracking-widest transition-all duration-300"
            :class="activeRegion === index 
              ? 'bg-mat-stone text-off-white' 
              : 'bg-surface-card text-secondary hover:text-text-primary border rounded-lg border-subtle hover:border-strong'"
          >
            {{ region.name }}
          </button>
        </div>

        <!-- Stats -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-16">
          <div class="bg-surface-card p-6 border rounded-lg border-subtle text-center">
            <span class="block text-3xl font-light text-action-primary mb-1">19</span>
            <span class="text-xs font-mono text-secondary uppercase">Empresas</span>
          </div>
          <div class="bg-surface-card p-6 border rounded-lg border-subtle text-center">
            <span class="block text-3xl font-light text-action-primary mb-1">14</span>
            <span class="text-xs font-mono text-secondary uppercase">Países</span>
          </div>
          <div class="bg-surface-card p-6 border rounded-lg border-subtle text-center">
            <span class="block text-3xl font-light text-action-primary mb-1">5</span>
            <span class="text-xs font-mono text-secondary uppercase">Continentes</span>
          </div>
          <div class="bg-surface-card p-6 border rounded-lg border-subtle text-center">
            <span class="block text-3xl font-light text-action-primary mb-1">100%</span>
            <span class="text-xs font-mono text-secondary uppercase">Premium</span>
          </div>
        </div>

        <!-- Competitors Grid -->
        <div class="space-y-6">
          <TransitionGroup name="fade">
            <div 
              v-for="competitor in regions[activeRegion].competitors" 
              :key="competitor.name"
              class="bg-surface-card border rounded-lg border-subtle hover:border-strong transition-all duration-500 overflow-hidden"
            >
              <div class="flex flex-col md:flex-row">
                <!-- Cover Image -->
                <div class="md:w-72 lg:w-80 xl:w-96 flex-shrink-0">
                  <a 
                    :href="competitor.url" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="block h-full"
                  >
                    <img 
                      :src="competitor.image" 
                      :alt="`Screenshot do site ${competitor.name}`"
                      class="w-full h-48 md:h-full object-cover object-top hover:scale-105 transition-transform duration-700"
                    />
                  </a>
                </div>

                <!-- Content -->
                <div class="flex-1 p-8">
                  <!-- Header -->
                  <div class="flex items-start justify-between mb-6">
                    <div>
                      <div class="flex items-center gap-3 mb-2">
                        <span class="text-2xl">{{ competitor.flag }}</span>
                        <h3 class="text-2xl font-light text-text-primary">{{ competitor.name }}</h3>
                      </div>
                      <a 
                        :href="competitor.url" 
                        target="_blank" 
                        rel="noopener noreferrer"
                        class="text-xs font-mono text-action-primary hover:underline"
                      >
                        {{ competitor.url.replace('https://', '') }}
                      </a>
                    </div>
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest px-3 py-1 bg-surface-subtle">
                      {{ competitor.country }}
                    </span>
                  </div>

                  <!-- Summary -->
                  <p class="text-secondary font-light leading-relaxed mb-8">
                    {{ competitor.summary }}
                  </p>

                  <!-- Analysis -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-surface-subtle/50 p-5 border-l-2 border-green-600/50">
                      <span class="text-xs font-bold uppercase tracking-widest text-text-primary mb-3 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-green-600"></span>
                        Forças
                      </span>
                      <ul class="text-sm text-secondary space-y-2">
                        <li v-for="strength in competitor.strengths" :key="strength">
                          {{ strength }}
                        </li>
                      </ul>
                    </div>
                    <div class="bg-surface-subtle/50 p-5 border-l-2 border-amber-500/50">
                      <span class="text-xs font-bold uppercase tracking-widest text-text-primary mb-3 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                        Oportunidades
                      </span>
                      <ul class="text-sm text-secondary space-y-2">
                        <li v-for="opportunity in competitor.opportunities" :key="opportunity">
                          {{ opportunity }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </TransitionGroup>
        </div>

      </div>
    </main>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>



