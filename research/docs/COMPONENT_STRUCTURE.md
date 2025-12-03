# Estrutura de Pastas - Design System PilarHomes

```
pilar-design-system/
│
├── 📁 tokens/                          # Design tokens
│   ├── colors.json                     # Paleta de cores
│   ├── typography.json                 # Tipografia
│   ├── spacing.json                    # Espaçamento
│   ├── shadows.json                    # Sombras
│   ├── borders.json                    # Bordas e radius
│   └── animations.json                 # Timing e easing
│
├── 📁 styles/                          # Estilos globais
│   ├── reset.css                       # CSS reset
│   ├── globals.css                     # Estilos globais
│   ├── utilities.css                   # Utilitários customizados
│   └── tailwind.config.js              # Configuração Tailwind
│
├── 📁 components/                      # Componentes UI
│   │
│   ├── 📁 Button/
│   │   ├── Button.vue                  # Componente
│   │   ├── Button.stories.js           # Storybook
│   │   ├── Button.test.js              # Testes
│   │   └── README.md                   # Documentação
│   │
│   ├── 📁 Card/
│   │   ├── Card.vue
│   │   ├── Card.stories.js
│   │   ├── Card.test.js
│   │   └── README.md
│   │
│   ├── 📁 Dialog/
│   │   ├── Dialog.vue
│   │   ├── Dialog.stories.js
│   │   ├── Dialog.test.js
│   │   └── README.md
│   │
│   ├── 📁 Input/
│   │   ├── Input.vue
│   │   ├── InputGroup.vue
│   │   ├── Input.stories.js
│   │   └── README.md
│   │
│   ├── 📁 Typography/
│   │   ├── Heading.vue
│   │   ├── Text.vue
│   │   ├── Typography.stories.js
│   │   └── README.md
│   │
│   ├── 📁 Skeleton/
│   │   ├── Skeleton.vue
│   │   ├── SkeletonCard.vue
│   │   └── README.md
│   │
│   ├── 📁 ImageViewer/
│   │   ├── ImageViewer.vue
│   │   ├── ImageGallery.vue
│   │   └── README.md
│   │
│   └── 📁 Share/
│       ├── ShareButton.vue
│       ├── ShareDropdown.vue
│       └── README.md
│
├── 📁 composables/                     # Vue composables / React hooks
│   ├── useDialog.js
│   ├── useToast.js
│   ├── useBreakpoint.js
│   ├── useScrollLock.js
│   └── useImageLazyLoad.js
│
├── 📁 icons/                           # Ícones SVG
│   ├── index.js                        # Export central
│   ├── ArrowRight.vue
│   ├── Close.vue
│   ├── Heart.vue
│   ├── Share.vue
│   └── ...
│
├── 📁 layouts/                         # Layouts de página
│   ├── DefaultLayout.vue
│   ├── FullWidthLayout.vue
│   └── DashboardLayout.vue
│
├── 📁 patterns/                        # Patterns/Templates
│   ├── PropertyCard.vue
│   ├── HeroSection.vue
│   ├── FilterBar.vue
│   ├── Navigation.vue
│   └── Footer.vue
│
├── 📁 assets/                          # Assets estáticos
│   ├── fonts/
│   │   ├── Inter/
│   │   │   ├── Inter-Regular.woff2
│   │   │   ├── Inter-Medium.woff2
│   │   │   ├── Inter-SemiBold.woff2
│   │   │   └── Inter-Bold.woff2
│   │   │
│   │   ├── Matter/
│   │   │   ├── MatterSQ-Regular.woff2
│   │   │   └── MatterSQ-Bold.woff2
│   │   │
│   │   └── Roboto/
│   │       ├── Roboto-Regular.woff2
│   │       └── Roboto-Medium.woff2
│   │
│   └── images/
│       ├── placeholders/
│       └── icons/
│
├── 📁 utils/                           # Utilitários
│   ├── formatters.js                   # Formatação (preço, data, etc)
│   ├── validators.js                   # Validações
│   ├── constants.js                    # Constantes
│   └── helpers.js                      # Helpers gerais
│
├── 📁 docs/                            # Documentação
│   ├── DESIGN_SYSTEM_PILARHOMES.md     # Doc completa
│   ├── IMPLEMENTATION_GUIDE_PILARHOMES.md
│   ├── DESIGN_SYSTEM_SUMMARY.md
│   ├── STACK_ANALYSIS_PILARHOMES.md
│   ├── COMPONENT_STRUCTURE.md          # Este arquivo
│   ├── CONTRIBUTING.md
│   └── CHANGELOG.md
│
├── 📁 .storybook/                      # Configuração Storybook
│   ├── main.js
│   ├── preview.js
│   └── theme.js
│
├── 📁 tests/                           # Testes
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── package.json
├── tailwind.config.js
├── vite.config.js (ou nuxt.config.js)
├── .eslintrc.js
├── .prettierrc
└── README.md
```

