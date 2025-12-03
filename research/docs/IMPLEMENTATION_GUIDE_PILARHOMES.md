# Guia de Implementação - Design System PilarHomes

> Exemplos práticos de código para implementar o Design System da Pilar

---

## 🎨 Configuração do Tailwind CSS

### tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx,vue}',
    './components/**/*.{js,ts,jsx,tsx,mdx,vue}',
    './app/**/*.{js,ts,jsx,tsx,mdx,vue}',
  ],
  theme: {
    extend: {
      colors: {
        // Primária
        primary: {
          DEFAULT: 'hsl(0, 0%, 0%)',
          light: {
            1: 'hsl(0, 0%, 40%)',
            2: 'hsl(0, 0%, 30%)',
            3: 'hsl(0, 0%, 20%)',
            4: 'hsl(0, 0%, 10%)',
          },
        },
        
        // Secondary
        secondary: {
          DEFAULT: 'hsl(48, 20%, 95%)',
          dark: {
            1: 'hsl(50, 12%, 91%)',
            2: 'hsl(32, 19%, 82%)',
          },
        },
        
        // Beige (Cor característica)
        beige: {
          DEFAULT: 'hsl(35, 54%, 75%)',
          light: {
            1: 'hsl(35, 52%, 92%)',
            2: 'hsl(34, 54%, 84%)',
          },
          dark: {
            1: 'hsl(33, 47%, 66%)',
            2: 'hsl(33, 42%, 55%)',
          },
        },
        
        // Blue
        blue: {
          DEFAULT: '#b9cddf',
          light: {
            1: 'hsl(208, 37%, 93%)',
            2: 'hsl(208, 38%, 87%)',
          },
          dark: {
            1: 'hsl(206, 44%, 67%)',
            2: 'hsl(206, 46%, 61%)',
          },
        },
        
        // Brown
        brown: {
          DEFAULT: 'hsl(29, 34%, 18%)',
          light: {
            1: 'hsl(30, 7%, 73%)',
            2: 'hsl(30, 9%, 45%)',
          },
          dark: {
            1: 'hsl(31, 36%, 14%)',
            2: 'hsl(25, 35%, 10%)',
          },
        },
        
        // Estados
        success: {
          DEFAULT: 'hsl(143, 100%, 34%)',
          light: {
            1: 'hsl(137, 35%, 92%)',
            2: 'hsl(140, 48%, 82%)',
          },
          dark: {
            1: 'hsl(141, 100%, 28%)',
            2: 'hsl(137, 100%, 19%)',
          },
        },
        
        error: {
          DEFAULT: 'hsl(359, 83%, 58%)',
          light: {
            1: 'hsl(347, 100%, 91%)',
            2: 'hsl(350, 100%, 82%)',
          },
          dark: {
            1: 'hsl(1, 65%, 50%)',
            2: 'hsl(0, 76%, 37%)',
          },
        },
        
        warning: {
          DEFAULT: 'hsl(39, 100%, 50%)',
          light: {
            1: 'hsl(43, 100%, 95%)',
            2: 'hsl(46, 90%, 76%)',
          },
          dark: {
            1: 'hsl(34, 88%, 52%)',
            2: 'hsl(25, 68%, 50%)',
          },
        },
        
        // Neutros
        white: {
          DEFAULT: 'hsl(0, 0%, 100%)',
          dark: {
            1: 'hsl(0, 0%, 98%)',
            2: 'hsl(0, 0%, 95%)',
            3: 'hsl(0, 0%, 90%)',
            4: 'hsl(0, 0%, 80%)',
          },
        },
      },
      
      fontFamily: {
        sans: ['Inter', 'Inter Fallback: Arial', 'sans-serif'],
        display: ['Matter SQ', 'Matter', 'sans-serif'],
        secondary: ['Roboto', 'Roboto Fallback: Arial', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace'],
      },
      
      spacing: {
        '0.5': '0.125rem',  // 2px
        '1': '0.25rem',     // 4px
        '2': '0.5rem',      // 8px
        '3': '0.75rem',     // 12px
        '4': '1rem',        // 16px
        '5': '1.25rem',     // 20px
        '6': '1.5rem',      // 24px
        '7': '1.75rem',     // 28px
        '8': '2rem',        // 32px
        '9': '2.25rem',     // 36px
        '10': '2.5rem',     // 40px
        '11': '2.75rem',    // 44px
        '12': '3rem',       // 48px
        '16': '4rem',       // 64px
        '20': '5rem',       // 80px
        '32': '8rem',       // 128px
      },
      
      borderRadius: {
        'none': '0',
        'sm': '0.125rem',   // 2px
        'DEFAULT': '0.25rem', // 4px
        'md': '0.5rem',     // 8px
        'lg': '1rem',       // 16px
        'full': '9999px',
      },
      
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],      // 12px
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],  // 14px
        'base': ['1rem', { lineHeight: '1.5rem' }],     // 16px
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],  // 18px
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],   // 20px
        '2xl': ['1.5rem', { lineHeight: '2rem' }],      // 24px
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }], // 30px
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],   // 36px
        '5xl': ['3rem', { lineHeight: '1' }],           // 48px
      },
      
      transitionDuration: {
        '150': '150ms',
        '200': '200ms',
        '300': '300ms',
        '400': '400ms',
        '500': '500ms',
        '1000': '1000ms',
        '1500': '1500ms',
      },
      
      transitionTimingFunction: {
        'slide': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      
      screens: {
        'xs': '481px',
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
      
      zIndex: {
        '0': '0',
        '10': '10',
        '20': '20',
        '30': '30',
        '40': '40',
        '50': '50',
        '60': '60',
        '70': '70',
        '80': '80',
        '90': '90',
        '100': '100',
        'fullscreen': '1000',
      },
    },
  },
  plugins: [],
}
```

---

## 🎨 CSS Global (styles.css)

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Cores Principais */
    --primary: 0 0% 0%;
    --primary-light-1: 0 0% 40%;
    --primary-light-2: 0 0% 30%;
    --primary-light-3: 0 0% 20%;
    --primary-light-4: 0 0% 10%;
    
    --secondary: 48 20% 95%;
    --beige: 35 54% 75%;
    --blue: #b9cddf;
    --brown: 29 34% 18%;
    
    /* Estados */
    --success: 143 100% 34%;
    --error: 359 83% 58%;
    --warning: 39 100% 50%;
    
    /* Neutros */
    --white: 0 0% 100%;
    --background: 0 0% 100%;
    --foreground: 0 0% 0%;
    
    /* Sistema */
    --border: 0 0% 14.9%;
    --input: 0 0% 14.9%;
    --ring: 0 0% 83.1%;
    
    /* Tipografia */
    --font-family-display: "Inter", "sans-serif";
  }
  
  * {
    @apply border-border;
  }
  
  body {
    @apply bg-background text-foreground font-sans;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
  
  /* Scroll Lock */
  body.scroll-locked {
    @apply fixed overflow-hidden w-full h-full;
    touch-action: none;
  }
}

@layer components {
  /* Componentes customizados aqui */
}

@layer utilities {
  /* Utilitários customizados */
  .no-scrollbar::-webkit-scrollbar {
    display: none;
  }
  
  .no-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
}
```

