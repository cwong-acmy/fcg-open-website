// React Theme — extracted from https://fusionconnectgroup.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
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
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '30': string;
    '48': string;
    '60': string;
    '76': string;
    '96': string;
    '10.4': string;
 *   };
 *   space: {
    '1': string;
    '40': string;
    '48': string;
    '64': string;
    '80': string;
    '96': string;
    '128': string;
    '141': string;
    '160': string;
    '170': string;
    '213': string;
 *   };
 *   radii: {
    xs: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
    md: string;
    lg: string;
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
    "secondary": "#111827",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#0f1114",
    "neutral200": "#6b7280",
    "neutral300": "#4b5563",
    "neutral400": "#000000",
    "neutral500": "#d1d5db",
    "neutral600": "#ffffff",
    "neutral700": "#f3f4f6",
    "neutral800": "#9ca3af",
    "neutral900": "#374151"
  },
  "fonts": {
    "body": "'Inter', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "30": "30px",
    "48": "48px",
    "60": "60px",
    "76": "76px",
    "96": "96px",
    "10.4": "10.4px"
  },
  "space": {
    "1": "1px",
    "40": "40px",
    "48": "48px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "128": "128px",
    "141": "141px",
    "160": "160px",
    "170": "170px",
    "213": "213px"
  },
  "radii": {
    "xs": "2px",
    "md": "6px",
    "lg": "15px",
    "xl": "24px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset",
    "xs": "rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px 20px 40px -15px",
    "md": "rgba(0, 0, 0, 0.15) 0px 0px 10px 0px",
    "lg": "rgba(0, 0, 0, 0.12) 0px 0px 32px 0px",
    "xl": "rgba(15, 17, 20, 0.18) 0px 28px 70px 0px"
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
      "main": "#111827",
      "light": "hsl(221, 39%, 26%)",
      "dark": "hsl(221, 39%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#f3f4f6"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0f1114"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "48px",
      "fontWeight": "500",
      "lineHeight": "48px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "32px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.4) 0px 0px 8px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.5) 0px 0px 8px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.9) 0px 0px 60px 0px, rgba(0, 0, 0, 0.2) 0px 0px 20px 0px inset",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 10px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.5) 0px 0px 10px 0px"
  ]
};

export default theme;
