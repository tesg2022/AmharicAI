<template>
  <div>
    <header class="site-header">
      <NuxtLink to="/" class="brand">
        <span class="brand-mark">አ</span>
        <span><strong>AmharicAI</strong><small>አማርኛ ለመማር</small></span>
      </NuxtLink>
      <nav>
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/course">Course</NuxtLink>
        <NuxtLink to="/tutor">AI Tutor</NuxtLink>
      </nav>
      <NuxtLink to="/course" class="nav-cta">Start learning</NuxtLink>
    </header>
    <main><NuxtPage /></main>
    <footer>
      <div><strong>AmharicAI</strong> · አማርኛ ለመማር</div>
      <div>READ · WRITE · SPEAK · LISTEN</div>
    </footer>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Ethiopic:wght@400;500;600;700&display=swap');
:root{--ink:#12312a;--muted:#61716c;--green:#16745b;--green2:#0f5c49;--mint:#e8f5ef;--cream:#f8f7f1;--line:#dbe7e1;--gold:#e9b949}
*{box-sizing:border-box} body{margin:0;background:var(--cream);color:var(--ink);font-family:Inter,'Noto Sans Ethiopic',sans-serif}
a{text-decoration:none;color:inherit}.site-header{height:76px;background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;padding:0 5vw;gap:30px;position:sticky;top:0;z-index:10}.brand{display:flex;align-items:center;gap:10px;margin-right:auto}.brand-mark{width:42px;height:42px;border-radius:12px;background:var(--green);color:#fff;display:grid;place-items:center;font-family:'Noto Sans Ethiopic';font-size:24px}.brand strong{display:block;font-size:17px}.brand small{display:block;color:var(--muted);font-family:'Noto Sans Ethiopic';font-size:11px}nav{display:flex;gap:24px;font-size:14px;color:#53645e}nav a.router-link-active{color:var(--green);font-weight:700}.nav-cta{background:var(--green);color:#fff;padding:11px 17px;border-radius:10px;font-size:13px;font-weight:700}main{min-height:calc(100vh - 136px)}footer{padding:28px 5vw;background:#103b31;color:#d9eee7;display:flex;justify-content:space-between;font-size:12px}
.container{width:min(1120px,90vw);margin:auto}.hero{padding:86px 0 70px;display:grid;grid-template-columns:1.15fr .85fr;gap:50px;align-items:center}.eyebrow{display:inline-flex;padding:7px 11px;background:var(--mint);color:var(--green2);border-radius:999px;font-size:12px;font-weight:800;letter-spacing:.04em}.hero h1{font-size:clamp(42px,6vw,72px);line-height:1.02;margin:18px 0}.hero h1 span{font-family:'Noto Sans Ethiopic';color:var(--green)}.hero p{font-size:18px;line-height:1.7;color:var(--muted);max-width:640px}.actions{display:flex;gap:12px;margin-top:28px}.btn{padding:14px 20px;border-radius:11px;font-weight:700;font-size:14px}.primary{background:var(--green);color:#fff}.secondary{background:#fff;border:1px solid var(--line)}.visual{background:linear-gradient(145deg,#dff2e8,#f4ead0);border:1px solid var(--line);border-radius:28px;padding:30px;min-height:330px;display:grid;place-items:center}.fidel-card{background:#fff;border-radius:20px;padding:28px;box-shadow:0 18px 50px #164f3b18;text-align:center;width:90%}.fidel-card .big{font-family:'Noto Sans Ethiopic';font-size:72px;color:var(--green)}.fidel-row{font-family:'Noto Sans Ethiopic';font-size:25px;letter-spacing:10px;color:#29483f;margin-top:12px}.section{padding:70px 0}.section h2{font-size:34px;margin:0 0 10px}.section-intro{color:var(--muted);max-width:680px;line-height:1.7}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px}.card h3{margin:12px 0 7px}.card p{color:var(--muted);line-height:1.6;font-size:14px}.icon{width:42px;height:42px;border-radius:12px;background:var(--mint);display:grid;place-items:center;font-size:20px}.quote{background:#123f34;color:#fff;border-radius:24px;padding:40px;font-family:'Noto Sans Ethiopic';font-size:24px;line-height:1.7}.quote small{display:block;font-family:Inter;color:#bdd7cf;font-size:13px;margin-top:12px}.page-head{padding:60px 0 25px}.page-head h1{font-size:48px;margin:10px 0}.unit-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:25px 0 70px}.unit{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;min-height:150px}.unit .num{color:var(--green);font-weight:800;font-size:12px}.unit h3{margin:9px 0;font-size:16px}.unit p{font-size:12px;color:var(--muted);line-height:1.5}.tutor{padding:65px 0;max-width:850px}.tutor-box{background:#fff;border:1px solid var(--line);border-radius:22px;padding:26px}.chat{background:#f2f7f4;border-radius:16px;padding:20px;margin-bottom:18px}.chat .amh{font-family:'Noto Sans Ethiopic';font-size:22px}.tutor textarea{width:100%;min-height:120px;border:1px solid var(--line);border-radius:12px;padding:15px;font:inherit;resize:vertical}.hint{color:var(--muted);font-size:13px;line-height:1.6}
@media(max-width:800px){.site-header{padding:0 4vw}.site-header nav{display:none}.hero{grid-template-columns:1fr;padding:55px 0}.grid{grid-template-columns:1fr}.unit-grid{grid-template-columns:repeat(2,1fr)}footer{display:block;line-height:2}.visual{min-height:270px}}
</style>
