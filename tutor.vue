<template><main class="page"><h1>AmharicAI TTS Tutor</h1><textarea v-model="text" rows="5"></textarea><button :disabled="loading||!text.trim()" @click="speak">{{loading?'Generating…':'🔊 Speak Amharic'}}</button><p v-if="error" class="error">{{error}}</p><AudioPlayer v-if="audioUrl" :src="audioUrl"/></main></template>
<script setup lang="ts">
const text=ref('ሰላም። ደህና ነህ?'); const audioUrl=ref(''); const loading=ref(false); const error=ref('')
const {speak:generateSpeech}=useTTS()
async function speak(){loading.value=true;error.value='';try{audioUrl.value=(await generateSpeech(text.value)).audio_url}catch(e:any){error.value=e?.data?.statusMessage||e?.message||'TTS request failed'}finally{loading.value=false}}
</script>
<style scoped>.page{max-width:760px;margin:60px auto;padding:24px;font-family:Inter,system-ui,sans-serif}textarea{width:100%;margin:20px 0;padding:12px;font-size:20px}button{padding:12px 18px}.error{color:#b42318}</style>
