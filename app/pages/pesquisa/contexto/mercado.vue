<script setup lang="ts">
useSeoMeta({
  title: 'Visão de Mercado - Pilar Homes',
  description: 'Análise do mercado imobiliário de alto padrão e oportunidades.'
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
            <span class="text-text-primary">Mercado</span>
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
            <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Cluster 01.2</span>
            <h1 class="text-4xl md:text-5xl font-light tracking-tighter mb-8 text-text-primary">Visão de<br/>Mercado</h1>
            <div class="w-12 h-1 bg-mat-stone mb-8"></div>
            
            <nav class="space-y-4 border-l border-subtle pl-6">
              <a href="#panorama" class="block text-sm font-medium text-primary hover:text-action-primary transition-colors">Panorama</a>
              <a href="#tendencias" class="block text-sm font-light text-secondary hover:text-text-primary transition-colors">Tendências</a>
              <a href="#oportunidades" class="block text-sm font-light text-secondary hover:text-text-primary transition-colors">Oportunidades</a>
            </nav>
          </aside>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6 space-y-8">
            
            <!-- Section: Panorama -->
            <section id="panorama" class="scroll-mt-32 bg-surface-card border border-subtle r rounded-lgounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Panorama do Mercado</h2>
              
              <div class="bg-surface-subtle p-8 border border-hairline mb-8 r rounded-lgounded-lg rounded-lg">
                <p class="text-secondary font-light leading-relaxed mb-6">
                  O mercado imobiliário de alto padrão no Brasil apresenta características únicas que demandam soluções digitais sofisticadas e experiências diferenciadas.
                </p>
                <p class="text-secondary font-light leading-relaxed">
                  A transformação digital do setor está em pleno curso, mas ainda há espaço significativo para inovação, especialmente na experiência do usuário final.
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                <div class="bg-surface-subtle p-6 border border-hairline r rounded-lgounded-lg text-center rounded-lg">
                  <span class="block text-4xl font-light text-action-primary mb-2">+15%</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Crescimento YoY</span>
                  <p class="text-xs text-secondary font-light mt-2">Mercado de alto padrão</p>
                </div>
                <div class="bg-surface-subtle p-6 border border-hairline r rounded-lgounded-lg text-center rounded-lg">
                  <span class="block text-4xl font-light text-action-primary mb-2">68%</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Mobile First</span>
                  <p class="text-xs text-secondary font-light mt-2">Primeiras buscas</p>
                </div>
                <div class="bg-surface-subtle p-6 border border-hairline r rounded-lgounded-lg text-center rounded-lg">
                  <span class="block text-4xl font-light text-action-primary mb-2">Visual</span>
                  <span class="text-xs font-mono text-secondary uppercase tracking-widest">Driven</span>
                  <p class="text-xs text-secondary font-light mt-2">Decisão por imagem</p>
                </div>
              </div>
            </section>

            <!-- Section: Tendências -->
            <section id="tendencias" class="scroll-mt-32 bg-surface-card border border-subtle r rounded-lgounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Tendências Identificadas</h2>
              
              <div class="space-y-6">
                <div class="bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/20 transition-colors">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Experiência Digital Premium</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Clientes de imóveis de luxo esperam que a experiência digital reflita a qualidade física do produto. Interfaces refinadas, navegação fluida e conteúdo visual de alta qualidade são essenciais.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">UX Premium</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Design</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/20 transition-colors">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Personalização e Curadoria</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    A jornada de compra é altamente personalizada. Ferramentas de comparação, salvamento de favoritos e recomendações baseadas em preferências são diferenciais competitivos.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Personalização</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">IA</span>
                  </div>
                </div>

                <div class="bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/20 transition-colors">
                  <h3 class="text-lg font-medium text-text-primary mb-3">Transparência e Informação</h3>
                  <p class="text-sm text-secondary font-light leading-relaxed mb-4">
                    Compradores demandam acesso completo a informações: plantas, especificações técnicas, análise de localização, histórico de preços e documentação clara.
                  </p>
                  <div class="flex gap-2">
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Dados</span>
                    <span class="text-xs px-2 py-1 bg-action-primary/10 text-action-primary rounded">Transparência</span>
                  </div>
                </div>
              </div>
            </section>

            <!-- Section: Oportunidades -->
            <section id="oportunidades" class="scroll-mt-32 bg-surface-card border border-subtle r rounded-lgounded-lg p-8 shadow-sm rounded-lg">
              <h2 class="text-2xl font-light text-text-primary mb-6">Oportunidades Identificadas</h2>
              
              <div class="grid grid-cols-1 gap-4">
                <div class="group bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/30 transition-colors">
                  <div class="flex items-start justify-between mb-3">
                    <h3 class="text-lg font-medium text-text-primary group-hover:text-action-primary transition-colors">Comparação Inteligente</h3>
                    <span class="text-xs font-mono text-action-primary uppercase tracking-widest">Alta</span>
                  </div>
                  <p class="text-sm text-secondary font-light">
                    Facilitar a decisão complexa de compra permitindo a comparação lado a lado de atributos técnicos e emocionais dos imóveis.
                  </p>
                </div>

                <div class="group bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/30 transition-colors">
                  <div class="flex items-start justify-between mb-3">
                    <h3 class="text-lg font-medium text-text-primary group-hover:text-action-primary transition-colors">Curadoria Visual</h3>
                    <span class="text-xs font-mono text-action-primary uppercase tracking-widest">Alta</span>
                  </div>
                  <p class="text-sm text-secondary font-light">
                    Utilizar o design da interface para valorizar a fotografia e os detalhes arquitetônicos, criando uma galeria aspiracional.
                  </p>
                </div>

                <div class="group bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/30 transition-colors">
                  <div class="flex items-start justify-between mb-3">
                    <h3 class="text-lg font-medium text-text-primary group-hover:text-action-primary transition-colors">Busca Contextual</h3>
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest">Média</span>
                  </div>
                  <p class="text-sm text-secondary font-light">
                    Incorporar contexto de localização, lifestyle e preferências pessoais nos resultados de busca para aumentar relevância.
                  </p>
                </div>

                <div class="group bg-surface-subtle p-6 border rounded-lg border-hairline hover:border-action-primary/30 transition-colors">
                  <div class="flex items-start justify-between mb-3">
                    <h3 class="text-lg font-medium text-text-primary group-hover:text-action-primary transition-colors">Tours Virtuais Imersivos</h3>
                    <span class="text-xs font-mono text-secondary uppercase tracking-widest">Média</span>
                  </div>
                  <p class="text-sm text-secondary font-light">
                    Integração de tecnologias 3D e realidade virtual para permitir visitas remotas com qualidade fotorrealística.
                  </p>
                </div>
              </div>

              <div class="mt-8 bg-action-primary/5 p-6 border-l-4 border-action-primary">
                <h4 class="text-sm font-medium text-text-primary mb-2">Insight Principal</h4>
                <p class="text-sm text-secondary font-light">
                  O mercado de luxo imobiliário está pronto para uma revolução digital que combine sofisticação estética com funcionalidade intuitiva. A oportunidade está em criar experiências que elevem o padrão do setor.
                </p>
              </div>
            </section>

            <!-- Navigation -->
            <div class="pt-8 border-t border-subtle flex justify-between items-center">
              <NuxtLink to="/pesquisa/contexto" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-secondary hover:text-action-primary transition-colors">
                <span class="text-lg">←</span> Voltar para Contexto
              </NuxtLink>
            </div>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>






