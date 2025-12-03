# Design System - PilarHomes

> **Documentação completa do Design System extraído do site pilarhomes.com.br**  
> Data da análise: 02 de Dezembro de 2025

---

## 📋 Índice

1. [Cores](#cores)
2. [Tipografia](#tipografia)
3. [Espaçamento](#espacamento)
4. [Componentes](#componentes)
5. [Ícones](#icones)
6. [Breakpoints](#breakpoints)
7. [Efeitos e Sombras](#efeitos-e-sombras)
8. [Grid e Layout](#grid-e-layout)
9. [Tokens CSS](#tokens-css)

---

## 🎨 Cores

### Paleta Principal

#### Primary (Preto)
```css
--primary: 0, 0%, 0%          /* HSL - Preto puro */
--primary-light-1: 0, 0%, 40% /* 40% lightness */
--primary-light-2: 0, 0%, 30% /* 30% lightness */
--primary-light-3: 0, 0%, 20% /* 20% lightness */
--primary-light-4: 0, 0%, 10% /* 10% lightness */
```

**Uso em Tailwind:**
- `text-primary` - Usado 144 vezes
- `bg-primary` - Usado 39 vezes
- `bg-primary/40` - Usado 50 vezes
- `hover:bg-primary` - Usado 24 vezes

#### Secondary (Bege/Creme)
```css
--secondary: 48, 20%, 95%        /* Base bege claro */
--secondary-dark-1: 50, 12%, 91%
--secondary-dark-2: 32, 19%, 82%
```

#### Beige (Cor característica da marca)
```css
--beige: 35, 54%, 75%
--beige-light-1: 35, 52%, 92%
--beige-light-2: 34, 54%, 84%
--beige-dark-1: 33, 47%, 66%
--beige-dark-2: 33, 42%, 55%
```

#### Blue (Azul institucional)
```css
--blue: #b9cddf              /* Hex direto */
--blue-light-1: 208, 37%, 93%
--blue-light-2: 208, 38%, 87%
--blue-dark-1: 206, 44%, 67%
--blue-dark-2: 206, 46%, 61%
```

#### Brown (Marrom/Terra)
```css
--brown: 29, 34%, 18%
--brown-light-1: 30, 7%, 73%
--brown-light-2: 30, 9%, 45%
--brown-dark-1: 31, 36%, 14%
--brown-dark-2: 25, 35%, 10%
```

### Cores de Estado

#### Success (Verde)
```css
--success: 143, 100%, 34%
--success-light-1: 137, 35%, 92%
--success-light-2: 140, 48%, 82%
--success-dark-1: 141, 100%, 28%
--success-dark-2: 137, 100%, 19%
```

#### Error (Vermelho)
```css
--error: 359, 83%, 58%
--error-light-1: 347, 100%, 91%
--error-light-2: 350, 100%, 82%
--error-dark-1: 1, 65%, 50%
--error-dark-2: 0, 76%, 37%
```

#### Warning (Amarelo/Laranja)
```css
--warning: 39, 100%, 50%
--warning-light-1: 43, 100%, 95%
--warning-light-2: 46, 90%, 76%
--warning-dark-1: 34, 88%, 52%
--warning-dark-2: 25, 68%, 50%
```

### Cores Neutras/Sistema

#### Branco
```css
--white: 0, 0%, 100%
--white-dark-1: 0, 0%, 98%
--white-dark-2: 0, 0%, 95%
--white-dark-3: 0, 0%, 90%
--white-dark-4: 0, 0%, 80%
```

**Uso em Tailwind:**
- `text-white` - Usado 202 vezes
- `bg-white` - Usado 35 vezes
- `bg-white/50` - Usado 48 vezes (50% de opacidade)

#### Escala de Cinza
```css
--background: 0, 0%, 3.9%
--foreground: 0, 0%, 98%
--muted: 0, 0%, 14.9%
--muted-foreground: 0, 0%, 63.9%
```

### Cores mais utilizadas no código

| Cor | Frequência | Uso |
|-----|------------|-----|
| `rgba(0,0,0,0.15)` | 32x | Sobreposição/overlay |
| `#FFF` | 14x | Branco puro |
| `#4C4C4C` | 12x | Cinza médio |
| `rgba(0,0,0,.1)` | 12x | Sombra leve |
| `#AAA` | 7x | Cinza claro |
| `#F2F2F2` | 7x | Background claro |
| `#000` | 7x | Preto puro |

### Sistema de Cores para UI

```css
--card: 0, 0%, 3.9%
--card-foreground: 0, 0%, 98%
--popover: 0, 0%, 3.9%
--popover-foreground: 0, 0%, 98%
--border: 0, 0%, 14.9%
--input: 0, 0%, 14.9%
--ring: 0, 0%, 83.1%
--accent: 0, 0%, 14.9%
--accent-foreground: 0, 0%, 98%
```

---

## 📝 Tipografia

### Famílias de Fonte

#### Primária - Inter
```css
font-family: Inter, "Inter Fallback: Arial", sans-serif;
--font-family-display: "Inter", "sans-serif";
```
**Uso:** Fonte principal do site, usada em quase todos os textos.

#### Secundária - Matter (Custom)
```css
font-family: Matter SQ;
font-family: Matter;
```
**Uso:** Tipografia especial/display, provavelmente para títulos ou destaques.

#### Terciária - Roboto
```css
font-family: Roboto, "Roboto Fallback: Arial";
```
**Uso:** Fonte alternativa para elementos específicos.

#### Monospace (Código/Dados)
```css
font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace;
```

### Escala de Tamanhos

**Classes Tailwind mais usadas:**
- `text-base` - 116 vezes (tamanho base)
- `text-sm` - 46 vezes (small)
- `text-xs` - 40 vezes (extra small)
- `text-[16px]` - 40 vezes (16px customizado)
- `text-[14px]` - 48 vezes (14px customizado)
- `text-[12px]` - 36 vezes (12px customizado)

### Hierarquia Tipográfica Sugerida

```css
/* Baseado nas classes encontradas */
.text-xs    { font-size: 0.75rem; }  /* 12px */
.text-sm    { font-size: 0.875rem; } /* 14px */
.text-base  { font-size: 1rem; }     /* 16px */
.text-lg    { font-size: 1.125rem; } /* 18px */
.text-xl    { font-size: 1.25rem; }  /* 20px */
.text-2xl   { font-size: 1.5rem; }   /* 24px */
```

### Pesos de Fonte (Font Weight)

Valores identificados no CSS:
- Regular (400)
- Medium (500)
- Semibold (600)
- Bold (700)

---

## 📏 Espaçamento

### Sistema de Espaçamento (Baseado em REM)

**Valores mais utilizados (em ordem de frequência):**

| Valor | Frequência | Pixels (16px base) | Uso comum |
|-------|------------|-------------------|-----------|
| `1.25rem` | 40x | 20px | Padding médio |
| `.5rem` | 38x | 8px | Gap pequeno |
| `1.5rem` | 35x | 24px | Padding/margin padrão |
| `2rem` | 33x | 32px | Espaço grande |
| `1rem` | 32x | 16px | Espaço base |
| `3rem` | 23x | 48px | Seções |
| `.75rem` | 22x | 12px | Padding pequeno |
| `2.75rem` | 20x | 44px | Espaço específico |
| `.25rem` | 18x | 4px | Gap mínimo |
| `2.25rem` | 16x | 36px | Espaço médio-grande |
| `5rem` | 13x | 80px | Seções grandes |
| `4rem` | 9x | 64px | Seções médias |
| `8rem` | 6x | 128px | Seções muito grandes |

### Escala de Espaçamento Recomendada

```css
/* Escala 4px base */
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
--space-32: 8rem;     /* 128px */
```

### Classes Tailwind de Padding/Margin

**Mais utilizadas:**
- `p-0` - 72 vezes
- `p-4` - 50 vezes (1rem = 16px)

---

## 🧩 Componentes

### Inventário de Componentes HTML

| Tipo | Quantidade | Observações |
|------|-----------|-------------|
| Divs com classes | 789 | Estrutura principal |
| Imagens | 161 | Alto uso de imagens |
| Buttons | 126 | Botões diversos |
| Links | 39 | Navegação |
| Sections | 14 | Seções principais |
| Headers | 8 | Cabeçalhos |
| Nav | 2 | Navegação principal |
| Footers | 2 | Rodapé |
| Inputs | 2 | Formulários |

### Componentes Identificados nos CSS

#### 1. Buttons

**Variantes identificadas:**
- Default (preto com borda)
- Primary (fundo preto)
- Transparent
- Com hover states

```css
/* Exemplo de estrutura */
.button {
  padding: 12px 16px;
  border-radius: 9999px; /* rounded-full */
  transition: all 0.15s ease-in-out;
}

.button-primary {
  background: var(--primary);
  color: var(--white);
}

.button-primary:hover {
  background: var(--primary-light-1);
}
```

**Classes Tailwind de botão:**
- `rounded-full` - 88 vezes
- `focus:outline-none` - 81 vezes
- `focus:ring-2` - 32 vezes
- `focus:ring-offset-2` - 32 vezes

#### 2. Cards/Containers

```css
.card {
  background: var(--card);
  color: var(--card-foreground);
  border-radius: var(--radius);
}
```

#### 3. Share Component

Componente de compartilhamento com duas variantes:

**Default:**
```css
[data-variant=default] {
  align-items: center;
  display: flex;
  gap: 1rem;
}

[data-variant=default] .share-icon-link {
  border: 1px solid var(--black);
  height: 2rem;
  width: 2rem;
  padding: 12px 16px;
}

[data-variant=default] .share-icon-link:hover {
  background: var(--black);
  color: var(--white);
}
```

**Dropdown:**
```css
[data-variant=dropdown] {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

[data-variant=dropdown] .share-icon-link {
  color: var(--darkgray);
  font-size: 0.75rem;
  gap: 1rem;
}

[data-variant=dropdown] .share-icon-link:hover {
  color: var(--black);
}
```

#### 4. Image Viewer (iv-container)

Componente complexo para visualização de imagens com:
- Fullscreen mode
- Zoom controls
- Snap view
- Touch gestures

```css
.iv-container {
  position: relative;
  overflow: hidden;
  user-select: none;
  /* Também usado com flexbox para centralização */
  align-items: center;
  display: flex;
  justify-content: center;
}

.iv-image {
  object-fit: cover;
  touch-action: none;
}
```

#### 5. Skeleton Loader

```css
.skeleton {
  animation: skeleton-pulse 1.5s ease-in-out infinite;
  background-color: #e0e0e0;
}

@keyframes skeleton-pulse {
  0%, 100% { background-color: #e0e0e0; }
  50% { background-color: #f0f0f0; }
}
```

#### 6. Dialog/Modal

```css
.CommandDialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100dvw;
  height: 100dvh;
  max-height: 100vh;
  overflow: hidden;
}

/* Animação de entrada/saída */
.slide-up-enter-active,
.slide-up-leave-active {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 50;
}

.slide-up-enter-from,
.slide-up-leave-to {
  transform: translateY(100%);
}
```

#### 7. Scroll Area

```css
[data-scroll-area] {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-padding-bottom: env(keyboard-inset-height, 0);
  touch-action: pan-y;
  transition: padding-bottom 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

#### 8. Layout Utilities

**Flex:**
- `flex` - 578 vezes
- `flex-col` - 199 vezes
- `text-nowrap` - 48 vezes

**Grid:**
- `grid` - 38 vezes

---

## 🎯 Ícones

### Sistema de Ícones

**Total de ícones SVG:** 98

### Tamanhos Padrão de ViewBox

| ViewBox | Frequência | Descrição |
|---------|-----------|-----------|
| `0 0 24 24` | 88x | Padrão principal (24x24) |
| `0 0 26 28` | 3x | Ícones maiores |
| `0 0 20 20` | 2x | Ícones menores |
| `0 0 1207 147` | 2x | Logos/gráficos largos |
| `0 -960 960 960` | 1x | Material Icons |

### Guideline de Ícones

```css
/* Tamanhos de ícone baseados no uso */
.icon-sm  { width: 0.9rem;  height: 0.9rem;  } /* ~14px */
.icon-md  { width: 1rem;    height: 1rem;    } /* 16px */
.icon-lg  { width: 1.5rem;  height: 1.5rem;  } /* 24px */
.icon-xl  { width: 2rem;    height: 2rem;    } /* 32px */
```

**Cores de ícone:**
- Herdam a cor do texto por padrão
- Usam `currentColor` para flexibilidade

---

## 📱 Breakpoints

### Sistema de Breakpoints Responsivos

**Breakpoints Tailwind identificados:**

```css
/* Mobile First */
@media (min-width: 481px)   { /* xs */ }
@media (min-width: 640px)   { /* sm */ }
@media (min-width: 768px)   { /* md */ }
@media (min-width: 800px)   { /* custom */ }
@media (min-width: 824px)   { /* custom */ }
@media (min-width: 960px)   { /* custom */ }
@media (min-width: 1024px)  { /* lg */ }
@media (min-width: 1200px)  { /* custom */ }
@media (min-width: 1280px)  { /* xl */ }
@media (min-width: 1400px)  { /* custom */ }
@media (min-width: 1536px)  { /* 2xl */ }
@media (min-width: 1728px)  { /* custom */ }
```

**Mobile breakpoints:**
```css
@media (max-width: 480px)   { /* mobile */ }
@media (max-width: 767px)   { /* tablet */ }
@media (max-width: 960px)   { /* desktop small */ }
```

### Breakpoints Recomendados

| Nome | Min-width | Uso |
|------|-----------|-----|
| `xs` | 0px | Mobile pequeno (padrão) |
| `sm` | 640px | Mobile landscape |
| `md` | 768px | Tablet |
| `lg` | 1024px | Desktop |
| `xl` | 1280px | Desktop grande |
| `2xl` | 1536px | Desktop extra grande |

### Media Query Especial

```css
@media (hover: hover) {
  /* Estilos apenas para dispositivos com hover */
}
```
Usado para evitar problemas de hover em dispositivos touch.

---

## ✨ Efeitos e Sombras

### Border Radius

**Valores mais usados:**

| Valor | Frequência | Uso |
|-------|-----------|-----|
| `9999px` | 5x | Pills/Fully rounded |
| `50%` | 4x | Círculos perfeitos |
| `8px` | 1x | Cantos suaves |
| `2px` | 1x | Cantos sutis |
| `0.25rem` | 1x | 4px |
| `0.125rem` | 1x | 2px |

**Classes Tailwind:**
- `rounded-full` - 88 vezes (9999px)
- `rounded-[2px]` - 35 vezes

### Box Shadow

**Sombras padrão:**

```css
/* Tailwind shadow system */
--tw-shadow: 0 0 #0000;
--tw-shadow-colored: 0 0 #0000;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
```

**Sombra especial (overlay):**
```css
box-shadow: 0 0 0 200px rgba(0, 0, 0, 0.5);
```
Usado para criar overlay/backdrop em modais.

### Transições

**Durações mais comuns:**
```css
transition-duration: 0.15s;   /* Padrão para interações */
transition-duration: 0.2s;    /* Efeitos suaves */
transition-duration: 0.3s;    /* Animações médias */
transition-duration: 0.4s;    /* Animações slide */
transition-duration: 0.5s;    /* Animações longas */
transition-duration: 1s;      /* Skeleton/loading */
transition-duration: 1.5s;    /* Pulse animations */
```

**Timing functions:**
```css
ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
ease-in: cubic-bezier(0.4, 0, 1, 1);
ease-out: cubic-bezier(0, 0, 0.2, 1);
ease-linear: linear;
```

**Easing especial para slides:**
```css
cubic-bezier(0.16, 1, 0.3, 1);  /* Slide natural */
```

### Estados de Foco

```css
.focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

/* Classes Tailwind */
focus:outline-none      /* Remove outline padrão */
focus:ring-2           /* Ring de 2px */
focus:ring-offset-2    /* Offset de 2px */
focus:bg-primary-light-4
focus:border-primary-light-4
```

---

## 📐 Grid e Layout

### Sistema de Grid

**Classes grid identificadas:**
- `grid` - 38 ocorrências

### Flex Layout

**Alto uso de flexbox:**
- `flex` - 578 vezes
- `flex-col` - 199 vezes
- `text-left` - 55 vezes

### Container System

**Estrutura de página:**
```css
body.scroll-locked {
  position: fixed !important;
  overflow: hidden !important;
  width: 100% !important;
  height: 100% !important;
  touch-action: none;
}
```

### Z-Index Layers

Baseado nos componentes identificados:

```css
.z-index-base: 1;
.z-index-dropdown: 10;
.z-index-sticky: 20;
.z-index-fixed: 30;
.z-index-modal-backdrop: 40;
.z-index-modal: 50;
.z-index-popover: 60;
.z-index-tooltip: 70;
.z-index-notification: 80;
.z-index-fullscreen: 1000;
```

---

## 🎨 Tokens CSS

### Variáveis CSS Completas

```css
:root {
  /* Cores Principais */
  --primary: 0, 0%, 0%;
  --primary-light-1: 0, 0%, 40%;
  --primary-light-2: 0, 0%, 30%;
  --primary-light-3: 0, 0%, 20%;
  --primary-light-4: 0, 0%, 10%;
  
  --secondary: 48, 20%, 95%;
  --secondary-dark-1: 50, 12%, 91%;
  --secondary-dark-2: 32, 19%, 82%;
  
  --tertiary: 20, 90%, 44%;
  
  /* Beige */
  --beige: 35, 54%, 75%;
  --beige-light-1: 35, 52%, 92%;
  --beige-light-2: 34, 54%, 84%;
  --beige-dark-1: 33, 47%, 66%;
  --beige-dark-2: 33, 42%, 55%;
  
  /* Blue */
  --blue: #b9cddf;
  --blue-light-1: 208, 37%, 93%;
  --blue-light-2: 208, 38%, 87%;
  --blue-dark-1: 206, 44%, 67%;
  --blue-dark-2: 206, 46%, 61%;
  
  /* Brown */
  --brown: 29, 34%, 18%;
  --brown-light-1: 30, 7%, 73%;
  --brown-light-2: 30, 9%, 45%;
  --brown-dark-1: 31, 36%, 14%;
  --brown-dark-2: 25, 35%, 10%;
  
  /* Estados */
  --success: 143, 100%, 34%;
  --success-light-1: 137, 35%, 92%;
  --success-light-2: 140, 48%, 82%;
  --success-dark-1: 141, 100%, 28%;
  --success-dark-2: 137, 100%, 19%;
  
  --error: 359, 83%, 58%;
  --error-light-1: 347, 100%, 91%;
  --error-light-2: 350, 100%, 82%;
  --error-dark-1: 1, 65%, 50%;
  --error-dark-2: 0, 76%, 37%;
  
  --warning: 39, 100%, 50%;
  --warning-light-1: 43, 100%, 95%;
  --warning-light-2: 46, 90%, 76%;
  --warning-dark-1: 34, 88%, 52%;
  --warning-dark-2: 25, 68%, 50%;
  
  /* Neutros */
  --white: 0, 0%, 100%;
  --white-dark-1: 0, 0%, 98%;
  --white-dark-2: 0, 0%, 95%;
  --white-dark-3: 0, 0%, 90%;
  --white-dark-4: 0, 0%, 80%;
  
  /* Sistema */
  --background: 0, 0%, 3.9%;
  --foreground: 0, 0%, 98%;
  --card: 0, 0%, 3.9%;
  --card-foreground: 0, 0%, 98%;
  --popover: 0, 0%, 3.9%;
  --popover-foreground: 0, 0%, 98%;
  --muted: 0, 0%, 14.9%;
  --muted-foreground: 0, 0%, 63.9%;
  --accent: 0, 0%, 14.9%;
  --accent-foreground: 0, 0%, 98%;
  --destructive: 0, 62.8%, 30.6%;
  --destructive-foreground: 0, 0%, 98%;
  --border: 0, 0%, 14.9%;
  --input: 0, 0%, 14.9%;
  --ring: 0, 0%, 83.1%;
  
  /* Links */
  --link: 208, 100%, 39%;
  
  /* Tipografia */
  --font-family-display: "Inter", "sans-serif";
  
  /* Tailwind Utilities */
  --tw-bg-opacity: 1;
  --tw-text-opacity: 1;
  --tw-border-opacity: 1;
  --tw-ring-color: rgba(59, 130, 246, 0.5);
  --tw-ring-offset-color: #fff;
  --tw-ring-offset-width: 0px;
  
  /* Transform */
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  
  /* Animations */
  --tw-enter-opacity: initial;
  --tw-enter-scale: initial;
  --tw-enter-rotate: initial;
  --tw-enter-translate-x: initial;
  --tw-enter-translate-y: initial;
  --tw-exit-opacity: initial;
  --tw-exit-scale: initial;
  --tw-exit-rotate: initial;
  --tw-exit-translate-x: initial;
  --tw-exit-translate-y: initial;
}
```

### Modo Dark (se aplicável)

```css
.dark {
  --background: 0, 0%, 3.9%;
  /* Outras variáveis dark mode */
}
```

---

## 📦 Arquitetura do Design System

### Stack Tecnológica Identificada

- **Framework CSS:** Tailwind CSS
- **Framework JS:** Nuxt.js (Vue.js)
- **Metodologia:** Utility-first com custom properties
- **Componentização:** Vue SFC (Single File Components)

### Estrutura de Arquivos CSS

1. `Hero.POdB4OBP.css` - Componentes de hero e dialogs
2. `Player.7CpoSrYN.css` - Image viewer/player
3. `Content.WoSByiah.css` - Componentes de conteúdo

### Naming Conventions

**Data attributes:**
- `data-variant` - Variantes de componentes
- `data-state` - Estados de UI (open/closed)
- `data-motion` - Direção de animação
- `data-side` - Posicionamento de popover
- `data-scroll-area` - Áreas com scroll customizado

---

## 🎯 Diretrizes de Uso

### Cores

1. **Primária (Preto):** Textos principais, botões primários, elementos de destaque
2. **Beige:** Cor característica da marca, backgrounds sutis, highlights
3. **Blue:** Links, elementos interativos secundários
4. **Branco:** Textos em fundos escuros, cards, backgrounds

### Espaçamento

- Use a escala de 4px (0.25rem) como base
- Múltiplos de 4: 4, 8, 12, 16, 20, 24, 32, 48, 64, 80, 128
- Evite valores arbitrários fora da escala

### Tipografia

- **Títulos:** Matter SQ ou Inter Bold/Semibold
- **Corpo:** Inter Regular/Medium
- **Destaque:** Roboto (uso específico)
- Mantenha hierarquia clara com tamanhos distintos

### Responsividade

- Mobile first approach
- Breakpoints principais: 768px (tablet), 1024px (desktop)
- Use `hover:hover` para evitar problemas em touch devices

### Acessibilidade

- Sempre use `focus-visible` para navegação por teclado
- Ring de foco com 2px de largura e 2px de offset
- Contraste adequado entre texto e background
- Touch targets mínimo de 44x44px

---

## 📚 Recursos Adicionais

### Ferramentas Complementares

- **Processamento de Imagens:** WebP com qualidade 80
- **CDN:** AWS CloudFront
- **Fonts:** Auto-hosted com fallbacks
- **Icons:** SVG inline com viewBox 24x24 padrão

### Performance

- Code splitting por componente
- CSS scoped por componente Vue
- Lazy loading de imagens
- Service Worker habilitado

---

## 📝 Notas Finais

Este design system foi extraído através de análise automatizada do site pilarhomes.com.br. 

**Recomendações para implementação:**

1. Criar biblioteca de componentes Vue/React baseada nos padrões identificados
2. Configurar Tailwind com os custom colors e spacing identificados
3. Implementar sistema de tokens CSS para fácil manutenção
4. Documentar componentes com Storybook ou similar
5. Manter consistência com os padrões de acessibilidade identificados

**Arquivos gerados:**
- `design_tokens_raw.md` - Análise bruta dos tokens
- `components_analysis.md` - Análise de componentes
- `Hero.POdB4OBP.css` - CSS do componente Hero
- `Player.7CpoSrYN.css` - CSS do Image Viewer
- `Content.WoSByiah.css` - CSS de compartilhamento

---

*Documentação gerada automaticamente em 02/12/2025*  
*Baseada na análise do site https://pilarhomes.com.br/*
