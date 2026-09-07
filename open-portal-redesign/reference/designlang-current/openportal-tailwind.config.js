/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(25, 95%, 97%)',
            '100': 'hsl(25, 95%, 94%)',
            '200': 'hsl(25, 95%, 86%)',
            '300': 'hsl(25, 95%, 76%)',
            '400': 'hsl(25, 95%, 64%)',
            '500': 'hsl(25, 95%, 50%)',
            '600': 'hsl(25, 95%, 40%)',
            '700': 'hsl(25, 95%, 32%)',
            '800': 'hsl(25, 95%, 24%)',
            '900': 'hsl(25, 95%, 16%)',
            '950': 'hsl(25, 95%, 10%)',
            DEFAULT: '#f97316'
        },
        secondary: {
            '50': 'hsl(229, 84%, 97%)',
            '100': 'hsl(229, 84%, 94%)',
            '200': 'hsl(229, 84%, 86%)',
            '300': 'hsl(229, 84%, 76%)',
            '400': 'hsl(229, 84%, 64%)',
            '500': 'hsl(229, 84%, 50%)',
            '600': 'hsl(229, 84%, 40%)',
            '700': 'hsl(229, 84%, 32%)',
            '800': 'hsl(229, 84%, 24%)',
            '900': 'hsl(229, 84%, 16%)',
            '950': 'hsl(229, 84%, 10%)',
            DEFAULT: '#020617'
        },
        accent: {
            '50': 'hsl(160, 84%, 97%)',
            '100': 'hsl(160, 84%, 94%)',
            '200': 'hsl(160, 84%, 86%)',
            '300': 'hsl(160, 84%, 76%)',
            '400': 'hsl(160, 84%, 64%)',
            '500': 'hsl(160, 84%, 50%)',
            '600': 'hsl(160, 84%, 40%)',
            '700': 'hsl(160, 84%, 32%)',
            '800': 'hsl(160, 84%, 24%)',
            '900': 'hsl(160, 84%, 16%)',
            '950': 'hsl(160, 84%, 10%)',
            DEFAULT: '#10b981'
        },
        'neutral-50': '#e2e4e9',
        'neutral-100': '#ffffff',
        'neutral-200': '#0f1114',
        'neutral-300': '#6b7280',
        'neutral-400': '#64748b',
        'neutral-500': '#52525b',
        'neutral-600': '#3f3f46',
        'neutral-700': '#1f1f1f',
        'neutral-800': '#fff7ed',
        'neutral-900': '#334155',
        background: '#f5f7fa',
        foreground: '#1f1f1f'
    },
    fontFamily: {
        sans: [
            'SF Pro Display',
            'sans-serif'
        ]
    },
    fontSize: {
        '9': [
            '9px',
            {
                lineHeight: '9px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '16px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '18px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '28px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '28px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '36px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '42px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '0px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '43.2px'
            }
        ],
        '44': [
            '44px',
            {
                lineHeight: '47.52px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '92.16px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '12': '24px',
        '14': '28px',
        '20': '40px',
        '24': '48px',
        '32': '64px',
        '39': '78px',
        '44': '88px',
        '56': '112px',
        '96': '192px',
        '136': '272px',
        '144': '288px'
    },
    borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '16px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 23, 42, 0.14) 0px 18px 50px 0px',
        xl: 'rgba(148, 163, 184, 0.2) 0px 24px 80px 0px, rgba(255, 255, 255, 0.92) 0px 1px 0px 0px inset'
    },
    screens: {
        sm: '640px',
        md: '768px',
        '851px': '851px',
        '900px': '900px',
        lg: '1024px',
        '1100px': '1100px',
        '1200px': '1200px',
        xl: '1280px',
        '2xl': '1536px'
    },
    transitionDuration: {
        '70': '0.07s',
        '80': '0.08s',
        '90': '0.09s',
        '140': '0.14s',
        '150': '0.15s',
        '180': '0.18s',
        '200': '0.2s',
        '210': '0.21s',
        '250': '0.25s',
        '260': '0.26s',
        '300': '0.3s',
        '820': '0.82s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.18, 0.86, 0.32, 1)'
    },
    container: {
        center: true,
        padding: '32px'
    },
    maxWidth: {
        container: '1500px'
    }
},
  },
};