---

## 📝 Detalhamento de Arquivos

### tokens/colors.json

```json
{
  "primary": {
    "DEFAULT": "hsl(0, 0%, 0%)",
    "light": {
      "1": "hsl(0, 0%, 40%)",
      "2": "hsl(0, 0%, 30%)",
      "3": "hsl(0, 0%, 20%)",
      "4": "hsl(0, 0%, 10%)"
    }
  },
  "beige": {
    "DEFAULT": "hsl(35, 54%, 75%)",
    "light": {
      "1": "hsl(35, 52%, 92%)",
      "2": "hsl(34, 54%, 84%)"
    },
    "dark": {
      "1": "hsl(33, 47%, 66%)",
      "2": "hsl(33, 42%, 55%)"
    }
  },
  "semantic": {
    "success": "hsl(143, 100%, 34%)",
    "error": "hsl(359, 83%, 58%)",
    "warning": "hsl(39, 100%, 50%)"
  }
}
```

### tokens/spacing.json

```json
{
  "spacing": {
    "0": "0",
    "1": "0.25rem",
    "2": "0.5rem",
    "3": "0.75rem",
    "4": "1rem",
    "5": "1.25rem",
    "6": "1.5rem",
    "8": "2rem",
    "10": "2.5rem",
    "12": "3rem",
    "16": "4rem",
    "20": "5rem",
    "32": "8rem"
  }
}
```

### tokens/typography.json

```json
{
  "fontFamily": {
    "sans": ["Inter", "Inter Fallback: Arial", "sans-serif"],
    "display": ["Matter SQ", "Matter", "sans-serif"],
    "secondary": ["Roboto", "Roboto Fallback: Arial", "sans-serif"]
  },
  "fontSize": {
    "xs": ["0.75rem", { "lineHeight": "1rem" }],
    "sm": ["0.875rem", { "lineHeight": "1.25rem" }],
    "base": ["1rem", { "lineHeight": "1.5rem" }],
    "lg": ["1.125rem", { "lineHeight": "1.75rem" }],
    "xl": ["1.25rem", { "lineHeight": "1.75rem" }],
    "2xl": ["1.5rem", { "lineHeight": "2rem" }],
    "3xl": ["1.875rem", { "lineHeight": "2.25rem" }],
    "4xl": ["2.25rem", { "lineHeight": "2.5rem" }],
    "5xl": ["3rem", { "lineHeight": "1" }]
  },
  "fontWeight": {
    "normal": "400",
    "medium": "500",
    "semibold": "600",
    "bold": "700"
  }
}
```

---

## 🎯 Organização de Componentes

### Estrutura padrão de um componente

```
ComponentName/
├── ComponentName.vue              # Componente principal
├── ComponentName.stories.js       # Storybook stories
├── ComponentName.test.js          # Testes unitários
├── ComponentName.types.ts         # TypeScript types (se usar TS)
├── variants/                      # Variantes (se houver)
│   ├── ComponentNamePrimary.vue
│   └── ComponentNameSecondary.vue
└── README.md                      # Documentação do componente
```

### Exemplo de README.md do componente

```markdown
# Button

Componente de botão com múltiplas variantes e tamanhos.

## Uso básico

\`\`\`vue
<Button variant="primary" size="md">
  Clique aqui
</Button>
\`\`\`

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | String | 'primary' | Variante visual do botão |
| size | String | 'md' | Tamanho do botão |
| disabled | Boolean | false | Estado desabilitado |
| fullWidth | Boolean | false | Largura total |

## Variantes

- `primary` - Botão primário (fundo preto)
- `secondary` - Botão secundário (fundo bege)
- `outline` - Botão com borda
- `ghost` - Botão transparente

## Tamanhos

- `sm` - Pequeno (padding reduzido)
- `md` - Médio (padrão)
- `lg` - Grande

## Eventos

- `@click` - Emitido ao clicar no botão

## Acessibilidade

- Suporte completo para navegação por teclado
- Estados de foco visíveis
- ARIA labels quando necessário
```

---

## 🚀 Scripts do package.json

```json
{
  "scripts": {
    "dev": "nuxt dev",
    "build": "nuxt build",
    "preview": "nuxt preview",
    "lint": "eslint --ext .js,.vue .",
    "lint:fix": "eslint --ext .js,.vue . --fix",
    "format": "prettier --write \"**/*.{js,vue,css,md}\"",
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build",
    "tokens:build": "node scripts/build-tokens.js",
    "icons:build": "node scripts/build-icons.js"
  }
}
```