---

## 🧩 Componentes Vue/React

### Button Component (Vue)

```vue
<template>
  <button
    :class="buttonClasses"
    :type="type"
    :disabled="disabled"
    @click="$emit('click', $event)"
  >
    <slot />
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'outline', 'ghost'].includes(value)
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  type: {
    type: String,
    default: 'button'
  },
  disabled: Boolean,
  fullWidth: Boolean,
})

const emit = defineEmits(['click'])

const buttonClasses = computed(() => {
  const base = 'inline-flex items-center justify-center font-medium transition-all duration-150 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed'
  
  const variants = {
    primary: 'bg-primary text-white hover:bg-primary-light-1 focus:ring-primary-light-2',
    secondary: 'bg-secondary text-primary hover:bg-secondary-dark-1',
    outline: 'border border-primary text-primary hover:bg-primary hover:text-white',
    ghost: 'bg-transparent text-primary hover:bg-primary/10',
  }
  
  const sizes = {
    sm: 'px-3 py-1.5 text-sm rounded-md',
    md: 'px-4 py-2 text-base rounded-full',
    lg: 'px-6 py-3 text-lg rounded-full',
  }
  
  const width = props.fullWidth ? 'w-full' : ''
  
  return [base, variants[props.variant], sizes[props.size], width].join(' ')
})
</script>
```

### Button Component (React/TypeScript)

