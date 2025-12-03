# Design System PilarHomes - Resumo Executivo

> Quick reference guide para o Design System da Pilar

---

## 🎨 Paleta de Cores - Quick Reference

### Cores Primárias
```
█ Preto      #000000   --primary
█ Beige      HSL(35, 54%, 75%)   --beige
█ Azul       #B9CDDF   --blue
█ Marrom     HSL(29, 34%, 18%)   --brown
```

### Cores de Estado
```
✓ Success    HSL(143, 100%, 34%)   Verde
✗ Error      HSL(359, 83%, 58%)    Vermelho
⚠ Warning    HSL(39, 100%, 50%)    Amarelo/Laranja
```

---

## 📏 Espaçamento - Sistema 4px

```
4px   8px   12px   16px   20px   24px   32px   48px   64px   80px   128px
▁     ▂     ▃      ▄      ▅      ▆      ▇      █      ██     ███    ████
0.25  0.5   0.75   1      1.25   1.5    2      3      4      5      8 rem
```

**Uso mais comum:**
- 8px (0.5rem) - Gaps pequenos
- 16px (1rem) - Base
- 20px (1.25rem) - Padding médio
- 24px (1.5rem) - Padding padrão
- 32px (2rem) - Espaço grande

---

## 📝 Tipografia

### Fontes
```
Principal: Inter (Google Fonts)
Display:   Matter SQ (Custom)
Secundária: Roboto
```

### Escala de Tamanhos
```
12px  14px  16px  18px  20px  24px  30px  36px  48px
xs    sm    base  lg    xl    2xl   3xl   4xl   5xl
```

---

## 🧩 Componentes Principais

### Button
```
Variants:  primary | secondary | outline | ghost
Sizes:     sm | md | lg
States:    default | hover | focus | disabled
Radius:    rounded-full (9999px)
```

### Card
```
Variants:  default | elevated | outlined
Padding:   none | sm (12px) | md (24px) | lg (32px)
Radius:    rounded-md (4px)
```

### Modal/Dialog
```
Animation: slide-up (0.4s cubic-bezier(0.16, 1, 0.3, 1))
Backdrop:  bg-black/50
Z-index:   50
```

---

## 📱 Breakpoints

```
Mobile:    < 640px
Tablet:    640px - 1023px
Desktop:   1024px - 1279px
Large:     1280px - 1535px
XL:        ≥ 1536px
```

**Approach:** Mobile First

---

## ✨ Efeitos

### Border Radius
```
sharp:     0px
sm:        2px
default:   4px
md:        8px
lg:        16px
full:      9999px (pill)
circle:    50%
```

### Transitions
```
Fast:      150ms  (interações)
Normal:    200ms  (hover states)
Smooth:    300ms  (animações)
Slide:     400ms  (modais)
```

### Timing Functions
```
ease-in-out:  cubic-bezier(0.4, 0, 0.2, 1)
slide:        cubic-bezier(0.16, 1, 0.3, 1)
```

---

## 🎯 Boas Práticas

### Acessibilidade
✓ Focus ring: 2px solid com 2px offset
✓ Touch targets: mínimo 44x44px
✓ Contraste: WCAG AA mínimo
✓ Navegação por teclado habilitada

### Performance
✓ Lazy loading de imagens
✓ Code splitting por componente
✓ WebP com quality 80
✓ CDN (CloudFront)

### Responsividade
✓ Mobile first approach
✓ Touch-friendly (44x44px mínimo)
✓ Safe area padding (iOS)
✓ `hover:hover` media query

---

## 📊 Estatísticas do Site

```
Componentes:
- Buttons:     126
- Images:      161
- SVG Icons:   98
- Links:       39
- Sections:    14

Classes mais usadas:
- flex:        578x
- text-white:  202x
- flex-col:    199x
- text-primary: 144x
- rounded-full: 88x
```

---

## 🎨 Tokens CSS - Variáveis Essenciais

```css
:root {
  /* Cores */
  --primary: 0 0% 0%;
  --beige: 35 54% 75%;
  --blue: #b9cddf;
  --white: 0 0% 100%;
  
  /* Tipografia */
  --font-family-display: "Inter", "sans-serif";
  
  /* Sistema */
  --border: 0 0% 14.9%;
  --ring: 0 0% 83.1%;
  --radius: 4px;
}
```

---

## 🚀 Stack Tecnológica

```
Framework:     Nuxt.js (Vue 3)
CSS:           Tailwind CSS
Hospedagem:    AWS CloudFront + ALB
Imagens:       Sistema customizado com WebP
Ícones:        SVG inline (24x24 padrão)
Fonts:         Self-hosted com fallbacks
```

---

## 📁 Arquivos Gerados

1. **DESIGN_SYSTEM_PILARHOMES.md** (Este arquivo)
   - Documentação completa do design system
   
2. **IMPLEMENTATION_GUIDE_PILARHOMES.md**
   - Exemplos de código
   - Configuração Tailwind
   - Componentes Vue/React
   
3. **STACK_ANALYSIS_PILARHOMES.md**
   - Análise técnica da stack
   - Performance e infraestrutura
   
4. **design_system_analysis/** (Pasta)
   - CSS files baixados
   - Tokens e análises brutas

---

## 🎯 Next Steps

### Para Implementar

1. ✅ Configurar Tailwind com as cores customizadas
2. ✅ Criar biblioteca de componentes base
3. ✅ Implementar sistema de tokens CSS
4. ✅ Configurar fonts (Inter, Matter SQ)
5. ✅ Setup de ícones SVG
6. ✅ Documentar no Storybook (opcional)

### Para Design

1. Criar Figma/Sketch com tokens
2. Documentar patterns de UI
3. Criar guia de ilustrações/imagens
4. Estabelecer tone of voice

### Para Dev

1. Setup do preprocessador CSS
2. Configurar linting (Tailwind)
3. Performance optimization
4. Accessibility audit

---

## 📞 Referências

- **Site analisado:** https://pilarhomes.com.br/
- **Data da análise:** 02/12/2025
- **Versão do deploy:** eba7fe8a8c54d5f94e813abc7f5acfe6b6ccad05

---

## 💡 Insights Importantes

### Identidade Visual
- **Minimalista e sofisticada**
- Uso predominante de preto e branco
- Beige como cor característica da marca
- Tipografia limpa (Inter)
- Imagens de alta qualidade

### UX Patterns
- Cards com hover states suaves
- Navegação clara e direta
- Sistema de filtros robusto
- Modal/dialog para ações secundárias
- Loading states com skeleton

### Mobile Experience
- Touch targets adequados (>44px)
- Scroll suave e otimizado
- Imagens responsivas
- Navegação adaptativa
- PWA ready (Service Worker)

---

*Quick reference criado em 02/12/2025*
*Baseado na análise completa do site PilarHomes*
