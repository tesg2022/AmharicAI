<template><main class="page"><h1>Lesson {{route.params.id}}</h1><p>Listen and repeat:</p><div v-for="p in phrases" :key="p.amharic" class="phrase"><div class="am">{{p.amharic}}</div><div>{{p.english}}</div><button @click="speak(p.amharic)">🔊 Listen</button></div><AudioPlayer v-if="audioUrl" :src="audioUrl"/></main></template>
<script setup lang="ts">
const route=useRoute();const {speak:generateSpeech}=useTTS();const audioUrl=ref('')
const phrases=[{amharic:'ሰላም። ደህና ነህ?',english:'Hello. How are you?'},{amharic:'ደህና ነኝ። አንተስ?',english:'I am fine. And you?'},{amharic:'ደህና ነኝ።',english:'I am fine.'}]
async function speak(text:string){audioUrl.value=(await generateSpeech(text)).audio_url}
</script>
<style scoped>.page{max-width:760px;margin:60px auto;padding:24px;font-family:Inter,system-ui,sans-serif}.phrase{border:1px solid #ddd;border-radius:12px;padding:16px;margin:12px 0}.am{font-size:24px;margin-bottom:6px}button{margin-top:10px;padding:8px 14px}</style>
