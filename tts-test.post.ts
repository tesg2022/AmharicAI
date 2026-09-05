export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  if (!body?.provider) throw createError({statusCode:400,statusMessage:'Provider is required'})

  // Production: authenticate admin here, then perform a provider-specific
  // health/request test. This starter avoids exposing secrets to the browser.
  const config = useRuntimeConfig()

  if (body.provider === 'amharicai' && !config.amharicaiTtsUrl)
    throw createError({statusCode:503,statusMessage:'AMHARICAI_TTS_URL is not configured'})

  if (body.provider === 'addis' && !config.addisApiKey)
    throw createError({statusCode:503,statusMessage:'ADDIS_API_KEY is not configured'})

  return {ok:true,provider:body.provider}
})