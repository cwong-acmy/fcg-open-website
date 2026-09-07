// React Theme — extracted from https://open.fusionconnectgroup.com/home
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
    neutral900: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '15': string;
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '28': string;
    '32': string;
    '36': string;
    '44': string;
    '96': string;
 *   };
 *   space: {
    '2': string;
    '24': string;
    '28': string;
    '40': string;
    '48': string;
    '64': string;
    '78': string;
    '88': string;
    '112': string;
    '192': string;
    '272': string;
    '288': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xl: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#f97316",
    "secondary": "#020617",
    "accent": "#10b981",
    "background": "#f5f7fa",
    "foreground": "#1f1f1f",
    "neutral50": "#e2e4e9",
    "neutral100": "#ffffff",
    "neutral200": "#0f1114",
    "neutral300": "#6b7280",
    "neutral400": "#64748b",
    "neutral500": "#52525b",
    "neutral600": "#3f3f46",
    "neutral700": "#1f1f1f",
    "neutral800": "#fff7ed",
    "neutral900": "#334155"
  },
  "fonts": {
    "body": "'SF Pro Display', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "36": "36px",
    "44": "44px",
    "96": "96px"
  },
  "space": {
    "2": "2px",
    "24": "24px",
    "28": "28px",
    "40": "40px",
    "48": "48px",
    "64": "64px",
    "78": "78px",
    "88": "88px",
    "112": "112px",
    "192": "192px",
    "272": "272px",
    "288": "288px"
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "16px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 23, 42, 0.14) 0px 18px 50px 0px",
    "xl": "rgba(148, 163, 184, 0.2) 0px 24px 80px 0px, rgba(255, 255, 255, 0.92) 0px 1px 0px 0px inset"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#f97316",
      "light": "hsl(25, 95%, 68%)",
      "dark": "hsl(25, 95%, 38%)"
    },
    "secondary": {
      "main": "#020617",
      "light": "hsl(229, 84%, 20%)",
      "dark": "hsl(229, 84%, 10%)"
    },
    "background": {
      "default": "#f5f7fa",
      "paper": "#f9fafb"
    },
    "text": {
      "primary": "#1f1f1f",
      "secondary": "#0f172a"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "0px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "36px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 18px 50px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 10px 30px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.16) 0px 18px 48px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 12px 34px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.38) 0px 24px 54px -34px"
  ]
};

export default theme;
