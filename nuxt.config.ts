export default defineNuxtConfig({
  devtools: { enabled: true },
  runtimeConfig: {
    addisApiKey: process.env.ADDIS_API_KEY || '',
    azureSpeechKey: process.env.AZURE_SPEECH_KEY || '',
    azureSpeechRegion: process.env.AZURE_SPEECH_REGION || '',
    googleApiKey: process.env.GOOGLE_API_KEY || '',
    amharicaiTtsUrl: process.env.AMHARICAI_TTS_URL || '',
    amharicaiTtsKey: process.env.AMHARICAI_TTS_KEY || '',
    amharicaiTtsModel: process.env.AMHARICAI_TTS_MODEL || 'AmharicAI-TTS-LoRA',
    public: {
      appName: 'AmharicAI',
      ttsEnabled: true
    }
  },
  css: [],
  compatibilityDate: '2025-01-01'
})