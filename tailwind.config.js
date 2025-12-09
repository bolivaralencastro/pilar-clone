/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    './components/**/*.{js,vue,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
    './error.vue'
  ],
  safelist: [
    // Garantir que cores primitivas sejam sempre geradas
    'bg-rich-black',
    'bg-mat-slate',
    'bg-mat-stone',
    'bg-porcelain',
    'bg-mist',
    'bg-chromium',
    'bg-platinum',
    'bg-pure-white',
    'bg-brand-orange',
    'bg-brand-orange-dark',
    'bg-status-success',
    'bg-status-alert',
    'bg-status-error',
  ],
  theme: {
    extend: {
      colors: {
        // ═══════════════════════════════════════════════════════════
        // 1. TOKENS PRIMITIVOS (Global Tokens)
        // Cores brutas que nunca mudam - base do sistema
        // ═══════════════════════════════════════════════════════════
        
        // Fundamentos Escuros
        'rich-black': '#121212',     // Base escura principal
        'mat-slate': '#2B3A42',      // Deep Slate - tons frios
        'mat-stone': '#4A4843',      // Graphite Stone - tons neutros
        
        // Fundamentos Claros (The White-to-Platinum Gradient)
        'pure-white': '#FFFFFF',     // Gray-0: Contraste máximo
        'porcelain': '#FAFAFA',      // Gray-50: Base clara principal
        'mist': '#F4F4F5',           // Gray-100: Sidebar / Hover (NOVO)
        'chromium': '#E4E4E7',       // Gray-200: Borda Sutil (NOVO)
        'platinum': '#D6D6D8',       // Gray-300: Estrutura / Disabled
        
        // Marca & Status (Primitivos)
        'brand-orange': '#D5500B',   // Pantone 1665 C
        'brand-orange-dark': '#B54209', // Hover state
        'status-success': '#00AE42',
        'status-alert': '#FFA400',
        'status-error': '#ED3A3D',
        
        // Presentation Colors
        'deep-brown': '#1A1410',     // Fundo escuro da apresentação
        'off-white': '#F5F5F0',      // Texto claro da apresentação
        'soft-beige': '#E8E6E1',     // Accent da apresentação
        
        // ═══════════════════════════════════════════════════════════
        // 2. TOKENS SEMÂNTICOS (Alias Tokens)
        // Conectados a variáveis CSS - mudam com tema
        // USO: bg-surface-base, text-primary, border-subtle
        // ═══════════════════════════════════════════════════════════
        
        // Superfícies (Backgrounds)
        'surface-base': 'rgb(var(--color-surface-base) / <alpha-value>)',
        'surface-card': 'rgb(var(--color-surface-card) / <alpha-value>)',
        'surface-subtle': 'rgb(var(--color-surface-subtle) / <alpha-value>)',
        'surface-offset': 'rgb(var(--color-surface-offset) / <alpha-value>)',
        'surface-brand': 'rgb(var(--color-surface-brand) / <alpha-value>)',

        // Textos (Text Colors)
        'text-primary': 'rgb(var(--color-text-primary) / <alpha-value>)',
        'text-secondary': 'rgb(var(--color-text-secondary) / <alpha-value>)',
        'text-inverse': 'rgb(var(--color-text-inverse) / <alpha-value>)',
        'text-link': 'rgb(var(--color-text-link) / <alpha-value>)',
        
        // Ações (Interactive States)
        'action-primary': 'rgb(var(--color-action-primary) / <alpha-value>)',
        'action-hover': 'rgb(var(--color-action-hover) / <alpha-value>)',
        
        // Bordas (Borders)
        'border-hairline': 'rgb(var(--color-border-hairline) / <alpha-value>)',
        'border-subtle': 'rgb(var(--color-border-subtle) / <alpha-value>)',
        'border-strong': 'rgb(var(--color-border-strong) / <alpha-value>)',
        'border-focus': 'rgb(var(--color-border-focus) / <alpha-value>)',
        
        // ═══════════════════════════════════════════════════════════
        // 3. LEGACY COMPATIBILITY
        // Mantido para não quebrar código existente
        // ═══════════════════════════════════════════════════════════
        primary: '#D5500B',
        secondary: 'rgb(var(--color-text-secondary) / <alpha-value>)',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['"Playfair Display"', 'serif'],
        display: ['Matter SQ', 'Matter', 'Inter', 'sans-serif'],
        playfair: ['"Playfair Display"', 'serif'],
        roboto: ['Roboto', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
      },
      boxShadow: {
        'card': '0 1px 3px 0 rgba(0, 0, 0, 0.05)',
        'card-hover': '0 10px 30px -10px rgba(0, 0, 0, 0.08)',
        'default': '0 1px 3px 0 rgba(0, 0, 0, 0.10)', // shadow-default
      },
      borderRadius: {
        'lg': '8px',   // Cards padrão
        'xl': '12px',  // Cards grandes
        '2xl': '16px'  // Elementos especiais
      }
    }
  },
  plugins: []
}
