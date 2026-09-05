export default defineNuxtConfig({
  compatibilityDate: '2025-01-01',
  devtools: { enabled: true },
  runtimeConfig: {
    AMHARICAI_TTS_URL: process.env.AMHARICAI_TTS_URL || '',
    AMHARICAI_TTS_KEY: process.env.AMHARICAI_TTS_KEY || '',
    AMHARICAI_TTS_MODEL: process.env.AMHARICAI_TTS_MODEL || 'AmharicAI-TTS-LoRA',
    public: { appName: 'AmharicAI', ttsEnabled: true }
  }
})
