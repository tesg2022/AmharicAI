export default defineEventHandler(async (event) => {
  // This executes strictly on the server. Credentials never leak to the client.
  const body = await readBody(event)
  const config = useRuntimeConfig()
  
  // TODO: Validate user subscription tier here via database before calling TTS
  
  try {
    const response = await $fetch(config.ttsApiUrl, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${config.ttsApiKey}` },
      body: { text: body.text }
    })
    return { audioUrl: response.audio_url }
  } catch (error) {
    throw createError({ statusCode: 500, statusMessage: 'Custom TTS generation failed' })
  }
})