```typescript
import React from 'react'

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  fullWidth?: boolean
  children: React.ReactNode
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  fullWidth = false,
  children,
  className = '',
  disabled,
  ...props
}) => {
  const baseClasses = 'inline-flex items-center justify-center font-medium transition-all duration-150 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed'
  
  const variantClasses = {
    primary: 'bg-primary text-white hover:bg-primary-light-1 focus:ring-primary-light-2',
    secondary: 'bg-secondary text-primary hover:bg-secondary-dark-1',
    outline: 'border border-primary text-primary hover:bg-primary hover:text-white',
    ghost: 'bg-transparent text-primary hover:bg-primary/10',
  }
  
  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm rounded-md',
    md: 'px-4 py-2 text-base rounded-full',
    lg: 'px-6 py-3 text-lg rounded-full',
  }
  
  const widthClass = fullWidth ? 'w-full' : ''
  
  const classes = [
    baseClasses,
    variantClasses[variant],
    sizeClasses[size],
    widthClass,
    className
  ].filter(Boolean).join(' ')
  
  return (
    <button
      className={classes}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  )
}
```

### Card Component (Vue)

```vue
<template>
  <div :class="cardClasses">
    <slot />
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'elevated', 'outlined'].includes(value)
  },
  padding: {
    type: String,
    default: 'md',
    validator: (value) => ['none', 'sm', 'md', 'lg'].includes(value)
  }
})

const cardClasses = computed(() => {
  const base = 'rounded-md'
  
  const variants = {
    default: 'bg-white',
    elevated: 'bg-white shadow-lg',
    outlined: 'bg-white border border-border',
  }
  
  const paddings = {
    none: '',
    sm: 'p-3',
    md: 'p-6',
    lg: 'p-8',
  }
  
  return [base, variants[props.variant], paddings[props.padding]].join(' ')
})
</script>
```

### Skeleton Loader (CSS)

```css
.skeleton {
  animation: skeleton-pulse 1.5s ease-in-out infinite;
  background-color: #e0e0e0;
  border-radius: 4px;
}

@keyframes skeleton-pulse {
  0%, 100% {
    background-color: #e0e0e0;
  }
  50% {
    background-color: #f0f0f0;
  }
}
```

```vue
<template>
  <div class="skeleton" :style="{ width, height }" />
</template>

<script setup>
defineProps({
  width: {
    type: String,
    default: '100%'
  },
  height: {
    type: String,
    default: '20px'
  }
})
</script>
```

### Dialog/Modal Component (Vue)

```vue
<template>
  <Teleport to="body">
    <Transition
      name="slide-up"
      @after-leave="$emit('after-leave')"
    >
      <div
        v-if="modelValue"
        class="fixed inset-0 z-50 flex items-end sm:items-center justify-center"
      >
        <!-- Backdrop -->
        <div
          class="fixed inset-0 bg-black/50 transition-opacity"
          @click="close"
        />
        
        <!-- Dialog -->
        <div
          class="relative bg-white rounded-t-lg sm:rounded-lg w-full max-w-lg max-h-[90vh] overflow-hidden"
          role="dialog"
          aria-modal="true"
        >
          <!-- Header -->
          <div class="flex items-center justify-between p-6 border-b">
            <h2 class="text-xl font-semibold">
              <slot name="title">{{ title }}</slot>
            </h2>
            <button
              class="p-2 hover:bg-gray-100 rounded-full transition-colors"
              @click="close"
            >
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <!-- Content -->
          <div class="p-6 overflow-y-auto" data-scroll-area>
            <slot />
          </div>
          
          <!-- Footer (optional) -->
          <div v-if="$slots.footer" class="p-6 border-t bg-gray-50">
            <slot name="footer" />
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  modelValue: Boolean,
  title: String,
  closeOnBackdrop: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['update:modelValue', 'after-leave'])

function close() {
  if (props.closeOnBackdrop) {
    emit('update:modelValue', false)
  }
}

// Lock scroll when modal is open
watch(() => props.modelValue, (isOpen) => {
  if (isOpen) {
    document.body.classList.add('scroll-locked')
  } else {
    document.body.classList.remove('scroll-locked')
  }
})
</script>

<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
  transform: translateY(100%);
}

@media (min-width: 640px) {
  .slide-up-enter-from,
  .slide-up-leave-to {
    transform: translateY(0) scale(0.95);
    opacity: 0;
  }
}
</style>
```

---

## 📱 Exemplos de Uso Responsivo

