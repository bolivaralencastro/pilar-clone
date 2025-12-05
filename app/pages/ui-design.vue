<script setup lang="ts">
</script>

<template>
  <div class="min-h-screen bg-porcelain text-text-text-primary selection:bg-action-primary/10 selection:text-text-text-primary">
    <!-- Header -->
    <header class="bg-white border-b border-border-subtle">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12 h-20 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="flex items-center gap-2 group">
            <img src="/images/logo-pilar.svg" alt="Pilar Homes" class="h-6 w-auto" />
          </NuxtLink>
          <div class="h-4 w-px bg-border-subtle"></div>
          <nav class="flex items-center gap-2 text-xs font-mono tracking-widest uppercase">
            <NuxtLink to="/" class="text-text-secondary hover:text-text-text-primary transition-colors">Home</NuxtLink>
            <span class="text-border-subtle">/</span>
            <span class="text-text-text-primary">UI Design</span>
          </nav>
        </div>
        <div class="text-xs font-mono text-action-primary tracking-widest uppercase">Bolívar Alencastro</div>
      </div>
    </header>

    <main class="py-16">
      <div class="max-w-[1400px] mx-auto px-6 lg:px-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <!-- Sidebar / Title -->
          <div class="lg:col-span-4">
            <div class="sticky top-32">
              <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Fase 04</span>
              <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-text-primary">UI Design</h1>
              <div class="w-12 h-1 bg-rich-black mb-8"></div>
              <p class="text-text-secondary text-lg font-light leading-relaxed">
                Sistema de design consolidado: paleta minimalista com fundamentos escuros, claros e acentos de marca.
              </p>
            </div>
          </div>

          <!-- Content -->
          <div class="lg:col-span-7 lg:col-start-6">
            <div class="space-y-12">
              
              <!-- Introdução -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8">
                <h3 class="text-2xl font-light mb-2 text-text-text-primary">Arquitetura do Sistema</h3>
                <p class="text-sm text-text-secondary font-light leading-relaxed">
                  Organização profissional dividida em duas camadas: 
                  <span class="font-medium text-text-text-primary">Primitivas</span> (Definição da Cor) e 
                  <span class="font-medium text-text-text-primary">Semânticas</span> (Aplicação da Cor).
                </p>
              </div>

              <!-- 01. PRIMITIVAS -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-text-primary">01. Primitives</h3>
                <p class="text-sm text-text-secondary mb-8 font-light">Global Palette · A Tinta</p>
                
                <!-- The White-to-Platinum Gradient -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">The Light Scale (White → Platinum)</h4>
                  <div class="grid grid-cols-5 gap-4">
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full border-b border-border-subtle" style="background-color: #FFFFFF;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Pure White</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#FFFFFF</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-0</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #FAFAFA;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Porcelain</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#FAFAFA</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-50</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #F4F4F5;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1 flex items-center gap-2">
                          Mist
                          <span class="px-1.5 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded font-mono">NEW</span>
                        </div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#F4F4F5</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-100</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #E4E4E7;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1 flex items-center gap-2">
                          Chromium
                          <span class="px-1.5 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded font-mono">NEW</span>
                        </div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#E4E4E7</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-200</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #D6D6D8;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Platinum</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#D6D6D8</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-300</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- The Dark Scale -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">The Dark Scale</h4>
                  <div class="grid grid-cols-3 gap-4">
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #121212;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Rich Black</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#121212</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-900</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #2B3A42;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Deep Slate</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#2B3A42</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-800 (Cool)</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #4A4843;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Graphite Stone</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#4A4843</div>
                        <div class="text-[9px] text-text-secondary mt-1">Gray-700 (Warm)</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Brand & Accent -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">Brand & Accent</h4>
                  <div class="grid grid-cols-4 gap-4">
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #D5500B;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Brand Orange</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#D5500B</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #2B3A42;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Deep Slate</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#2B3A42</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Feedback -->
                <div>
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">Feedback</h4>
                  <div class="grid grid-cols-3 gap-4">
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #00AE42;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Success</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#00AE42</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #FFA400;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Warning</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#FFA400</div>
                      </div>
                    </div>
                    <div class="bg-surface-base border border-border-subtle rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                      <div class="h-24 w-full" style="background-color: #ED3A3D;"></div>
                      <div class="p-3">
                        <div class="text-xs font-medium text-text-text-primary mb-1">Error</div>
                        <div class="text-[10px] font-mono text-text-secondary uppercase">#ED3A3D</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 02. TOKENS SEMÂNTICOS -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-text-primary">02. Semantic Tokens</h3>
                <p class="text-sm text-text-secondary mb-8 font-light">Usage · A Função</p>
                
                <!-- Surface -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">Surface (Backgrounds)</h4>
                  <div class="overflow-hidden border border-border-subtle rounded-lg">
                    <table class="w-full">
                      <thead class="bg-surface-subtle">
                        <tr>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[10%]">Preview</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[25%]">Token Name</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[20%]">Reference</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[45%]">Usage Guidelines</th>
                        </tr>
                      </thead>
                      <tbody class="bg-surface-base">
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-border-subtle" style="background-color: #FAFAFA;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">surface-base</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Porcelain</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Cor de fundo padrão da página (body). Evita fadiga visual.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-border-subtle" style="background-color: #FFFFFF;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">surface-card</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Pure White</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Cards, Modais e painéis flutuantes para criar elevação.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-border-subtle" style="background-color: #F4F4F5;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              surface-subtle
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">NEW</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Mist</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Sidebars, áreas secundárias e hovers sutis.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border border-border-subtle" style="background-color: #D6D6D8;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">surface-offset</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Platinum</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Seções com contraste médio, estados disabled.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- Typography -->
                <div class="mb-8">
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">Typography</h4>
                  <div class="overflow-hidden border border-border-subtle rounded-lg">
                    <table class="w-full">
                      <thead class="bg-surface-subtle">
                        <tr>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[10%]">Preview</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[25%]">Token Name</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[20%]">Reference</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[45%]">Usage</th>
                        </tr>
                      </thead>
                      <tbody class="bg-surface-base">
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-bold text-text-text-primary">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">text-text-primary</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Rich Black</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Títulos, cabeçalhos e corpo de texto principal. Máxima legibilidade.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-semibold text-text-secondary">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">text-secondary</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Graphite Stone</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Subtítulos, legendas e textos de apoio. Menor peso visual.</td>
                        </tr>
                        <tr class="border-t border-border-subtle" style="background-color: #121212;">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-semibold" style="color: #FFFFFF;">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 rounded text-xs font-mono" style="background-color: rgba(255,255,255,0.1); color: #D6D6D8;">text-inverse</span>
                          </td>
                          <td class="px-4 py-4 text-sm" style="color: #D6D6D8;">Pure White</td>
                          <td class="px-4 py-4 text-sm" style="color: #D6D6D8;">Texto sobre fundos escuros (Botões, Hero, Footer).</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <span class="text-2xl font-semibold text-text-link">Aa</span>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">text-link</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Brand Orange</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Links, CTAs textuais ou palavras em destaque (usar com moderação).</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- Borders & Dividers -->
                <div>
                  <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-4">Borders & Dividers</h4>
                  <div class="overflow-hidden border border-border-subtle rounded-lg">
                    <table class="w-full">
                      <thead class="bg-surface-subtle">
                        <tr>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[10%]">Preview</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[25%]">Token Name</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[20%]">Reference</th>
                          <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[45%]">Usage</th>
                        </tr>
                      </thead>
                      <tbody class="bg-surface-base">
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border bg-surface-base" style="border-color: #F4F4F5;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              border-hairline
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">NEW</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Mist</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Divisões quase invisíveis, separadores sutis em tabelas.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border bg-surface-base" style="border-color: #E4E4E7;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              border-subtle
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">UPD</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Chromium</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Bordas padrão de cards, inputs inativos e divisórias.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border bg-surface-base" style="border-color: #D6D6D8;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-flex px-2 py-1 bg-surface-subtle rounded text-xs font-mono  items-center gap-2">
                              border-strong
                              <span class="px-1 py-0.5 bg-action-primary/10 text-action-primary text-[8px] rounded">NEW</span>
                            </span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Platinum</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Divisões com contraste, bordas de destaque estrutural.</td>
                        </tr>
                        <tr class="border-t border-border-subtle">
                          <td class="px-4 py-4">
                            <div class="w-10 h-10 rounded border-2 bg-surface-base" style="border-color: #121212;"></div>
                          </td>
                          <td class="px-4 py-4">
                            <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">border-focus</span>
                          </td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Rich Black</td>
                          <td class="px-4 py-4 text-sm text-text-secondary">Inputs ativos, focos ou bordas que exigem máxima atenção.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>

              <!-- Border Radius -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-text-primary">Border Radius</h3>
                <p class="text-sm text-text-secondary mb-8 font-light">Hierarquia de arredondamento para cards e elementos</p>
                
                <div class="overflow-hidden border border-border-subtle rounded-lg">
                  <table class="w-full">
                    <thead class="bg-surface-subtle">
                      <tr>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[15%]">Preview</th>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[20%]">Class</th>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[15%]">Value</th>
                        <th class="text-left px-4 py-3 text-[10px] font-mono uppercase tracking-wider text-text-secondary w-[50%]">Usage</th>
                      </tr>
                    </thead>
                    <tbody class="bg-surface-base">
                      <tr class="border-t border-border-subtle">
                        <td class="px-4 py-4">
                          <div class="w-16 h-16 bg-surface-subtle border border-border-subtle rounded-lg"></div>
                        </td>
                        <td class="px-4 py-4">
                          <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">rounded-lg</span>
                        </td>
                        <td class="px-4 py-4 text-sm font-mono text-text-secondary">8px</td>
                        <td class="px-4 py-4 text-sm text-text-secondary">Cards padrão, containers principais, modais.</td>
                      </tr>
                      <tr class="border-t border-border-subtle">
                        <td class="px-4 py-4">
                          <div class="w-16 h-16 bg-surface-subtle border border-border-subtle rounded-xl"></div>
                        </td>
                        <td class="px-4 py-4">
                          <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">rounded-lg</span>
                        </td>
                        <td class="px-4 py-4 text-sm font-mono text-text-secondary">12px</td>
                        <td class="px-4 py-4 text-sm text-text-secondary">Cards grandes, hero sections, painéis destacados.</td>
                      </tr>
                      <tr class="border-t border-border-subtle">
                        <td class="px-4 py-4">
                          <div class="w-16 h-16 bg-surface-subtle border border-border-subtle rounded-2xl"></div>
                        </td>
                        <td class="px-4 py-4">
                          <span class="inline-block px-2 py-1 bg-surface-subtle rounded text-xs font-mono">rounded-2xl</span>
                        </td>
                        <td class="px-4 py-4 text-sm font-mono text-text-secondary">16px</td>
                        <td class="px-4 py-4 text-sm text-text-secondary">Elementos especiais, imagens destacadas, containers de nível superior.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Typography -->
              <div class="bg-surface-card border rounded-lg border-border-subtle p-8 hover:border-action-primary/30 transition-colors duration-500">
                <h3 class="text-2xl font-light mb-2 text-text-text-primary">Tipografia</h3>
                <p class="text-sm text-text-secondary mb-8 font-light">Hierarquia tipográfica completa</p>
                
                <div class="space-y-10">
                  
                  <!-- Famílias de Fonte -->
                  <div>
                    <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-6">Famílias de Fonte</h4>
                    <div class="space-y-6">
                      
                      <!-- Inter (Primária) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-brand-orange">
                        <div class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-2">Primária · Inter</div>
                        <p class="text-2xl font-sans text-text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-text-secondary">Fonte principal · Quase todos os textos</p>
                      </div>

                      <!-- Matter SQ (Display) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-text-secondary">
                        <div class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-2">Display · Matter SQ</div>
                        <p class="text-2xl font-display text-text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-text-secondary">Tipografia especial · Títulos e destaques</p>
                      </div>

                      <!-- Roboto (Terciária) -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-border-strong">
                        <div class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-2">Terciária · Roboto</div>
                        <p class="text-2xl font-roboto text-text-text-primary mb-2">The quick brown fox jumps</p>
                        <p class="text-xs text-text-secondary">Alternativa · Elementos específicos</p>
                      </div>

                      <!-- Monospace -->
                      <div class="p-4 bg-surface-subtle border-l-4 border-border-strong">
                        <div class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-2">Código · Monospace</div>
                        <p class="text-lg font-mono text-text-text-primary mb-2">console.log("Hello World")</p>
                        <p class="text-xs text-text-secondary">Dados técnicos · Código e valores</p>
                      </div>

                    </div>
                  </div>

                  <!-- Pesos de Fonte -->
                  <div>
                    <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-6">Pesos de Fonte (Inter)</h4>
                    <div class="grid grid-cols-2 gap-4">
                      <div class="p-3 bg-surface-subtle">
                        <div class="text-base font-light text-text-text-primary mb-1">Light (300)</div>
                        <div class="text-xs font-mono text-text-secondary">Textos leves</div>
                      </div>
                      <div class="p-3 bg-surface-subtle">
                        <div class="text-base font-normal text-text-text-primary mb-1">Regular (400)</div>
                        <div class="text-xs font-mono text-text-secondary">Corpo de texto</div>
                      </div>
                      <div class="p-3 bg-surface-subtle">
                        <div class="text-base font-medium text-text-text-primary mb-1">Medium (500)</div>
                        <div class="text-xs font-mono text-text-secondary">Ênfase moderada</div>
                      </div>
                      <div class="p-3 bg-surface-subtle">
                        <div class="text-base font-semibold text-text-text-primary mb-1">Semibold (600)</div>
                        <div class="text-xs font-mono text-text-secondary">Subtítulos</div>
                      </div>
                      <div class="p-3 bg-surface-subtle">
                        <div class="text-base font-bold text-text-text-primary mb-1">Bold (700)</div>
                        <div class="text-xs font-mono text-text-secondary">Destaque forte</div>
                      </div>
                    </div>
                  </div>

                  <!-- Escala de Tamanhos -->
                  <div>
                    <h4 class="text-xs font-mono text-text-secondary uppercase tracking-widest mb-6">Escala de Tamanhos</h4>
                    <div class="space-y-3">
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-xs text-text-text-primary">text-xs</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">12px · 0.75rem</span>
                        <span class="text-xs text-text-secondary">Labels, captions</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-sm text-text-text-primary">text-sm</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">14px · 0.875rem</span>
                        <span class="text-xs text-text-secondary">Textos pequenos</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-base text-text-text-primary">text-base</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">16px · 1rem</span>
                        <span class="text-xs text-text-secondary">Corpo principal</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-lg text-text-text-primary">text-lg</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">18px · 1.125rem</span>
                        <span class="text-xs text-text-secondary">Textos destacados</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-xl text-text-text-primary">text-xl</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">20px · 1.25rem</span>
                        <span class="text-xs text-text-secondary">Subtítulos pequenos</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-2xl text-text-text-primary">text-2xl</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">24px · 1.5rem</span>
                        <span class="text-xs text-text-secondary">Títulos de seção</span>
                      </div>
                      <div class="flex items-baseline justify-between border-b border-border-subtle pb-2">
                        <span class="text-3xl text-text-text-primary">text-3xl</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">30px · 1.875rem</span>
                        <span class="text-xs text-text-secondary">Títulos principais</span>
                      </div>
                      <div class="flex items-baseline justify-between pb-2">
                        <span class="text-5xl text-text-text-primary">text-5xl</span>
                        <span class="text-xs font-mono text-text-secondary mr-auto ml-4">48px · 3rem</span>
                        <span class="text-xs text-text-secondary">Display / Hero</span>
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






