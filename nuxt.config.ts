export default defineNuxtConfig({
  compatibilityDate: '2026-01-01',
  // SSR enabled for secure API routing and SEO
  ssr: true,
  app: {
    head: { title: 'AmharicAI — Voice-First Learning Platform' }
  },
  runtimeConfig: {
    stripeSecretKey: process.env.STRIPE_SECRET_KEY,
    ttsApiUrl: process.env.AMHARICAI_TTS_URL,
    ttsApiKey: process.env.AMHARICAI_TTS_KEY,
    public: { baseUrl: process.env.BASE_URL || 'http://localhost:3000' }
  }
})
