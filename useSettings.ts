export function useSettings() {
  const ttsEnabled=useState('ttsEnabled',()=>true)
  return {ttsEnabled}
}