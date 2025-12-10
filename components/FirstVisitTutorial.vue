<template>
  <Teleport to="body">
    <Transition name="fade">
      <div 
        v-if="showTutorial"
        class="fixed inset-0 z-[100] flex items-center justify-center px-4"
        @click.self="handleClose"
      >
        <!-- Backdrop com blur -->
        <div class="absolute inset-0 bg-text-primary/20 backdrop-blur-sm"></div>
        
        <!-- Dialog -->
        <div class="relative bg-surface-subtle rounded-2xl max-w-2xl w-full shadow-2xl border border-border-subtle overflow-hidden">
          <!-- Close Button -->
          <button
            @click="handleClose"
            class="absolute top-4 right-4 text-text-secondary hover:text-text-primary transition-colors z-10"
            aria-label="Fechar tutorial"
          >
            <i class="lni lni-close text-2xl"></i>
          </button>
          
          <!-- Content -->
          <div class="p-8 md:p-12">
            <!-- Header -->
            <div class="mb-8">
              <div class="flex items-center gap-3 mb-4">
                <i class="lni lni-compass text-4xl text-action-primary"></i>
                <h2 class="text-3xl md:text-4xl font-light tracking-tight text-text-primary">
                  Bem-vindo ao Projeto
                </h2>
              </div>
              <p class="text-text-secondary font-light text-lg">
                Esta é uma jornada completa de design e engenharia. Aqui estão algumas dicas para navegar:
              </p>
            </div>

            <!-- Instructions Grid -->
            <div class="space-y-6 mb-8">
              <!-- Navigation -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-arrow-left-circle text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Navegação por Teclado</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Use <kbd class="px-2 py-1 rounded bg-surface-card border border-border-subtle text-xs font-mono">←</kbd> e 
                    <kbd class="px-2 py-1 rounded bg-surface-card border border-border-subtle text-xs font-mono">→</kbd> para navegar entre seções
                  </p>
                </div>
              </div>

              <!-- Menu -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-menu text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Menu de Navegação</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Clique no menu no topo direito para acessar todas as seções do projeto
                  </p>
                </div>
              </div>

              <!-- Flow -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-network text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Fluxo Estruturado</h3>
                  <p class="text-sm text-text-secondary font-light">
                    O projeto segue uma ordem cronológica: Briefing → Planejamento → Discovery → Estratégia → Ideação → UI Design → Protótipo → Roadmap
                  </p>
                </div>
              </div>

              <!-- Logo Home -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-home text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Voltar ao Início</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Clique no logo "Pilar Homes" no topo esquerdo para retornar à página inicial
                  </p>
                </div>
              </div>
            </div>

            <!-- Footer Actions -->
            <div class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center justify-between pt-6 border-t border-border-subtle">
              <label class="flex items-center gap-2 text-sm text-text-secondary cursor-pointer group">
                <input 
                  v-model="dontShowAgain" 
                  type="checkbox"
                  class="w-4 h-4 rounded border-border-subtle text-action-primary focus:ring-action-primary focus:ring-offset-0"
                />
                <span class="group-hover:text-text-primary transition-colors">Não mostrar novamente</span>
              </label>
              
              <button
                @click="handleClose"
                class="px-6 py-3 bg-action-primary hover:bg-action-hover text-text-inverse rounded-lg font-medium transition-colors"
              >
                Começar a Explorar
              </button>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
const showTutorial = ref(false)
const dontShowAgain = ref(false)

const STORAGE_KEY = 'pilar-tutorial-dismissed'

onMounted(() => {
  // Verifica se o usuário já viu o tutorial
  const dismissed = localStorage.getItem(STORAGE_KEY)
  if (!dismissed) {
    // Pequeno delay para melhor UX
    setTimeout(() => {
      showTutorial.value = true
    }, 500)
  }
})

const handleClose = () => {
  showTutorial.value = false
  
  if (dontShowAgain.value) {
    localStorage.setItem(STORAGE_KEY, 'true')
  }
}

// Fechar com tecla ESC
onMounted(() => {
  const handleEscape = (e: KeyboardEvent) => {
    if (e.key === 'Escape' && showTutorial.value) {
      handleClose()
    }
  }
  
  window.addEventListener('keydown', handleEscape)
  
  onUnmounted(() => {
    window.removeEventListener('keydown', handleEscape)
  })
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active .relative,
.fade-leave-active .relative {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-enter-from .relative {
  opacity: 0;
  transform: scale(0.95) translateY(10px);
}

.fade-leave-to .relative {
  opacity: 0;
  transform: scale(0.95) translateY(10px);
}

kbd {
  display: inline-block;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}
</style>
