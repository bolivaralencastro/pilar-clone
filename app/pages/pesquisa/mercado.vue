<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

useSeoMeta({
  title: 'Visão de Mercado - Pilar Homes',
  description: 'Análise do mercado imobiliário de alto padrão e oportunidades.'
})

const activeSection = ref('macro')

const updateActiveSection = () => {
  const sections = ['macro', 'liquidez', 'fragmentacao', 'comprador', 'valorizacao', 'wealth', 'credito', 'exclusividade']
  const scrollPosition = window.scrollY + 200
  
  for (let i = sections.length - 1; i >= 0; i--) {
    const section = document.getElementById(sections[i])
    if (section && section.offsetTop <= scrollPosition) {
      activeSection.value = sections[i]
      break
    }
  }
}

onMounted(() => {
  window.addEventListener('scroll', updateActiveSection)
  updateActiveSection()
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateActiveSection)
})

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
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-secondary hover:text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <NuxtLink to="/pesquisa" class="text-secondary hover:text-text-primary transition-colors">Discovery</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Mercado</span>
          </nav>
        </div>
        <!-- Menu Button with Dropdown -->
        <div class="relative">
          <button 
            @click="toggleMenu"
            class="flex items-center gap-2 text-xs font-mono text-action-primary tracking-widest uppercase hover:text-text-primary transition-colors cursor-pointer"
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
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          <!-- Sidebar -->
          <aside class="lg:col-span-4 sticky top-32 h-fit">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 01.2</span>
            <h1 class="text-4xl md:text-5xl font-light tracking-tighter mb-8 text-text-primary">Visão de<br/>Mercado</h1>
            <div class="w-12 h-1 bg-mat-stone mb-8"></div>
            
            <nav class="space-y-4 border-l border-subtle pl-6">
              <a href="#macro" 
                :class="activeSection === 'macro' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Dados Macro do Mercado
              </a>
              <a href="#liquidez" 
                :class="activeSection === 'liquidez' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Liquidez
              </a>
              <a href="#fragmentacao" 
                :class="activeSection === 'fragmentacao' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Fragmentação do Mercado
              </a>
              <a href="#comprador" 
                :class="activeSection === 'comprador' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Comportamento do Comprador
              </a>
              <a href="#valorizacao" 
                :class="activeSection === 'valorizacao' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Valorização por Região
              </a>
              <a href="#wealth" 
                :class="activeSection === 'wealth' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Wealth Growth
              </a>
              <a href="#credito" 
                :class="activeSection === 'credito' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Crédito para Alta Renda
              </a>
              <a href="#exclusividade" 
                :class="activeSection === 'exclusividade' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Exclusividade
              </a>
            </nav>
          </aside>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6 space-y-8">
            
            <!-- Section: Dados Macro do Mercado -->
            <section id="macro" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Dados Macro do Mercado de Luxo</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed mb-4">
                  O mercado imobiliário brasileiro em 2025 apresenta estabilidade com variações trimestrais, influenciado por <strong class="text-text-primary font-medium">juros elevados (Selic em 15%)</strong> e dependência de programas como o Minha Casa Minha Vida (MCMV).
                </p>
                <p class="text-secondary font-light leading-relaxed">
                  De acordo com a CBIC, no segundo trimestre de 2025, houve estabilidade nas vendas e redução de 4,1% na oferta total de imóveis, com <strong class="text-text-primary font-medium">290 mil unidades</strong> disponíveis nacionalmente.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg text-center">
                  <span class="block text-4xl font-light text-action-primary mb-2">R$ 400-500bi</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Mercado Total Anual</span>
                  <p class="text-xs text-secondary font-light mt-2">Projeção 2025</p>
                </div>
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg text-center">
                  <span class="block text-4xl font-light text-action-primary mb-2">414.375</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Unidades Lançadas</span>
                  <p class="text-xs text-secondary font-light mt-2">12 meses até Q2 2025</p>
                </div>
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg text-center">
                  <span class="block text-4xl font-light text-action-primary mb-2">R$ 260bi</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">VGL Total</span>
                  <p class="text-xs text-secondary font-light mt-2">Valor Geral de Lançamento</p>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Segmento de Luxo (>R$ 2M)</h3>
              
              <div class="space-y-4 mb-6">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex justify-between items-start mb-3">
                    <div>
                      <h4 class="text-base font-medium text-text-primary mb-1">Share do Mercado</h4>
                      <p class="text-sm text-secondary font-light">Participação do segmento de luxo</p>
                    </div>
                    <span class="text-3xl font-light text-action-primary">10-12%</span>
                  </div>
                  <p class="text-xs text-secondary font-light">Do valor total transacionado no mercado imobiliário</p>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex justify-between items-start mb-3">
                    <div>
                      <h4 class="text-base font-medium text-text-primary mb-1">São Paulo Q1 2025</h4>
                      <p class="text-sm text-secondary font-light">Movimentação do segmento</p>
                    </div>
                    <span class="text-3xl font-light text-action-primary">R$ 4,5bi</span>
                  </div>
                  <div class="flex items-center gap-2 mt-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">+47% crescimento</span>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex justify-between items-start mb-3">
                    <div>
                      <h4 class="text-base font-medium text-text-primary mb-1">Crescimento YoY</h4>
                      <p class="text-sm text-secondary font-light">Segmento premium vs. mercado geral</p>
                    </div>
                    <span class="text-3xl font-light text-action-primary">7-15%</span>
                  </div>
                  <p class="text-xs text-secondary font-light">Superando mercado geral (6-10%), mas com crescimento desigual</p>
                </div>
              </div>

              <div class="bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Contexto Crítico</h4>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  São Paulo é o <strong class="text-text-primary">maior hub de luxo na América Latina</strong>, mas 80% dos empresários preveem piora econômica devido a juros altos que freiam o financiamento. Riscos incluem sobreoferta, fragmentação e dependência de compradores de alta renda vulneráveis a instabilidades macroeconômicas.
                </p>
              </div>
            </section>

            <!-- Section: Liquidez -->
            <section id="liquidez" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Dados sobre Liquidez</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  O tempo médio de venda de imóveis no Brasil é <strong class="text-text-primary font-medium">5-10x mais lento</strong> que mercados maduros devido a ineficiências estruturais como burocracia, falta de padronização, duplicidade de anúncios e baixa qualidade visual.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Tempo Médio de Venda</h3>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <!-- Brasil -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <h4 class="text-lg font-medium text-text-primary mb-4">Brasil 2025</h4>
                  <div class="space-y-3">
                    <div class="flex justify-between items-center pb-3 border-b border-hairline">
                      <span class="text-sm text-secondary">Residencial Nacional</span>
                      <span class="text-base font-medium text-text-primary">8-18 meses</span>
                    </div>
                    <div class="flex justify-between items-center pb-3 border-b border-hairline">
                      <span class="text-sm text-secondary">Alto Padrão SP</span>
                      <span class="text-base font-medium text-text-primary">12-24 meses</span>
                    </div>
                    <div class="flex justify-between items-center">
                      <span class="text-sm text-secondary">Super Prime (>R$8M)</span>
                      <span class="text-base font-medium text-action-primary">18-30 meses</span>
                    </div>
                  </div>
                </div>

                <!-- Mercados Maduros -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <h4 class="text-lg font-medium text-text-primary mb-4">Mercados Maduros</h4>
                  <div class="space-y-3">
                    <div class="flex justify-between items-center pb-3 border-b border-hairline">
                      <span class="text-sm text-secondary">EUA (NY, LA, Miami)</span>
                      <span class="text-base font-medium text-text-primary">30-120 dias</span>
                    </div>
                    <div class="flex justify-between items-center pb-3 border-b border-hairline">
                      <span class="text-sm text-secondary">Europa (Londres, Paris)</span>
                      <span class="text-base font-medium text-text-primary">60-120 dias</span>
                    </div>
                    <div class="flex justify-between items-center">
                      <span class="text-sm text-secondary">Portugal (Lisboa)</span>
                      <span class="text-base font-medium text-text-primary">60-180 dias</span>
                    </div>
                  </div>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Causas da Baixa Liquidez</h3>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-surface-subtle p-5 border border-hairline rounded-lg">
                  <h4 class="text-sm font-medium text-text-primary mb-2">Duplicidade de Anúncios</h4>
                  <p class="text-xs text-secondary font-light">Mesmo imóvel anunciado por múltiplos corretores sem coordenação</p>
                </div>
                <div class="bg-surface-subtle p-5 border border-hairline rounded-lg">
                  <h4 class="text-sm font-medium text-text-primary mb-2">Baixa Qualidade Visual</h4>
                  <p class="text-xs text-secondary font-light">Fotos ruins ou amadoras que não valorizam o imóvel</p>
                </div>
                <div class="bg-surface-subtle p-5 border border-hairline rounded-lg">
                  <h4 class="text-sm font-medium text-text-primary mb-2">Desorganização de Estoque</h4>
                  <p class="text-xs text-secondary font-light">Falta de curadoria e organização do portfólio disponível</p>
                </div>
                <div class="bg-surface-subtle p-5 border border-hairline rounded-lg">
                  <h4 class="text-sm font-medium text-text-primary mb-2">Juros Altos (Selic 15%)</h4>
                  <p class="text-xs text-secondary font-light">Redução de compradores financiados e desaceleração das vendas</p>
                </div>
              </div>
            </section>

            <!-- Section: Fragmentação -->
            <section id="fragmentacao" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Fragmentação do Mercado</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  O Brasil é o <strong class="text-text-primary font-medium">segundo maior mercado global</strong> em número de corretores, atrás apenas dos EUA, mas reflete saturação e baixa profissionalização.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-3">550-730 mil</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Corretores Ativos</span>
                  <p class="text-xs text-secondary font-light mt-3">Crescimento de 44-195% nos últimos 15 anos</p>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-3">70 mil+</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Imobiliárias</span>
                  <p class="text-xs text-secondary font-light mt-3">Nenhuma com market share >3% em SP</p>
                </div>
              </div>

              <div class="bg-action-primary/5 p-6 border-l-4 border-action-primary mb-6">
                <h4 class="text-sm font-medium text-text-primary mb-2">Pulverização Extrema</h4>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  Alta fragmentação confirma desorganização do mercado, especialmente no segmento de luxo latino-americano, com práticas competitivas predatórias, duplicidade de listagens e falta de regulação.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Consequências</h3>

              <div class="space-y-3">
                <div class="flex items-start gap-3 bg-surface-subtle p-4 border border-hairline rounded-lg">
                  <span class="text-action-primary text-xl mt-1">→</span>
                  <div>
                    <h4 class="text-sm font-medium text-text-primary mb-1">Consolidação Limitada</h4>
                    <p class="text-xs text-secondary font-light">Fragmentação persistente dificulta eficiência em escala</p>
                  </div>
                </div>
                <div class="flex items-start gap-3 bg-surface-subtle p-4 border border-hairline rounded-lg">
                  <span class="text-action-primary text-xl mt-1">→</span>
                  <div>
                    <h4 class="text-sm font-medium text-text-primary mb-1">Práticas Predatórias</h4>
                    <p class="text-xs text-secondary font-light">Competição desorganizada prejudica experiência do cliente</p>
                  </div>
                </div>
                <div class="flex items-start gap-3 bg-surface-subtle p-4 border border-hairline rounded-lg">
                  <span class="text-action-primary text-xl mt-1">→</span>
                  <div>
                    <h4 class="text-sm font-medium text-text-primary mb-1">Baixa Profissionalização</h4>
                    <p class="text-xs text-secondary font-light">Saturação do mercado sem padronização de qualidade</p>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Comportamento do Comprador -->
            <!-- Section: Comportamento do Comprador -->
            <section id="comprador" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Comportamento do Comprador de Luxo</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  O comportamento mudou para <strong class="text-text-primary font-medium">digital</strong>, com foco em <strong class="text-text-primary font-medium">mobile-first</strong> e <strong class="text-text-primary font-medium">visual-first</strong>, mas compradores de alta renda priorizam privacidade.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">50-68%</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Mobile-First</span>
                  <p class="text-xs text-secondary font-light mt-2">Buscas iniciadas no mobile</p>
                </div>
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">+40-60%</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Fotografia Pro</span>
                  <p class="text-xs text-secondary font-light mt-2">Aumento em visitas</p>
                </div>
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">3x</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Visual Quality</span>
                  <p class="text-xs text-secondary font-light mt-2">Mais tráfego para luxo</p>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Fatores Chave de Decisão</h3>

              <div class="space-y-4">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <h4 class="text-base font-medium text-text-primary mb-2">Decisão por Imagem</h4>
                  <p class="text-sm text-secondary font-light mb-3">
                    Fotografia profissional é fator chave de decisão preliminar, aumentando visitas em 40-60% e leads qualificados em +30%.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Visual</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Primeira Impressão</span>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <h4 class="text-base font-medium text-text-primary mb-2">Conteúdo Visual de Alta Qualidade</h4>
                  <p class="text-sm text-secondary font-light mb-3">
                    Imóveis de luxo recebem 3x mais tráfego com conteúdo visual de alta qualidade, como vídeos e tours virtuais.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Vídeo</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Tours 360°</span>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <h4 class="text-base font-medium text-text-primary mb-2">Buyer Journey Digital</h4>
                  <p class="text-sm text-secondary font-light mb-3">
                    49% de intenção de compra online, com perfil incluindo millennials e solteiras, com foco em preço acessível e localização.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Digital</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Millennials</span>
                  </div>
                </div>
              </div>

              <div class="mt-6 bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Consideração Crítica</h4>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  Dependência visual é forte, mas plataformas digitais podem expor excessivamente, reduzindo apelo para compradores premium sensíveis a privacidade. Canais offline ainda são preferidos para due diligence final.
                </p>
              </div>
            </section>

            <!-- Section: Valorização por Região -->
            <section id="valorizacao" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Valorização por Região - São Paulo</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  Principais bairros de São Paulo apresentam <strong class="text-text-primary font-medium">valorização média de 31-177%</strong> entre 2020-2025, com ticket médio variando de R$ 4-12 milhões para imóveis de luxo.
                </p>
              </div>

              <div class="space-y-4">
                <!-- Jardins -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-text-primary mb-1">Jardins (Jardim Paulistano)</h3>
                      <p class="text-xs text-secondary font-light">Bairro tradicional de alto padrão</p>
                    </div>
                    <span class="text-2xl font-light text-action-primary">+47-60%</span>
                  </div>
                  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Ticket Médio</p>
                      <p class="text-sm font-medium text-text-primary">R$ 5-12M</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">m²</p>
                      <p class="text-sm font-medium text-text-primary">R$ 25-40k</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Estoque >R$2M</p>
                      <p class="text-sm font-medium text-text-primary">Alto</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Tempo Venda</p>
                      <p class="text-sm font-medium text-text-primary">12-18m</p>
                    </div>
                  </div>
                </div>

                <!-- Itaim Bibi -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-text-primary mb-1">Itaim Bibi</h3>
                      <p class="text-xs text-secondary font-light">Hub corporativo e residencial</p>
                    </div>
                    <span class="text-2xl font-light text-action-primary">+32-39%</span>
                  </div>
                  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Ticket Médio</p>
                      <p class="text-sm font-medium text-text-primary">R$ 6-10M</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">m²</p>
                      <p class="text-sm font-medium text-text-primary">R$ 19-20k</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Estoque >R$2M</p>
                      <p class="text-sm font-medium text-text-primary">Médio-alto</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Tempo Venda</p>
                      <p class="text-sm font-medium text-text-primary">12-20m</p>
                    </div>
                  </div>
                  <div class="mt-3">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">+187% em ruas específicas</span>
                  </div>
                </div>

                <!-- Vila Nova Conceição -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-text-primary mb-1">Vila Nova Conceição</h3>
                      <p class="text-xs text-secondary font-light">Epicentro do super luxo</p>
                    </div>
                    <span class="text-2xl font-light text-action-primary">+31-41%</span>
                  </div>
                  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Ticket Médio</p>
                      <p class="text-sm font-medium text-text-primary">R$ 6-9M</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">m²</p>
                      <p class="text-sm font-medium text-text-primary">R$ 26-32k</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">VGV</p>
                      <p class="text-sm font-medium text-text-primary">R$ 648M</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Tempo Venda</p>
                      <p class="text-sm font-medium text-text-primary">16-24m</p>
                    </div>
                  </div>
                </div>

                <!-- Brooklin -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-text-primary mb-1">Brooklin</h3>
                      <p class="text-xs text-secondary font-light">Região em forte expansão</p>
                    </div>
                    <span class="text-2xl font-light text-action-primary">+70-100%</span>
                  </div>
                  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Ticket Médio</p>
                      <p class="text-sm font-medium text-text-primary">R$ 4-5M</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">m²</p>
                      <p class="text-sm font-medium text-text-primary">R$ 17-20k</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Projetos</p>
                      <p class="text-sm font-medium text-text-primary">97</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Tempo Venda</p>
                      <p class="text-sm font-medium text-text-primary">12-20m</p>
                    </div>
                  </div>
                  <div class="mt-3">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">+75,6% vendas >R$2M</span>
                  </div>
                </div>

                <!-- Pinheiros -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-text-primary mb-1">Pinheiros</h3>
                      <p class="text-xs text-secondary font-light">Bairro vibrante e valorizado</p>
                    </div>
                    <span class="text-2xl font-light text-action-primary">+43-177%</span>
                  </div>
                  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Ticket Médio</p>
                      <p class="text-sm font-medium text-text-primary">R$ 4-6M</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">m²</p>
                      <p class="text-sm font-medium text-text-primary">R$ 15-20k</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Lançamentos</p>
                      <p class="text-sm font-medium text-text-primary">302</p>
                    </div>
                    <div class="bg-surface-subtle p-3 rounded">
                      <p class="text-xs text-secondary mb-1">Tempo Venda</p>
                      <p class="text-sm font-medium text-text-primary">12-18m</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-8 bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Considerações Críticas</h4>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  Valorização é alta, mas suscetível a bolhas e envelhecimento de prédios em bairros nobres, com condomínios subindo e migração para regiões periféricas. Mercados secundários enfrentam sobreoferta.
                </p>
              </div>
            </section>

            <!-- Section: Wealth Growth -->
            <section id="wealth" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Wealth Growth no Brasil</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  O Brasil tem demanda potencial com crescimento de UHNWIs, mas enfrenta <strong class="text-text-primary font-medium">migração líquida negativa</strong> e concentração de riqueza em São Paulo.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">200-433k</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Milionários</span>
                  <p class="text-xs text-secondary font-light mt-3">Estimativa 2025</p>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">+7%</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Crescimento UHNWIs</span>
                  <p class="text-xs text-secondary font-light mt-3">Net worth >US$100M anual</p>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">São Paulo - Hub Latino-Americano</h3>

              <div class="bg-surface-card p-6 border border-subtle rounded-lg mb-6">
                <div class="flex items-start justify-between mb-4">
                  <div>
                    <h4 class="text-base font-medium text-text-primary mb-1">Concentração de Alta Renda</h4>
                    <p class="text-sm text-secondary font-light">4ª cidade milionária das Américas</p>
                  </div>
                  <span class="text-3xl font-light text-action-primary">40%</span>
                </div>
                <p class="text-xs text-secondary font-light">
                  Maior cidade milionária da América Latina em concentração de wealth
                </p>
              </div>

              <div class="bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Desafios</h4>
                <ul class="space-y-2 text-sm text-secondary font-light">
                  <li class="flex items-start gap-2">
                    <span class="text-action-primary mt-1">•</span>
                    <span><strong class="text-text-primary">Migração Negativa:</strong> -1.200 indivíduos UHNWIs em 2025</span>
                  </li>
                  <li class="flex items-start gap-2">
                    <span class="text-action-primary mt-1">•</span>
                    <span><strong class="text-text-primary">6º lugar global:</strong> Em perdas de milionários</span>
                  </li>
                  <li class="flex items-start gap-2">
                    <span class="text-action-primary mt-1">•</span>
                    <span><strong class="text-text-primary">Concentração SP:</strong> Exposição a riscos regionais e instabilidade</span>
                  </li>
                  <li class="flex items-start gap-2">
                    <span class="text-action-primary mt-1">•</span>
                    <span><strong class="text-text-primary">Desigualdade:</strong> Reduz compradores efetivos apesar da demanda existente</span>
                  </li>
                </ul>
              </div>
            </section>

            <!-- Section: Crédito para Alta Renda -->
            <section id="credito" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Crédito para Alta Renda</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  Financiamento imobiliário para alta renda enfrenta <strong class="text-text-primary font-medium">juros elevados</strong> e contração de crédito, mas pode fazer sentido se retornos de investimentos superarem custos.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-4">Juros de Financiamento</h3>
                  <div class="text-center mb-4">
                    <span class="block text-5xl font-light text-action-primary mb-2">10-12%</span>
                    <span class="text-sm font-mono text-secondary uppercase tracking-widest">a.a. + TR</span>
                  </div>
                  <p class="text-xs text-secondary font-light text-center">Média 11-12,5% com projeções de queda lenta para 2026</p>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <h3 class="text-lg font-medium text-text-primary mb-4">Selic Atual</h3>
                  <div class="text-center mb-4">
                    <span class="block text-5xl font-light text-action-primary mb-2">15%</span>
                    <span class="text-sm font-mono text-secondary uppercase tracking-widest">Taxa Básica</span>
                  </div>
                  <p class="text-xs text-secondary font-light text-center">Crédito encolheu 10% em 2025</p>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Retorno de Investimentos (Alta Renda)</h3>

              <div class="space-y-3 mb-8">
                <div class="flex justify-between items-center p-4 bg-surface-subtle border border-hairline rounded-lg">
                  <span class="text-sm text-secondary">Imóveis (valorização + renda)</span>
                  <span class="text-lg font-medium text-action-primary">19,1% a.a.</span>
                </div>
                <div class="flex justify-between items-center p-4 bg-surface-subtle border border-hairline rounded-lg">
                  <span class="text-sm text-secondary">Renda Fixa</span>
                  <span class="text-lg font-medium text-text-primary">>12% a.a.</span>
                </div>
                <div class="flex justify-between items-center p-4 bg-surface-subtle border border-hairline rounded-lg">
                  <span class="text-sm text-secondary">Financiamento Imobiliário</span>
                  <span class="text-lg font-medium text-text-primary">11-12,5% a.a.</span>
                </div>
              </div>

              <div class="bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Análise</h4>
                <p class="text-sm text-secondary font-light leading-relaxed mb-3">
                  <strong class="text-text-primary">Financiar pode fazer sentido</strong> se retornos de investimentos (19,1% em imóveis) superam juros de financiamento (11-12,5%), incentivando alavancagem.
                </p>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  <strong class="text-text-primary">Porém:</strong> Política habitacional ajuda médio padrão, mas luxo depende de juros privados. Alta Selic (15%) eleva custos, questionando sustentabilidade para alta renda e aumentando risco de inadimplência.
                </p>
              </div>
            </section>

            <!-- Section: Exclusividade -->
            <section id="exclusividade" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Dados sobre Exclusividade</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 rounded-lg">
                <p class="text-secondary font-light leading-relaxed">
                  Imóveis com exclusividade apresentam <strong class="text-text-primary font-medium">resultados significativamente melhores</strong>, mas dependem de confiança no corretor e podem limitar exposição em mercados fragmentados.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">20-40%</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Mais Rápido</span>
                  <p class="text-xs text-secondary font-light mt-3">Velocidade de venda</p>
                </div>
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">3x</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Conversão</span>
                  <p class="text-xs text-secondary font-light mt-3">Leads para vendas</p>
                </div>
                <div class="bg-surface-card p-6 border border-subtle rounded-lg text-center">
                  <span class="block text-5xl font-light text-action-primary mb-2">↓</span>
                  <span class="text-sm font-mono text-secondary uppercase tracking-widest">Conflitos</span>
                  <p class="text-xs text-secondary font-light mt-3">Entre corretores</p>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Benefícios da Exclusividade</h3>

              <div class="space-y-3 mb-6">
                <div class="flex items-start gap-3 bg-surface-subtle p-4 border border-hairline rounded-lg">
                  <span class="text-action-primary text-xl mt-1">✓</span>
                  <div>
                    <h4 class="text-sm font-medium text-text-primary mb-1">Marketing Personalizado</h4>
                    <p class="text-xs text-secondary font-light">Atenção estratégica e ruído digital reduzido</p>
                  </div>
                </div>
                <div class="flex items-start gap-3 bg-surface-subtle p-4 border border-hairline rounded-lg">
                  <span class="text-action-primary text-xl mt-1">✓</span>
                  <div>
                    <h4 class="text-sm font-medium text-text-primary mb-1">Melhor Apresentação</h4>
                    <p class="text-xs text-secondary font-light">Sem marca d'água, estética elevada e curadoria visual</p>
                  </div>
                </div>
                <div class="flex items-start gap-3 bg-surface-subtle p-4 border border-hairline rounded-lg">
                  <span class="text-action-primary text-xl mt-1">✓</span>
                  <div>
                    <h4 class="text-sm font-medium text-text-primary mb-1">Redução de Conflitos</h4>
                    <p class="text-xs text-secondary font-light">Evita concorrência predatória entre corretores no mesmo imóvel</p>
                  </div>
                </div>
              </div>

              <div class="bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Considerações</h4>
                <p class="text-sm text-secondary font-light leading-relaxed mb-3">
                  <strong class="text-text-primary">Vantagem clara:</strong> Exclusividade pode acelerar vendas significativamente e aumentar conversão através de marketing focado e melhor experiência.
                </p>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  <strong class="text-text-primary">Limitação:</strong> Restringe exposição em mercados fragmentados, podendo limitar alcance. Estratégias híbridas (ativa/reativa) são recomendadas, mas não resolvem dependência de portais ou volatilidade de leads digitais.
                </p>
              </div>
            </section>

            <!-- Navigation -->
            <div class="pt-8 border-t border-subtle flex justify-between items-center">
              <NuxtLink to="/pesquisa" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
                <span class="text-lg">←</span> Voltar para Discovery
              </NuxtLink>
            </div>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>







