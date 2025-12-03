# Design System Pilar — Guia Único e Completo

Documento unificado com tudo o que é necessário para implementar, manter e evoluir o design system da Pilar. Reúne cores, tipografia, espaçamento, componentes, padrões de interação, tokens prontos para Tailwind/CSS e referências de estrutura de pastas extraídas da pasta de pesquisa.

---

## Índice
1. [Principais atalhos](#principais-atalhos)
2. [Fundamentos de marca](#fundamentos-de-marca)
   - [Paleta de cores](#paleta-de-cores)
   - [Tipografia](#tipografia)
   - [Espaçamento e grid](#espaçamento-e-grid)
3. [Componentes e padrões](#componentes-e-padrões)
4. [Responsividade e breakpoints](#responsividade-e-breakpoints)
5. [Interações, sombras e estados](#interações-sombras-e-estados)
6. [Acessibilidade e performance](#acessibilidade-e-performance)
7. [Tokens prontos para Tailwind/CSS](#tokens-prontos-para-tailwindcss)
8. [Inventário e métricas de uso](#inventário-e-métricas-de-uso)
9. [Estrutura recomendada do design system](#estrutura-recomendada-do-design-system)
10. [Checklist de adoção](#checklist-de-adoção)
11. [Guia prático de implementação](#guia-prático-de-implementação)
12. [Cobertura das fontes originais](#cobertura-das-fontes-originais)

---

## Principais atalhos
- **CSS variables rápidas:** copie o bloco em [Tokens prontos](#tokens-prontos-para-tailwindcss).
- **Cores oficiais:** preto (`--primary`), beige (`--beige`), azul (`--blue`), marrom (`--brown`) e estados (`--success`, `--error`, `--warning`).
- **Tipografia:** Inter (base), Matter/Matter SQ (display), Roboto (secundária), monospace para dados. Escala de 12px a 48px.
- **Espaçamento:** sistema de 4px com 8/16/20/24/32px como valores mais recorrentes.
- **Componentes-chave:** Button, Card, Dialog/Modal, Input (campo e group), Typography (Heading/Text), Skeleton, ImageViewer, Share.
- **Breakpoints:** mobile-first — `<640px`, `640–1023px`, `1024–1279px`, `1280–1535px`, `≥1536px` (com pontos adicionais 768/960/1200/1400/1728px).
- **Interações:** transições de 150–400ms, `cubic-bezier(0.16, 1, 0.3, 1)` para modais, radius padrão `4px` (pill `9999px`).

---

## Fundamentos de marca

### Paleta de cores
**Primárias**
- **Primary (Preto):** `--primary: 0 0% 0%` + variações `--primary-light-[1-4]` (10–40% lightness) para hover/focus.
- **Beige:** `--beige: 35 54% 75%` com tons claros/escuros (`--beige-light-[1-2]`, `--beige-dark-[1-2]`).
- **Blue:** `--blue: #b9cddf` com variantes `--blue-light-[1-2]` e `--blue-dark-[1-2]` para links/CTAs secundários.
- **Brown:** `--brown: 29 34% 18%` + variações `--brown-light-[1-2]` e `--brown-dark-[1-2]` para fundos ou divisões de seção.

**Estados**
- **Success:** `--success: 143 100% 34%` com tons `light` e `dark` para feedback.
- **Error:** `--error: 359 83% 58%` com variantes claras/escuras.
- **Warning:** `--warning: 39 100% 50%` com variantes claras/escuras.

**Neutros e superfícies**
- Branco base `--white` e gradações até 80%.
- Sistema de UI: `--background: 3.9%`, `--foreground: 98%`, `--muted`/`--muted-foreground` (14.9%/63.9%), `--border`/`--input` (14.9%), `--ring: 83.1%`.
- Superfícies: `--card`, `--popover`, `--accent` e respectivos `-foreground`.

**Recomendações**
- Preferir `text-primary`, `bg-primary`, `bg-primary/40` e `hover:bg-primary` em Tailwind (usos mais frequentes).
- Para sobreposições, sombras e backdrops, usar `rgba(0,0,0,0.1–0.15)`; para backdrop de modal, `rgba(0,0,0,0.5)`.
- Freq. no código legado: `text-primary` (144x), `bg-primary` (39x), `bg-primary/40` (50x), `hover:bg-primary` (24x).

### Tipografia
- **Famílias:** Inter (principal), Matter/Matter SQ (display), Roboto (secundária), monospace para dados.
- **Escala sugerida (px → Tailwind):** 12 (`text-xs`), 14 (`text-sm`), 16 (`text-base`), 18 (`text-lg`), 20 (`text-xl`), 24 (`text-2xl`), 30 (`text-3xl`), 36 (`text-4xl`), 48 (`text-5xl`).
- **Pesos usuais:** 400 (regular), 500 (medium), 600 (semibold), 700 (bold).
- **Práticas:**
  - Títulos: Matter/Matter SQ para destaque; Inter bold/semibold como fallback.
  - Corpo: Inter 16px (`text-base`) com line-height confortável (1.5x).
  - Legendas/detalhes: 12–14px com peso 500 para legibilidade.
  - Campos e botões: 14–16px, peso 500/600.
- Freq. de uso em produção: `text-base` (116x), `text-sm` (46x), `text-xs` (40x); tamanhos custom `text-[14px]` (48x) e `text-[12px]` (36x).

### Espaçamento e grid
- **Sistema 4px:** 0, 4, 8, 12, 16, 20, 24, 32, 48, 64, 80, 128px.
- **Mais usados:** 8px (gaps pequenos), 16px (base), 20px (padding médio), 24px (padding padrão), 32px (espaços maiores), 48–80px (seções), 128px (hero ou áreas amplas).
- **Grid/Layout:** predominância de flex (`flex`, `flex-col`) com uso de grid em vitrines/listagens; containers grandes podem usar 12 colunas.
- **Safe area:** respeitar áreas de segurança em mobile e targets mínimos de 44x44px.
- **Frequências reais** (HTML analisado): `1.25rem` (20px, 40x), `0.5rem` (8px, 38x), `1.5rem` (24px, 35x), `2rem` (32px, 33x), `1rem` (16px, 32x), `3rem` (48px, 23x), `0.75rem` (12px, 22x), `2.75rem` (44px, 20x), `0.25rem` (4px, 18x), `2.25rem` (36px, 16x), `5rem` (80px, 13x), `4rem` (64px, 9x), `8rem` (128px, 6x).

---

## Componentes e padrões
### Button
- Variantes: **primary**, **secondary**, **outline**, **ghost**.
- Tamanhos: **sm**, **md**, **lg**.
- Estados: default, hover, focus, disabled; foco com `focus:ring-2 focus:ring-offset-2`.
- Forma: `rounded-full` (pill) como padrão; animações rápidas (~150–200ms).

### Card / Containers
- Variantes: **default**, **elevated**, **outlined**.
- Padding: none, 12px (sm), 24px (md), 32px (lg).
- Radius: `--radius` (4px) ou `rounded-md`; usar `shadow-sm` leve em elevates.

### Dialog / Modal
- Backdrop `bg-black/50`; animação **slide-up** 0.4s com `cubic-bezier(0.16, 1, 0.3, 1)`.
- Z-index padrão 50; aplicar `overscroll-behavior: contain` para evitar scroll em background e travar body (`scroll-locked`).

### Inputs (campo e group)
- Campos simples e agrupados (`InputGroup`) com bordas `--border`/`--input`, radius 4px, foco com `ring` claro.
- Incluir estados de erro/sucesso seguindo cores semânticas.

### Typography (Heading/Text)
- Componentes reutilizáveis para títulos e parágrafos, alinhados à escala de tamanhos e pesos descritos.

### Skeleton Loader
- Animação `skeleton-pulse` de 1.5s alternando tons de cinza; cards variantes para placeholders de listas.

### Image Viewer / Gallery
- Suporte a fullscreen, zoom e gestos; containers `flex` com `overflow: hidden` e `object-fit: cover`.

### Share
- Duas variantes: botão em linha com ícones contornados e dropdown em coluna (tipografia 12–14px).

### Patterns e layouts
- Hero, PropertyCard, FilterBar, Navigation e Footer estão mapeados como patterns recomendados para reutilização.

### Ícones
- 98 SVGs mapeados; **viewBox 24x24** como padrão. Sugestão de tamanhos: sm (~14px), md (16px), lg (24px), xl (32px). Usar `currentColor` para herdar cor.

---

## Responsividade e breakpoints
- **Abordagem:** mobile first.
- **Faixas principais:** `<640px` (mobile), `640–1023px` (tablet), `1024–1279px` (desktop), `1280–1535px` (large), `≥1536px` (XL).
- **Faixas adicionais usadas em componentes:** 768px, 960px, 1200px, 1400px, 1728px.
- **Práticas:** media query `@media (hover: hover)` para desabilitar efeitos em touch; garantir padding de safe area em iOS.

---

## Interações, sombras e estados
- **Border radius:** 0, 2, 4 (`--radius`), 8, 16px; pill 9999px; círculo 50%.
- **Transições:** 150–400ms. Interações rápidas (150–200ms), hover (200–300ms), modais (400ms).
- **Curvas:** `ease-in-out` (`cubic-bezier(0.4, 0, 0.2, 1)`) e `cubic-bezier(0.16, 1, 0.3, 1)` para entradas/saídas suaves.
- **Sombras:** overlays leves `rgba(0,0,0,0.1–0.15)`; backdrop de modal `0 0 0 200px rgba(0,0,0,0.5)`.
- **Z-index padrão:** base 1, dropdown 10, sticky 20, fixed 30, modal/backdrop 40–50, popover 60, tooltip 70, fullscreen 1000.

---

## Acessibilidade e performance
- **A11y:** anel de foco 2px com offset, contraste mínimo AA, navegação por teclado, alvos de toque ≥44x44px.
- **Performance:** lazy loading de imagens, code splitting por componente, imagens WebP (quality ~80), CDN (CloudFront), CSS encapsulado por componente.
- **Responsividade:** mobile first, touch-friendly, uso de `hover:hover`, safe area em iOS.

---

## Tokens prontos para Tailwind/CSS
```css
:root {
  /* Cores de marca */
  --primary: 0 0% 0%;
  --primary-light-1: 0 0% 40%;
  --primary-light-2: 0 0% 30%;
  --primary-light-3: 0 0% 20%;
  --primary-light-4: 0 0% 10%;

  --beige: 35 54% 75%;
  --beige-light-1: 35 52% 92%;
  --beige-light-2: 34 54% 84%;
  --beige-dark-1: 33 47% 66%;
  --beige-dark-2: 33 42% 55%;

  --blue: #b9cddf;
  --blue-light-1: 208 37% 93%;
  --blue-light-2: 208 38% 87%;
  --blue-dark-1: 206 44% 67%;
  --blue-dark-2: 206 46% 61%;

  --brown: 29 34% 18%;
  --brown-light-1: 30 7% 73%;
  --brown-light-2: 30 9% 45%;
  --brown-dark-1: 31 36% 14%;
  --brown-dark-2: 25 35% 10%;

  /* Estados */
  --success: 143 100% 34%;
  --success-light-1: 137 35% 92%;
  --success-light-2: 140 48% 82%;
  --success-dark-1: 141 100% 28%;
  --success-dark-2: 137 100% 19%;

  --error: 359 83% 58%;
  --error-light-1: 347 100% 91%;
  --error-light-2: 350 100% 82%;
  --error-dark-1: 1 65% 50%;
  --error-dark-2: 0 76% 37%;

  --warning: 39 100% 50%;
  --warning-light-1: 43 100% 95%;
  --warning-light-2: 46 90% 76%;
  --warning-dark-1: 34 88% 52%;
  --warning-dark-2: 25 68% 50%;

  /* Neutros / sistema */
  --white: 0 0% 100%;
  --white-dark-1: 0 0% 98%;
  --white-dark-2: 0 0% 95%;
  --white-dark-3: 0 0% 90%;
  --white-dark-4: 0 0% 80%;
  --background: 0 0% 3.9%;
  --foreground: 0 0% 98%;
  --muted: 0 0% 14.9%;
  --muted-foreground: 0 0% 63.9%;
  --card: 0 0% 3.9%;
  --card-foreground: 0 0% 98%;
  --popover: 0 0% 3.9%;
  --popover-foreground: 0 0% 98%;
  --border: 0 0% 14.9%;
  --input: 0 0% 14.9%;
  --ring: 0 0% 83.1%;
  --accent: 0 0% 14.9%;
  --accent-foreground: 0 0% 98%;

  /* Tipografia */
  --font-family-display: "Inter", "sans-serif";
  --radius: 4px;
}
```

**Sugestão Tailwind (`tailwind.config`):** mapear `colors.primary = 'hsl(var(--primary))'` e equivalentes para beige, blue, brown, success, error e warning; definir `borderRadius.DEFAULT = 'var(--radius)'` e escalas de espaçamento em múltiplos de 4px.

---

## Inventário e métricas de uso
- **Classes mais frequentes:** `flex` (578x), `text-white` (202x), `flex-col` (199x), `text-primary` (144x), `rounded-full` (88x).
- **Componentes HTML detectados:** 126 botões, 161 imagens, 98 ícones SVG (24x24), 39 links, 14 seções.
- **Cores mais usadas em código:** `rgba(0,0,0,0.15)`, `#FFF`, `#4C4C4C`, `rgba(0,0,0,.1)`, `#AAA`, `#F2F2F2`, `#000`.

---

## Estrutura recomendada do design system
Sugestão de organização de pastas para manter tokens, estilos e componentes alinhados às referências de pesquisa:

```
pilar-design-system/
├── tokens/ (colors.json, typography.json, spacing.json, shadows.json, borders.json, animations.json)
├── styles/ (reset.css, globals.css, utilities.css, tailwind.config.js)
├── components/
│   ├── Button/ (componente, stories, testes, README)
│   ├── Card/
│   ├── Dialog/
│   ├── Input/ (Input.vue, InputGroup.vue)
│   ├── Typography/ (Heading.vue, Text.vue)
│   ├── Skeleton/
│   ├── ImageViewer/
│   └── Share/
├── composables/ (useDialog, useToast, useBreakpoint, useScrollLock, useImageLazyLoad)
├── icons/ (SVGs 24x24 e export central)
├── layouts/ (Default, FullWidth, Dashboard)
├── patterns/ (PropertyCard, HeroSection, FilterBar, Navigation, Footer)
├── assets/ (fonts Inter/Matter/Roboto + placeholders)
├── utils/ (formatters, validators, constants, helpers)
├── docs/ (este guia + README/CHANGELOG/IMPLEMENTATION_GUIDE)
└── .storybook/ (main.js, preview.js, theme.js)
```

---

## Checklist de adoção
1) **Configurar Tailwind** com cores mapeadas para `hsl(var(--token))`, radius `--radius` e escala 4px.
2) **Publicar tokens globais** via `:root` e disponibilizar fallback em CSS para temas claros/escuros se necessário.
3) **Reutilizar componentes-chave** (Button, Card, Dialog, Input, Typography, Skeleton, ImageViewer, Share) seguindo variantes e estados definidos.
4) **Garantir A11y**: foco visível, contraste AA, navegação por teclado, alvos ≥44x44px.
5) **Aplicar padrões de interação**: transições 150–400ms, curvas padrão, z-index hierárquico e bloqueio de scroll em modais.
6) **Documentar no Storybook** (ou similar) e manter CHANGELOG/README do design system atualizado.
7) **Monitorar uso**: revisar classes e tokens mais usados para manter consistência e evitar deriva de estilo.

---

## Guia prático de implementação
### Tailwind: mapeamento completo de tokens
```ts
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: 'hsl(0, 0%, 0%)', light: { 1: 'hsl(0, 0%, 40%)', 2: 'hsl(0, 0%, 30%)', 3: 'hsl(0, 0%, 20%)', 4: 'hsl(0, 0%, 10%)' } },
        secondary: { DEFAULT: 'hsl(48, 20%, 95%)', dark: { 1: 'hsl(50, 12%, 91%)', 2: 'hsl(32, 19%, 82%)' } },
        beige: { DEFAULT: 'hsl(35, 54%, 75%)', light: { 1: 'hsl(35, 52%, 92%)', 2: 'hsl(34, 54%, 84%)' }, dark: { 1: 'hsl(33, 47%, 66%)', 2: 'hsl(33, 42%, 55%)' } },
        blue: { DEFAULT: '#b9cddf', light: { 1: 'hsl(208, 37%, 93%)', 2: 'hsl(208, 38%, 87%)' }, dark: { 1: 'hsl(206, 44%, 67%)', 2: 'hsl(206, 46%, 61%)' } },
        brown: { DEFAULT: 'hsl(29, 34%, 18%)', light: { 1: 'hsl(30, 7%, 73%)', 2: 'hsl(30, 9%, 45%)' }, dark: { 1: 'hsl(31, 36%, 14%)', 2: 'hsl(25, 35%, 10%)' } },
        success: { DEFAULT: 'hsl(143, 100%, 34%)', light: { 1: 'hsl(137, 35%, 92%)', 2: 'hsl(140, 48%, 82%)' }, dark: { 1: 'hsl(141, 100%, 28%)', 2: 'hsl(137, 100%, 19%)' } },
        error: { DEFAULT: 'hsl(359, 83%, 58%)', light: { 1: 'hsl(347, 100%, 91%)', 2: 'hsl(350, 100%, 82%)' }, dark: { 1: 'hsl(1, 65%, 50%)', 2: 'hsl(0, 76%, 37%)' } },
        warning: { DEFAULT: 'hsl(39, 100%, 50%)', light: { 1: 'hsl(43, 100%, 95%)', 2: 'hsl(46, 90%, 76%)' }, dark: { 1: 'hsl(34, 88%, 52%)', 2: 'hsl(25, 68%, 50%)' } },
        white: { DEFAULT: 'hsl(0, 0%, 100%)', dark: { 1: 'hsl(0, 0%, 98%)', 2: 'hsl(0, 0%, 95%)', 3: 'hsl(0, 0%, 90%)', 4: 'hsl(0, 0%, 80%)' } },
        background: 'hsl(0, 0%, 3.9%)',
        foreground: 'hsl(0, 0%, 98%)',
        border: 'hsl(0, 0%, 14.9%)',
        input: 'hsl(0, 0%, 14.9%)',
        ring: 'hsl(0, 0%, 83.1%)',
        accent: 'hsl(0, 0%, 14.9%)',
        'accent-foreground': 'hsl(0, 0%, 98%)',
      },
      fontFamily: {
        sans: ['Inter', 'Inter Fallback: Arial', 'sans-serif'],
        display: ['Matter SQ', 'Matter', 'sans-serif'],
        secondary: ['Roboto', 'Roboto Fallback: Arial', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace'],
      },
      spacing: { '0.5': '0.125rem', 1: '0.25rem', 2: '0.5rem', 3: '0.75rem', 4: '1rem', 5: '1.25rem', 6: '1.5rem', 7: '1.75rem', 8: '2rem', 9: '2.25rem', 10: '2.5rem', 11: '2.75rem', 12: '3rem', 16: '4rem', 20: '5rem', 32: '8rem' },
      borderRadius: { none: '0', sm: '0.125rem', DEFAULT: '0.25rem', md: '0.5rem', lg: '1rem', full: '9999px' },
      fontSize: {
        xs: ['0.75rem', { lineHeight: '1rem' }], sm: ['0.875rem', { lineHeight: '1.25rem' }], base: ['1rem', { lineHeight: '1.5rem' }],
        lg: ['1.125rem', { lineHeight: '1.75rem' }], xl: ['1.25rem', { lineHeight: '1.75rem' }], '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }], '4xl': ['2.25rem', { lineHeight: '2.5rem' }], '5xl': ['3rem', { lineHeight: '1' }],
      },
      transitionDuration: { 150: '150ms', 200: '200ms', 300: '300ms', 400: '400ms', 500: '500ms', 1000: '1000ms', 1500: '1500ms' },
      transitionTimingFunction: { slide: 'cubic-bezier(0.16, 1, 0.3, 1)' },
      screens: { xs: '481px', sm: '640px', md: '768px', lg: '1024px', xl: '1280px', '2xl': '1536px' },
      zIndex: { 0: '0', 10: '10', 20: '20', 30: '30', 40: '40', 50: '50', 60: '60', 70: '70', 80: '80', 90: '90', 100: '100', fullscreen: '1000' },
    },
  },
  plugins: [],
}
```

### CSS base (layer `@base`)
```css
@layer base {
  :root {
    --primary: 0 0% 0%;
    --primary-light-1: 0 0% 40%;
    --primary-light-2: 0 0% 30%;
    --primary-light-3: 0 0% 20%;
    --primary-light-4: 0 0% 10%;
    --secondary: 48 20% 95%;
    --beige: 35 54% 75%;
    --blue: #b9cddf;
    --brown: 29 34% 18%;
    --success: 143 100% 34%;
    --error: 359 83% 58%;
    --warning: 39 100% 50%;
    --white: 0 0% 100%;
    --background: 0 0% 3.9%;
    --foreground: 0 0% 98%;
    --border: 0 0% 14.9%;
    --input: 0 0% 14.9%;
    --ring: 0 0% 83.1%;
    --font-family-display: "Inter", "sans-serif";
  }

  * { @apply border-border; }
  body { @apply bg-background text-foreground font-sans; font-feature-settings: "rlig" 1, "calt" 1; }
  body.scroll-locked { @apply fixed overflow-hidden w-full h-full; touch-action: none; }
  .no-scrollbar::-webkit-scrollbar { display: none; }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
}
```

### Snippets de componentes (Vue/React)
- **Button**: variantes `primary | secondary | outline | ghost`, tamanhos `sm | md | lg`, `focus:ring-2 focus:ring-offset-2`, `rounded-full` por padrão; classes base `inline-flex items-center justify-center font-medium transition-all duration-150`.
- **Card**: variantes `default | elevated | outlined`, paddings `none | sm | md | lg`, radius `rounded-md`; usar `shadow-sm`/`shadow-lg` nas versões elevadas.
- **Dialog/Modal**: `fixed inset-0 z-50 flex items-end sm:items-center`, backdrop `bg-black/50`, transição `slide-up` com `cubic-bezier(0.16, 1, 0.3, 1)`, travar scroll do body (`scroll-locked`).
- **Skeleton**: animação `skeleton-pulse 1.5s ease-in-out infinite` entre tons `#e0e0e0` e `#f0f0f0`; borda de 4px.
- **Share/Image Viewer**: suportar fullscreen/zoom e opções em coluna, tipografia 12–14px, ícones contornados 24x24.

---

## Cobertura das fontes originais
- **Inclui conteúdo integral** dos arquivos removidos (`COLOR_GUIDE_PILARHOMES.md`, `DESIGN_SYSTEM_PILARHOMES.md`, `DESIGN_SYSTEM_SUMMARY.md` e `IMPLEMENTATION_GUIDE_PILARHOMES.md`), preservando tokens detalhados, frequências de uso e guias de implementação.
- **Inventários, tabelas de espaçamento, contagens de classes e exemplos de código** foram trazidos para este guia para manter rastreabilidade e permitir reconstrução fiel do design system sem consultar múltiplos documentos.

