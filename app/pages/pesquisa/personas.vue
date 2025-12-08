<script setup lang="ts">
import AppIcon from '../../../components/AppIcon.vue'
import { ref, onMounted, onUnmounted } from 'vue'

useSeoMeta({
  title: 'Stakeholders & Personas - Pilar Homes',
  description: 'Documentação dos stakeholders e personas do ecossistema Pilar.'
})

const activeSection = ref('protagonista')

const updateActiveSection = () => {
  const sections = ['protagonista', 'comprador', 'vendedor', 'builders', 'analogia']
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
            <span class="text-text-primary">Personas</span>
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
          <!-- Sidebar / Title -->
          <div class="lg:col-span-4">
            <div class="sticky top-32">
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 02</span>
              <h1 class="text-4xl md:text-5xl font-light tracking-tighter mb-8 text-text-primary">Stakeholders<br/>& Personas</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-sm text-secondary font-light mb-8 leading-relaxed">
                Documentação dos principais stakeholders do ecossistema Pilar e suas necessidades, dores e proposta de valor.
              </p>
              
              <nav class="space-y-4 border-l border-subtle pl-6">
                <a href="#protagonista" 
                  :class="activeSection === 'protagonista' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                  O Protagonista
                </a>
                <a href="#comprador" 
                  :class="activeSection === 'comprador' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                  O Comprador
                </a>
                <a href="#vendedor" 
                  :class="activeSection === 'vendedor' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                  O Vendedor
                </a>
                <a href="#builders" 
                  :class="activeSection === 'builders' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                  Os Builders
                </a>
                <a href="#analogia" 
                  :class="activeSection === 'analogia' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                  Analogia
                </a>
              </nav>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6 space-y-8">
            
            <!-- Section: O Protagonista -->
            <section id="protagonista" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <div class="flex items-start gap-4 mb-6">
                <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                  <AppIcon name="lni-user" class="text-action-primary" style="font-size: 24px;" />
                </div>
                <div>
                  <h2 class="text-2xl font-light text-text-primary mb-2">Arquétipo 1: O Protagonista</h2>
                  <p class="text-sm text-secondary font-light">Corretor de Alto Padrão</p>
                </div>
              </div>
              
              <div class="bg-surface-subtle p-6 border border-hairline rounded-lg mb-8">
                <p class="text-secondary font-light leading-relaxed">
                  Este é o <strong class="text-text-primary font-medium">stakeholder central</strong> do modelo de negócios da Pilar, a quem a empresa se propõe a colocar <strong class="text-text-primary font-medium">"no topo"</strong> da experiência imobiliária.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Características vs. Proposta de Valor</h3>

              <div class="space-y-4 mb-8">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Empreendedor Autônomo</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Baixa remuneração (apenas 20% a 30% da comissão no modelo tradicional)
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Comissão Invertida — Fica com <strong class="font-medium">85% a 90%</strong> da comissão (10% a 15% para a Pilar)
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Profissional Nível Sênior</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Altos custos fixos (marketing, jurídico, tecnologia, escritório)
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Estrutura Asset Light — Eliminação de custos fixos, operando no sucesso (sem taxa antecipada ou mensalidade)
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Especialista Nichado</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Falta de liquidez do imóvel (tempo médio de venda de 16 meses no Brasil)
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Rede Colaborativa (MLS Privado) — Acesso a <strong class="font-medium">20 mil imóveis</strong> e <strong class="font-medium">750+ corretores</strong> para parcerias (50% das vendas são em rede)
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Focado no Comercial</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Necessidade de suporte jurídico, tecnológico e de marketing
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Backoffice Robusto — CRM proprietário, site white-label personalizado, gestão de leads, assessoria jurídica em contratos e diligência prévia
                    </p>
                  </div>
                </div>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Sub-Arquétipos de Corretores</h3>

              <div class="space-y-4">
                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg hover:border-action-primary/20 transition-colors">
                  <h4 class="text-base font-medium text-text-primary mb-2">1. O Especialista Nichado</h4>
                  <p class="text-xs text-secondary font-light mb-3 italic">Ex: Homesphere, Denise no Jardins</p>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-3">
                    Possui track record comprovado (mais de 5 anos) e alta performance, muitas vezes vindo de outras áreas como o mercado financeiro. É focado em nicho (seja regionalmente, como Jardins ou Panambi, ou por tipo de imóvel).
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Track Record</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Nicho</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Autonomia</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg hover:border-action-primary/20 transition-colors">
                  <h4 class="text-base font-medium text-text-primary mb-2">2. O Aspirante a Empreendedor</h4>
                  <p class="text-xs text-secondary font-light mb-3 italic">Ex: Yan Acioli (ex-stylist)</p>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-3">
                    Profissional com 1 a 3 anos de experiência ou migrando de carreira (como executivos ou pessoal de startup). Busca a credibilidade e a estrutura da Pilar para dar o salto na carreira.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Migração</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Flexibilidade</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Alto Potencial</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border border-hairline rounded-lg hover:border-action-primary/20 transition-colors">
                  <h4 class="text-base font-medium text-text-primary mb-2">3. A Boutique 2.0</h4>
                  <p class="text-xs text-secondary font-light mb-3 italic">Time de Líderes (2 a 25 corretores)</p>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-3">
                    Pequenas imobiliárias ou grupos de sócios que buscam reinventar o modelo de comissionamento (pagando mais aos corretores) e precisam de ferramentas de gestão, treinamento e mentoria para reter talentos.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Gestão</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">White-Label</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Retenção</span>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: O Comprador -->
            <section id="comprador" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <div class="flex items-start gap-4 mb-6">
                <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                  <AppIcon name="lni-diamond-alt" class="text-action-primary" style="font-size: 24px;" />
                </div>
                <div>
                  <h2 class="text-2xl font-light text-text-primary mb-2">Arquétipo 2: O Comprador</h2>
                  <p class="text-sm text-secondary font-light">Cliente de Alto Padrão</p>
                </div>
              </div>
              
              <div class="bg-surface-subtle p-6 border border-hairline rounded-lg mb-8">
                <p class="text-secondary font-light leading-relaxed">
                  Este é o público-alvo do portal <strong class="text-text-primary font-medium">PilarHomes</strong>, buscando imóveis <strong class="text-text-primary font-medium">acima de R$ 2 milhões</strong>, sendo a faixa de R$ 1M a R$ 5M a dominante em São Paulo.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Características vs. Proposta de Valor</h3>

              <div class="space-y-4">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Exigente e Impaciente</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Necessidade de atendimento em menos de 5 minutos, pois a demora leva ao cancelamento do contato
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução PilarHomes:</strong> Conexão com Especialistas — Atendimento sob medida e conexão direta com corretores especialistas no bairro e no perfil do imóvel
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Busca Curadoria</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Fragmentação do mercado e anúncios duplicados ou com informações inconsistentes
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução PilarHomes:</strong> Portfólio Curado — Portal dedicado exclusivamente ao alto padrão, com curadoria de imóveis e sem anúncios repetidos
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Alto Nível de Decisão</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> A transação é complexa, de alto valor e baixa frequência, exigindo confiança e segurança
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução PilarHomes:</strong> Credibilidade e Segurança — Prova social (depoimentos), números (R$ 3 bilhões negociados) e transparência nas informações de precificação e dados de mercado
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Busca Inspiração e Lifestyle</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Quer visualizar o potencial do imóvel e do bairro (lifestyle)
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução PilarHomes:</strong> Curadorias Assinadas — Imóveis selecionados por influenciadores de design e arquitetura, além de busca por pontos de interesse (POI) e ruas famosas
                    </p>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: O Vendedor -->
            <section id="vendedor" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <div class="flex items-start gap-4 mb-6">
                <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                  <AppIcon name="lni-home" class="text-action-primary" style="font-size: 24px;" />
                </div>
                <div>
                  <h2 class="text-2xl font-light text-text-primary mb-2">Arquétipo 3: O Vendedor/Proprietário</h2>
                  <p class="text-sm text-secondary font-light">Fornecedor de Imóveis</p>
                </div>
              </div>
              
              <div class="bg-surface-subtle p-6 border border-hairline rounded-lg mb-8">
                <p class="text-secondary font-light leading-relaxed">
                  Os proprietários são a <strong class="text-text-primary font-medium">fonte de supply (oferta)</strong> e buscam parceiros que minimizem o risco e acelerem a venda de seus ativos de alto valor.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Características vs. Proposta de Valor</h3>

              <div class="space-y-4">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Busca Discrição</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Não quer exposição pública do imóvel (principalmente para tickets mais altos) por questões de privacidade ou segurança
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Off-Market — Permite que o imóvel seja compartilhado apenas com os corretores da rede Pilar (750+ profissionais) sem ser anunciado publicamente
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Preza por Eficiência</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Perigo de "queimar" o imóvel por precificação errada ou demora na venda
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Gestão Exclusiva — O corretor parceiro utiliza dados de transações (se disponíveis no sistema Pilar) para justificar a precificação correta e evitar que o imóvel fique muito tempo no mercado
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Demanda Alcance</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Dor:</strong> Quer que o imóvel seja visto pelo maior número de compradores qualificados
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Solução Pilar:</strong> Efeito Rede — O imóvel, mesmo exclusivo (gestão única), é distribuído instantaneamente para a rede de parceiros, aumentando a probabilidade de liquidez
                    </p>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Os Builders -->
            <section id="builders" class="scroll-mt-32 bg-surface-card border border-subtle rounded-lg p-8 shadow-sm">
              <div class="flex items-start gap-4 mb-6">
                <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                  <AppIcon name="lni-code-alt" class="text-action-primary" style="font-size: 24px;" />
                </div>
                <div>
                  <h2 class="text-2xl font-light text-text-primary mb-2">Arquétipo 4: O Time Interno de Tecnologia</h2>
                  <p class="text-sm text-secondary font-light">Os Builders</p>
                </div>
              </div>
              
              <div class="bg-surface-subtle p-6 border border-hairline rounded-lg mb-8">
                <p class="text-secondary font-light leading-relaxed">
                  Este grupo é responsável por entregar as <strong class="text-text-primary font-medium">ferramentas que sustentam o modelo de negócio</strong> leve e eficiente da Pilar.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-4">Características & Entregáveis</h3>

              <div class="space-y-4">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Time Tech de 20 Builders</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Necessidade:</strong> Overhead operacional (tarefas time-consuming, tickets repetitivos)
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Foco:</strong> Automação (AI) — Uso de Claude 3.5 Sonnet para geração de código Python (code generation) e relatórios, reduzindo o tempo de horas para minutos/segundos
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Inovação Contínua</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Necessidade:</strong> Evitar que o sistema se torne um "Frankenstein" complexo e pouco útil
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Foco:</strong> Desenvolvimento Minimalista — Resolver os problemas principais (high-impact features), iterando constantemente com feedback direto dos corretores (living system)
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Thought Leadership</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Necessidade:</strong> Recrutar e reter talentos técnicos em um mercado competitivo
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Foco:</strong> Blog de Engenharia — Canal para compartilhar desafios técnicos, arquitetura (Nuxt.js, MongoDB, AWS) e cultura de transparência, atraindo engenheiros
                    </p>
                  </div>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-start justify-between mb-3">
                    <div class="flex-1">
                      <h4 class="text-base font-medium text-text-primary mb-2">Stack Moderna</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        <strong class="text-text-primary">Necessidade:</strong> Garantir alta performance, escalabilidade e SEO otimizado
                      </p>
                    </div>
                  </div>
                  <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">Foco:</strong> Tecnologia de Ponta — Nuxt.js (SSR), Tailwind CSS e infraestrutura AWS (CloudFront), permitindo a rápida replicação de sites white-label para boutiques
                    </p>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Analogia -->
            <section id="analogia" class="scroll-mt-32 bg-gradient-to-br from-action-primary/5 to-action-primary/10 border border-action-primary/20 rounded-lg p-8 shadow-sm">
              <h2 class="text-2xl font-light text-text-primary mb-6">Analogia: Central de Distribuição de Serviços de Luxo</h2>
              
              <div class="bg-white/60 p-6 rounded-lg mb-6">
                <p class="text-secondary font-light leading-relaxed mb-4">
                  O ecossistema Pilar opera como uma <strong class="text-text-primary font-medium">Central de Distribuição de Serviços de Luxo</strong>, similar a uma operação de Fórmula 1.
                </p>
              </div>

              <div class="space-y-4">
                <div class="bg-white/60 p-6 rounded-lg border-l-4 border-action-primary">
                  <div class="flex items-start gap-4">
                    <div class="w-10 h-10 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                      <AppIcon name="lni-user" class="text-action-primary" style="font-size: 20px;" />
                    </div>
                    <div>
                      <h4 class="text-base font-medium text-text-primary mb-2">O Protagonista (Corretor)</h4>
                      <p class="text-sm text-secondary font-light leading-relaxed">
                        É o <strong class="text-text-primary">Piloto de Fórmula 1</strong>, que tem talento e rede, mas precisa do melhor carro de corrida. A Pilar fornece o <strong class="text-text-primary">Carro (Tecnologia e Estrutura)</strong> e a <strong class="text-text-primary">Pista (Rede de Parcerias)</strong>, cobrando apenas uma pequena porcentagem do prêmio da vitória.
                      </p>
                    </div>
                  </div>
                </div>

                <div class="bg-white/60 p-6 rounded-lg border-l-4 border-action-primary">
                  <div class="flex items-start gap-4">
                    <div class="w-10 h-10 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                      <AppIcon name="lni-users" class="text-action-primary" style="font-size: 20px;" />
                    </div>
                    <div>
                      <h4 class="text-base font-medium text-text-primary mb-2">O Comprador e o Vendedor</h4>
                      <p class="text-sm text-secondary font-light leading-relaxed">
                        São os <strong class="text-text-primary">Clientes VIPs na arquibancada</strong>, que querem uma experiência de alta velocidade e sem atritos, garantida pela coordenação eficiente dos pilotos (corretores).
                      </p>
                    </div>
                  </div>
                </div>

                <div class="bg-white/60 p-6 rounded-lg border-l-4 border-action-primary">
                  <div class="flex items-start gap-4">
                    <div class="w-10 h-10 bg-action-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                      <AppIcon name="lni-code-alt" class="text-action-primary" style="font-size: 20px;" />
                    </div>
                    <div>
                      <h4 class="text-base font-medium text-text-primary mb-2">O Time Interno (Builders)</h4>
                      <p class="text-sm text-secondary font-light leading-relaxed">
                        É a <strong class="text-text-primary">Equipe de Pit Stop de Alto Nível</strong>, trabalhando nos bastidores para garantir que o carro tenha as ferramentas mais rápidas (AI, CRM) e que a comunicação entre os pilotos seja instantânea.
                      </p>
                    </div>
                  </div>
                </div>
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




