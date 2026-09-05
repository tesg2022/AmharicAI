<template>
  <form @submit.prevent="save">
    <label>TTS Provider *</label>
    <select v-model="form.provider" required>
      <option value="">Select provider</option>
      <option value="addis">Addis AI — Amharic TTS</option>
      <option value="azure">Azure Speech</option>
      <option value="google">Google Cloud Speech</option>
      <option value="amharicai">AmharicAI Custom TTS</option>
    </select>

    <section v-if="form.provider==='addis'"><label>Addis API Key *</label><input v-model="form.addis_api_key" type="password" autocomplete="new-password"></section>
    <section v-if="form.provider==='azure'">
      <label>Azure Speech Key *</label><input v-model="form.azure_speech_key" type="password" autocomplete="new-password">
      <label>Azure Region *</label><input v-model="form.azure_speech_region" placeholder="eastus">
    </section>
    <section v-if="form.provider==='google'"><label>Google API Key *</label><input v-model="form.google_api_key" type="password" autocomplete="new-password"></section>
    <section v-if="form.provider==='amharicai'">
      <label>TTS Base URL *</label><input v-model="form.amharicai_tts_url" placeholder="https://your-tts-host">
      <label>TTS API Key</label><input v-model="form.amharicai_tts_key" type="password" autocomplete="new-password">
      <label>TTS Model</label><input v-model="form.amharicai_tts_model">
    </section>

    <label class="check"><input v-model="form.enabled" type="checkbox"> Enable speech generation</label>
    <div class="actions">
      <button type="button" @click="test" class="secondary">🔊 Test Speech Connection</button>
      <button type="submit" class="primary">🔐 Save Securely</button>
    </div>
    <p v-if="message" :class="{ok:success,err:!success}">{{ message }}</p>
  </form>
</template>

<script setup lang="ts">
const form=reactive({
  provider:'',enabled:true,addis_api_key:'',azure_speech_key:'',azure_speech_region:'',
  google_api_key:'',amharicai_tts_url:'',amharicai_tts_key:'',amharicai_tts_model:'AmharicAI-TTS-LoRA'
})
const message=ref(''),success=ref(false)
async function test(){
  if(!form.provider){message.value='Select a provider first.';success.value=false;return}
  try{await $fetch('/api/admin/tts-test',{method:'POST',body:{provider:form.provider}});message.value='Speech connection test succeeded.';success.value=true}
  catch(e){message.value='Speech test failed. Check backend configuration.';success.value=false}
}
async function save(){
  try{await $fetch('/api/admin/tts-secrets',{method:'POST',body:form});message.value='Configuration saved securely on the backend.';success.value=true}
  catch(e){message.value='Could not save configuration.';success.value=false}
}
</script>

<style scoped>
label{display:block;font-weight:700;margin:17px 0 7px}input,select{width:100%;padding:12px;border:1px solid #ccd9d4;border-radius:9px;font:inherit;box-sizing:border-box}.check{font-weight:500}.check input{width:auto}.actions{display:flex;gap:9px;margin-top:22px;flex-wrap:wrap}button{padding:11px 15px;border:0;border-radius:9px;font-weight:800;cursor:pointer}.primary{background:#16805a;color:#fff}.secondary{background:#edf3f0}.ok{padding:10px;background:#eaf7f0;color:#087443}.err{padding:10px;background:#fff1f0;color:#b42318}
</style>