# Design System - Pilar Clone

## Sumário
1. [Introdução](#introdução)
2. [Paleta de Cores](#paleta-de-cores)
3. [Tipografia](#tipografia)
4. [Espaçamento e Layout](#espaçamento-e-layout)
5. [Sombras e Elevação](#sombras-e-elevação)
6. [Border Radius](#border-radius)
7. [Componentes](#componentes)
8. [Tokens de Design](#tokens-de-design)
9. [Boas Práticas](#boas-práticas)

---

## Introdução

Este documento consolida todas as informações sobre o design system do Pilar Clone, um sistema de design moderno e consistente para aplicações imobiliárias. O design system é construído usando Tailwind CSS e segue princípios de design modernos com foco em usabilidade, acessibilidade e consistência visual.

### Princípios de Design
- **Consistência**: Uso uniforme de cores, espaçamentos e componentes
- **Hierarquia Visual**: Clara distinção entre elementos primários e secundários
- **Acessibilidade**: Contraste adequado e suporte a leitores de tela
- **Responsividade**: Design adaptável a diferentes tamanhos de tela
- **Performance**: Otimização de imagens e carregamento

---

## Paleta de Cores

### Cores Primárias

#### Primary (Preto/Cinza Escuro)
- **DEFAULT**: `#101828` - Cor principal do sistema, usada para textos primários, botões e headers
- **Light**: `#1D2939` - Variação clara para estados hover
- **Dark**: `#0C111D` - Variação escura para ênfase extra

**Uso recomendado**: Textos principais, botões primários, navegação, logo

#### Accent (Dourado)
- **DEFAULT**: `#D4AF37` - Cor de destaque para elementos importantes
- **Hover**: `#B8962F` - Estado hover para elementos com accent

**Uso recomendado**: Destaques, CTAs especiais, elementos premium

### Cores de Texto

- **Primary**: `#101828` - Texto principal
- **Secondary**: `#475467` - Texto secundário e descritivo
- **Muted**: `#667085` - Texto de baixa importância, labels

### Escala de Cinza

Escala completa de cinza para backgrounds, bordas e estados:

```css
25:  #FCFCFD
50:  #F9FAFB
100: #F2F4F7
200: #E4E7EC
300: #D0D5DD
400: #98A2B3
500: #667085
600: #475467
700: #344054
800: #1D2939
900: #101828
```

### Cores de Background

- **Primary**: `#FFFFFF` - Background principal (branco)
- **Secondary**: `#F9FAFB` - Background de página
- **Tertiary**: `#F2F4F7` - Background alternativo para seções

### Cores de Borda

- **DEFAULT**: `#E4E7EC` - Borda padrão para cards e inputs
- **Hover**: `#D0D5DD` - Borda em estado hover

### Cores de Status

- **Success**: `#12B76A` - Mensagens de sucesso, confirmações
- **Warning**: `#F79009` - Avisos e atenções
- **Error**: `#F04438` - Erros e alertas críticos

### Cores de Badges

Para indicadores de tipo de transação:

- **Sale (Venda)**: Background `green-100`, Texto `green-800`
- **Rent (Aluguel)**: Background `blue-100`, Texto `blue-800`

---

## Tipografia

### Família de Fontes

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

**Inter** é a fonte primária do sistema, com fallbacks para fontes do sistema operacional.

### Hierarquia de Texto

#### Headings (Títulos)
- **H1**: Usado para títulos de página principais
- **H2**: Usado para seções importantes
- **H3**: Usado para cards e sub-seções (ex: títulos de imóveis)

#### Body Text
- **Base**: Texto padrão do corpo
- **Small**: Texto menor para informações secundárias (ex: localização)
- **Extra Small**: Texto muito pequeno para labels e metadados

#### Font Weights
- **Regular** (400): Texto padrão
- **Medium** (500): Links e botões
- **Semibold** (600): Sub-títulos e destaque moderado
- **Bold** (700): Títulos e elementos de forte ênfase

### Suavização de Fonte

```css
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale;
```

Aplicado globalmente para melhor renderização em diferentes dispositivos.

---

## Espaçamento e Layout

### Container Principal

```css
max-width: 1280px (7xl)
padding: 1rem (mobile) | 1.5rem (sm) | 2rem (lg)
```

### Grid de Propriedades

Layout responsivo para cards de imóveis:
- **Mobile**: 1 coluna
- **Tablet (md)**: 2 colunas
- **Desktop (lg)**: 3 colunas

### Espaçamento Interno (Padding)

Componentes seguem escala consistente:
- **Card padding**: `1rem` (16px)
- **Button padding**: `0.5rem 1rem` (vertical x horizontal)
- **Input padding**: `0.75rem` (12px)

### Gaps e Margens

- **Gap pequeno**: `0.25rem` - `0.5rem` para elementos muito próximos
- **Gap médio**: `1rem` - `1.5rem` para agrupamentos
- **Gap grande**: `2rem` - `3rem` para seções

---

## Sombras e Elevação

### Sistema de Sombras

#### Small Shadow
```css
box-shadow: 0 1px 2px 0 rgba(16, 24, 40, 0.05);
```
**Uso**: Elementos sutis, badges, pequenos cards

#### Medium Shadow (Card Default)
```css
box-shadow: 0 1px 3px 0 rgba(16, 24, 40, 0.1), 
            0 1px 2px 0 rgba(16, 24, 40, 0.06);
```
**Uso**: Cards de imóveis, containers principais

**Nota**: No arquivo CSS, também está definido como `--shadow-md` com valores ligeiramente diferentes para uso alternativo.

#### Large Shadow (Card Hover)
```css
box-shadow: 0 10px 15px -3px rgba(16, 24, 40, 0.1), 
            0 4px 6px -2px rgba(16, 24, 40, 0.05);
```
**Uso**: Estado hover de cards, elementos elevados

#### Extra Large Shadow
```css
box-shadow: 0 12px 16px -4px rgba(16, 24, 40, 0.08), 
            0 4px 6px -2px rgba(16, 24, 40, 0.03);
```
**Uso**: Modais, dropdowns, elementos flutuantes

### Hierarquia de Elevação

1. **Nível 0**: Sem sombra (elementos planos)
2. **Nível 1**: Small shadow (badges, tags)
3. **Nível 2**: Card shadow (cards padrão)
4. **Nível 3**: Card hover shadow (interação)
5. **Nível 4**: Large shadow (modais, menus)

---

## Border Radius

### Escala de Arredondamento

```css
sm: 6px   - Elementos pequenos
md: 8px   - Padrão para inputs e botões
lg: 12px  - Cards e containers
xl: 16px  - Containers grandes
2xl: 16px - Elementos especiais
```

### Aplicação

- **Botões**: `8px` (rounded-md)
- **Inputs**: `8px` (rounded-md)
- **Cards**: `12px` (rounded-xl)
- **Badges**: `9999px` (rounded-full - círculo completo)
- **Imagens de Avatar**: `9999px` (rounded-full)

---

## Componentes

### Botões

#### Button Primary
```css
.btn-primary {
  background: #101828;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 500;
  transition: background-color 200ms;
}

.btn-primary:hover {
  background: #1D2939;
}

.btn-primary:focus {
  outline: none;
  box-shadow: 0 0 0 2px white, 0 0 0 4px #101828;
}
```

**Uso**: Ações principais, CTAs importantes (ex: "Anunciar")

#### Button Secondary
```css
.btn-secondary {
  background: white;
  color: #101828;
  border: 1px solid #E4E7EC;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 500;
  transition: background-color 200ms;
}

.btn-secondary:hover {
  background: #F9FAFB;
}
```

**Uso**: Ações secundárias (ex: "Favoritos")

#### Button Accent
```css
.btn-accent {
  background: #D4AF37;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 500;
  transition: background-color 200ms;
}

.btn-accent:hover {
  background: #B8962F;
}
```

**Uso**: Ações especiais, premium features

### Cards

#### Property Card
```css
.card {
  background: white;
  border-radius: 12px;
  border: 1px solid #E4E7EC;
  box-shadow: 0 1px 3px 0 rgba(16, 24, 40, 0.1), 
              0 1px 2px 0 rgba(16, 24, 40, 0.06);
  transition: box-shadow 200ms;
}

.card:hover {
  box-shadow: 0 10px 15px -3px rgba(16, 24, 40, 0.1), 
              0 4px 6px -2px rgba(16, 24, 40, 0.05);
}
```

**Estrutura do Card**:
- Imagem: Aspect ratio 4:3, com hover scale
- Badges: Posicionados no canto superior esquerdo
- Botão Favorito: Canto superior direito
- Conteúdo: Padding de 1rem
- Características: Border top com ícones

### Inputs e Formulários

#### Input
```css
.input {
  width: 100%;
  padding: 0.5rem 0.75rem;
  border: 1px solid #E4E7EC;
  border-radius: 8px;
}

.input:focus {
  outline: none;
  box-shadow: 0 0 0 2px #101828;
  border-color: transparent;
}

.input::placeholder {
  color: #667085;
}
```

#### Select
```css
.select {
  width: 100%;
  padding: 0.5rem 0.75rem;
  border: 1px solid #E4E7EC;
  border-radius: 8px;
  background: white;
  appearance: none;
  cursor: pointer;
}

.select:focus {
  outline: none;
  box-shadow: 0 0 0 2px #101828;
  border-color: transparent;
}
```

### Badges

#### Badge Base
```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: 9999px;
}
```

#### Badge Sale (Venda)
```css
.badge-sale {
  background: rgb(220 252 231); /* green-100 */
  color: rgb(22 101 52); /* green-800 */
}
```

#### Badge Rent (Aluguel)
```css
.badge-rent {
  background: rgb(219 234 254); /* blue-100 */
  color: rgb(30 64 175); /* blue-800 */
}
```

### Header

**Estrutura**:
- Background branco com borda inferior
- Altura fixa: `4rem` (64px)
- Sticky no topo (z-index: 50)
- Logo à esquerda com link para home
- Navegação centralizada (oculta em mobile)
- Ações à direita (Favoritos, Anunciar)
- Barra de loading opcional na base

**Classes principais**:
```css
.sticky .top-0 .z-50
.bg-white .border-b .border-gray-200
.h-16
```

### Footer

Estrutura modular para informações de rodapé, links e copyright.

---

## Tokens de Design

### CSS Custom Properties

Todos os tokens estão definidos na raiz do documento:

```css
:root {
  /* Cores Primárias */
  --color-primary: #101828;
  --color-primary-light: #1D2939;
  --color-accent: #D4AF37;
  --color-accent-hover: #B8962F;
  
  /* Cores de Texto */
  --color-text-primary: #101828;
  --color-text-secondary: #475467;
  --color-text-muted: #667085;
  
  /* Cores de Background */
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F9FAFB;
  --color-bg-tertiary: #F2F4F7;
  
  /* Cores de Borda */
  --color-border: #E4E7EC;
  --color-border-hover: #D0D5DD;
  
  /* Cores de Status */
  --color-success: #12B76A;
  --color-warning: #F79009;
  --color-error: #F04438;
  
  /* Sombras */
  --shadow-sm: 0 1px 2px 0 rgba(16, 24, 40, 0.05);
  --shadow-md: 0 4px 8px -2px rgba(16, 24, 40, 0.1), 
               0 2px 4px -2px rgba(16, 24, 40, 0.06);
  --shadow-lg: 0 12px 16px -4px rgba(16, 24, 40, 0.08), 
               0 4px 6px -2px rgba(16, 24, 40, 0.03);
  
  /* Border Radius */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
}
```

### Uso dos Tokens

Os tokens podem ser usados diretamente em CSS:

```css
.custom-element {
  color: var(--color-text-primary);
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}
```

---

## Boas Práticas

### 1. Consistência de Cores

✅ **Faça**:
- Use cores da paleta definida
- Mantenha contraste adequado (WCAG AA mínimo)
- Use `primary` para elementos principais
- Use `accent` com moderação para destaques

❌ **Não faça**:
- Criar cores customizadas fora da paleta
- Usar cores muito similares para propósitos diferentes
- Ignorar a hierarquia de cores

### 2. Espaçamento

✅ **Faça**:
- Use a escala de espaçamento do Tailwind (múltiplos de 4px)
- Mantenha espaçamento consistente entre elementos similares
- Use gap e flex/grid para layouts

❌ **Não faça**:
- Usar valores arbitrários de margin/padding
- Misturar unidades (px, rem, %) sem necessidade
- Espaçamento inconsistente entre seções

### 3. Componentes

✅ **Faça**:
- Reutilize classes de componentes existentes (.btn-primary, .card, etc.)
- Mantenha a estrutura HTML consistente
- Use transições suaves (200-300ms)

❌ **Não faça**:
- Recriar estilos que já existem
- Sobrescrever estilos de componentes sem necessidade
- Criar variações muito diferentes do design base

### 4. Responsividade

✅ **Faça**:
- Teste em múltiplos tamanhos de tela
- Use breakpoints do Tailwind (sm, md, lg, xl)
- Implemente mobile-first quando possível

❌ **Não faça**:
- Assumir que o design funciona em todos os tamanhos
- Ignorar estados de tablet
- Criar breakpoints customizados sem necessidade

### 5. Performance

✅ **Faça**:
- Use lazy loading para imagens (`loading="lazy"`)
- Otimize imagens antes de fazer upload
- Use aspect-ratio para evitar layout shifts

❌ **Não faça**:
- Carregar imagens grandes desnecessariamente
- Ignorar otimização de assets
- Criar animações pesadas que afetam performance

### 6. Acessibilidade

✅ **Faça**:
- Use labels descritivos (aria-label quando necessário)
- Mantenha foco visível em elementos interativos
- Garanta contraste adequado de cores

❌ **Não faça**:
- Remover outlines de foco sem substituição
- Usar apenas cor para transmitir informação
- Ignorar leitores de tela

### 7. Scrollbar Personalizada

O sistema inclui scrollbar customizada:

```css
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--color-bg-tertiary);
}

::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--color-text-muted);
}
```

### 8. Estados de Interação

Todos os elementos interativos devem ter estados claros:

- **Default**: Estado padrão
- **Hover**: Mudança sutil de cor ou elevação
- **Active**: Feedback visual ao clicar
- **Focus**: Ring visível para navegação por teclado
- **Disabled**: Opacidade reduzida e cursor não permitido

---

## Manutenção do Design System

### Quando Adicionar Novos Elementos

1. **Verifique se já existe**: Consulte este documento antes de criar novos componentes
2. **Siga os padrões**: Novos elementos devem seguir as convenções estabelecidas
3. **Documente**: Adicione novos componentes a este documento
4. **Teste**: Valide em diferentes cenários e dispositivos

### Versionamento

Mudanças no design system devem ser:
- **Documentadas**: Atualizar este arquivo
- **Comunicadas**: Informar a equipe sobre mudanças
- **Testadas**: Garantir compatibilidade com componentes existentes

### Contribuindo

Para propor mudanças no design system:
1. Abra uma discussão sobre a necessidade da mudança
2. Apresente casos de uso e exemplos
3. Documente a proposta
4. Implemente após aprovação
5. Atualize este documento

---

## Recursos e Ferramentas

### Ferramentas Utilizadas

- **Tailwind CSS**: Framework CSS utility-first
- **Vue 3**: Framework JavaScript para componentes
- **Nuxt 3**: Framework meta para Vue.js
- **Inter Font**: Tipografia principal

### Links Úteis

- [Documentação Tailwind CSS](https://tailwindcss.com/docs)
- [Paleta de Cores Tailwind](https://tailwindcss.com/docs/customizing-colors)
- [Vue 3 Documentation](https://vuejs.org/)
- [Nuxt 3 Documentation](https://nuxt.com/)

---

## Changelog

### Versão 1.0.0 - Dezembro 2024
- ✅ Consolidação inicial do design system
- ✅ Documentação de paleta de cores
- ✅ Documentação de tipografia
- ✅ Documentação de componentes principais
- ✅ Tokens de design CSS
- ✅ Guia de boas práticas

---

**Última atualização**: Dezembro 2024  
**Mantido por**: Equipe Pilar Clone  
**Versão**: 1.0.0
