<script setup lang="ts">
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
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-action-primary/10 selection:text-text-primary">
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
            <span class="text-text-primary">UI Design</span>
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

    <main class="py-16 relative z-0">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <!-- Sidebar / Title -->
          <div class="lg:col-span-4">
            <div class="sticky top-32">
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 04</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">UI Design</h1>
              <div class="w-12 h-1 bg-mat-stone mb-8"></div>
              <p class="text-secondary text-lg font-light leading-relaxed">
                Sistema de design consolidado: paleta minimalista com fundamentos escuros, claros e acentos de marca.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              
              <!-- Introdução -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8">
                <h3 class="text-2xl font-light mb-2 text-text-primary">Arquitetura do Sistema</h3>
                <p class="text-sm text-secondary font-light leading-relaxed">
                  Organização profissional dividida em duas camadas: 
                  <span class="font-medium text-text-primary">Primitivas</span> (Definição da Cor) e 
                  <span class="font-medium text-text-primary">Semânticas</span> (Aplicação da Cor).
                </p>
              </div>

              <!-- 01. PRIMITIVAS -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-primary">01. Primitives</h3>
                <p class="text-sm text-secondary mb-8 font-light">Global Palette · A Tinta</p>
                
                <!-- The White-to-Platinum Gradient -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">The Light Scale (White → Platinum)</h4>
                  <div class="grid grid-cols-5 gap-4">
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full border-b border-subtle" style="background-color: #FFFFFF;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Pure White</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#FFFFFF</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-0</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #FAFAFA;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Porcelain</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#FAFAFA</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-50</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #F4F4F5;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1 flex items-center gap-2">
                          Mist
                          <span class="px-1.5 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded font-mono">NEW</span>
                        </div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#F4F4F5</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-100</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #E4E4E7;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1 flex items-center gap-2">
                          Chromium
                          <span class="px-1.5 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded font-mono">NEW</span>
                        </div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#E4E4E7</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-200</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #D6D6D8;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Platinum</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#D6D6D8</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-300</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- The Dark Scale -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">The Dark Scale</h4>
                  <div class="grid grid-cols-3 gap-4">
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #121212;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Rich Black</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#121212</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-900</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #2B3A42;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Deep Slate</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#2B3A42</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-800 (Cool)</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #4A4843;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Graphite Stone</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#4A4843</div>
                        <div class="text-[9px] text-secondary mt-1">Gray-700 (Warm)</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Brand & Accent -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">Brand & Accent</h4>
                  <div class="grid grid-cols-4 gap-4">
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #D5500B;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Brand Orange</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#D5500B</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #2B3A42;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Deep Slate</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#2B3A42</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Feedback -->
                <div>
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">Feedback</h4>
                  <div class="grid grid-cols-3 gap-4">
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #00AE42;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Success</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#00AE42</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #FFA400;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Warning</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#FFA400</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #ED3A3D;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-primary mb-1">Error</div>
                        <div class="text-[10px] font-mono text-secondary uppercase">#ED3A3D</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 02. TOKENS SEMÂNTICOS -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-primary">02. Semantic Tokens</h3>
                <p class="text-sm text-secondary mb-8 font-light">Usage · A Função</p>
                
                <!-- Surface -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">Surface (Backgrounds)</h4>
                  <div class="overflow-hidden border border-subtle rounded-lg">
                    <table class="w-full">
                      <thead class="bg-surface-subtle">
                        <tr>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[10%]">Preview</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[25%]">Token Name</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[20%]">Reference</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[45%]">Usage Guidelines</th>
                        </tr>
                      </thead>
                      <tbody class="bg-surface-base">
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-subtle" style="background-color: #FAFAFA;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">surface-base</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Porcelain</td>
                          <td class="px-4 py-4 text-sm text-secondary">Cor de fundo padrão da página (body). Evita fadiga visual.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-subtle" style="background-color: #FFFFFF;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">surface-card</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Pure White</td>
                          <td class="px-4 py-4 text-sm text-secondary">Cards, Modais e painéis flutuantes para criar elevação.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-subtle" style="background-color: #F4F4F5;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              surface-subtle
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">NEW</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Mist</td>
                          <td class="px-4 py-4 text-sm text-secondary">Sidebars, áreas secundárias e hovers sutis.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-subtle" style="background-color: #D6D6D8;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">surface-offset</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Platinum</td>
                          <td class="px-4 py-4 text-sm text-secondary">Seções com contraste médio, estados disabled.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- Typography -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">Typography</h4>
                  <div class="overflow-hidden border border-subtle rounded-lg">
                    <table class="w-full">
                      <thead class="bg-surface-subtle">
                        <tr>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[10%]">Preview</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[25%]">Token Name</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[20%]">Reference</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[45%]">Usage</th>
                        </tr>
                      </thead>
                      <tbody class="bg-surface-base">
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-bold text-text-primary">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">text-text-primary</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Rich Black</td>
                          <td class="px-4 py-4 text-sm text-secondary">Títulos, cabeçalhos e corpo de texto principal. Máxima legibilidade.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-semibold text-secondary">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">text-secondary</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Graphite Stone</td>
                          <td class="px-4 py-4 text-sm text-secondary">Subtítulos, legendas e textos de apoio. Menor peso visual.</td>
                        </tr>
                        <tr class="border-t border-subtle" style="background-color: #121212;">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-semibold" style="color: #FFFFFF;">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 rounded text-xs font-mono" style="background-color: rgba(255,255,255,0.1); color: #D6D6D8;">text-inverse</span>
                          </td>
                          <td class="px-4 py-4 text-sm" style="color: #D6D6D8;">Pure White</td>
                          <td class="px-4 py-4 text-sm" style="color: #D6D6D8;">Texto sobre fundos escuros (Botões, Hero, Footer).</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-semibold text-text-link">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">text-link</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Brand Orange</td>
                          <td class="px-4 py-4 text-sm text-secondary">Links, CTAs textuais ou palavras em destaque (usar com moderação).</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- Borders & Dividers -->
                <div>
                  <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-4">Borders & Dividers</h4>
                  <div class="overflow-hidden border border-subtle rounded-lg">
                    <table class="w-full">
                      <thead class="bg-surface-subtle">
                        <tr>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[10%]">Preview</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[25%]">Token Name</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[20%]">Reference</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[45%]">Usage</th>
                        </tr>
                      </thead>
                      <tbody class="bg-surface-base">
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border bg-surface-base" style="border-color: #F4F4F5;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              border-hairline
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">NEW</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Mist</td>
                          <td class="px-4 py-4 text-sm text-secondary">Divisões quase invisíveis, separadores sutis em tabelas.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border bg-surface-base" style="border-color: #E4E4E7;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              border-subtle
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">UPD</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Chromium</td>
                          <td class="px-4 py-4 text-sm text-secondary">Bordas padrão de cards, inputs inativos e divisórias.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border bg-surface-base" style="border-color: #D6D6D8;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              border-strong
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">NEW</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Platinum</td>
                          <td class="px-4 py-4 text-sm text-secondary">Divisões com contraste, bordas de destaque estrutural.</td>
                        </tr>
                        <tr class="border-t border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border-2 bg-surface-base" style="border-color: #121212;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">border-focus</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-secondary">Rich Black</td>
                          <td class="px-4 py-4 text-sm text-secondary">Inputs ativos, focos ou bordas que exigem máxima atenção.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>

              <!-- Border Radius -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-primary">Border Radius</h3>
                <p class="text-sm text-secondary mb-8 font-light">Hierarquia de arredondamento para cards e elementos</p>
                
                <div class="overflow-hidden border border-subtle rounded-lg">
                  <table class="w-full">
                    <thead class="bg-surface-subtle">
                      <tr>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[15%]">Preview</th>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[20%]">Class</th>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[15%]">Value</th>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-secondary w-[50%]">Usage</th>
                      </tr>
                    </thead>
                    <tbody class="bg-surface-base">
                      <tr class="border-t border-subtle">
                        <td class="px-4 py-4">
                          <div class="w-16 h-16 bg-surface-subtle border border-subtle rounded-lg"></div>
                        </td>
                        <td class="px-4 py-4">
                          <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">rounded-lg</span>
                        </td>
                        <td class="px-4 py-4 text-sm font-mono text-secondary">8px</td>
                        <td class="px-4 py-4 text-sm text-secondary">Cards padrão, containers principais, modais.</td>
                      </tr>
                      <tr class="border-t border-subtle">
                        <td class="px-4 py-4">
                          <div class="w-16 h-16 bg-surface-subtle border border-subtle rounded-xl"></div>
                        </td>
                        <td class="px-4 py-4">
                          <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">rounded-lg</span>
                        </td>
                        <td class="px-4 py-4 text-sm font-mono text-secondary">12px</td>
                        <td class="px-4 py-4 text-sm text-secondary">Cards grandes, hero sections, painéis destacados.</td>
                      </tr>
                      <tr class="border-t border-subtle">
                        <td class="px-4 py-4">
                          <div class="w-16 h-16 bg-surface-subtle border border-subtle rounded-2xl"></div>
                        </td>
                        <td class="px-4 py-4">
                          <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">rounded-2xl</span>
                        </td>
                        <td class="px-4 py-4 text-sm font-mono text-secondary">16px</td>
                        <td class="px-4 py-4 text-sm text-secondary">Elementos especiais, imagens destacadas, containers de nível superior.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Typography -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-primary">Tipografia</h3>
                <p class="text-sm text-secondary mb-8 font-light">Hierarquia tipográfica completa</p>
                
                <div class="space-y-10">
                  
                  <!-- Famílias de Fonte -->
                  <div>
                    <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-6">Famílias de Fonte</h4>
                    <div class="space-y-6">
                      
                      <!-- Inter (Primária) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-brand-orange">
                        <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-2">Primária · Inter</div>
                        <p class="text-2xl font-sans text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-secondary">Fonte principal · UI, Corpo de texto e Elementos técnicos</p>
                      </div>

                      <!-- Matter SQ (Display) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-text-secondary">
                        <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-2">Display · Matter SQ</div>
                        <p class="text-2xl font-display text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-secondary">Branding corporativo · Títulos padrão</p>
                      </div>

                      <!-- Playfair Display (Luxury Extension) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-text-primary">
                        <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-2">Luxury Extension · Playfair Display</div>
                        <p class="text-2xl font-playfair text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-secondary">Editorial e Curadoria · Títulos emocionais</p>
                      </div>

                      <!-- Roboto (Terciária) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-strong">
                        <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-2">Terciária · Roboto</div>
                        <p class="text-2xl font-roboto text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-secondary">Alternativa · Elementos legados</p>
                      </div>

                      <!-- Monospace -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-strong">
                        <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-2">Código · Monospace</div>
                        <p class="text-lg font-mono text-text-primary mb-2">console.log("Hello World")</p>
                        <p class="text-xs text-secondary">Dados técnicos · Código e valores</p>
                      </div>

                    </div>
                  </div>

                  <!-- Pesos de Fonte -->
                  <div>
                    <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-6">Pesos de Fonte</h4>
                    
                    <!-- Inter -->
                    <div class="mb-6">
                      <h5 class="text-xs font-medium text-text-primary mb-3">Inter (Functional)</h5>
                      <div class="grid grid-cols-2 gap-4">
                        <div class="p-3 bg-surface-subtle">
                          <div class="text-base font-thin text-text-primary mb-1">Thin (100)</div>
                          <div class="text-xs font-mono text-secondary">Títulos "High Luxury"</div>
                        </div>
                        <div class="p-3 bg-surface-subtle">
                          <div class="text-base font-light text-text-primary mb-1">Light (300)</div>
                          <div class="text-xs font-mono text-secondary">Corpo de texto principal</div>
                        </div>
                        <div class="p-3 bg-surface-subtle">
                          <div class="text-base font-normal text-text-primary mb-1">Regular (400)</div>
                          <div class="text-xs font-mono text-secondary">Padrão para UI</div>
                        </div>
                        <div class="p-3 bg-surface-subtle">
                          <div class="text-base font-semibold text-text-primary mb-1">Semibold (600)</div>
                          <div class="text-xs font-mono text-secondary">Subtítulos e botões</div>
                        </div>
                      </div>
                    </div>

                    <!-- Playfair Display -->
                    <div>
                      <h5 class="text-xs font-medium text-text-primary mb-3">Playfair Display (Emotional)</h5>
                      <div class="grid grid-cols-2 gap-4">
                        <div class="p-3 bg-surface-subtle">
                          <div class="text-base font-playfair font-normal text-text-primary mb-1">Regular (400)</div>
                          <div class="text-xs font-mono text-secondary">Títulos de destaque</div>
                        </div>
                        <div class="p-3 bg-surface-subtle">
                          <div class="text-base font-playfair italic text-text-primary mb-1">Italic (400)</div>
                          <div class="text-xs font-mono text-secondary">Palavras-chave (Mix & Match)</div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Luxury Compositions -->
                  <div>
                    <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-6">Luxury Compositions (Mix & Match)</h4>
                    <div class="p-8 bg-surface-subtle border border-subtle rounded-lg text-center">
                      <div class="mb-2">
                        <span class="font-sans font-thin uppercase tracking-[0.2em] text-sm text-text-primary">The</span>
                      </div>
                      <div class="mb-2">
                        <span class="font-playfair italic text-4xl text-text-primary">Pilar Homes</span>
                      </div>
                      <div class="mb-6">
                        <span class="font-sans font-thin uppercase tracking-[0.2em] text-sm text-text-primary">Collection</span>
                      </div>
                      <p class="text-xs text-secondary max-w-md mx-auto">
                        Estratégia de combinação: Camada Estrutural (Inter Thin Uppercase) + Camada Emocional (Playfair Italic).
                      </p>
                    </div>
                  </div>

                  <!-- Escala de Tamanhos -->
                  <div>
                    <h4 class="text-xs font-mono text-secondary uppercase tracking-widest mb-6">Escala de Tamanhos</h4>
                    <div class="space-y-3">
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-xs text-text-primary">text-xs</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">12px · 0.75rem</span>
                        <span class="text-xs text-secondary">Labels, captions</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-sm text-text-primary">text-sm</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">14px · 0.875rem</span>
                        <span class="text-xs text-secondary">Textos pequenos</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-base text-text-primary">text-base</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">16px · 1rem</span>
                        <span class="text-xs text-secondary">Corpo principal</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-lg text-text-primary">text-lg</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">18px · 1.125rem</span>
                        <span class="text-xs text-secondary">Textos destacados</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-xl text-text-primary">text-xl</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">20px · 1.25rem</span>
                        <span class="text-xs text-secondary">Subtítulos pequenos</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-2xl text-text-primary">text-2xl</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">24px · 1.5rem</span>
                        <span class="text-xs text-secondary">Títulos de seção</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-subtle pb-2">
                        <span class="text-3xl text-text-primary">text-3xl</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">30px · 1.875rem</span>
                        <span class="text-xs text-secondary">Títulos principais</span>
                      </div>
                      <div class="flex items-baseline justify-between pb-2">
                        <span class="text-5xl text-text-primary">text-5xl</span>
                        <span class="text-xs font-mono text-secondary mr-auto ml-4">48px · 3rem</span>
                        <span class="text-xs text-secondary">Display / Hero</span>
                      </div>
                    </div>
                  </div>

                </div>
              </div>
              <!-- Atomic Design Components -->
              <div class="bg-surface-card border rounded-lg border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-6 text-text-primary">Componentes - Atomic Design</h3>
                
                <!-- Comparison Floating Bar Component -->
                <div class="mb-12">
                  <h4 class="text-xl font-light mb-4 text-text-primary flex items-center gap-2">
                    <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">Molecule</span>
                    Barra de Comparação Flutuante
                  </h4>
                  
                  <div class="mb-6">
                    <h5 class="text-base font-medium text-text-primary mb-3">Descrição</h5>
                    <p class="text-sm text-secondary font-light leading-relaxed">
                      Componente que permite ao usuário selecionar múltiplos imóveis para comparação side-by-side. 
                      A barra aparece de forma persistente na parte inferior da tela e se expande em um modal quando 
                      dois ou mais imóveis são selecionados.
                    </p>
                  </div>
                  
                  <div class="mb-6">
                    <h5 class="text-base font-medium text-text-primary mb-3">Estrutura Atômica</h5>
                    <ul class="text-sm text-secondary font-light space-y-2">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span><strong class="text-text-primary">Átomos:</strong> Botões (adicionar, remover, comparar), ícones, imagens de miniatura, texto de contagem</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span><strong class="text-text-primary">Moléculas:</strong> Avatar de propriedade com imagem e ícone de remoção, grupo de botões de ação</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span><strong class="text-text-primary">Organismos:</strong> Barra flutuante completa (Contendo avatares, botões e rótulos)</span>
                      </li>
                    </ul>
                  </div>
                  
                  <div class="mb-6">
                    <h5 class="text-base font-medium text-text-primary mb-3">Passo a Passo de Interações</h5>
                    <div class="space-y-4">
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">1</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Visualização Inicial</h6>
                          <p class="text-sm text-secondary font-light mb-3">Barra aparece na parte inferior da tela com espaço para selecionar até 4 imóveis</p>
                          <div class="p-4 bg-surface-card rounded-lg border border-border-subtle inline-block">
                            <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 w-auto justify-between md:justify-start">
                              <div class="flex flex-col">
                                <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
                                <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-secondary mt-1">0 de 4</span>
                              </div>
                              <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                              </div>
                              <button class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium bg-surface-offset/50 text-text-secondary/50 backdrop-blur-sm ml-2 cursor-not-allowed">
                                Comparar
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">2</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Adição de Imóvel</h6>
                          <p class="text-sm text-secondary font-light mb-3">Usuário seleciona um imóvel (checkbox ou botão) e o avatar do imóvel aparece na barra</p>
                          <div class="p-4 bg-surface-card rounded-lg border border-border-subtle inline-block">
                            <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 w-auto justify-between md:justify-start">
                              <div class="flex flex-col">
                                <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
                                <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-secondary mt-1">1 de 4</span>
                              </div>
                              <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative overflow-hidden bg-surface-offset shadow-md">
                                  <div class="w-full h-full bg-gradient-to-br from-brand-orange to-mat-stone rounded-full flex items-center justify-center text-white font-bold">A</div>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                              </div>
                              <button class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium bg-surface-offset/50 text-text-secondary/50 backdrop-blur-sm ml-2 cursor-not-allowed">
                                Comparar
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">3</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Expansão</h6>
                          <p class="text-sm text-secondary font-light mb-3">Ao selecionar 2 ou mais imóveis, o botão "Comparar" é habilitado e a barra permanece visível</p>
                          <div class="p-4 bg-surface-card rounded-lg border border-border-subtle inline-block">
                            <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 w-auto justify-between md:justify-start">
                              <div class="flex flex-col">
                                <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
                                <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-secondary mt-1">2 de 4</span>
                              </div>
                              <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative overflow-hidden bg-surface-offset shadow-md">
                                  <div class="w-full h-full bg-gradient-to-br from-brand-orange to-mat-stone rounded-full flex items-center justify-center text-white font-bold">A</div>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative overflow-hidden bg-surface-offset shadow-md">
                                  <div class="w-full h-full bg-gradient-to-br from-mat-stone to-surface-offset rounded-full flex items-center justify-center text-white font-bold">B</div>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                              </div>
                              <button class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium bg-text-primary text-white ml-2 transform shadow-md hover:bg-text-primary/90">
                                Comparar
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">4</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Comparação</h6>
                          <p class="text-sm text-secondary font-light mb-3">Ao clicar em "Comparar", um modal se abre mostrando os imóveis lado a lado</p>
                          <div class="p-4 bg-surface-card rounded-lg border border-border-subtle inline-block">
                            <div class="w-80 h-64 bg-surface-subtle rounded-lg border border-border-subtle flex items-center justify-center">
                              <div class="text-center">
                                <i class="lni lni-stats-up text-3xl text-text-secondary mb-2"></i>
                                <p class="text-sm text-text-secondary font-light">Modal de Comparação</p>
                                <p class="text-xs text-text-tertiary mt-1">Visualização side-by-side</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">5</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Remoção</h6>
                          <p class="text-sm text-secondary font-light mb-3">Usuário pode remover imóveis da comparação clicando no ícone de remoção</p>
                          <div class="p-4 bg-surface-card rounded-lg border border-border-subtle inline-block">
                            <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 w-auto justify-between md:justify-start">
                              <div class="flex flex-col">
                                <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
                                <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-secondary mt-1">1 de 4</span>
                              </div>
                              <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative overflow-hidden bg-surface-offset shadow-md">
                                  <div class="w-full h-full bg-gradient-to-br from-brand-orange to-mat-stone rounded-full flex items-center justify-center text-white font-bold">A</div>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                                <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner">
                                  <i class="lni lni-plus text-sm"></i>
                                </div>
                              </div>
                              <button class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium bg-surface-offset/50 text-text-secondary/50 backdrop-blur-sm ml-2 cursor-not-allowed">
                                Comparar
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="p-6 bg-surface-subtle rounded-lg border border-hairline">
                    <h5 class="text-base font-medium text-text-primary mb-3">Preview Funcional</h5>
                    <div class="flex items-center justify-center h-40 bg-surface-card rounded-lg border border-border-subtle relative">
                      <div class="flex flex-col items-center gap-2 w-full max-w-md">
                        <div class="backdrop-blur-xl bg-white/80 text-text-primary rounded-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center py-2 md:py-3 pl-4 md:pl-6 pr-2 md:pr-3 gap-3 md:gap-6 border border-white/60 ring-1 ring-black/5 relative w-full md:w-auto justify-between md:justify-start">
                          <div class="flex flex-col">
                            <span class="font-serif italic text-base md:text-lg leading-none text-text-primary whitespace-nowrap">Sua Seleção</span>
                            <span class="text-[8px] md:text-[9px] uppercase tracking-widest text-text-secondary mt-1">2 de 4</span>
                          </div>
                          <div class="flex items-center -space-x-2 md:-space-x-3 pl-2 md:pl-4">
                            <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative group cursor-pointer overflow-hidden bg-surface-offset shadow-md hover:shadow-lg transition-all hover:scale-105">
                              <div class="w-full h-full bg-gradient-to-br from-brand-orange to-mat-stone rounded-full flex items-center justify-center text-white font-bold">A</div>
                              <!-- Hover Remove Icon -->
                              <div class="absolute inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all">
                                <i class="lni lni-minus text-white text-xs md:text-lg"></i>
                              </div>
                            </div>
                            <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-white relative group cursor-pointer overflow-hidden bg-surface-offset shadow-md hover:shadow-lg transition-all hover:scale-105">
                              <div class="w-full h-full bg-gradient-to-br from-mat-stone to-surface-offset rounded-full flex items-center justify-center text-white font-bold">B</div>
                              <!-- Hover Remove Icon -->
                              <div class="absolute inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all">
                                <i class="lni lni-minus text-white text-xs md:text-lg"></i>
                              </div>
                            </div>
                            <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner transition-all">
                              <i class="lni lni-plus text-sm"></i>
                            </div>
                            <div class="w-8 h-8 md:w-12 md:h-12 rounded-full border-2 border-border-subtle bg-surface-offset/40 backdrop-blur-sm flex items-center justify-center text-text-secondary/40 shadow-inner transition-all">
                              <i class="lni lni-plus text-sm"></i>
                            </div>
                          </div>
                          <button class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium bg-text-primary text-white hover:bg-text-primary/90 hover:scale-105 hover:shadow-lg active:scale-95 ml-2 transform shadow-md transition-all duration-300">
                            Comparar
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Property Card Component -->
                <div>
                  <h4 class="text-xl font-light mb-4 text-text-primary flex items-center gap-2">
                    <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">Organism</span>
                    Cards de Imóveis (Vertical e Horizontal)
                  </h4>
                  
                  <div class="mb-6">
                    <h5 class="text-base font-medium text-text-primary mb-3">Descrição</h5>
                    <p class="text-sm text-secondary font-light leading-relaxed">
                      Componente para exibição de informações de imóveis em diferentes layouts. 
                      Disponível em versão vertical (padrão para listagens) e horizontal (para comparação e detalhes).
                    </p>
                  </div>
                  
                  <div class="mb-6">
                    <h5 class="text-base font-medium text-text-primary mb-3">Estrutura Atômica</h5>
                    <ul class="text-sm text-secondary font-light space-y-2">
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span><strong class="text-text-primary">Átomos:</strong> Imagem, texto de título, preço, especificações, ícones</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span><strong class="text-text-primary">Moléculas:</strong> Cabeçalho com nome e localização, rodapé com preço e avatar do agente</span>
                      </li>
                      <li class="flex items-start gap-2">
                        <span class="text-action-primary mt-1">•</span>
                        <span><strong class="text-text-primary">Organismos:</strong> Card completo de imóvel (contendo imagem, conteúdo e rodapé)</span>
                      </li>
                    </ul>
                  </div>
                  
                  <div class="mb-6">
                    <h5 class="text-base font-medium text-text-primary mb-3">Passo a Passo de Interações</h5>
                    <div class="space-y-4">
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">1</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Visualização Padrão</h6>
                          <p class="text-sm text-secondary font-light mb-3">Card exibe imagem, nome do imóvel, bairro, especificações e preço</p>
                          <div class="bg-surface-card rounded-lg border border-border-subtle p-4 inline-block">
                            <div class="flex flex-col relative">
                              <!-- Image Container -->
                              <div class="relative overflow-hidden rounded bg-surface-offset h-48">
                                <div class="w-full h-full bg-gradient-to-br from-brand-orange/20 to-mat-stone/20 flex items-center justify-center">
                                  <div class="text-center p-4">
                                    <i class="lni lni-home text-3xl text-text-secondary mb-2 block"></i>
                                    <span class="text-xs text-text-secondary font-medium">Imagem do Imóvel</span>
                                  </div>
                                </div>
                              </div>
                              
                              <!-- Content -->
                              <div class="pt-4">
                                <!-- Meta Row -->
                                <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
                                  <span class="text-text-tertiary">Vila Madalena</span>
                                  <span class="text-text-tertiary/60">REF: 001</span>
                                </div>
                                
                                <!-- Property Name -->
                                <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
                                  Cobertura Exclusiva
                                </h3>
                                
                                <!-- Specs -->
                                <p class="font-mono text-xs text-text-secondary mt-1">280m² | 4 suítes | 4 vagas</p>
                                
                                <!-- Footer -->
                                <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
                                  <span class="font-bold text-sm text-text-primary">R$ 2.800.000</span>
                                  
                                  <!-- Agent Avatar -->
                                  <div class="flex items-center gap-2">
                                    <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
                                      <span class="text-text-tertiary text-[9px] font-medium">J</span>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">2</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Hover</h6>
                          <p class="text-sm text-secondary font-light mb-3">Ao passar o mouse, botão de ação (salvar) aparece no canto superior direito</p>
                          <div class="bg-surface-card rounded-lg border border-border-subtle p-4 inline-block">
                            <div class="group flex flex-col relative">
                              <!-- Image Container -->
                              <div class="relative overflow-hidden rounded bg-surface-offset h-48">
                                <div class="w-full h-full bg-gradient-to-br from-brand-orange/20 to-mat-stone/20 flex items-center justify-center">
                                  <div class="text-center p-4">
                                    <i class="lni lni-home text-3xl text-text-secondary mb-2 block"></i>
                                    <span class="text-xs text-text-secondary font-medium">Imagem do Imóvel</span>
                                  </div>
                                </div>
                                
                                <!-- Hover Actions (always visible for demo purposes) -->
                                <div class="absolute top-3 right-3">
                                  <button class="w-9 h-9 bg-surface-card/90 backdrop-blur-sm rounded-full flex items-center justify-center text-text-secondary hover:text-text-primary hover:bg-surface-card">
                                    <i class="lni lni-heart text-base"></i>
                                  </button>
                                </div>
                              </div>
                              
                              <!-- Content -->
                              <div class="pt-4">
                                <!-- Meta Row -->
                                <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
                                  <span class="text-text-tertiary">Vila Madalena</span>
                                  <span class="text-text-tertiary/60">REF: 001</span>
                                </div>
                                
                                <!-- Property Name -->
                                <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
                                  Cobertura Exclusiva
                                </h3>
                                
                                <!-- Specs -->
                                <p class="font-mono text-xs text-text-secondary mt-1">280m² | 4 suítes | 4 vagas</p>
                                
                                <!-- Footer -->
                                <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
                                  <span class="font-bold text-sm text-text-primary">R$ 2.800.000</span>
                                  
                                  <!-- Agent Avatar -->
                                  <div class="flex items-center gap-2">
                                    <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
                                      <span class="text-text-tertiary text-[9px] font-medium">J</span>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">3</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Modo Seleção</h6>
                          <p class="text-sm text-secondary font-light mb-3">Checkbox aparece no canto superior esquerdo para adicionar à comparação</p>
                          <div class="bg-surface-card rounded-lg border border-border-subtle p-4 inline-block">
                            <div class="flex flex-col relative">
                              <!-- Selection Overlay -->
                              <div class="absolute inset-0 z-20 rounded border-2 border-transparent bg-text-primary/5"></div>
                              
                              <!-- Image Container -->
                              <div class="relative overflow-hidden rounded bg-surface-offset h-48">
                                <div class="w-full h-full bg-gradient-to-br from-brand-orange/20 to-mat-stone/20 flex items-center justify-center">
                                  <div class="text-center p-4">
                                    <i class="lni lni-home text-3xl text-text-secondary mb-2 block"></i>
                                    <span class="text-xs text-text-secondary font-medium">Imagem do Imóvel</span>
                                  </div>
                                </div>
                                
                                <!-- Selection Checkbox -->
                                <div class="absolute top-3 left-3 z-30">
                                  <div class="w-6 h-6 rounded-full border bg-text-primary border-text-primary text-surface-base flex items-center justify-center">
                                    <i class="lni lni-checkmark text-xs font-bold"></i>
                                  </div>
                                </div>
                              </div>
                              
                              <!-- Content -->
                              <div class="pt-4">
                                <!-- Meta Row -->
                                <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
                                  <span class="text-text-tertiary">Vila Madalena</span>
                                  <span class="text-text-tertiary/60">REF: 001</span>
                                </div>
                                
                                <!-- Property Name -->
                                <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
                                  Cobertura Exclusiva
                                </h3>
                                
                                <!-- Specs -->
                                <p class="font-mono text-xs text-text-secondary mt-1">280m² | 4 suítes | 4 vagas</p>
                                
                                <!-- Footer -->
                                <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
                                  <span class="font-bold text-sm text-text-primary">R$ 2.800.000</span>
                                  
                                  <!-- Agent Avatar -->
                                  <div class="flex items-center gap-2">
                                    <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
                                      <span class="text-text-tertiary text-[9px] font-medium">J</span>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">4</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Seleção</h6>
                          <p class="text-sm text-secondary font-light mb-3">Ao selecionar, o card é marcado e adicionado à barra de comparação</p>
                          <div class="bg-surface-card rounded-lg border border-border-subtle p-4 inline-block">
                            <div class="flex flex-col relative">
                              <!-- Selection Overlay -->
                              <div class="absolute inset-0 z-20 rounded border-2 border-transparent bg-text-primary/5"></div>
                              
                              <!-- Image Container -->
                              <div class="relative overflow-hidden rounded bg-surface-offset h-48">
                                <div class="w-full h-full bg-gradient-to-br from-brand-orange/20 to-mat-stone/20 flex items-center justify-center">
                                  <div class="text-center p-4">
                                    <i class="lni lni-home text-3xl text-text-secondary mb-2 block"></i>
                                    <span class="text-xs text-text-secondary font-medium">Imagem do Imóvel</span>
                                  </div>
                                </div>
                                
                                <!-- Selection Checkbox -->
                                <div class="absolute top-3 left-3 z-30">
                                  <div class="w-6 h-6 rounded-full border bg-text-primary border-text-primary text-surface-base flex items-center justify-center">
                                    <i class="lni lni-checkmark text-xs font-bold"></i>
                                  </div>
                                </div>
                              </div>
                              
                              <!-- Content -->
                              <div class="pt-4">
                                <!-- Meta Row -->
                                <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
                                  <span class="text-text-tertiary">Vila Madalena</span>
                                  <span class="text-text-tertiary/60">REF: 001</span>
                                </div>
                                
                                <!-- Property Name -->
                                <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
                                  Cobertura Exclusiva
                                </h3>
                                
                                <!-- Specs -->
                                <p class="font-mono text-xs text-text-secondary mt-1">280m² | 4 suítes | 4 vagas</p>
                                
                                <!-- Footer -->
                                <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
                                  <span class="font-bold text-sm text-text-primary">R$ 2.800.000</span>
                                  
                                  <!-- Agent Avatar -->
                                  <div class="flex items-center gap-2">
                                    <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
                                      <span class="text-text-tertiary text-[9px] font-medium">J</span>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex items-start gap-4 p-4 bg-surface-subtle rounded-lg border border-hairline">
                        <span class="text-lg font-bold text-action-primary bg-surface-card w-8 h-8 rounded-full flex items-center justify-center">5</span>
                        <div class="flex-1">
                          <h6 class="font-medium text-text-primary">Clique</h6>
                          <p class="text-sm text-secondary font-light mb-3">Ao clicar no card (fora da seleção), usuário é levado à página de detalhes</p>
                          <div class="bg-surface-card rounded-lg border border-border-subtle p-4 inline-block">
                            <div class="flex flex-col relative">
                              <!-- Image Container -->
                              <div class="relative overflow-hidden rounded bg-surface-offset h-48">
                                <div class="w-full h-full bg-gradient-to-br from-brand-orange/20 to-mat-stone/20 flex items-center justify-center">
                                  <div class="text-center p-4">
                                    <i class="lni lni-home text-3xl text-text-secondary mb-2 block"></i>
                                    <span class="text-xs text-text-secondary font-medium">Imagem do Imóvel</span>
                                  </div>
                                </div>
                              </div>
                              
                              <!-- Content -->
                              <div class="pt-4">
                                <!-- Meta Row -->
                                <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
                                  <span class="text-text-tertiary">Vila Madalena</span>
                                  <span class="text-text-tertiary/60">REF: 001</span>
                                </div>
                                
                                <!-- Property Name -->
                                <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
                                  Cobertura Exclusiva
                                </h3>
                                
                                <!-- Specs -->
                                <p class="font-mono text-xs text-text-secondary mt-1">280m² | 4 suítes | 4 vagas</p>
                                
                                <!-- Footer -->
                                <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
                                  <span class="font-bold text-sm text-text-primary">R$ 2.800.000</span>
                                  
                                  <!-- Agent Avatar -->
                                  <div class="flex items-center gap-2">
                                    <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
                                      <span class="text-text-tertiary text-[9px] font-medium">J</span>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Vertical Card -->
                  <div class="mb-6">
                    <h6 class="text-sm font-medium text-text-primary mb-3">Versão Vertical</h6>
                    <div class="bg-surface-card rounded-lg border border-border-subtle p-4">
                      <div class="flex flex-col relative">
                        <!-- Image Container -->
                        <div class="relative overflow-hidden rounded bg-surface-offset h-64">
                          <div class="w-full h-full bg-gradient-to-br from-brand-orange/20 to-mat-stone/20 flex items-center justify-center">
                            <div class="text-center p-4">
                              <i class="lni lni-home text-3xl text-text-secondary mb-2 block"></i>
                              <span class="text-xs text-text-secondary font-medium">Imagem do Imóvel</span>
                            </div>
                          </div>
                        </div>
                        
                        <!-- Content -->
                        <div class="pt-4">
                          <!-- Meta Row -->
                          <div class="flex justify-between items-center text-[9px] uppercase tracking-widest mb-2">
                            <span class="text-text-tertiary">Vila Madalena</span>
                            <span class="text-text-tertiary/60">REF: 001</span>
                          </div>
                          
                          <!-- Property Name -->
                          <h3 class="font-light text-text-primary leading-tight tracking-tight text-base">
                            Cobertura Exclusiva com Vista Deslumbrante
                          </h3>
                          
                          <!-- Specs -->
                          <p class="font-mono text-xs text-text-secondary mt-1">280m² | 4 suítes | 4 vagas</p>
                          
                          <!-- Footer -->
                          <div class="flex justify-between items-center pt-3 mt-3 border-t border-border-subtle">
                            <span class="font-bold text-sm text-text-primary">R$ 2.800.000</span>
                            
                            <!-- Agent Avatar -->
                            <div class="flex items-center gap-2">
                              <div class="w-6 h-6 bg-surface-offset rounded-full flex items-center justify-center">
                                <span class="text-text-tertiary text-[9px] font-medium">J</span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Horizontal Card -->
                  <div>
                    <h6 class="text-sm font-medium text-text-primary mb-3">Versão Horizontal</h6>
                    <div class="bg-surface-card rounded-lg border border-border-subtle p-4">
                      <div class="flex items-center gap-4">
                        <!-- Image -->
                        <div class="flex-shrink-0 w-32 h-32 rounded overflow-hidden bg-surface-offset">
                          <div class="w-full h-full bg-gradient-to-br from-mat-stone/30 to-brand-orange/20 flex items-center justify-center">
                            <i class="lni lni-home text-2xl text-text-secondary"></i>
                          </div>
                        </div>
                        
                        <!-- Content -->
                        <div class="flex-grow min-w-0">
                          <div class="flex justify-between items-start">
                            <div>
                              <h3 class="font-medium text-text-primary leading-tight text-sm">
                                Apartamento Moderno
                              </h3>
                              <p class="text-[10px] text-text-secondary mt-1 uppercase tracking-wider">Jardins</p>
                            </div>
                            <button class="text-text-secondary hover:text-status-error ml-2">
                              <i class="lni lni-trash-can text-sm"></i>
                            </button>
                          </div>
                          
                          <p class="font-mono text-xs text-text-secondary mt-2">160m² | 3 suítes | 2 vagas</p>
                          
                          <div class="mt-2">
                            <p class="text-xs text-text-secondary font-bold">R$ 1.450.000</p>
                          </div>
                          
                          <div class="flex items-center gap-2 mt-2">
                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-surface-subtle text-text-secondary border border-border-subtle whitespace-nowrap">
                              Segurança 24h
                            </span>
                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-surface-subtle text-text-secondary border border-border-subtle whitespace-nowrap">
                              Concierge
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>








