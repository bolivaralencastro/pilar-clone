<template>
  <div class="font-sans text-text-primary min-h-screen bg-surface-base">
    
    <!-- Header -->
    <HeaderLuxury />

    <div class="relative">
      <!-- HERO EDITORIAL (Estilo Aman Resorts) -->
      <header class="pt-20 pb-12 px-6 text-center max-w-4xl mx-auto">
      
      <!-- Bairro (Título Principal - Serif Display) -->
      <h1 class="text-5xl md:text-6xl font-serif font-light text-text-primary mb-3 tracking-tight">Jardins</h1>
      
      <!-- Cidade (Pequeno abaixo) -->
      <span class="block text-xs uppercase tracking-[0.2em] text-text-tertiary mb-8">São Paulo</span>
      
      <!-- Descrição Elegante -->
      <p class="text-sm md:text-base font-light text-text-secondary leading-relaxed mb-6 max-w-2xl mx-auto">
        Um refúgio de sofisticação onde a arquitetura clássica encontra a modernidade. 
        Ruas arborizadas, alta gastronomia e as boutiques mais exclusivas definem 
        o estilo de vida inconfundível desta região icônica.
      </p>

      <!-- Contagem de imóveis -->
      <span class="text-xs uppercase tracking-[0.15em] text-text-tertiary">127 imóveis encontrados</span>

    </header>

    <!-- CONTROL BAR (Sticky) -->
    <div class="sticky top-0 z-40 bg-surface-base border-t border-b border-border-subtle">
      <div class="container mx-auto px-6 h-14 flex justify-between items-center text-[10px] uppercase tracking-[0.15em] font-medium text-text-primary">
        
        <!-- Lado Esquerdo: Filtros, Ordenação e Busca -->
        <div class="flex items-center gap-6">
          <button 
            @click="showFilters = true"
            class="flex items-center gap-2 hover:text-text-secondary transition-colors"
          >
            <i class="lni lni-funnel text-xs"></i>
            <span>Aplicar Filtros</span>
          </button>
          
          <div class="h-4 w-px bg-border-subtle"></div>

          <button class="flex items-center gap-2 hover:text-text-secondary transition-colors group">
            <span>Ordenar por Recomendados</span>
            <i class="lni lni-chevron-down text-[8px] group-hover:rotate-180 transition-transform"></i>
          </button>

          <div class="h-4 w-px bg-border-subtle"></div>

          <!-- Busca inline -->
          <div class="relative hidden md:block">
            <input 
              type="text" 
              v-model="searchQuery"
              placeholder="Buscar..."
              class="w-48 bg-transparent border-b border-border-subtle py-1 text-xs lowercase tracking-normal font-light focus:outline-none focus:border-text-primary transition-colors placeholder:text-text-tertiary placeholder:italic"
            />
            <div class="absolute right-0 top-1/2 -translate-y-1/2 text-text-tertiary/50">
              <i class="lni lni-search text-[10px]"></i>
            </div>
          </div>
        </div>

        <!-- Lado Direito: Comparar + Mapa -->
        <div class="flex items-center gap-6">
          <button 
            @click="toggleComparisonMode"
            class="flex items-center gap-2 transition-colors"
            :class="isComparisonMode ? 'text-text-primary font-medium' : 'hover:text-text-secondary'"
          >
            <span>Comparar</span>
            <span v-if="selectedProperties.length > 0" class="bg-text-primary text-surface-base text-[9px] w-4 h-4 rounded-full flex items-center justify-center">
              {{ selectedProperties.length }}
            </span>
          </button>
          
          <div class="h-4 w-px bg-border-subtle"></div>

          <button 
            @click="viewMode = viewMode === 'grid' ? 'map' : 'grid'"
            class="flex items-center gap-2 hover:text-text-secondary transition-colors"
          >
            <span>{{ viewMode === 'grid' ? 'Ver Mapa' : 'Ver Grid' }}</span>
            <i :class="viewMode === 'grid' ? 'lni-map' : 'lni-grid-alt'" class="lni text-xs"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Main Content -->
    <main class="container mx-auto px-6 pb-16 mt-12">
      
      <!-- Editorial Grid View -->
      <div v-if="viewMode === 'grid'" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="property in properties" 
          :key="property.id" 
          class="col-span-1"
        >
          <PropertyCardV2 
            :property="property" 
            imageHeight="medium" 
            :selectionMode="isComparisonMode"
            :isSelected="selectedProperties.some(p => p.id === property.id)"
            @toggle-selection="handleSelection"
          />
        </div>
      </div>

      <!-- Map View -->
      <div v-else class="flex gap-6 items-start relative">
        <!-- Sidebar with Cards (scroll com a página) -->
        <div class="w-full md:w-[420px] space-y-4 pb-16">
          <div 
            v-for="property in properties" 
            :key="property.id" 
            class="bg-surface-card rounded-lg overflow-hidden flex shadow-sm border border-border-subtle group cursor-pointer hover:shadow-md transition-shadow"
          >
            <!-- Image -->
            <div class="w-32 h-32 bg-surface-offset flex-shrink-0 overflow-hidden relative">
              <img 
                v-if="!imageErrors.has(property.id)"
                :src="property.image" 
                :alt="property.name"
                class="w-full h-full object-cover"
                @error="handleImageError(property.id)"
              />
              <div 
                v-else 
                class="w-full h-full flex flex-col items-center justify-center bg-surface-offset text-text-tertiary"
              >
                <i class="lni lni-image text-xl mb-1 opacity-30"></i>
              </div>
            </div>
            <!-- Content -->
            <div class="p-3 flex-1 flex flex-col justify-between">
              <div>
                <p class="text-[9px] uppercase tracking-widest text-text-tertiary">{{ property.neighborhood }}</p>
                <h3 class="font-serif font-semibold text-sm text-text-primary leading-tight mt-1">{{ property.name }}</h3>
              </div>
              <div>
                <p class="font-bold text-sm text-text-primary">{{ property.price }}</p>
                <p class="font-mono text-[10px] text-text-secondary">{{ property.specs }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Map Placeholder (Sticky) -->
        <div class="hidden md:block flex-1 sticky top-[80px] h-[calc(100vh-104px)] z-10">
          <div class="w-full h-full bg-surface-offset rounded-lg flex items-center justify-center border border-border-subtle">
            <div class="text-center">
              <div class="w-16 h-16 bg-surface-card rounded-full flex items-center justify-center mx-auto mb-4 border border-border-subtle">
                <i class="lni lni-map-marker text-2xl text-text-tertiary"></i>
              </div>
              <p class="text-text-tertiary text-sm">Mapa interativo</p>
              <p class="text-text-tertiary/60 text-xs mt-1">Placeholder para integração</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Load More -->
      <div v-if="viewMode === 'grid'" class="mt-12 flex justify-center">
        <button class="border border-border-strong px-8 py-4 rounded text-sm hover:bg-surface-subtle hover:text-text-primary transition-colors text-text-secondary">
          Carregar mais imóveis
        </button>
      </div>

    </main>
    </div>

    <!-- Footer -->
    <FooterLuxury />

    <!-- COMPARISON FLOATING BAR -->
    <Teleport to="body">
      <Transition 
        enter-active-class="transform transition duration-500 ease-out"
        enter-from-class="translate-y-full opacity-0"
        enter-to-class="translate-y-0 opacity-100"
        leave-active-class="transform transition duration-300 ease-in"
        leave-from-class="translate-y-0 opacity-100"
        leave-to-class="translate-y-full opacity-0"
      >
        <div 
          v-if="isComparisonMode" 
          class="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 flex flex-col items-center gap-4"
        >
          <!-- The Bar -->
          <div class="bg-[#0f172b] text-white rounded-full shadow-2xl flex items-center py-2 pl-6 pr-3 gap-6 border border-white/10">
            
            <!-- Label -->
            <div class="flex flex-col">
              <span class="font-serif italic text-lg leading-none">Sua Seleção</span>
              <span class="text-[9px] uppercase tracking-widest text-gray-400 mt-1">{{ selectedProperties.length }} Imóveis</span>
            </div>

            <!-- Avatars -->
            <div class="flex items-center -space-x-3 pl-4">
              <!-- Empty Slots / Selected Items -->
              <template v-for="(item, index) in 3" :key="index">
                <div 
                  v-if="selectedProperties[index]"
                  class="w-12 h-12 rounded-full border-2 border-[#0f172b] relative group cursor-pointer overflow-hidden bg-surface-offset"
                  @click="removeSelection(selectedProperties[index].id)"
                >
                  <img :src="selectedProperties[index].image" class="w-full h-full object-cover" />
                  <!-- Hover Remove Icon -->
                  <div class="absolute inset-0 bg-black/50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                    <i class="lni lni-minus text-white"></i>
                  </div>
                </div>
                <div 
                  v-else
                  class="w-12 h-12 rounded-full border-2 border-[#0f172b] bg-white/5 flex items-center justify-center text-white/20"
                >
                  <i class="lni lni-plus"></i>
                </div>
              </template>
            </div>

            <!-- Action Button -->
            <button 
              @click="navigateToCompare"
              class="px-6 py-3 rounded-full text-[10px] uppercase tracking-widest font-medium transition-all duration-300 ml-2 transform"
              :class="selectedProperties.length >= 2 ? 'bg-white text-[#0f172b] hover:bg-gray-100 hover:scale-105 hover:shadow-[0_0_15px_rgba(255,255,255,0.3)] active:scale-95' : 'bg-white/10 text-white/30 cursor-not-allowed'"
              :disabled="selectedProperties.length < 2"
            >
              Comparar
            </button>

          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- FILTERS PANEL (Painel Flutuante) -->
    <Teleport to="body">
      <Transition name="fade">
        <div 
          v-if="showFilters" 
          class="fixed inset-0 z-50 flex items-stretch justify-end p-4"
        >
          <!-- Backdrop -->
          <div 
            class="absolute inset-0 bg-text-primary/40 backdrop-blur-sm"
            @click="showFilters = false"
          ></div>
          
          <!-- Panel -->
          <div class="relative w-full max-w-md bg-surface-base rounded-lg shadow-2xl overflow-hidden flex flex-col animate-slide-in-right">
            
            <!-- Header do Painel -->
            <div class="flex items-center justify-between px-6 py-5 border-b border-border-subtle">
              <h2 class="text-lg font-light tracking-tight text-text-primary">Filtros</h2>
              <button 
                @click="showFilters = false"
                class="w-8 h-8 flex items-center justify-center text-text-tertiary hover:text-text-primary transition-colors"
              >
                <i class="lni lni-close text-lg"></i>
              </button>
            </div>

            <!-- Conteúdo Scrollável -->
            <div class="flex-1 overflow-y-auto px-6 py-6 space-y-8">
              
              <!-- BAIRROS -->
              <div class="space-y-4">
                <button 
                  @click="toggleSection('bairros')"
                  class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
                >
                  <span>Bairros</span>
                  <i :class="openSections.includes('bairros') ? 'lni-chevron-up' : 'lni-chevron-down'" class="lni text-xs"></i>
                </button>
                
                <div v-if="openSections.includes('bairros')" class="space-y-3">
                  <!-- Busca -->
                  <div class="relative">
                    <input 
                      type="text" 
                      placeholder="Buscar por bairros"
                      class="w-full bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary transition-colors"
                    />
                  </div>
                  
                  <!-- Em destaque -->
                  <p class="text-[10px] uppercase tracking-widest text-text-tertiary">Bairros em destaque</p>
                  <div class="flex flex-wrap gap-2">
                    <button 
                      v-for="bairro in ['Itaim Bibi', 'Jardim Paulista', 'Vila Nova Conceição', 'Jardim América', 'Higienópolis']" 
                      :key="bairro"
                      class="px-3 py-1.5 text-xs border border-border-subtle rounded-full hover:border-text-primary hover:bg-surface-subtle transition-colors"
                    >
                      {{ bairro }}
                    </button>
                  </div>
                </div>
              </div>

              <!-- ÁREA ÚTIL -->
              <div class="space-y-4">
                <button 
                  @click="toggleSection('area')"
                  class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
                >
                  <span>Área útil</span>
                  <i :class="openSections.includes('area') ? 'lni-chevron-up' : 'lni-chevron-down'" class="lni text-xs"></i>
                </button>
                
                <div v-if="openSections.includes('area')" class="flex gap-3">
                  <input type="text" placeholder="Mín m²" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                  <input type="text" placeholder="Máx m²" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                </div>
              </div>

              <!-- VALOR DE VENDA -->
              <div class="space-y-4">
                <button 
                  @click="toggleSection('valor')"
                  class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
                >
                  <span>Valor de venda</span>
                  <i :class="openSections.includes('valor') ? 'lni-chevron-up' : 'lni-chevron-down'" class="lni text-xs"></i>
                </button>
                
                <div v-if="openSections.includes('valor')" class="flex gap-3">
                  <input type="text" placeholder="Mín R$" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                  <input type="text" placeholder="Máx R$" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                </div>
              </div>

              <!-- TIPO DE IMÓVEL -->
              <div class="space-y-4">
                <button 
                  @click="toggleSection('tipo')"
                  class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
                >
                  <span>Tipo de imóvel</span>
                  <i :class="openSections.includes('tipo') ? 'lni-chevron-up' : 'lni-chevron-down'" class="lni text-xs"></i>
                </button>
                
                <div v-if="openSections.includes('tipo')" class="space-y-3">
                  <div class="relative">
                    <input 
                      type="text" 
                      placeholder="Buscar por tipo de imóvel"
                      class="w-full bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary transition-colors"
                    />
                  </div>
                  
                  <p class="text-[10px] uppercase tracking-widest text-text-tertiary">Tipo de imóvel em destaque</p>
                  <div class="flex flex-wrap gap-2">
                    <button 
                      v-for="tipo in ['Apartamento', 'Cobertura', 'Duplex', 'Casa de vila']" 
                      :key="tipo"
                      class="px-3 py-1.5 text-xs border border-border-subtle rounded-full hover:border-text-primary hover:bg-surface-subtle transition-colors"
                    >
                      {{ tipo }}
                    </button>
                  </div>
                </div>
              </div>

              <!-- CÔMODOS -->
              <div class="space-y-4">
                <button 
                  @click="toggleSection('comodos')"
                  class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
                >
                  <span>Cômodos</span>
                  <i :class="openSections.includes('comodos') ? 'lni-chevron-up' : 'lni-chevron-down'" class="lni text-xs"></i>
                </button>
                
                <div v-if="openSections.includes('comodos')" class="space-y-5">
                  <!-- Quartos -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Quartos</p>
                    <div class="flex gap-2">
                      <button 
                        v-for="opt in ['Qualquer', '+1', '+2', '+3', '+4', '+5']" 
                        :key="opt"
                        class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors"
                      >
                        {{ opt }}
                      </button>
                    </div>
                  </div>
                  
                  <!-- Suítes -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Suítes</p>
                    <div class="flex gap-2">
                      <button 
                        v-for="opt in ['Qualquer', '+1', '+2', '+3', '+4', '+5']" 
                        :key="opt"
                        class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors"
                      >
                        {{ opt }}
                      </button>
                    </div>
                  </div>
                  
                  <!-- Banheiros -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Banheiros</p>
                    <div class="flex gap-2">
                      <button 
                        v-for="opt in ['Qualquer', '+1', '+2', '+3', '+4', '+5']" 
                        :key="opt"
                        class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors"
                      >
                        {{ opt }}
                      </button>
                    </div>
                  </div>
                  
                  <!-- Vagas -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Vagas</p>
                    <div class="flex gap-2">
                      <button 
                        v-for="opt in ['Qualquer', '+1', '+2', '+3', '+4', '+5']" 
                        :key="opt"
                        class="flex-1 py-2 text-xs border border-border-subtle rounded hover:border-text-primary hover:bg-surface-subtle transition-colors"
                      >
                        {{ opt }}
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <!-- MAIS FILTROS -->
              <div class="space-y-4">
                <button 
                  @click="toggleSection('mais')"
                  class="w-full flex items-center justify-between text-sm font-medium text-text-primary"
                >
                  <span>Mais filtros</span>
                  <i :class="openSections.includes('mais') ? 'lni-chevron-up' : 'lni-chevron-down'" class="lni text-xs"></i>
                </button>
                
                <div v-if="openSections.includes('mais')" class="space-y-5">
                  <!-- Características -->
                  <div class="space-y-3">
                    <div class="relative">
                      <input 
                        type="text" 
                        placeholder="Buscar por características"
                        class="w-full bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary transition-colors"
                      />
                    </div>
                    
                    <p class="text-[10px] uppercase tracking-widest text-text-tertiary">Características em destaque</p>
                    <div class="flex flex-wrap gap-2">
                      <button 
                        v-for="carac in ['Piscina privativa', 'Varanda gourmet', 'Academia', 'Ar-condicionado']" 
                        :key="carac"
                        class="px-3 py-1.5 text-xs border border-border-subtle rounded-full hover:border-text-primary hover:bg-surface-subtle transition-colors"
                      >
                        {{ carac }}
                      </button>
                    </div>
                  </div>
                  
                  <!-- Status -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Status do imóvel</p>
                    <div class="flex gap-2">
                      <button class="px-3 py-1.5 text-xs border border-border-subtle rounded-full hover:border-text-primary hover:bg-surface-subtle transition-colors">
                        Exclusivo
                      </button>
                    </div>
                  </div>
                  
                  <!-- Valor m² -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Valor do m²</p>
                    <div class="flex gap-3">
                      <input type="text" placeholder="Mín R$/m²" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                      <input type="text" placeholder="Máx R$/m²" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                    </div>
                  </div>
                  
                  <!-- IPTU -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">IPTU mensal</p>
                    <div class="flex gap-3">
                      <input type="text" placeholder="Mín R$" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                      <input type="text" placeholder="Máx R$" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                    </div>
                  </div>
                  
                  <!-- Condomínio -->
                  <div class="space-y-2">
                    <p class="text-xs text-text-secondary">Taxa de condomínio mensal</p>
                    <div class="flex gap-3">
                      <input type="text" placeholder="Mín R$" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                      <input type="text" placeholder="Máx R$" class="flex-1 bg-surface-card border border-border-subtle rounded px-3 py-2 text-sm placeholder:text-text-tertiary focus:outline-none focus:border-text-primary" />
                    </div>
                  </div>
                </div>
              </div>

            </div>

            <!-- Footer do Painel -->
            <div class="px-6 py-5 border-t border-border-subtle bg-surface-base flex items-center justify-between gap-4">
              <button class="text-xs uppercase tracking-widest text-text-tertiary hover:text-text-primary transition-colors underline underline-offset-4">
                Limpar filtros
              </button>
              <button 
                @click="showFilters = false"
                class="flex-1 bg-text-primary text-surface-base py-3 text-xs uppercase tracking-widest font-medium hover:bg-text-primary/90 transition-colors rounded"
              >
                Ver 16.215 imóveis
              </button>
            </div>

          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- Flowchart Toggle -->
    <button 
      @click="showFlowchart = true"
      class="fixed bottom-6 right-6 z-40 w-12 h-12 bg-surface-base border border-border-subtle rounded-full flex items-center justify-center shadow-xl hover:bg-surface-subtle hover:scale-105 transition-all text-text-secondary group"
      title="Ver Fluxo"
    >
      <i class="lni lni-network text-xl group-hover:text-text-primary transition-colors"></i>
    </button>

    <!-- Flowchart Modal -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="showFlowchart" class="fixed inset-0 z-[60] bg-surface-base/95 backdrop-blur-sm flex flex-col">
          <!-- Header -->
          <div class="flex items-center justify-between px-6 py-4 border-b border-border-subtle bg-surface-base">
            <div class="flex items-center gap-3">
              <div class="w-8 h-8 bg-surface-offset rounded flex items-center justify-center">
                <i class="lni lni-network text-text-primary"></i>
              </div>
              <div>
                <h2 class="text-sm font-medium uppercase tracking-widest text-text-primary">Fluxo de Comparação</h2>
                <p class="text-[10px] text-text-tertiary">Diagrama de estados e interações</p>
              </div>
            </div>
            <button 
              @click="showFlowchart = false" 
              class="w-10 h-10 flex items-center justify-center hover:bg-surface-offset rounded-full transition-colors text-text-secondary hover:text-text-primary"
            >
              <i class="lni lni-close text-lg"></i>
            </button>
          </div>
          <!-- Viewer -->
          <div class="flex-1 overflow-hidden relative bg-surface-offset/30">
             <FlowchartViewer>
               <MermaidRenderer :code="mermaidCode" />
             </FlowchartViewer>
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup lang="ts">
import HeaderLuxury from './HeaderLuxury.vue'
import FooterLuxury from './FooterLuxury.vue'
import PropertyCardV2 from './PropertyCardV2.vue'
import FlowchartViewer from '../FlowchartViewer.vue'
import MermaidRenderer from '../MermaidRenderer.vue'

const mermaidCode = `
flowchart TD
    %% --- CAMADA DE NAVEGAÇÃO ---
    subgraph Navigation ["📍 Navegação & Páginas"]
        direction TB
        Home["🏠 Pág 01: Home<br/>(Porta de Entrada)"]
        Results["📋 Pág 02: Resultados<br/>(Busca & Mapa)"]
        Curation["✨ Pág 04: Curadoria<br/>(Coleções Temáticas)"]
        Details["💎 Pág 03: Detalhe (Single)<br/>(Imersão Total)"]

        %% Fluxo de navegação básica
        Home --> Results & Curation
        Results -.->|Clica no Card| Details
        Curation -.->|Clica no Card| Details
    end

    %% --- CAMADA DE PERSISTÊNCIA (BARRA FLUTUANTE) ---
    subgraph PersistentUI ["⚓ Barra Flutuante de Comparação"]
        direction TB
        %% Ações de adicionar à comparação vindas de várias origens
        ActionAdd["🖱️ Ação: Selecionar Card<br/>(Checkbox ou Botão)"]
        
        Results --> ActionAdd
        Curation --> ActionAdd
        Details --> ActionAdd
        
        ActionAdd --> FloatingBar["🚧 Barra Flutuante Ativa<br/>(Persiste no rodapé/topo)"]
        
        %% Lógica de Estado da Barra
        FloatingBar --> CheckState{"Qtd. Selecionada?"}
        
        CheckState -- "< 2 Imóveis" --> KeepBrowsing["👀 Botão 'Comparar' Inativo<br/>User continua navegando"]
        CheckState -- ">= 2 Imóveis" --> ReadyState["✅ Botão 'Comparar' Ativo"]
        
        %% O loop de persistência: volta para a navegação visualmente
        KeepBrowsing -.->|Barra permanece visível| Navigation
        ReadyState -.->|Barra permanece visível| Navigation
    end

    %% --- FLUXO DE EXECUÇÃO (COMPARAR) ---
    subgraph CompareFlow ["Tela de Comparação"]
        ReadyState -->|Clicou Comparar| ManualView["📊 Tabela Side-by-Side<br/>(Página de Comparação)"]
        ManualView --> Insights["💡 Insights de IA<br/>sobre a seleção"]
        ManualView --> Actions["⚡ Ações Finais:<br/>Agendar, Ofertar"]
    end

    %% --- FLUXO DE IA (EXCLUSIVO SINGLE PAGE) ---
    subgraph AIFlow ["Fluxo IA (Exclusivo Single-Page)"]
        direction TB
        Details -->|Botão 'Analisar Valor'| Analyze["🤖 Processar Análise IA"]
        Analyze --> AutoView["📈 Popup IA:<br/>Preço, Similares, Fatores"]
        
        %% Integração: Da IA para a Barra Flutuante
        AutoView -->|Botão 'Add à Comparação'| FloatingBar
    end

    %% --- ESTILIZAÇÃO ---
    classDef nav fill:#f1faee,stroke:#1d3557,stroke-width:2px,color:#1d3557,rx:5,ry:5
    classDef bar fill:#cdb4db,stroke:#5c2a9d,stroke-width:2px,color:#333,rx:10,ry:10
    classDef action fill:#bde0fe,stroke:#457b9d,stroke-width:1px,color:#1d3557,rx:5,ry:5
    classDef manual fill:#e9c46a,stroke:#d4a373,stroke-width:1px,color:#333,rx:5,ry:5
    classDef ai fill:#a2d2ff,stroke:#023e8a,stroke-width:1px,color:#1d3557,rx:5,ry:5
    classDef decision fill:#ffafcc,stroke:#e63946,stroke-width:1px,color:#333,rx:5,ry:5

    %% Aplicação das Classes
    class Home,Results,Curation,Details nav
    class FloatingBar,KeepBrowsing,ReadyState bar
    class ActionAdd action
    class ManualView,Insights,Actions manual
    class Analyze,AutoView ai
    class CheckState decision
`

// Types
interface Property {
  id: number
  name: string
  neighborhood: string
  ref: string
  price: string
  specs: string
  image: string
  agent: { name: string; company: string }
}

// Row configuration type
// Define os tipos de linha disponíveis para o grid editorial
type RowType = 'single' | 'two-col' | 'three-col' | 'four-col'
type ImageHeight = 'tall' | 'medium' | 'short'

interface GridRow {
  type: RowType        // Tipo de layout da linha
  count: number        // Quantidade de cards na linha
  imageHeight: ImageHeight  // Altura das imagens (todas iguais na linha)
}

// State
const viewMode = ref<'grid' | 'map'>('grid')
const searchQuery = ref('')
const showFilters = ref(false)
const openSections = ref<string[]>(['bairros'])
const imageErrors = ref<Set<number>>(new Set())
const showFlowchart = ref(false)

const handleImageError = (id: number) => {
  imageErrors.value.add(id)
}

// Comparison State
const isComparisonMode = ref(false)
const selectedProperties = ref<Property[]>([])

const toggleComparisonMode = () => {
  isComparisonMode.value = !isComparisonMode.value
  if (!isComparisonMode.value) {
    selectedProperties.value = []
  }
}

const handleSelection = (property: Property) => {
  const index = selectedProperties.value.findIndex(p => p.id === property.id)
  if (index >= 0) {
    selectedProperties.value.splice(index, 1)
  } else {
    if (selectedProperties.value.length < 3) {
      selectedProperties.value.push(property)
    }
  }
}

const removeSelection = (id: number) => {
  const index = selectedProperties.value.findIndex(p => p.id === id)
  if (index >= 0) {
    selectedProperties.value.splice(index, 1)
  }
}

const router = useRouter()
const navigateToCompare = () => {
  router.push('/compare')
}

// Toggle seção do filtro
const toggleSection = (section: string) => {
  if (openSections.value.includes(section)) {
    openSections.value = openSections.value.filter(s => s !== section)
  } else {
    openSections.value.push(section)
  }
}

// ============================================
// CONFIGURAÇÃO DO GRID EDITORIAL
// ============================================
// Defina aqui a sequência de linhas e seus formatos.
// Cada linha terá cards com dimensões idênticas.
// 
// Tipos disponíveis:
// - 'single': 1 card full-width (destaque máximo)
// - 'two-col': 2 cards lado a lado (50% cada)
// - 'three-col': 3 cards lado a lado (33% cada)
// - 'four-col': 4 cards lado a lado (25% cada)
//
// Alturas de imagem:
// - 'tall': 400px (para destaques)
// - 'medium': 340px (padrão)
// - 'short': 280px (para grids densos)
// ============================================

const gridRows = ref<GridRow[]>([
  { type: 'two-col', count: 2, imageHeight: 'tall' },
  { type: 'three-col', count: 3, imageHeight: 'medium' },
  { type: 'two-col', count: 2, imageHeight: 'medium' },
  { type: 'three-col', count: 3, imageHeight: 'medium' },
  { type: 'two-col', count: 2, imageHeight: 'tall' },
])

// Calcula o índice inicial de cada linha
const getRowStartIndex = (rowIndex: number): number => {
  let start = 0
  for (let i = 0; i < rowIndex; i++) {
    start += gridRows.value[i].count
  }
  return start
}

// Retorna os imóveis para uma linha específica
const getPropertiesForRow = (rowIndex: number): Property[] => {
  const start = getRowStartIndex(rowIndex)
  const count = gridRows.value[rowIndex].count
  return properties.value.slice(start, start + count)
}

// Mock data for properties (sem layout, agora controlado pelas rows)
const properties = ref<Property[]>([
  // === LINHA 1: 2 colunas ===
  {
    id: 1,
    name: 'Casa Del Sol',
    neighborhood: 'Jardins — SP',
    ref: 'LE4592',
    price: 'R$ 9.250.000',
    specs: '420m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Laura S.', company: 'Elite Realty' }
  },
  {
    id: 2,
    name: 'Residencial Dos Lagos',
    neighborhood: 'Itaim Bibi — SP',
    ref: 'LE4593',
    price: 'R$ 7.800.000',
    specs: '380m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Sofia B.', company: 'Elite Realty' }
  },
  // === LINHA 2: 3 colunas ===
  {
    id: 3,
    name: 'Villa Toscana',
    neighborhood: 'Vila Nova Conceição — SP',
    ref: 'LE4594',
    price: 'R$ 6.950.000',
    specs: '350m² / 3 Suítes',
    image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Alice R.', company: 'Elite Realty' }
  },
  {
    id: 4,
    name: 'Edifício Atlântica',
    neighborhood: 'Morumbi — SP',
    ref: 'LE4595',
    price: 'R$ 8.750.000',
    specs: '480m² / 5 Suítes',
    image: 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Isabella V.', company: 'Elite Realty' }
  },
  {
    id: 5,
    name: 'Quinta da Baroneza',
    neighborhood: 'Higienópolis — SP',
    ref: 'LE4596',
    price: 'R$ 6.500.000',
    specs: '320m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600210491892-03d54cc0d578?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Maria Clara N.', company: 'Elite Realty' }
  },
  // === LINHA 3: 2 colunas ===
  {
    id: 6,
    name: 'Haras da Prata',
    neighborhood: 'Perdizes — SP',
    ref: 'LE4597',
    price: 'R$ 8.900.000',
    specs: '520m² / 5 Suítes',
    image: 'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Beatriz F.', company: 'Elite Realty' }
  },
  {
    id: 7,
    name: 'Palazzo di Fiori',
    neighborhood: 'Pinheiros — SP',
    ref: 'LE4598',
    price: 'R$ 7.300.000',
    specs: '400m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600585154526-990dced4db0d?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Maria Eduarda C.', company: 'Elite Realty' }
  },
  // === LINHA 4: 3 colunas ===
  {
    id: 8,
    name: 'Mansão Imperial',
    neighborhood: 'Alto de Pinheiros — SP',
    ref: 'LE4599',
    price: 'R$ 9.500.000',
    specs: '600m² / 6 Suítes',
    image: 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Giovanna D.', company: 'Elite Realty' }
  },
  {
    id: 9,
    name: 'Solar das Palmeiras',
    neighborhood: 'Moema — SP',
    ref: 'LE4600',
    price: 'R$ 9.100.000',
    specs: '450m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Valentina L.', company: 'Elite Realty' }
  },
  {
    id: 10,
    name: 'Fazenda Boa Vista',
    neighborhood: 'Vila Mariana — SP',
    ref: 'LE4601',
    price: 'R$ 12.800.000',
    specs: '850m² / 6 Suítes',
    image: 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Helena E.', company: 'Elite Realty' }
  },
  // === LINHA 5: 2 colunas ===
  {
    id: 11,
    name: 'Porto Feliz Resort',
    neighborhood: 'Brooklin — SP',
    ref: 'LE4602',
    price: 'R$ 7.650.000',
    specs: '390m² / 4 Suítes',
    image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Ana M.', company: 'Elite Realty' }
  },
  {
    id: 12,
    name: 'Vivendas do Parque',
    neighborhood: 'Cidade Jardim — SP',
    ref: 'LE4603',
    price: 'R$ 8.500.000',
    specs: '520m² / 5 Suítes',
    image: 'https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?q=80&w=2574&auto=format&fit=crop',
    agent: { name: 'Manuela P.', company: 'Elite Realty' }
  }
])
</script>

<style scoped>
/* Custom scrollbar hiding for clean UI */
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Micro-interação de Zoom suave do DS */
.img-zoom { 
  transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1); 
}
.group:hover .img-zoom { 
  transform: scale(1.05); 
}

/* Animação do painel de filtros */
.animate-slide-in-right {
  animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Transição fade para backdrop */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active .animate-slide-in-right {
  animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-leave-active .animate-slide-in-right {
  animation: slideOutRight 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes slideOutRight {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%);
    opacity: 0;
  }
}
</style>