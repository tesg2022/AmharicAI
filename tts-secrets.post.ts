export default defineEventHandler(()=>{throw createError({statusCode:501,statusMessage:'Secrets are intentionally not persisted. Use server environment variables or a production secret manager.'})})
