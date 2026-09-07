<template>
  <div>
    <header class="navbar">
      <NuxtLink to="/">Home</NuxtLink>
      <NuxtLink to="/lessons/01">Course</NuxtLink>
      <NuxtLink to="/tutor">AI Tutor</NuxtLink>
      <NuxtLink to="/translate">Translate</NuxtLink>
      <NuxtLink to="/pricing">Pricing</NuxtLink>
      <NuxtLink to="/dashboard">Dashboard</NuxtLink>
    </header>
    <main style="padding: 2rem; font-family: sans-serif;"><NuxtPage /></main>
  </div>
</template>
<style> .navbar { display: flex; gap: 1rem; padding: 1rem; background: #f4f4f4; } </style>
