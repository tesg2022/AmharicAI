export default defineEventHandler(async () => {
  const config = useRuntimeConfig()

  const configured = Boolean(config.AMHARICAI_TTS_URL)

  return {
    ok: configured,
    provider: 'amharicai-custom',
    message: configured
      ? 'Custom AmharicAI TTS URL is configured. A live generation can now validate the backend contract.'
      : 'Custom AmharicAI TTS URL is not configured.'
  }
})
