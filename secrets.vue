<template>
  <div class="page">
    <div class="settings">
      <h1>🔐 Speech & AI Settings</h1>
      <p class="muted">Configure one server-side TTS provider. Real credentials are never displayed after saving.</p>
      <SecretsForm />
    </div>
  </div>
</template>
<script setup lang="ts"></script>
<style scoped>
.settings{max-width:820px;margin:auto;background:#fff;border:1px solid #dce5e1;border-radius:18px;padding:30px}.muted{color:#68756f}
</style>