---

## 📦 Dependências Recomendadas

### Core

```json
{
  "dependencies": {
    "vue": "^3.3.0",
    "nuxt": "^3.8.0",
    "@nuxtjs/tailwindcss": "^6.10.0",
    "@vueuse/core": "^10.7.0",
    "@vueuse/nuxt": "^10.7.0"
  }
}
```

### Dev Dependencies

```json
{
  "devDependencies": {
    "@storybook/vue3": "^7.6.0",
    "@storybook/addon-essentials": "^7.6.0",
    "@vitest/ui": "^1.0.0",
    "vitest": "^1.0.0",
    "@vue/test-utils": "^2.4.0",
    "eslint": "^8.55.0",
    "prettier": "^3.1.0",
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.0",
    "tailwindcss": "^3.4.0"
  }
}
```

---

## 🎨 Configuração do Tailwind (completa)

### tailwind.config.js

```javascript
const colors = require('./tokens/colors.json')
const spacing = require('./tokens/spacing.json')
const typography = require('./tokens/typography.json')

module.exports = {
  content: [
    './components/**/*.{js,vue,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
  ],
  theme: {
    extend: {
      colors,
      spacing: spacing.spacing,
      fontFamily: typography.fontFamily,
      fontSize: typography.fontSize,
      fontWeight: typography.fontWeight,
      // ... resto da config (veja IMPLEMENTATION_GUIDE_PILARHOMES.md)
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
```

---

## 📚 Nuxt Config (se usar Nuxt)

### nuxt.config.js

```javascript
export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
    '@vueuse/nuxt',
  ],
  
  css: [
    '~/styles/globals.css',
  ],
  
  app: {
    head: {
      title: 'PilarHomes Design System',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true },
      ],
    },
  },
  
  tailwindcss: {
    cssPath: '~/styles/tailwind.css',
    configPath: 'tailwind.config.js',
  },
})
```

---

## 🔧 Scripts Úteis

### scripts/build-tokens.js

```javascript
// Script para gerar CSS a partir dos tokens JSON
const fs = require('fs')
const colors = require('../tokens/colors.json')

function generateCSSVariables(tokens, prefix = '') {
  let css = ':root {\n'
  
  for (const [key, value] of Object.entries(tokens)) {
    if (typeof value === 'object' && !Array.isArray(value)) {
      css += generateCSSVariables(value, `${prefix}${key}-`)
    } else {
      css += `  --${prefix}${key}: ${value};\n`
    }
  }
  
  css += '}\n'
  return css
}

const css = generateCSSVariables(colors, 'color-')
fs.writeFileSync('./styles/tokens.css', css)
console.log('✅ Tokens CSS gerados com sucesso!')
```

---

## 📖 Storybook Config

### .storybook/preview.js

```javascript
import '../styles/globals.css'

export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
  controls: {
    matchers: {
      color: /(background|color)$/i,
      date: /Date$/,
    },
  },
  backgrounds: {
    default: 'white',
    values: [
      { name: 'white', value: '#ffffff' },
      { name: 'beige', value: 'hsl(35, 54%, 75%)' },
      { name: 'dark', value: '#000000' },
    ],
  },
}
```

---

## ✅ Checklist de Implementação

### Setup Inicial
- [ ] Criar estrutura de pastas
- [ ] Configurar Tailwind CSS
- [ ] Setup de fonts (Inter, Matter SQ, Roboto)
- [ ] Configurar tokens JSON
- [ ] Setup Storybook

### Componentes Base
- [ ] Button
- [ ] Card
- [ ] Input
- [ ] Typography (Heading, Text)
- [ ] Dialog/Modal
- [ ] Skeleton Loader

### Componentes Complexos
- [ ] Image Viewer
- [ ] Navigation
- [ ] Footer
- [ ] Property Card
- [ ] Filter Bar
- [ ] Hero Section

### Utilitários
- [ ] Composables/Hooks
- [ ] Formatters
- [ ] Validators
- [ ] Icons library

### Documentação
- [ ] README.md de cada componente
- [ ] Storybook stories
- [ ] Guias de uso
- [ ] Changelog

### Testes
- [ ] Setup de testes (Vitest)
- [ ] Testes unitários dos componentes
- [ ] Testes de acessibilidade
- [ ] Coverage mínimo de 80%

### Performance
- [ ] Lazy loading de componentes
- [ ] Code splitting
- [ ] Otimização de imagens
- [ ] Tree shaking

---

*Estrutura criada em 02/12/2025*  
*Baseada no Design System PilarHomes extraído*
