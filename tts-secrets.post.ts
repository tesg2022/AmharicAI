export default defineEventHandler(async (event) => {
  // IMPORTANT: add real admin authentication/authorization and a secret
  // manager before production. Do not persist secrets in a public file.
  const body = await readBody(event)
  if (!body?.provider) throw createError({statusCode:400,statusMessage:'Provider is required'})

  return {
    ok:true,
    provider:body.provider,
    message:'Configuration accepted by the API. Connect this endpoint to your server secret manager.'
  }
})