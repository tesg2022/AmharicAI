export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const body = await readBody<{ text?: string }>(event)

  const text = body?.text?.trim()
  if (!text) {
    throw createError({
      statusCode: 400,
      statusMessage: 'text is required'
    })
  }

  if (!config.AMHARICAI_TTS_URL) {
    throw createError({
      statusCode: 503,
      statusMessage: 'AmharicAI custom TTS URL is not configured on the server.'
    })
  }

  const target = `${config.AMHARICAI_TTS_URL.replace(/\/$/, '')}/api/v1/tts`

  const response: any = await $fetch(target, {
    method: 'POST',
    headers: {
      ...(config.AMHARICAI_TTS_KEY
        ? { Authorization: `Bearer ${config.AMHARICAI_TTS_KEY}` }
        : {}),
      'content-type': 'application/json'
    },
    body: {
      text,
      model: config.AMHARICAI_TTS_MODEL || 'AmharicAI-TTS-LoRA'
    }
  })

  if (!response?.audio_url) {
    throw createError({
      statusCode: 502,
      statusMessage: 'Custom AmharicAI TTS returned no audio_url.'
    })
  }

  return {
    provider: 'amharicai-custom',
    ...response
  }
})
