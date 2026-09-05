<template>
  <div class="app-shell">
    <header class="topbar">
      <NuxtLink to="/" class="brand">🌍 <span>AmharicAI</span></NuxtLink>
      <nav>
        <NuxtLink to="/">Learn</NuxtLink>
        <NuxtLink to="/tutor">AI Tutor</NuxtLink>
        <NuxtLink to="/settings/secrets">Speech Settings</NuxtLink>
      </nav>
    </header>
    <main><NuxtPage /></main>
  </div>
</template>

<style>
*{box-sizing:border-box}
body{margin:0;background:#f4f8f6;color:#17211d;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:inherit;text-decoration:none}
.topbar{height:68px;padding:0 5%;display:flex;align-items:center;justify-content:space-between;background:#0f6044;color:#fff}
.brand{font-size:20px;font-weight:800}
nav{display:flex;gap:20px;font-size:14px}
main{min-height:calc(100vh - 68px)}
.page{max-width:1100px;margin:auto;padding:42px 20px}
</style>