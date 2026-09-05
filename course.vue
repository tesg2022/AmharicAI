<script setup lang="ts">
const units = [
['01','Fidel & Pronunciation','Read, write and pronounce the Fidel.'],
['02','Greetings','Everyday greetings and responses.'],
['03','Introducing Yourself','Names, origins and simple introductions.'],
['04','Introducing Others','Introduce family, friends and people around you.'],
['05','Amharic Verbs','Build useful verb patterns.'],
['06','Shopping','Prices, bargaining and practical phrases.'],
['07','Food & Drink','Order, describe and talk about food.'],
['08','Time','Ask and answer about time and meetings.'],
['09','Story','Talk about what happened.'],
['10','Directions','Ask for and give directions.'],
['11','Shopping II','Clothing and describing what you want.'],
['12','Months & Weather','Calendar, seasons and weather.'],
['13','Sentence Structure','Understand how Amharic sentences are built.'],
['14','Appointments & Invitations','Arrange meetings and invitations.'],
['15','Boundaries & Safety','Useful language for personal boundaries.'],
['16','Health','Describe symptoms and ask for help.'],
['17','Emergency','Safety and emergency communication.'],
['18','Household','Useful home and daily-life vocabulary.'],
['19','Job Vocabulary','Workplace words and communication.'],
['20','Ongoing Learning','Review, practice and keep progressing.']
]
</script>

<template>
  <div class="container">
    <section class="page-head">
      <span class="eyebrow">20-UNIT COURSE</span>
      <h1>AmharicAI Course</h1>
      <p class="section-intro">A structured path from Fidel and pronunciation to everyday communication, with dialogues, examples and exercises.</p>
    </section>
    <div class="unit-grid">
      <article v-for="u in units" :key="u[0]" class="unit">
        <div class="num">UNIT {{ u[0] }}</div>
        <h3>{{ u[1] }}</h3>
        <p>{{ u[2] }}</p>
      </article>
    </div>
  </div>
</template>
