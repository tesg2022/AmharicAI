<template>
  <div class="page">
    <section class="hero">
      <div>
        <p class="eyebrow">READ • WRITE • SPEAK • LISTEN</p>
        <h1>Learn Amharic with <span>AmharicAI</span></h1>
        <p>Fidel, pronunciation, vocabulary, grammar, conversations and AI-powered speech practice.</p>
        <NuxtLink class="button" to="/lessons/1">Start Lesson</NuxtLink>
      </div>
      <div class="fidel">ሀ ሁ ሂ<br>ለ ሉ ሊ<br>ሰ ሱ ሲ</div>
    </section>

    <h2>Learning Units</h2>
    <div class="cards">
      <NuxtLink v-for="u in units" :key="u.id" :to="`/lessons/${u.id}`" class="card">
        <small>UNIT {{ u.id }}</small><h3>{{ u.amharic }}</h3><p>{{ u.title }}</p>
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
const units = [
  {id:1,amharic:'ፊደል',title:'Fidel & Pronunciation'},
  {id:2,amharic:'ሰላምታ',title:'Greetings'},
  {id:3,amharic:'ራስን ማስተዋወቅ',title:'Introducing Yourself'},
  {id:4,amharic:'ሌሎችን ማስተዋወቅ',title:'Introducing Others'},
  {id:5,amharic:'ግሶች',title:'Amharic Verbs'},
  {id:6,amharic:'መግዛት',title:'Shopping'},
  {id:7,amharic:'ምግብ እና መጠጥ',title:'Food & Drink'},
  {id:8,amharic:'ሰዓት',title:'Time'},
  {id:9,amharic:'ታሪክ መናገር',title:'Story'},
  {id:10,amharic:'መንገድ መጠየቅ',title:'Directions'}
]
</script>

<style scoped>
.hero{display:grid;grid-template-columns:1.4fr .6fr;gap:30px;padding:45px;border-radius:24px;background:linear-gradient(135deg,#0f6044,#16805a);color:#fff}
.eyebrow{letter-spacing:.12em;font-size:12px;font-weight:800}
h1{font-size:clamp(34px,5vw,58px);margin:12px 0}.hero p{font-size:18px;line-height:1.6}
h1 span{color:#b9f0d2}.button{display:inline-block;margin-top:12px;padding:12px 18px;border-radius:10px;background:#fff;color:#0f6044;font-weight:800}
.fidel{font-size:42px;line-height:1.7;text-align:center;align-self:center}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.card{background:#fff;border:1px solid #dce5e1;border-radius:15px;padding:18px}.card small{color:#16805a;font-weight:800}.card h3{margin:9px 0}.card p{color:#68756f}
@media(max-width:760px){.hero{grid-template-columns:1fr}.cards{grid-template-columns:1fr 1fr}.fidel{display:none}}
</style>