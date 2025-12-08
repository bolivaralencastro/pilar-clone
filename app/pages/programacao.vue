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
  <div class="min-h-screen bg-porcelain text-text-primary selection:bg-soft-beige selection:text-text-primary">
    <!-- Background SVG -->
    <div class="fixed bottom-0 left-0 opacity-[0.02] pointer-events-none z-0 scale-[3] origin-bottom-left">
      <svg width="380" height="328" viewBox="0 0 380 328" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M95 0L0 163.917L95 327.834H285L380 163.917L285 0H95ZM252.274 307.033L34.4494 181.755L283.277 38.6387L252.274 307.033Z" fill="black"/>
      </svg>
    </div>

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
            <span class="text-text-primary">Programação</span>
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
        
        <!-- Header Section -->
        <div class="mb-12">
          <span class="text-xs font-mono text-action-primary tracking-widest uppercase mb-4 block">Agenda & Planejamento</span>
          <h1 class="text-5xl font-light tracking-tighter mb-8 text-text-primary">Cronograma</h1>
          <p class="text-secondary text-lg font-light leading-relaxed max-w-3xl">
            Organização do cronograma para entrega do desafio em 1 semana, conciliando com jornada de trabalho integral (08h às 17h).
          </p>
        </div>

        <!-- Availability Info -->
        <div class="mb-8 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-surface-card border rounded-lg border-subtle p-6">
            <h3 class="text-xs font-mono uppercase tracking-widest mb-4 text-secondary">Disponibilidade Semanal</h3>
            <ul class="space-y-3">
              <li class="flex justify-between text-sm">
                <span class="font-medium text-text-primary">Segunda - Sexta</span>
                <span class="text-secondary">~2h / dia (19h-21h)</span>
              </li>
              <li class="flex justify-between text-sm">
                <span class="font-medium text-text-primary">Sábado - Domingo</span>
                <span class="text-secondary">~4h / dia (14h-18h)</span>
              </li>
              <li class="flex justify-between text-sm border-t border-subtle pt-3">
                <span class="font-medium text-text-primary">Total Estimado</span>
                <span class="text-action-primary font-medium">~18h</span>
              </li>
            </ul>
          </div>

          <div class="bg-surface-subtle border border-hairline p-6 rounded-lg">
            <h3 class="text-xs font-mono uppercase tracking-widest mb-4 text-deep-brown">Entrega Final</h3>
            <div class="space-y-2">
              <div class="text-2xl font-light text-text-primary">Terça-feira, 09 Dez</div>
              <div class="text-sm text-secondary">Envio do repositório e apresentação final</div>
            </div>
          </div>
        </div>

        <!-- Gantt Chart -->
        <div class="bg-surface-card border rounded-lg border-subtle p-8">
          
          <!-- Header with Days -->
          <div class="grid grid-cols-9 gap-2 mb-6">
            <div class="col-span-2 text-xs font-mono text-secondary uppercase tracking-widest">Fase</div>
            <div class="text-center">
              <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-1">Ter</div>
              <div class="text-[10px] text-secondary">02</div>
            </div>
            <div class="text-center">
              <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-1">Qua</div>
              <div class="text-[10px] text-secondary">03</div>
            </div>
            <div class="text-center">
              <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-1">Qui</div>
              <div class="text-[10px] text-secondary">04</div>
            </div>
            <div class="text-center">
              <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-1">Sex</div>
              <div class="text-[10px] text-secondary">05</div>
            </div>
            <div class="text-center">
              <div class="text-xs font-mono text-action-primary uppercase tracking-widest mb-1">Sáb</div>
              <div class="text-[10px] text-action-primary">06</div>
            </div>
            <div class="text-center">
              <div class="text-xs font-mono text-action-primary uppercase tracking-widest mb-1">Dom</div>
              <div class="text-[10px] text-action-primary">07</div>
            </div>
            <div class="text-center">
              <div class="text-xs font-mono text-secondary uppercase tracking-widest mb-1">Seg</div>
              <div class="text-[10px] text-secondary">08</div>
            </div>
          </div>

          <div class="space-y-4">
            
            <!-- Row 1: Planejamento -->
            <div class="grid grid-cols-9 gap-2 items-center group">
              <div class="col-span-2">
                <div class="text-sm font-medium text-text-primary mb-1">Planejamento</div>
                <div class="text-xs text-secondary">Briefing & Setup</div>
              </div>
              <div class="bg-surface-subtle border border-strong p-3 rounded group-hover:bg-surface-subtle transition-colors rounded-lg">
                <div class="text-[10px] text-deep-brown font-medium">19h-21h</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
            </div>

            <!-- Row 2: Discovery -->
            <div class="grid grid-cols-9 gap-2 items-center group">
              <div class="col-span-2">
                <div class="text-sm font-medium text-text-primary mb-1">Discovery</div>
                <div class="text-xs text-secondary">Pesquisa & Análise</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-info-blue/20 border border-info-blue p-3 rounded group-hover:bg-info-blue/30 transition-colors">
                <div class="text-[10px] text-info-blue font-medium">19h-21h</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
            </div>

            <!-- Row 3: Ideação -->
            <div class="grid grid-cols-9 gap-2 items-center group">
              <div class="col-span-2">
                <div class="text-sm font-medium text-text-primary mb-1">Ideação</div>
                <div class="text-xs text-secondary">Fluxos & IA</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-action-primary/10 border border-subtle p-3 rounded-lg group-hover:border-action-primary/30 transition-colors rounded-lg">
                <div class="text-[10px] text-text-primary font-medium">19h-21h</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
            </div>

            <!-- Row 4: Design System -->
            <div class="grid grid-cols-9 gap-2 items-center group">
              <div class="col-span-2">
                <div class="text-sm font-medium text-text-primary mb-1">Design System</div>
                <div class="text-xs text-secondary">Tokens & Setup</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-success-green/20 border border-success-green p-3 rounded group-hover:bg-success-green/30 transition-colors">
                <div class="text-[10px] text-success-green font-medium">19h-21h</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
            </div>

            <!-- Row 5: Desenvolvimento -->
            <div class="grid grid-cols-9 gap-2 items-center group">
              <div class="col-span-2">
                <div class="text-sm font-medium text-text-primary mb-1">Desenvolvimento</div>
                <div class="text-xs text-secondary">Core & Features</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="col-span-2 bg-surface-subtle border border-strong p-3 rounded group-hover:bg-surface-subtle transition-colors rounded-lg">
                <div class="text-[10px] text-text-primary font-medium">14h-18h (Ambos)</div>
              </div>
              <div class="bg-surface-subtle"></div>
            </div>

            <!-- Row 6: QA & Entrega -->
            <div class="grid grid-cols-9 gap-2 items-center group">
              <div class="col-span-2">
                <div class="text-sm font-medium text-text-primary mb-1">QA & Entrega</div>
                <div class="text-xs text-secondary">Testes & Deploy</div>
              </div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-surface-subtle"></div>
              <div class="bg-action-primary/20 border border-action-primary p-3 rounded group-hover:bg-action-primary/30 transition-colors">
                <div class="text-[10px] text-action-primary font-medium">Entrega 21h</div>
              </div>
            </div>

          </div>

        </div>

      </div>
    </main>
  </div>
</template>





