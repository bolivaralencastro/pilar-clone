/**
 * PilarHomes Design Tokens
 * TypeScript/JavaScript Module
 * Version: 1.0.0
 */

export const tokens = {
  colors: {
    primary: {
      black: 'hsl(0, 0%, 0%)',
      charcoal: 'hsl(0, 0%, 5%)',
    },
    neutral: {
      white: 'hsl(0, 0%, 100%)',
      gray: {
        100: 'hsl(0, 0%, 94%)',
        200: 'hsl(0, 0%, 88%)',
        400: 'hsl(0, 0%, 67%)',
        600: 'hsl(0, 0%, 43%)',
      },
    },
    accent: {
      beige: 'hsl(35, 54%, 75%)',
    },
    semantic: {
      textPrimary: 'hsl(0, 0%, 0%)',
      textSecondary: 'hsl(0, 0%, 43%)',
      textMuted: 'hsl(0, 0%, 67%)',
      background: 'hsl(0, 0%, 100%)',
      border: 'hsl(0, 0%, 88%)',
    },
  },

  typography: {
    fontFamily: {
      primary: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif",
    },
    fontSize: {
      xs: '0.75rem',
      sm: '0.875rem',
      base: '1rem',
      lg: '1.125rem',
      xl: '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
    },
    fontWeight: {
      light: 300,
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
    lineHeight: {
      tight: 1.25,
      normal: 1.5,
      relaxed: 1.75,
    },
  },

  spacing: {
    0: '0',
    1: '4px',
    2: '8px',
    3: '12px',
    4: '16px',
    5: '20px',
    6: '24px',
    8: '32px',
    10: '40px',
    12: '48px',
    16: '64px',
    20: '80px',
    24: '96px',
  },

  borderRadius: {
    none: '0',
    sm: '2px',
    base: '4px',
    md: '8px',
    lg: '12px',
    xl: '16px',
    '2xl': '24px',
    pill: '9999px',
    full: '50%',
  },

  shadows: {
    sm: '0 1px 2px rgba(0, 0, 0, 0.05)',
    base: '0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06)',
    md: '0 4px 6px rgba(0, 0, 0, 0.07), 0 2px 4px rgba(0, 0, 0, 0.06)',
    lg: '0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05)',
    xl: '0 20px 25px rgba(0, 0, 0, 0.15), 0 10px 10px rgba(0, 0, 0, 0.04)',
  },

  transitions: {
    duration: {
      fast: '0.15s',
      base: '0.3s',
      slow: '0.5s',
    },
    timing: {
      default: 'ease-in-out',
      easeIn: 'ease-in',
      easeOut: 'ease-out',
      linear: 'linear',
    },
  },

  breakpoints: {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
    '2xl': '1536px',
  },
} as const;

// TypeScript types
export type ColorToken = typeof tokens.colors;
export type TypographyToken = typeof tokens.typography;
export type SpacingToken = typeof tokens.spacing;
export type BorderRadiusToken = typeof tokens.borderRadius;
export type ShadowToken = typeof tokens.shadows;
export type TransitionToken = typeof tokens.transitions;
export type BreakpointToken = typeof tokens.breakpoints;

// Helper functions
export const getColor = (path: string): string => {
  const keys = path.split('.');
  let value: any = tokens.colors;
  for (const key of keys) {
    value = value[key];
    if (value === undefined) return '';
  }
  return value;
};

export const getSpacing = (multiplier: keyof typeof tokens.spacing): string => {
  return tokens.spacing[multiplier];
};

export default tokens;
