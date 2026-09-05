export default defineEventHandler(() => {
  const config = useRuntimeConfig()

  return {
    ok: true,
    service: 'AmharicAI Custom TTS',
    provider: 'amharicai-custom',
    configured: Boolean(config.AMHARICAI_TTS_URL)
  }
})
