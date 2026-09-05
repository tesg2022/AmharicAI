<template>
  <form @submit.prevent="save">
    <h2>AmharicAI Custom TTS</h2>

    <label>
      Custom TTS URL
      <input v-model="customUrl" placeholder="https://your-tts-host" />
    </label>

    <label>
      Server API key
      <input v-model="customKey" type="password" autocomplete="off" />
    </label>

    <label>
      Model
      <input v-model="model" placeholder="AmharicAI-TTS-LoRA" />
    </label>

    <button type="submit">Save Configuration</button>
    <button type="button" @click="test">Test Configuration</button>

    <p v-if="message">{{ message }}</p>
  </form>
</template>

<script setup lang="ts">
const customUrl = ref('')
const customKey = ref('')
const model = ref('AmharicAI-TTS-LoRA')
const message = ref('')

async function save() {
  message.value =
    'Configuration accepted. Store the real values in server environment variables or a secret manager.'
}

async function test() {
  try {
    const result: any = await $fetch('/api/admin/tts-test', {
      method: 'POST'
    })
    message.value = result.message
  } catch (e: any) {
    message.value =
      e?.data?.statusMessage || 'Configuration test failed.'
  }
}
</script>

<style scoped>
form { display:grid; gap:14px; max-width:620px; }
label { display:grid; gap:6px; font-weight:600; }
input { padding:10px; }
button { padding:10px 14px; width:max-content; }
</style>
