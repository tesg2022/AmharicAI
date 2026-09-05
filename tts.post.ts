export default defineEventHandler(async (event) => {
  const body=await readBody(event)
  if(!body?.text) throw createError({statusCode:400,statusMessage:'Text is required'})

  const config=useRuntimeConfig()

  if(!config.amharicaiTtsUrl)
    throw createError({statusCode:503,statusMessage:'AMHARICAI_TTS_URL is not configured'})

  // IMPORTANT:
  // Replace the following forwarding block with the exact validated
  // AmharicAI TTS backend contract before production.
  const response=await $fetch<any>(`${config.amharicaiTtsUrl}/api/v1/tts`,{
    method:'POST',
    headers: config.amharicaiTtsKey ? {'Authorization':`Bearer ${config.amharicaiTtsKey}`} : {},
    body:{
      text:body.text,
      steps:body.steps ?? 32,
      guidance_scale:body.guidance_scale ?? 2.0,
      model:config.amharicaiTtsModel
    }
  })

  return response
})