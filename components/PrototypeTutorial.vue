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
        <div class="relative bg-surface-subtle rounded-2xl max-w-2xl w-full max-h-[90vh] shadow-2xl border border-border-subtle overflow-hidden flex flex-col">
          <!-- Close Button -->
          <button
            @click="handleClose"
            class="absolute top-4 right-4 text-text-secondary hover:text-text-primary transition-colors z-10"
            aria-label="Fechar tutorial"
          >
            <i class="lni lni-close text-2xl"></i>
          </button>
          
          <!-- Content -->
          <div class="p-8 md:p-12 overflow-y-auto">
            <!-- Header -->
            <div class="mb-6">
              <div class="flex items-center gap-3 mb-3">
                <i class="lni lni-eye text-3xl text-action-primary"></i>
                <h2 class="text-2xl md:text-3xl font-light tracking-tight text-text-primary">
                  Visualizador de Protótipos
                </h2>
              </div>
              <p class="text-text-secondary font-light">
                Navegue pelo protótipo proposto e compare com a versão atual do site.
              </p>
            </div>

            <!-- Instructions Grid -->
            <div class="space-y-4 mb-6">
              <!-- Tabs -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-layers text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Alternância de Abas</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Use as abas no centro do menu para alternar entre <span class="font-medium text-text-primary">"Nova Versão"</span>, <span class="font-medium text-text-primary">"Atual"</span> e <span class="font-medium text-text-primary">"Fluxograma"</span>
                  </p>
                </div>
              </div>

              <!-- View Modes -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-display text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Modos de Visualização</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Alterne entre visualização Desktop e Mobile usando os botões no canto superior direito
                  </p>
                </div>
              </div>

              <!-- Flowchart -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-network text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Fluxograma de Navegação</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Clique na aba "Fluxograma" para visualizar o mapa completo de navegação e interações do protótipo
                  </p>
                </div>
              </div>

              <!-- Keyboard Shortcuts -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-control-panel text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Atalhos de Teclado</h3>
                  <p class="text-sm text-text-secondary font-light">
                    <kbd class="px-2 py-1 rounded bg-surface-card border border-border-subtle text-xs font-mono mr-1">H</kbd> Ocultar/Mostrar Menu
                    <span class="mx-2">•</span>
                    <kbd class="px-2 py-1 rounded bg-surface-card border border-border-subtle text-xs font-mono mr-1">F</kbd> Tela Cheia
                    <span class="mx-2">•</span>
                    <kbd class="px-2 py-1 rounded bg-surface-card border border-border-subtle text-xs font-mono mr-1">I</kbd> Informações
                  </p>
                </div>
              </div>

              <!-- Back -->
              <div class="flex items-start gap-4">
                <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-surface-card border border-border-subtle flex items-center justify-center">
                  <i class="lni lni-arrow-left text-action-primary text-xl"></i>
                </div>
                <div>
                  <h3 class="font-medium text-text-primary mb-1">Voltar ao Índice</h3>
                  <p class="text-sm text-text-secondary font-light">
                    Use a seta no canto superior esquerdo para retornar ao índice de protótipos
                  </p>
                </div>
              </div>
            </div>

            <!-- Footer Actions -->
            <div class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center justify-between pt-4 border-t border-border-subtle">
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
                Explorar Protótipo
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

const STORAGE_KEY = 'pilar-prototype-tutorial-dismissed'

onMounted(() => {
  // Verifica se o usuário já viu o tutorial
  const dismissed = localStorage.getItem(STORAGE_KEY)
  if (!dismissed) {
    // Pequeno delay para melhor UX
    setTimeout(() => {
      showTutorial.value = true
    }, 800)
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
</style>
