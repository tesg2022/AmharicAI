export default defineNuxtConfig({
  compatibilityDate: '2026-01-01',
  devtools: { enabled: false },
  app: {
    head: {
      title: 'AmharicAI — Learn Amharic',
      meta: [
        { name: 'description', content: 'Read, write, speak and listen to Amharic with AmharicAI.' }
      ]
    }
  }
})
