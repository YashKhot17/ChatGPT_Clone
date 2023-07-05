/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors:{
        chatgrey: {50: '#343541'},
        chatblack: {50: '#202123'}
      }
    },
  },
  plugins: [],
}

