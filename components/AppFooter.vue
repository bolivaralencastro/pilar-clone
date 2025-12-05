<script setup lang="ts">
</script>

<template>
  <footer class="bg-deep-brown text-off-white py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Logo e Descrição -->
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-10 h-10 bg-off-white rounded-lg flex items-center justify-center">
              <span class="text-deep-brown font-bold text-xl">P</span>
            </div>
            <span class="text-xl font-bold">Pilar Clone</span>
          </div>
          <p class="text-off-white/80 mb-4">
            Clone do sistema de busca de imóveis Pilar Homes. 
            Projeto desenvolvido para fins de estudo.
          </p>
          <p class="text-off-white/60 text-sm">
            Este é um projeto de estudo. Dados fornecidos pela API pública da Pilar Homes.
          </p>
        </div>
        
        <!-- Links Rápidos -->
        <div>
          <h4 class="font-semibold mb-4">Links</h4>
          <ul class="space-y-2">
            <li>
              <NuxtLink to="/" class="text-off-white/80 hover:text-off-white transition-colors">
                Buscar Imóveis
              </NuxtLink>
            </li>
            <li>
              <a 
                href="https://pilarhomes.com.br" 
                target="_blank" 
                rel="noopener noreferrer"
                class="text-off-white/80 hover:text-off-white transition-colors"
              >
                Site Original
              </a>
            </li>
            <li>
              <a 
                href="https://github.com" 
                target="_blank" 
                rel="noopener noreferrer"
                class="text-off-white/80 hover:text-off-white transition-colors"
              >
                GitHub
              </a>
            </li>
          </ul>
        </div>
        
        <!-- Tecnologias -->
        <div>
          <h4 class="font-semibold mb-4">Tecnologias</h4>
          <ul class="space-y-2 text-off-white/80">
            <li>Nuxt.js 3</li>
            <li>Vue.js 3</li>
            <li>Tailwind CSS</li>
            <li>Vercel</li>
          </ul>
        </div>
      </div>
      
      <!-- Copyright -->
      <div class="border-t border-off-white/10 mt-8 pt-8 text-center text-off-white/60 text-sm">
        <p>© 2025 Pilar Clone. Projeto de estudo - Não oficial.</p>
      </div>
    </div>
  </footer>
</template>
