<template>
  <div class="page">
    <NuxtLink to="/">← All units</NuxtLink>
    <div class="lesson">
      <small>UNIT {{ id }}</small>
      <h1>{{ lesson.title }}</h1>
      <h2>{{ lesson.amharic }}</h2>
      <div class="phrase">
        <div class="am">ሰላም። ደህና ነህ?</div>
        <div class="en">Hello. Are you well?</div>
        <button @click="speak('ሰላም። ደህና ነህ?')">🔊 Listen</button>
      </div>
      <div class="phrase">
        <div class="am">ደህና ነኝ።</div>
        <div class="en">I am well.</div>
        <button @click="speak('ደህና ነኝ።')">🔊 Listen</button>
      </div>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const id = computed(() => String(route.params.id))
const lesson = computed(() => ({title:'Greetings',amharic:'ሰላምታ'}))
const { speak, error } = useTTS()
</script>

<style scoped>
.lesson{max-width:760px;margin:25px auto;background:#fff;padding:32px;border-radius:18px;border:1px solid #dce5e1}
.lesson>small{color:#16805a;font-weight:800}.phrase{border:1px solid #dce5e1;border-radius:14px;padding:20px;margin-top:15px}.am{font-size:28px}.en{color:#68756f;margin:7px 0 15px}button{padding:10px 14px;border:0;border-radius:9px;background:#16805a;color:#fff;font-weight:700}.error{color:#b42318}
</style>