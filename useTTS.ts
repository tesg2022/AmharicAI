export function useTTS() {
  const audioUrl=ref('')
  const loading=ref(false)
  const error=ref('')

  async function speak(text:string) {
    if(!text.trim()) return
    loading.value=true; error.value=''; audioUrl.value=''
    try {
      const result=await $fetch<{audio_url:string}>('/api/tts',{
        method:'POST',
        body:{text,steps:32,guidance_scale:2.0}
      })
      audioUrl.value=result.audio_url
    } catch(e:any) {
      error.value=e?.data?.statusMessage || e?.message || 'TTS request failed.'
    } finally { loading.value=false }
  }
  return {audioUrl,loading,error,speak}
}