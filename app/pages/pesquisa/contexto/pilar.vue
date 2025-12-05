<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

useSeoMeta({
  title: 'Contexto & Negócio - Pilar Homes',
  description: 'Análise do contexto de negócio e mercado da Pilar Homes.'
})

const activeSection = ref('sobre')

const updateActiveSection = () => {
  const sections = ['sobre', 'timeline', 'estrutura', 'tecnologia', 'servicos', 'hubs', 'modelo']
  const scrollPosition = window.scrollY + 200 // offset for better UX
  
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
            <NuxtLink to="/pesquisa/contexto" class="text-secondary hover:text-text-primary transition-colors">Contexto</NuxtLink>
            <span class="text-text-primary/20">/</span>
            <span class="text-text-primary">Pilar</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          <!-- Sidebar -->
          <aside class="lg:col-span-4 sticky top-32 h-fit">
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 01.1</span>
            <h1 class="text-4xl md:text-5xl font-light tracking-tighter mb-8 text-text-primary">Sobre a<br/>Pilar</h1>
            <div class="w-12 h-1 bg-mat-stone mb-8"></div>
            
            <nav class="space-y-4 border-l border-subtle pl-6">
              <a href="#sobre" 
                :class="activeSection === 'sobre' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Sobre a Pilar
              </a>
              <a href="#timeline" 
                :class="activeSection === 'timeline' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Linha do Tempo
              </a>
              <a href="#estrutura" 
                :class="activeSection === 'estrutura' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Estrutura Organizacional
              </a>
              <a href="#tecnologia" 
                :class="activeSection === 'tecnologia' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Tecnologia
              </a>
              <a href="#servicos" 
                :class="activeSection === 'servicos' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Serviços de Suporte
              </a>
              <a href="#hubs" 
                :class="activeSection === 'hubs' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Hubs Físicos
              </a>
              <a href="#modelo" 
                :class="activeSection === 'modelo' ? 'block text-sm font-medium text-action-primary' : 'block text-sm font-light text-secondary hover:text-text-primary transition-colors'">
                Modelo de Remuneração
              </a>
            </nav>
          </aside>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6 space-y-8">
            
            <!-- Section: Sobre - Hero Section -->
            <section id="sobre" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm min-h-[100vh] flex flex-col items-center justify-center text-center rounded-lg">
              <!-- Intro -->
              <div class="max-w-3xl">
                <p class="text-lg text-secondary font-light leading-relaxed mb-6">
                  A Pilar é uma proptech que atua como um <strong class="text-text-primary font-medium">ecossistema de suporte ao corretor</strong>, oferecendo tecnologia de ponta, infraestrutura robusta e serviços completos para valorizar o trabalho do profissional imobiliário.
                </p>
                <p class="text-lg text-secondary font-light leading-relaxed mb-12">
                  Com o modelo <strong class="text-text-primary font-medium">"Corretores no Topo"</strong>, a Pilar coloca a marca do corretor e sua boutique no centro do negócio, fornecendo toda a estrutura necessária para o sucesso das transações.
                </p>
                
                <!-- Fundadores - Assinatura -->
                <div class="pt-8 border-t border-subtle">
                  <div class="flex justify-center gap-8 text-left">
                    <div>
                      <p class="text-sm font-medium text-text-primary">Felipe Abramovay</p>
                      <p class="text-xs text-secondary font-light">CEO & Cofounder</p>
                    </div>
                    <div>
                      <p class="text-sm font-medium text-text-primary">Luiz Gilbert</p>
                      <p class="text-xs text-secondary font-light">Cofounder</p>
                    </div>
                    <div>
                      <p class="text-sm font-medium text-text-primary">Raphael Sampaio</p>
                      <p class="text-xs text-secondary font-light">Cofounder</p>
                    </div>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Linha do Tempo -->
            <section id="timeline" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm rounded-lg">
              <h2 class="text-3xl font-light text-text-primary mb-12 text-center">Linha do Tempo</h2>
              
              <div class="space-y-8 max-w-3xl mx-auto">
                  <!-- 2021 -->
                  <div>
                    <h4 class="text-lg font-medium text-text-primary mb-4">2021 — Fundação</h4>
                    <div class="space-y-3 relative pl-8 border-l-2 border-action-primary/20">
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Meados de 2021</span>
                          <p class="text-sm text-text-primary">Felipe Abramovay, Luiz Gilbert e Rafael Sampaio começaram a estudar a tese da Pilar</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Setembro</span>
                          <p class="text-sm text-text-primary font-medium">Fundação da Pilar</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Nov/Dez</span>
                          <p class="text-sm text-text-primary">Primeira rodada de investimento: <strong class="text-action-primary">US$ 800.000</strong></p>
                          <p class="text-xs text-secondary mt-1">Participação: Canary e Latitude</p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- 2022 -->
                  <div>
                    <h4 class="text-lg font-medium text-text-primary mb-4">2022 — Início das Operações</h4>
                    <div class="space-y-3 relative pl-8 border-l-2 border-action-primary/20">
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Janeiro</span>
                          <p class="text-sm text-text-primary">A empresa começou a operar</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Maio</span>
                          <p class="text-sm text-text-primary">A Pilar começou a gerar receita</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">17 de Maio</span>
                          <p class="text-sm text-text-primary">Primeira publicação no Instagram @sou_pilar</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">2022</span>
                          <p class="text-sm text-text-primary">Rodada de investimento: <strong class="text-action-primary">US$ 4,7 milhões</strong></p>
                          <p class="text-xs text-secondary mt-1">Liderada pelo Atlântico</p>
                          <p class="text-sm text-text-primary mt-2">VGV alcançado: <strong class="text-action-primary">R$ 250 milhões</strong></p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- 2023 -->
                  <div>
                    <h4 class="text-lg font-medium text-text-primary mb-4">2023 — Crescimento & Rebranding</h4>
                    <div class="space-y-3 relative pl-8 border-l-2 border-action-primary/20">
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">10 de Abril</span>
                          <p class="text-sm text-text-primary">Primeiro vídeo do YouTube da empresa</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">13 de Abril</span>
                          <p class="text-sm text-text-primary">Primeira publicação no Spotify</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">2023</span>
                          <p class="text-sm text-text-primary">Selecionada para o programa Scale-Up da Endeavor</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">09 de Setembro</span>
                          <p class="text-sm text-text-primary font-medium">Rebranding — Pivot para marca mais sofisticada</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">2023</span>
                          <p class="text-sm text-text-primary">VGV: <strong class="text-action-primary">R$ 1 bilhão</strong></p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- 2024 -->
                  <div>
                    <h4 class="text-lg font-medium text-text-primary mb-4">2024 — Consolidação</h4>
                    <div class="space-y-3 relative pl-8 border-l-2 border-action-primary/20">
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Janeiro</span>
                          <p class="text-sm text-text-primary">Renato Feller se junta como CMO</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">24 de Maio</span>
                          <p class="text-sm text-text-primary">Primeiro Pilar Day</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Junho-Julho</span>
                          <p class="text-sm text-text-primary">Campanha "A Melhor Rede Tem Nome"</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Out/Nov</span>
                          <p class="text-sm text-text-primary">Início da expansão para Curitiba</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">18 de Novembro</span>
                          <p class="text-sm text-text-primary">Primeira publicação @pilarhomes_</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">22 de Novembro</span>
                          <p class="text-sm text-text-primary">Matéria da Exame sobre PilarHomes</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">2024</span>
                          <p class="text-sm text-text-primary">VGV: <strong class="text-action-primary">R$ 2,5 bilhões</strong></p>
                          <p class="text-xs text-secondary mt-1">~80 colaboradores</p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- 2025 -->
                  <div>
                    <h4 class="text-lg font-medium text-text-primary mb-4">2025 — Expansão Acelerada</h4>
                    <div class="space-y-3 relative pl-8 border-l-2 border-action-primary/20">
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">16 de Janeiro</span>
                          <p class="text-sm text-text-primary">Primeira publicação na Pilar Engineering</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">04 de Abril</span>
                          <p class="text-sm text-text-primary">Segundo Pilar Day</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">Abril</span>
                          <p class="text-sm text-text-primary font-medium">Ultrapassou <strong class="text-action-primary">R$ 1 bilhão</strong> em vendas no mês</p>
                          <p class="text-sm text-text-primary mt-2">Inauguração do escritório em Curitiba</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">12 de Maio</span>
                          <p class="text-sm text-text-primary">Rodada Série A: <strong class="text-action-primary">US$ 6,5 milhões</strong></p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">01 de Agosto</span>
                          <p class="text-sm text-text-primary">R$ 180 milhões distribuídos em comissões em 3 anos</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-surface-subtle border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">14 de Novembro</span>
                          <p class="text-sm text-text-primary">Entrevista no podcast "Mercado Imobiliário de Canto a Canto"</p>
                        </div>
                      </div>
                      <div class="relative">
                        <span class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-mat-stone border-4 border-surface-card"></span>
                        <div>
                          <span class="text-sm font-mono text-secondary block mb-1">03 de Dezembro</span>
                          <p class="text-sm text-text-primary font-medium">Parceria com Zimmermann</p>
                          <p class="text-sm text-text-primary mt-1">Projeção: <strong class="text-action-primary">R$ 5 bilhões em VGV até 2026</strong></p>
                        </div>
                      </div>
                    </div>
                  </div>
              </div>
            </section>

            <!-- Section: Estrutura Organizacional -->
            <section id="estrutura" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm rounded-lg">
              <h2 class="text-3xl font-light text-text-primary mb-8">Estrutura Organizacional</h2>
              <p class="text-sm text-secondary font-light mb-6">A área de <strong class="text-text-primary font-medium">Tecnologia é central</strong>, representando <strong class="text-text-primary font-medium">40% do time</strong> da Pilar.</p>
              
              <div class="space-y-3">
                  <!-- Engineering & Tech -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Engenharia & Tech</h4>
                      <span class="text-2xl font-light text-action-primary">10-12</span>
                    </div>
                    <p class="text-sm text-secondary font-light mb-2">
                      Engenheiros Sênior de Software, Tech Leads (Python Backend, Frontend, Full Stack), Staff Engineers, e desenvolvedores Mobile (Flutter).
                    </p>
                    <p class="text-xs font-mono text-secondary">
                      <strong class="text-text-primary">Liderança:</strong> Renato Crudo (Senior Software Engineering Manager)
                    </p>
                  </div>

                  <!-- Marketing & Growth -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Marketing & Growth</h4>
                      <span class="text-2xl font-light text-action-primary">12-15</span>
                    </div>
                    <p class="text-sm text-secondary font-light mb-2">
                      Coordenadores de Mídia Social, Analistas de Marketing (incluindo IA no Marketing) e Coordenador de Conteúdo e Relações Públicas.
                    </p>
                    <p class="text-xs font-mono text-secondary">
                      <strong class="text-text-primary">Liderança:</strong> Renato Feller (CMO), Carolina Bertoldi (Head of Marketing)
                    </p>
                  </div>

                  <!-- Business Development -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Business Development & Expansão</h4>
                      <span class="text-2xl font-light text-action-primary">10+</span>
                    </div>
                    <p class="text-sm text-secondary font-light mb-2">
                      Business Managers, expansão para novas cidades (Curitiba, liderada por Henrique Marcelino) e prospecção de Novos Negócios.
                    </p>
                    <p class="text-xs font-mono text-secondary">
                      <strong class="text-text-primary">Liderança:</strong> Júlio César Bium Barbosa (Head Comercial), Diego Biagi (Sócio Institucional)
                    </p>
                  </div>

                  <!-- Customer Success -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Customer Success & Operations</h4>
                      <span class="text-2xl font-light text-action-primary">8-10</span>
                    </div>
                    <p class="text-sm text-secondary font-light mb-2">
                      Especialistas em Customer Success, Business Operation e Coordenação de FP&A e Ops.
                    </p>
                    <p class="text-xs font-mono text-secondary">
                      <strong class="text-text-primary">Liderança:</strong> Rafael Halpern (Head of Customer Success)
                    </p>
                  </div>

                  <!-- Produto & Design -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Produto & Design</h4>
                      <span class="text-2xl font-light text-action-primary">5-7</span>
                    </div>
                    <p class="text-sm text-secondary font-light mb-2">
                      Lead Product Designer, Product Manager e Product Designer.
                    </p>
                    <p class="text-xs font-mono text-secondary">
                      <strong class="text-text-primary">Liderança:</strong> Fernando Meirelles Pereira (Lead Product Designer), Beatriz Trombini (Product Manager)
                    </p>
                  </div>

                  <!-- Pessoas & Cultura -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Pessoas & Cultura</h4>
                      <span class="text-2xl font-light text-action-primary">5-7</span>
                    </div>
                    <p class="text-sm text-secondary font-light mb-2">
                      Desenvolvimento Organizacional e Aquisição de Talentos (HRBP).
                    </p>
                    <p class="text-xs font-mono text-secondary">
                      <strong class="text-text-primary">Liderança:</strong> Samara Nery (Head de Pessoas)
                    </p>
                  </div>

                  <!-- Jurídico & Financeiro -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Jurídico & Financeiro</h4>
                      <span class="text-2xl font-light text-action-primary">4-6</span>
                    </div>
                    <p class="text-sm text-secondary font-light">
                      Finanças, soluções financeiras e assessoria jurídica pós-venda imobiliário.
                    </p>
                  </div>

                  <!-- Suporte & Outros -->
                  <div class="bg-surface-card p-6 border rounded-lg border-subtle hover:border-action-primary/20 transition-colors group">
                    <div class="flex justify-between items-start mb-3">
                      <h4 class="text-base font-medium text-text-primary group-hover:text-action-primary transition-colors">Suporte & Outros</h4>
                      <span class="text-2xl font-light text-action-primary">10+</span>
                    </div>
                    <p class="text-sm text-secondary font-light">
                      Funções de Suporte, incluindo Recepção e operações gerais.
                    </p>
                  </div>
                </div>
            </section>

            <!-- Section: Tecnologia -->
            <section id="tecnologia" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm">
              <h2 class="text-3xl font-light text-text-primary mb-8">🌐 Tecnologia</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline rounded-lg mb-8">
                <p class="text-secondary font-light leading-relaxed mb-6">
                  A Pilar desenvolve internamente toda sua infraestrutura digital — um dos pilares estratégicos da operação, com cerca de <strong class="text-text-primary font-medium">40% do time dedicado a produto e engenharia</strong>.
                </p>
              </div>

              <h3 class="text-xl font-light text-text-primary mb-6">Principais Ferramentas</h3>
              
              <div class="space-y-6">
                <!-- Rede Pilar -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex items-start gap-4">
                    <div class="flex-shrink-0 w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center">
                      <span class="text-2xl">🔗</span>
                    </div>
                    <div class="flex-1">
                      <h4 class="text-lg font-medium text-text-primary mb-2">Rede Pilar (Marketplace Interno)</h4>
                      <p class="text-sm text-secondary font-light mb-4">
                        Sistema de compartilhamento de portfólios entre <strong class="text-text-primary">750+ corretores</strong> e <strong class="text-text-primary">220+ boutiques</strong>.
                      </p>
                      <div class="bg-action-primary/5 p-4 border-l-4 border-action-primary">
                        <p class="text-sm text-text-primary font-light">
                          É o <strong class="font-medium">motor de liquidez do ecossistema</strong>: mais de <strong class="font-medium">50% das vendas de 2024</strong> vieram de parcerias.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- PilarHomes -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex items-start gap-4">
                    <div class="flex-shrink-0 w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center">
                      <span class="text-2xl">🏠</span>
                    </div>
                    <div class="flex-1">
                      <h4 class="text-lg font-medium text-text-primary mb-2">PilarHomes (Portal B2C)</h4>
                      <p class="text-sm text-secondary font-light mb-3">
                        Plataforma voltada ao cliente final, com algoritmos de IA que destacam anúncios conforme:
                      </p>
                      <ul class="space-y-2 text-sm text-secondary">
                        <li class="flex items-start gap-2">
                          <span class="text-action-primary mt-1">•</span>
                          <span>Perfil do comprador e histórico de navegação</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="text-action-primary mt-1">•</span>
                          <span>Performance do corretor (respostas rápidas, qualidade do material)</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>

                <!-- Ferramentas de Produtividade -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors">
                  <div class="flex items-start gap-4">
                    <div class="flex-shrink-0 w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center">
                      <span class="text-2xl">⚡</span>
                    </div>
                    <div class="flex-1">
                      <h4 class="text-lg font-medium text-text-primary mb-2">Ferramentas de Produtividade</h4>
                      <ul class="space-y-2 text-sm text-secondary">
                        <li class="flex items-start gap-2">
                          <span class="text-action-primary mt-1">•</span>
                          <span><strong class="text-text-primary">CAPTA</strong> — captação via WhatsApp</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="text-action-primary mt-1">•</span>
                          <span>Criação de peças de marketing</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="text-action-primary mt-1">•</span>
                          <span>Agendamento de fotografias</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="text-action-primary mt-1">•</span>
                          <span>Integrações operacionais que reduzem fricção no dia a dia</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Serviços de Suporte -->
            <section id="servicos" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm">
              <h2 class="text-3xl font-light text-text-primary mb-8">🧰 Serviços de Suporte (Backoffice)</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline rounded-lg mb-8">
                <p class="text-secondary font-light leading-relaxed">
                  A Pilar trabalha em modelo <strong class="text-text-primary font-medium">asset-light</strong>, removendo do corretor tudo que não é comercial.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Marketing & Branding -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors group">
                  <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center mb-4 group-hover:bg-action-primary/20 transition-colors">
                    <span class="text-2xl">🎨</span>
                  </div>
                  <h4 class="text-base font-medium text-text-primary mb-3">Marketing & Branding</h4>
                  <ul class="space-y-2 text-sm text-secondary font-light">
                    <li>• Criação da marca do corretor</li>
                    <li>• Identidade visual</li>
                    <li>• Redes sociais</li>
                    <li>• Tráfego pago e conteúdo</li>
                  </ul>
                </div>

                <!-- Jurídico & Comercial -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors group">
                  <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center mb-4 group-hover:bg-action-primary/20 transition-colors">
                    <span class="text-2xl">⚖️</span>
                  </div>
                  <h4 class="text-base font-medium text-text-primary mb-3">Jurídico & Comercial</h4>
                  <ul class="space-y-2 text-sm text-secondary font-light">
                    <li>• Contratos e diligências</li>
                    <li>• Compliance (KYC)</li>
                    <li>• Apoio em negociações complexas</li>
                  </ul>
                </div>

                <!-- Infraestrutura Operacional -->
                <div class="bg-surface-card p-6 border border-subtle rounded-lg hover:border-action-primary/20 transition-colors group">
                  <div class="w-12 h-12 bg-action-primary/10 rounded-lg flex items-center justify-center mb-4 group-hover:bg-action-primary/20 transition-colors">
                    <span class="text-2xl">🔧</span>
                  </div>
                  <h4 class="text-base font-medium text-text-primary mb-3">Infraestrutura Operacional</h4>
                  <ul class="space-y-2 text-sm text-secondary font-light">
                    <li>• Processos organizados</li>
                    <li>• Ferramentas integradas</li>
                    <li>• Suporte contínuo</li>
                    <li>• Fluidez nas transações</li>
                  </ul>
                </div>
              </div>
            </section>

            <!-- Section: Hubs Físicos -->
            <section id="hubs" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm">
              <h2 class="text-3xl font-light text-text-primary mb-8">🏢 Ambiente Físico (Hubs)</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline rounded-lg mb-6">
                <p class="text-secondary font-light leading-relaxed mb-4">
                  Escritórios em <strong class="text-text-primary font-medium">São Paulo e Curitiba</strong> funcionam como Hubs de conexão, coworkings e pontos de encontro que fortalecem a cultura de parceria — um dos diferenciais do modelo.
                </p>
                <p class="text-secondary font-light leading-relaxed">
                  O contato presencial cria <strong class="text-text-primary font-medium">confiança</strong> e favorece <strong class="text-text-primary font-medium">colaborações entre boutiques</strong>.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-center gap-3 mb-4">
                    <span class="text-3xl">📍</span>
                    <h4 class="text-lg font-medium text-text-primary">São Paulo</h4>
                  </div>
                  <p class="text-sm text-secondary font-light">
                    Hub principal com espaços de coworking, salas de reunião e ambiente de networking para corretores e parceiros.
                  </p>
                </div>

                <div class="bg-surface-card p-6 border border-subtle rounded-lg">
                  <div class="flex items-center gap-3 mb-4">
                    <span class="text-3xl">📍</span>
                    <h4 class="text-lg font-medium text-text-primary">Curitiba</h4>
                  </div>
                  <p class="text-sm text-secondary font-light">
                    Expansão estratégica para fortalecer a presença no Sul, facilitando parcerias regionais e suporte local.
                  </p>
                </div>
              </div>
            </section>

            <!-- Section: Modelo de Remuneração -->
            <section id="modelo" class="scroll-mt-24 bg-surface-card border border-subtle rounded-lg p-12 shadow-sm">
              <h2 class="text-3xl font-light text-text-primary mb-8">💰 Modelo de Remuneração</h2>

              <div class="bg-surface-subtle p-8 border border-hairline rounded-lg mb-8">
                <p class="text-lg text-secondary font-light leading-relaxed">
                  O modelo da Pilar é <strong class="text-text-primary font-medium">100% alinhado ao sucesso do corretor</strong>: só há remuneração quando há venda.
                </p>
              </div>

              <div class="space-y-6 mb-8">
                <!-- Comissão -->
                <div class="bg-surface-card p-8 border border-subtle rounded-lg">
                  <h3 class="text-xl font-light text-text-primary mb-4">Comissão (Take Rate)</h3>
                  
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">
                    <div>
                      <div class="flex items-baseline gap-3 mb-2">
                        <span class="text-4xl font-light text-action-primary">10-25%</span>
                        <span class="text-sm font-mono text-secondary uppercase tracking-widest">Pilar</span>
                      </div>
                      <p class="text-sm text-secondary font-light">
                        A Pilar retém entre 10% a 25% da comissão<br/>
                        <span class="text-xs">(em alguns modelos 10–15%)</span>
                      </p>
                    </div>
                    
                    <div>
                      <div class="flex items-baseline gap-3 mb-2">
                        <span class="text-4xl font-light text-text-primary">75-90%</span>
                        <span class="text-sm font-mono text-secondary uppercase tracking-widest">Corretor</span>
                      </div>
                      <p class="text-sm text-secondary font-light">
                        O corretor fica com 75% a 90% do valor da venda
                      </p>
                    </div>
                  </div>

                  <div class="bg-action-primary/5 p-6 border-l-4 border-action-primary">
                    <p class="text-sm text-text-primary font-light">
                      <strong class="font-medium">vs. Mercado Tradicional:</strong> Imobiliárias tradicionais retêm <strong class="font-medium">60–70%</strong> da comissão.
                    </p>
                  </div>
                </div>

                <!-- Setup & Planos -->
                <div class="bg-surface-card p-8 border border-subtle rounded-lg">
                  <h3 class="text-xl font-light text-text-primary mb-4">Setup & Planos</h3>
                  
                  <div class="space-y-4">
                    <div class="flex items-start gap-4">
                      <span class="text-action-primary text-xl mt-1">→</span>
                      <div>
                        <p class="text-sm text-text-primary font-medium mb-1">Processo Seletivo</p>
                        <p class="text-sm text-secondary font-light">
                          Entrada na plataforma após aprovação, com cobrança de setup em alguns casos para criação da marca.
                        </p>
                      </div>
                    </div>

                    <div class="flex items-start gap-4">
                      <span class="text-action-primary text-xl mt-1">→</span>
                      <div>
                        <p class="text-sm text-text-primary font-medium mb-1">Planos Evolutivos</p>
                        <p class="text-sm text-secondary font-light mb-3">
                          Três níveis que ampliam benefícios conforme a performance:
                        </p>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                          <div class="bg-surface-subtle p-4 rounded-lg border border-hairline">
                            <p class="text-xs font-mono uppercase tracking-widest text-action-primary mb-1">Fundação</p>
                            <p class="text-xs text-secondary">Plano inicial</p>
                          </div>
                          <div class="bg-surface-subtle p-4 rounded-lg border border-hairline">
                            <p class="text-xs font-mono uppercase tracking-widest text-action-primary mb-1">Horizonte</p>
                            <p class="text-xs text-secondary">Plano intermediário</p>
                          </div>
                          <div class="bg-surface-subtle p-4 rounded-lg border border-hairline">
                            <p class="text-xs font-mono uppercase tracking-widest text-action-primary mb-1">Skyline</p>
                            <p class="text-xs text-secondary">Plano avançado</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Visão Estratégica -->
              <div class="bg-gradient-to-br from-action-primary/5 to-action-primary/10 p-8 rounded-lg border border-action-primary/20">
                <h3 class="text-xl font-light text-text-primary mb-4">🎯 Visão Estratégica</h3>
                <p class="text-secondary font-light leading-relaxed mb-4">
                  A Pilar funciona como um <strong class="text-text-primary font-medium">ecossistema</strong> que combina tecnologia, rede e infraestrutura para que corretores independentes construam sua própria marca com escala e credibilidade.
                </p>
                <p class="text-secondary font-light leading-relaxed mb-6">
                  A <strong class="text-text-primary font-medium">Rede Pilar</strong> resolve o maior gargalo do mercado tradicional: <strong class="text-text-primary font-medium">falta de portfólio e liquidez</strong> fora do próprio nicho.
                </p>
                
                <div class="bg-white/50 p-6 rounded-lg border border-action-primary/30">
                  <p class="text-sm text-text-primary font-light italic leading-relaxed">
                    <strong class="font-medium not-italic">Metáfora:</strong><br/>
                    No modelo tradicional, a imobiliária retém a maior parte do valor gerado pelo corretor.<br/>
                    A Pilar age como uma <strong class="font-medium not-italic">liga moderna</strong> que fornece tecnologia, parcerias e ferramentas —<br/>
                    <strong class="font-medium not-italic text-action-primary">o corretor faz o gol, e fica com a maior parte do prêmio</strong>.
                  </p>
                </div>
              </div>
            </section>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>






