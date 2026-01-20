/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                flask: "#00b4d8", // A fresh blue/cyan for FlaskHub
                dark: "#0a192f",
            },
            fontFamily: {
                mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
            },
            boxShadow: {
                'neon': '0 0 15px rgba(0, 180, 216, 0.2)',
                'neon-strong': '0 0 20px rgba(0, 180, 216, 0.3)',
            },
        },
    },
    plugins: [],
}
