# Pilar Homes - Design System

Comprehensive design system for the Pilar Homes application, containing all design tokens, components, and guidelines.

## Table of Contents
1. [Color System](#color-system)
2. [Typography](#typography)
3. [Spacing System](#spacing-system)
4. [Border Radius](#border-radius)
5. [Shadows](#shadows)
6. [Component Guidelines](#component-guidelines)
7. [Utility Classes](#utility-classes)
8. [Breakpoints](#breakpoints)

---

## Color System

### Primitive Colors (Global Tokens)

#### Dark Foundations
- **rich-black**: `#121212` - Base escura principal
- **mat-slate**: `#2B3A42` - Deep Slate - tons frios
- **mat-stone**: `#4A4843` - Graphite Stone - tons neutros

#### Light Foundations (The White-to-Platinum Gradient)
- **pure-white**: `#FFFFFF` - Gray-0: Contraste máximo
- **porcelain**: `#FAFAFA` - Gray-50: Base clara principal
- **mist**: `#F4F4F5` - Gray-100: Sidebar / Hover (NOVO)
- **chromium**: `#E4E4E7` - Gray-200: Borda Sutil (NOVO)
- **platinum**: `#D6D6D8` - Gray-300: Estrutura / Disabled

#### Brand & Status Colors
- **brand-orange**: `#D5500B` - Pantone 1665 C
- **brand-orange-dark**: `#B54209` - Hover state
- **status-success**: `#00AE42`
- **status-alert**: `#FFA400`
- **status-error**: `#ED3A3D`

#### Presentation Colors
- **deep-brown**: `#1A1410` - Fundo escuro da apresentação
- **off-white**: `#F5F5F0` - Texto claro da apresentação
- **soft-beige**: `#E8E6E1` - Accent da apresentação

### Semantic Tokens (Alias Tokens)

#### Surface Colors (Backgrounds)
- **surface-base**: `rgb(var(--color-surface-base) / <alpha-value>)` - Porcelain (Gray-50) - #FAFAFA - Cor de fundo padrão da página (body). Evita fadiga visual.
- **surface-card**: `rgb(var(--color-surface-card) / <alpha-value>)` - Pure White (Gray-0) - #FFFFFF - Cards, Modais e painéis flutuantes para criar elevação.
- **surface-subtle**: `rgb(var(--color-surface-subtle) / <alpha-value>)` - Mist (Gray-100) - #F4F4F5 - Sidebars, áreas secundárias e hovers sutis.
- **surface-offset**: `rgb(var(--color-surface-offset) / <alpha-value>)` - Platinum (Gray-300) - #D6D6D8 - Seções com contraste médio, estados disabled.
- **surface-brand**: `rgb(var(--color-surface-brand) / <alpha-value>)` - Brand Orange - #D5500B

#### Text Colors
- **text-primary**: `rgb(var(--color-text-primary) / <alpha-value>)` - Rich Black - #121212 - Títulos, cabeçalhos e corpo de texto principal. Máxima legibilidade.
- **text-secondary**: `rgb(var(--color-text-secondary) / <alpha-value>)` - Graphite Stone - #4A4843 - Subtítulos, legendas e textos de apoio. Menor peso visual.
- **text-inverse**: `rgb(var(--color-text-inverse) / <alpha-value>)` - Pure White - #FFFFFF - Texto sobre fundos escuros (Botões, Hero, Footer).
- **text-link**: `rgb(var(--color-text-link) / <alpha-value>)` - Brand Orange - #D5500B - Links, CTAs textuais ou palavras em destaque (usar com moderação).

#### Action Colors (Interactive States)
- **action-primary**: `rgb(var(--color-action-primary) / <alpha-value>)` - Brand Orange - #D5500B
- **action-hover**: `rgb(var(--color-action-hover) / <alpha-value>)` - Brand Orange Dark - #B54209

#### Border Colors
- **border-hairline**: `rgb(var(--color-border-hairline) / <alpha-value>)` - Mist - #F4F4F5 - Divisões quase invisíveis, separadores sutis em tabelas.
- **border-subtle**: `rgb(var(--color-border-subtle) / <alpha-value>)` - Chromium - #E4E4E7 - Bordas padrão de cards, inputs inativos e divisórias.
- **border-strong**: `rgb(var(--color-border-strong) / <alpha-value>)` - Platinum - #D6D6D8 - Divisões com contraste, bordas de destaque estrutural.
- **border-focus**: `rgb(var(--color-border-focus) / <alpha-value>)` - Rich Black - #121212 - Inputs ativos, focos ou bordas que exigem máxima atenção.

### CSS Variables (Light Mode)
- `--color-surface-base`: 250 250 250 (Porcelain - Gray-50)
- `--color-surface-card`: 255 255 255 (Pure White - Gray-0)
- `--color-surface-subtle`: 244 244 245 (Mist - Gray-100)
- `--color-surface-offset`: 214 214 216 (Platinum - Gray-300)
- `--color-surface-brand`: 213 80 11 (Brand Orange)
- `--color-text-primary`: 18 18 18 (Rich Black)
- `--color-text-secondary`: 74 72 67 (Graphite Stone)
- `--color-text-inverse`: 255 255 255 (Pure White)
- `--color-text-link`: 213 80 11 (Brand Orange)
- `--color-action-primary`: 213 80 11 (Brand Orange)
- `--color-action-hover`: 181 66 9 (Brand Orange Dark)
- `--color-border-hairline`: 244 244 245 (Mist)
- `--color-border-subtle`: 228 228 231 (Chromium)
- `--color-border-strong`: 214 214 216 (Platinum)
- `--color-border-focus`: 18 18 18 (Rich Black)

### CSS Variables (Dark Mode)
- `--color-surface-base`: 18 18 18 (Rich Black)
- `--color-surface-card`: 43 58 66 (Deep Slate)
- `--color-surface-subtle`: 74 72 67 (Graphite Stone)
- `--color-surface-offset`: 74 72 67 (Graphite Stone)
- `--color-surface-brand`: 213 80 11 (Brand Orange)
- `--color-text-primary`: 250 250 250 (Porcelain)
- `--color-text-secondary`: 214 214 216 (Platinum)
- `--color-text-inverse`: 18 18 18 (Rich Black)
- `--color-text-link`: 213 80 11 (Brand Orange)
- `--color-action-primary`: 213 80 11 (Brand Orange)
- `--color-action-hover`: 181 66 9 (Brand Orange Dark)
- `--color-border-hairline`: 43 58 66 (Deep Slate)
- `--color-border-subtle`: 74 72 67 (Graphite Stone)
- `--color-border-strong`: 214 214 216 (Platinum)
- `--color-border-focus`: 250 250 250 (Porcelain)

---

## Typography

### Font Families
- **Primary**: Inter - Fonte principal · UI, Corpo de texto e Elementos técnicos.
- **Display**: Matter SQ - Branding corporativo · Títulos padrão.
- **Luxury Extension (Novo)**: Playfair Display - Editorial e Curadoria · Títulos emocionais, nomes de coleções e destaques.
- **Tertiary**: Roboto - Alternativa · Elementos legados.
- **Monospace**: ui-monospace, SFMono-Regular - Dados técnicos.

### Font Weights
#### Inter (Functional)
- **Thin (100)**: Uso exclusivo em títulos "High Luxury" (caps lock).
- **Light (300)**: Corpo de texto principal e labels elegantes.
- **Regular (400)**: Padrão para UI.
- **Semibold (600)**: Subtítulos e botões.

#### Playfair Display (Emotional)
- **Regular (400)**: Títulos de destaque.
- **Italic (400)**: Palavras-chave em títulos compostos (Mix & Match).

### Luxury Compositions (Mix & Match Strategy)
Esta estratégia deve ser usada em seções de destaque, hero banners e cards de produtos de alto valor.

1.  **The Structural Layer (Sans-Serif):**
    *   **Font**: Inter
    *   **Weight**: Thin (100) ou Light (300)
    *   **Case**: Uppercase
    *   **Tracking**: Wide (`0.1em` a `0.25em`)
    *   **Uso**: Categorias, preposições ou a parte "racional" do título.

2.  **The Emotional Layer (Serif):**
    *   **Font**: Playfair Display
    *   **Style**: Italic (preferencialmente) ou Regular
    *   **Case**: Title Case ou Lowercase
    *   **Uso**: A palavra-chave, o nome do empreendimento ou a parte "sentimental".

### Font Sizes
- **text-xs**: 12px · 0.75rem - Labels, captions
- **text-sm**: 14px · 0.875rem - Textos pequenos, Botões Enquire
- **text-base**: 16px · 1rem - Corpo principal
- **text-lg**: 18px · 1.125rem - Textos destacados
- **text-xl**: 20px · 1.25rem - Subtítulos pequenos
- **text-2xl**: 24px · 1.5rem - Títulos de seção
- **text-3xl**: 30px · 1.875rem - Títulos principais
- **text-5xl**: 48px · 3rem - Display / Hero

---

## Spacing System

### Base Unit
- 4px base unit system

### Common Spacing Values
- `.25rem` (4px) - 18 vezes
- `.5rem` (8px) - 38 vezes
- `.75rem` (12px) - 22 vezes
- `1rem` (16px) - 32 vezes
- `1.25rem` (20px) - 40 vezes
- `1.5rem` (24px) - 35 vezes
- `2rem` (32px) - 33 vezes
- `2.25rem` (36px) - 16 vezes
- `2.75rem` (44px) - 20 vezes
- `3rem` (48px) - 23 vezes
- `4rem` (64px) - 9 vezes
- `5rem` (80px) - 13 vezes
- `8rem` (128px) - 6 vezes

---

## Border Radius

- **rounded-lg**: 8px - Cards padrão, containers principais, modais
- **rounded-xl**: 12px - Cards grandes, hero sections, painéis destacados
- **rounded-2xl**: 16px - Elementos especiais, imagens destacadas, containers de nível superior
- **9999px**: Pill - Botões e avatares circulares
- **50%**: Circular - Imagens de perfil e botões circulares

---

## Shadows

- **shadow-card**: `0 1px 3px 0 rgba(0, 0, 0, 0.05)` - Sombra padrão para cards
- **shadow-card-hover**: `0 10px 30px -10px rgba(0, 0, 0, 0.08)` - Sombra em hover para cards
- **shadow-default**: `0 1px 3px 0 rgba(0, 0, 0, 0.10)` - Sombra padrão

---

## Component Guidelines

### Buttons

#### Primary Button
- Class: `btn-primary`
- Styles: `px-6 py-3 bg-action-primary text-white font-medium rounded-full hover:bg-action-hover transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-action-primary`

#### Secondary Button
- Class: `btn-secondary`
- Styles: `px-6 py-3 bg-surface-card text-primary font-medium rounded-full border border-border-subtle hover:bg-surface-offset transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-border-subtle`

#### Enquire Button (Luxury Context) - NOVO
- **Uso**: Para produtos de alto valor ou contato sob demanda. Substitui o Primary Button em contextos editoriais.
- Class: `btn-enquire`
- Styles: `px-6 py-3 bg-transparent text-primary font-medium rounded-full border border-border-strong hover:border-brand-orange hover:text-brand-orange hover:bg-brand-orange/5 transition-all duration-300`

### Cards
- Class: `card`
- Styles: `bg-surface-card border border-border-subtle p-6 hover:border-border-focus transition-colors duration-300 shadow-card`

---

## Utility Classes

### Frequently Used Classes
- `flex` - 578 times
- `text-white` - 202 times
- `flex-col` - 199 times
- `text-primary` - 144 times
- `text-base` - 116 times
- `rounded-full` - 88 times
- `focus:outline-none` - 81 times
- `p-0` - 72 times
- `text-left` - 55 times
- `bg-primary/40` - 50 times
- `p-4` - 50 times
- `bg-white/50` - 48 times
- `text-nowrap` - 48 times
- `text-[14px]` - 48 times
- `text-sm` - 46 times
- `hover:decoration-primary` - 41 times
- `text-xs` - 40 times
- `text-[16px]` - 40 times
- `bg-primary` - 39 times
- `grid` - 38 times
- `text-[12px]` - 36 times
- `bg-white` - 35 times
- `rounded-[2px]` - 35 times
- `bg-transparent` - 34 times
- `focus:ring-offset-2` - 32 times
- `focus:ring-2` - 32 times
- `hover:border-primary-light-4` - 26 times
- `focus:bg-primary-light-4` - 26 times
- `focus:border-primary-light-4` - 26 times
- `hover:bg-primary` - 24 times

---

## Breakpoints

### Responsive Design
- Mobile-first approach
- Breakpoints:
  - Mobile: `<640px`
  - Tablet: `640px - 1023px`
  - Desktop: `1024px - 1279px`
  - Large: `1280px - 1535px`
  - XL: `≥1536px`

### Media Queries Used
- `@media (min-width: 640px)` - Small screens
- `@media (min-width: 768px)` - Medium screens
- `@media (min-width: 1024px)` - Large screens
- `@media (min-width: 1280px)` - Extra large screens
- `@media (min-width: 1536px)` - 2XL screens
- `@media screen and (max-width: 767px)` - Small and below
- `@media (hover: hover)` - Hover-capable devices

---

## Design System Rules

### Color Usage
- Prefer `surface-base` (Porcelain) for standard backgrounds to reduce eye strain in Light Mode.
- Use `text-secondary` (Graphite Stone) for body text instead of pure black for a more sophisticated look.

### Typography Standards
- **Mix & Match**: Em títulos de destaque, combine sempre a estrutura técnica (Inter Sans) com a elegância emocional (Playfair Serif).
- **Hierarchy**: Use `text-xs` com espaçamento (tracking) largo para labels e categorização.
- **Weights**: Evite pesos acima de 600 em contextos de luxo; prefira o contraste de tamanho e família tipográfica.

### Accessibility
- Maintain contrast ratios for readability
- Use proper focus states for interactive elements
- Ensure text is legible across all contexts

---

## Legacy Compatibility
- Primary: `#D5500B` - Maintido para não quebrar código existente
- Secondary: `rgb(var(--color-text-secondary) / <alpha-value>)` - Mantido para não quebrar código existente