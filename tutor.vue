<template>
  <div class="page">
    <h1>🎙️ Amharic AI Tutor</h1>
    <p>Type an Amharic phrase and practice listening.</p>
    <textarea v-model="text" placeholder="ሰላም፣ እንዴት ነህ?"></textarea>
    <br><button @click="speak(text)" :disabled="loading">{{ loading ? 'Generating…' : '🔊 Speak Amharic' }}</button>
    <p v-if="error" class="error">{{ error }}</p>
    <audio v-if="audioUrl" :src="audioUrl" controls autoplay></audio>
  </div>
</template>
<script setup lang="ts">
const text=ref('ሰላም፣ እንዴት ነህ?')
const {speak,audioUrl,loading,error}=useTTS()
</script>
<style scoped>
textarea{width:100%;max-width:760px;min-height:130px;padding:15px;border:1px solid #ccd9d4;border-radius:12px;font:18px system-ui}
button{margin:12px 0;padding:12px 18px;border:0;border-radius:10px;background:#16805a;color:#fff;font-weight:800}.error{color:#b42318}
</style>