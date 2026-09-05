export function useTTS() {
  async function speak(text: string) {
    return await $fetch<{
      audio_url: string
      provider: string
      clip_id?: string
    }>('/api/tts', {
      method: 'POST',
      body: { text }
    })
  }

  return { speak }
}
