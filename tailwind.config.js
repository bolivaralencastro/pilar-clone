/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './components/**/*.{js,vue,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
    './error.vue'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#101828',
          light: '#1D2939',
          dark: '#0C111D'
        },
        accent: {
          DEFAULT: '#D4AF37',
          hover: '#B8962F'
        },
        gray: {
          25: '#FCFCFD',
          50: '#F9FAFB',
          100: '#F2F4F7',
          200: '#E4E7EC',
          300: '#D0D5DD',
          400: '#98A2B3',
          500: '#667085',
          600: '#475467',
          700: '#344054',
          800: '#1D2939',
          900: '#101828'
        }
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif']
      },
      boxShadow: {
        'card': '0 1px 3px 0 rgba(16, 24, 40, 0.1), 0 1px 2px 0 rgba(16, 24, 40, 0.06)',
        'card-hover': '0 10px 15px -3px rgba(16, 24, 40, 0.1), 0 4px 6px -2px rgba(16, 24, 40, 0.05)'
      },
      borderRadius: {
        'xl': '12px',
        '2xl': '16px'
      }
    }
  },
  plugins: []
}
