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
            '50': 'hsl(221, 39%, 97%)',
            '100': 'hsl(221, 39%, 94%)',
            '200': 'hsl(221, 39%, 86%)',
            '300': 'hsl(221, 39%, 76%)',
            '400': 'hsl(221, 39%, 64%)',
            '500': 'hsl(221, 39%, 50%)',
            '600': 'hsl(221, 39%, 40%)',
            '700': 'hsl(221, 39%, 32%)',
            '800': 'hsl(221, 39%, 24%)',
            '900': 'hsl(221, 39%, 16%)',
            '950': 'hsl(221, 39%, 10%)',
            DEFAULT: '#111827'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#0f1114',
        'neutral-200': '#6b7280',
        'neutral-300': '#4b5563',
        'neutral-400': '#000000',
        'neutral-500': '#d1d5db',
        'neutral-600': '#ffffff',
        'neutral-700': '#f3f4f6',
        'neutral-800': '#9ca3af',
        'neutral-900': '#374151',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ]
    },
    fontSize: {
        '8': [
            '8px',
            {
                lineHeight: '12px',
                letterSpacing: '0.8px'
            }
        ],
        '9': [
            '9px',
            {
                lineHeight: '13.5px'
            }
        ],
        '10': [
            '10px',
            {
                lineHeight: '14px',
                letterSpacing: '1.8px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16px',
                letterSpacing: '-0.6px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '20px',
                letterSpacing: '-0.35px'
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
                lineHeight: '28px',
                letterSpacing: '-0.5px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '32px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '36px',
                letterSpacing: '-0.75px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '48px',
                letterSpacing: '-1.2px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '60px',
                letterSpacing: '-3px'
            }
        ],
        '76': [
            '76px',
            {
                lineHeight: '76px',
                letterSpacing: '-1.9px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '96px',
                letterSpacing: '-4.8px'
            }
        ],
        '10.4': [
            '10.4px',
            {
                lineHeight: '15.6px'
            }
        ]
    },
    spacing: {
        '20': '40px',
        '24': '48px',
        '32': '64px',
        '40': '80px',
        '48': '96px',
        '64': '128px',
        '80': '160px',
        '85': '170px',
        '1px': '1px',
        '141px': '141px',
        '213px': '213px'
    },
    borderRadius: {
        xs: '2px',
        md: '6px',
        lg: '15px',
        xl: '24px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset',
        xs: 'rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px 20px 40px -15px',
        md: 'rgba(0, 0, 0, 0.15) 0px 0px 10px 0px',
        lg: 'rgba(0, 0, 0, 0.12) 0px 0px 32px 0px',
        xl: 'rgba(15, 17, 20, 0.18) 0px 28px 70px 0px'
    },
    screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px'
    },
    transitionDuration: {
        '75': '0.075s',
        '100': '0.1s',
        '150': '0.15s',
        '180': '0.18s',
        '200': '0.2s',
        '220': '0.22s',
        '240': '0.24s',
        '300': '0.3s',
        '500': '0.5s',
        '700': '0.7s',
        '1000': '1s',
        '1200': '1.2s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.23, 1, 0.32, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1600px'
    }
},
  },
};