```vue
<template>
  <!-- Grid responsivo -->
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
    <div v-for="item in items" :key="item.id" class="...">
      <!-- Item content -->
    </div>
  </div>
  
  <!-- Stack vertical em mobile, horizontal em desktop -->
  <div class="flex flex-col md:flex-row gap-4">
    <div class="flex-1">...</div>
    <div class="flex-1">...</div>
  </div>
  
  <!-- Texto responsivo -->
  <h1 class="text-2xl md:text-3xl lg:text-4xl xl:text-5xl font-bold">
    Título Responsivo
  </h1>
  
  <!-- Padding responsivo -->
  <section class="px-4 sm:px-6 lg:px-8 py-8 lg:py-16">
    <!-- Content -->
  </section>
  
  <!-- Esconder em mobile -->
  <div class="hidden md:block">
    Visível apenas em desktop
  </div>
  
  <!-- Mostrar apenas em mobile -->
  <div class="block md:hidden">
    Visível apenas em mobile
  </div>
</template>
```

---

## 🎨 Utilitários Customizados

```css
/* Truncate text with ellipsis */
.truncate-2-lines {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Aspect ratio containers */
.aspect-16-9 {
  aspect-ratio: 16 / 9;
}

.aspect-4-3 {
  aspect-ratio: 4 / 3;
}

.aspect-square {
  aspect-ratio: 1 / 1;
}

/* Safe area padding (for iOS) */
.safe-area-top {
  padding-top: env(safe-area-inset-top);
}

.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}

/* Smooth scroll */
.smooth-scroll {
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
}

/* Focus visible only for keyboard navigation */
.focus-visible:focus-visible {
  outline: 2px solid hsl(var(--ring));
  outline-offset: 2px;
}
```

---

## 🎯 Patterns Comuns

### Hero Section

```vue
<template>
  <section class="relative h-screen flex items-center justify-center bg-black text-white">
    <!-- Background Image -->
    <div class="absolute inset-0 opacity-50">
      <img
        src="hero-bg.jpg"
        alt=""
        class="w-full h-full object-cover"
      />
    </div>
    
    <!-- Content -->
    <div class="relative z-10 text-center px-4 max-w-4xl mx-auto">
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6">
        O endereço dos melhores endereços
      </h1>
      <p class="text-lg md:text-xl mb-8 text-white/90">
        Encontre casas e apartamentos à venda nos melhores endereços
      </p>
      <Button variant="primary" size="lg">
        Explorar Imóveis
      </Button>
    </div>
  </section>
</template>
```

### Property Card

```vue
<template>
  <article class="group bg-white rounded-md overflow-hidden shadow-sm hover:shadow-lg transition-shadow duration-300">
    <!-- Image -->
    <div class="relative aspect-4-3 overflow-hidden">
      <img
        :src="property.image"
        :alt="property.title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
      />
      
      <!-- Badge -->
      <div v-if="property.isExclusive" class="absolute top-4 left-4 bg-primary text-white px-3 py-1 text-sm rounded-full">
        Exclusivo PilarHomes
      </div>
    </div>
    
    <!-- Content -->
    <div class="p-6">
      <!-- Price -->
      <p class="text-2xl font-bold text-primary mb-2">
        {{ formatPrice(property.price) }}
      </p>
      
      <!-- Title -->
      <h3 class="text-lg font-semibold mb-2 truncate-2-lines">
        {{ property.title }}
      </h3>
      
      <!-- Location -->
      <p class="text-sm text-gray-600 mb-4">
        {{ property.location }}
      </p>
      
      <!-- Details -->
      <div class="flex items-center gap-4 text-sm text-gray-500">
        <span>{{ property.bedrooms }} quartos</span>
        <span>{{ property.area }}m²</span>
        <span>{{ property.parking }} vagas</span>
      </div>
    </div>
  </article>
</template>

<script setup>
defineProps({
  property: {
    type: Object,
    required: true
  }
})

function formatPrice(price) {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  }).format(price)
}
</script>
```

---

## 🚀 Performance Tips

### Lazy Loading de Imagens

```vue
<template>
  <img
    :src="placeholder"
    :data-src="src"
    :alt="alt"
    class="lazy-image"
    loading="lazy"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  src: String,
  alt: String,
  placeholder: {
    type: String,
    default: 'data:image/svg+xml,...' // SVG placeholder
  }
})

onMounted(() => {
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target
          img.src = img.dataset.src
          imageObserver.unobserve(img)
        }
      })
    })
    
    imageObserver.observe(document.querySelector('.lazy-image'))
  }
})
</script>
```

---

*Guia gerado em 02/12/2025 baseado no Design System PilarHomes*
