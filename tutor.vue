<script setup lang="ts">
const text = ref('')
const response = ref('ሰላም! እንዴት ልርዳህ?')
function ask() {
  if (!text.value.trim()) return
  response.value = 'ጥሩ ጥያቄ ነው። በአማርኛ መልስ ለመስጠት የAI Tutor አገልግሎት ሲገናኝ ይህ ቦታ ይጠቀማል።'
}
</script>

<template>
  <div class="container tutor">
    <span class="eyebrow">AI LANGUAGE PRACTICE</span>
    <h1>AmharicAI Tutor</h1>
    <p class="section-intro">Practise Amharic through guided conversation. The interface is ready for the future AI tutor and custom voice pipeline.</p>
    <div class="tutor-box">
      <div class="chat">
        <div class="amh">{{ response }}</div>
        <div class="hint">Try: “ስሜ አለማየሁ ነው።” or ask “ስንት ነው?”</div>
      </div>
      <textarea v-model="text" placeholder="Write an Amharic sentence or ask a question…"></textarea>
      <div class="actions">
        <button class="btn primary" @click="ask">Practise →</button>
      </div>
    </div>
  </div>
</template>
