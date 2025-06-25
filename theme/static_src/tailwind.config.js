/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/*/.html',
    '../../templates/*/.html',
    '../../*/templates//.html',
    '../*/.html',
  ],
  safelist: [
    {pattern: /bg-gradient-to-r/},
    {pattern: /from-\w+-\d+/},
    {pattern: /to-\w+-\d+/},
    {pattern: /hover:from-\w+-\d+/},
    {pattern: /hover:to-\w+-\d+/},
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}