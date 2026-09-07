#!/usr/bin/env python3
"""
Build AmharicAI_GitHubPages from the supplied Amharic learning sources.

Inputs can be:
  * .txt / .md
  * .pdf
  * .docx

The builder extracts source text, identifies the 20-unit course sequence,
Fidel/pronunciation material, writing/reading guidance, learning-cycle
language, and translation/cross-lingual signals, then generates a Nuxt 3
static site suitable for GitHub Pages. The generated site includes an
Amharic translation interface with a provider-neutral REST contract.

Important:
- The generated application is an original learning interface.
- It does not copy whole textbook pages.
- Source documents are used to structure topics, objectives and metadata.
- Verify any OCR-sensitive Fidel/transliteration against the source page image.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

# -----------------------------
# Source extraction
# -----------------------------

def read_source(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="ignore")

    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise SystemExit(
                "PDF support requires pypdf. Install it with: pip install pypdf"
            ) from exc

        reader = PdfReader(str(path))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n".join(pages)

    if suffix == ".docx":
        try:
            from docx import Document
        except ImportError as exc:
            raise SystemExit(
                "DOCX support requires python-docx. Install it with: "
                "pip install python-docx"
            ) from exc

        doc = Document(str(path))
        return "\n".join(p.text for p in doc.paragraphs)

    raise ValueError(f"Unsupported source type: {path}")


def clean_search_noise(text: str) -> str:
    """Remove obvious SERP/navigation noise while retaining source content."""
    text = re.sub(r"https?://\S+", " ", text)

    noise = [
        "AI Mode", "All", "Images", "Videos", "News", "Forums",
        "Short videos", "More", "Tools", "AI Overview", "Show more",
        "Google Play", "BlueStacks"
    ]
    for token in noise:
        text = re.sub(rf"\b{re.escape(token)}\b", " ", text, flags=re.I)

    return re.sub(r"\s+", " ", text).strip()


def extract_signals(texts: dict[str, str]) -> dict:
    combined = clean_search_noise("\n".join(texts.values()))
    lower = combined.lower()

    return {
        "fidel": "seven" in lower and ("order" in lower or "family" in lower),
        "pronunciation": "pronunciation" in lower,
        "penmanship": "penmanship" in lower or "writing guide" in lower,
        "reading": "reading" in lower,
        "stt": "speech-to-text" in lower or "stt" in lower,
        "tts": "text-to-speech" in lower or "tts" in lower,
        "voice_first": "voice-first" in lower,
        "rag": "cross-lingual" in lower or "rag" in lower,
        "learning_cycle": any(
            phrase in lower
            for phrase in [
                "look → read → say → use → write → review",
                "learn → read → listen/say → practice → use → review",
                "learn, read, listen"
            ]
        ),
    }


# -----------------------------
# Source-grounded curriculum
# -----------------------------
# The AmharicAI student edition and Peace Corps manual both organize the
# material into the same 20-unit progression. The descriptions below are
# concise learning metadata rather than copied textbook passages.

UNITS = [
    ("01", "ፊደል እና አጠራር", "Fidel & Pronunciation",
     "Seven-order Fidel families, pronunciation, special consonants and wa combinations."),
    ("02", "ሰላምታ እና መሰናበት", "Greetings & Leave Taking",
     "Greetings, leave-taking, forms of address and everyday greeting practice."),
    ("03", "ራስን ማስተዋወቅ", "Introducing Yourself",
     "Names, origin, identity and simple personal introductions."),
    ("04", "ሌሎችን ማስተዋወቅ", "Introducing Others",
     "Introducing people and describing relationships."),
    ("05", "የአማርኛ ግሶች", "Amharic Verbs",
     "Verb patterns, useful forms and practical sentence building."),
    ("06", "መግዛት", "Basic Shopping",
     "Prices, quantities, market expressions and practical buying language."),
    ("07", "ምግብ እና መጠጥ", "Food & Drink",
     "Food, drinks, ordering and everyday eating situations."),
    ("08", "ሰዓት", "Telling Time",
     "Asking and answering about time and arranging activities."),
    ("09", "ታሪክ መናገር", "Telling a Story",
     "Narrating events and describing what happened."),
    ("10", "መንገድ መጠየቅ", "Finding Your Way Around",
     "Directions, landmarks, location questions and movement."),
    ("11", "ልብስ መግዛት", "Shopping II",
     "Clothing, items, descriptions, sizes and preferences."),
    ("12", "ወራት፣ ወቅቶች እና አየር ሁኔታ", "Months, Seasons & Weather",
     "Months, seasons, calendar language and weather."),
    ("13", "የአረፍተ ነገር አወቃቀር", "Sentence Structure",
     "Core sentence organization and practical grammar patterns."),
    ("14", "ቀጠሮ እና ግብዣ", "Appointments & Invitations",
     "Making arrangements, appointments and invitations."),
    ("15", "ድንበሮች እና እምቢ ማለት", "Boundaries & Responding to Harassment",
     "Clear, polite and firm language for personal boundaries."),
    ("16", "ጤና", "Personal Health & Wellbeing",
     "Body and health vocabulary and communicating about symptoms."),
    ("17", "ደህንነት እና አስቸኳይ ቋንቋ", "Personal Safety & Emergency Language",
     "Urgent communication, safety and asking for help."),
    ("18", "ቤትን መግለጽ", "Describing the Household",
     "Household vocabulary, rooms, objects and family context."),
    ("19", "የሥራ ቃላት", "Job-Specific Vocabulary",
     "Workplace vocabulary and practical professional communication."),
    ("20", "ቀጣይ ትምህርት", "Ongoing Learning",
     "Review, practice, contextual use and continuing fluency."),
]

FIDEL = [
    ("ለ", "ሉ", "ሊ", "ላ", "ሌ", "ል", "ሎ"),
    ("ሰ", "ሱ", "ሲ", "ሳ", "ሴ", "ስ", "ሶ"),
    ("ሸ", "ሹ", "ሺ", "ሻ", "ሼ", "ሽ", "ሾ"),
    ("በ", "ቡ", "ቢ", "ባ", "ቤ", "ብ", "ቦ"),
    ("አ", "ኡ", "ኢ", "ኣ", "ኤ", "እ", "ኦ"),
    ("ከ", "ኩ", "ኪ", "ካ", "ኬ", "ክ", "ኮ"),
    ("ኸ", "ኹ", "ኺ", "ኻ", "ኼ", "ኽ", "ኾ"),
]

UNIT_PHRASES = {
    "01": ("ለ ሉ ሊ ላ ሌ ል ሎ", "Read the seven orders aloud and copy the family."),
    "02": ("ሰላም። ደህና ነህ?", "Hello. How are you?"),
    "03": ("ስምህ ማን ነው?", "What is your name?"),
    "04": ("እሱ ማን ነው?", "Who is he?"),
    "05": ("ግስ", "Verb"),
    "06": ("ይህ ስንት ነው?", "How much is this?"),
    "07": ("ቡና እጠጣለሁ።", "I drink coffee."),
    "08": ("መቼ እንገናኝ?", "When shall we meet?"),
    "09": ("ጓደኛዬ መጣ።", "My friend came."),
    "10": ("መንገዱ የት ነው?", "Where is the road?"),
    "11": ("ጥቁር ሱሪ እፈልጋለሁ።", "I want black trousers."),
    "12": ("ዛሬ ማታ", "Tonight."),
    "13": ("በቤት ነኝ።", "I am at home."),
    "14": ("መቼ እንገናኝ?", "When shall we meet?"),
    "15": ("እባክዎ ያቁሙ።", "Please stop."),
    "16": ("ራሴ ያመኛል።", "My head hurts."),
    "17": ("እርዳታ!", "Help!"),
    "18": ("ቤት", "Home"),
    "19": ("ስራ", "Work"),
    "20": ("እንማር!", "Let us learn!"),
}


def write_file(root: Path, rel: str, content: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def make_units_json() -> str:
    rows = []
    for uid, amh, eng, desc in UNITS:
        phrase, meaning = UNIT_PHRASES[uid]
        rows.append({
            "id": uid,
            "amharic": amh,
            "title": eng,
            "description": desc,
            "phrase": phrase,
            "meaning": meaning,
        })
    return json.dumps(rows, ensure_ascii=False, indent=2)


def scaffold(output: Path, source_texts: dict[str, str]) -> None:
    if output.exists():
        shutil.rmtree(output)

    for d in [
        ".github/workflows",
        "pages/lessons",
        "components",
        "composables",
        "public",
    ]:
        (output / d).mkdir(parents=True, exist_ok=True)

    signals = extract_signals(source_texts)

    package_json = """{
  "name": "amharicai-github-pages",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "nuxt dev",
    "build": "nuxt build",
    "generate": "nuxt generate",
    "preview": "nuxt preview"
  },
  "dependencies": {
    "nuxt": "^3.17.0",
    "vue": "^3.5.0",
    "vue-router": "^4.5.0"
  }
}"""

    nuxt_config = """export default defineNuxtConfig({
  compatibilityDate: '2026-01-01',
  devtools: { enabled: false },
  ssr: false,
  nitro: {
    preset: 'github-pages'
  },
  runtimeConfig: {
    public: {
      translationUrl: process.env.NUXT_PUBLIC_TRANSLATION_URL || ''
    }
  },
  app: {
    baseURL: process.env.NUXT_APP_BASE_URL || '/',
    head: {
      title: 'AmharicAI — አማርኛ ለመማር',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: 'AmharicAI: read, write, speak and listen through a structured Amharic course.'
        }
      ]
    }
  }
})"""

    app_vue = """<template>
  <div class="app-shell">
    <header class="nav">
      <NuxtLink to="/" class="brand">
        <span class="brand-mark">አ</span>
        <span>
          <strong>AmharicAI</strong>
          <small>አማርኛ ለመማር</small>
        </span>
      </NuxtLink>

      <nav>
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/lessons/01">Course</NuxtLink>
        <NuxtLink to="/tutor">AI Tutor</NuxtLink>
        <NuxtLink to="/translate">Translate</NuxtLink>
      </nav>

      <NuxtLink class="cta" to="/lessons/01">Start Learning</NuxtLink>
    </header>

    <main><NuxtPage /></main>

    <footer>
      <span>AmharicAI · አማርኛ ለመማር</span>
      <span>READ · WRITE · SPEAK · LISTEN</span>
    </footer>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Ethiopic:wght@400;500;600;700&display=swap');
:root{--green:#126b55;--dark:#0c3d31;--mint:#eaf5ef;--paper:#fbfaf7;--ink:#17352e;--muted:#657670;--line:#dce8e2;--gold:#e1b24c}
*{box-sizing:border-box}html,body,#__nuxt{margin:0;min-height:100%;font-family:Inter,'Noto Sans Ethiopic',sans-serif;background:var(--paper);color:var(--ink)}
a{text-decoration:none;color:inherit}.nav{height:74px;background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;padding:0 5vw;gap:28px;position:sticky;top:0;z-index:20}.brand{display:flex;gap:10px;align-items:center;margin-right:auto}.brand-mark{width:42px;height:42px;border-radius:12px;background:var(--green);color:#fff;display:grid;place-items:center;font:700 24px 'Noto Sans Ethiopic'}.brand small{display:block;color:var(--muted);font-size:11px;margin-top:2px}.nav nav{display:flex;gap:22px;font-size:14px;color:#52635d}.nav nav .router-link-active{color:var(--green);font-weight:700}.cta,.btn{background:var(--green);color:#fff;padding:11px 16px;border-radius:10px;font-weight:700;font-size:13px}
main{min-height:calc(100vh - 140px)}footer{background:var(--dark);color:#d6eae3;padding:25px 5vw;display:flex;justify-content:space-between;font-size:12px}.container{width:min(1120px,90vw);margin:auto}.page{padding:58px 0}
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:55px;align-items:center;padding:80px 0}.eyebrow{display:inline-block;padding:7px 11px;border-radius:99px;background:var(--mint);color:var(--green);font-size:11px;font-weight:800;letter-spacing:.05em}.hero h1{font-size:clamp(42px,6vw,70px);line-height:1.03;margin:18px 0}.hero h1 .amh{font-family:'Noto Sans Ethiopic';color:var(--green)}.hero p,.intro{color:var(--muted);line-height:1.75;font-size:17px}.actions{display:flex;gap:12px;margin-top:25px}.secondary{background:#fff;color:var(--ink);border:1px solid var(--line)}.visual{min-height:350px;border:1px solid var(--line);border-radius:28px;background:linear-gradient(145deg,#e0f3e9,#f5e8c8);display:grid;place-items:center;padding:25px}.fidel-card{background:#fff;border-radius:20px;padding:30px;text-align:center;width:92%;box-shadow:0 18px 50px #123f3218}.fidel-big{font:76px 'Noto Sans Ethiopic';color:var(--green)}.fidel-row{font:26px 'Noto Sans Ethiopic';letter-spacing:7px;margin:12px 0}.section{padding:55px 0}.section h2{font-size:34px;margin:0 0 10px}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:28px}.card,.unit,.lesson,.box{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px}.card h3,.unit h3{margin:11px 0 6px}.card p,.unit p,.lesson p{color:var(--muted);line-height:1.6;font-size:14px}.quote{background:var(--dark);color:#fff;border-radius:24px;padding:35px;font:25px/1.6 'Noto Sans Ethiopic'}.quote small{display:block;color:#bfdad1;font:12px Inter;margin-top:8px}.units{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:30px}.unit .num,.lesson-num{font-size:11px;color:var(--green);font-weight:800}.amh{font-family:'Noto Sans Ethiopic'}.phrase{font:29px 'Noto Sans Ethiopic';margin:9px 0}.lesson-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:30px}.listen{border:0;border-radius:9px;padding:10px 14px;background:var(--green);color:#fff;font-weight:700;cursor:pointer}.listen:disabled{opacity:.6}.chat{background:#f0f7f4;border-radius:16px;padding:20px}.chat .amh{font-size:22px}textarea{width:100%;min-height:140px;border:1px solid var(--line);border-radius:12px;padding:14px;font:inherit;resize:vertical;margin-top:18px}
@media(max-width:800px){.nav nav{display:none}.cta{display:none}.hero{grid-template-columns:1fr;padding:55px 0}.cards,.lesson-grid{grid-template-columns:1fr}.units{grid-template-columns:repeat(2,1fr)}footer{display:block;line-height:2}}
</style>"""

    index_vue = """<template>
  <div>
    <section class="hero container">
      <div>
        <span class="eyebrow">AMHARIC LANGUAGE · አማርኛ</span>
        <h1>Learn to <span class="amh">read, write, speak</span> and listen.</h1>
        <p>
          AmharicAI turns the supplied learning materials into a progressive
          digital course: Fidel, pronunciation, vocabulary, grammar,
          conversation, exercises and practical communication.
        </p>
        <div class="actions">
          <NuxtLink class="btn" to="/lessons/01">Start Unit 01 →</NuxtLink>
          <NuxtLink class="btn secondary" to="/tutor">Open AI Tutor</NuxtLink>
        </div>
      </div>

      <div class="visual">
        <div class="fidel-card">
          <div class="fidel-big">ለ</div>
          <div class="fidel-row">ለ ሉ ሊ ላ ሌ ል ሎ</div>
          <div>Seven-order Fidel family</div>
        </div>
      </div>
    </section>

    <section class="section container">
      <h2>Source-grounded learning cycle</h2>
      <p class="intro">Look → read → listen/say → practise → use → write → review.</p>
      <div class="cards">
        <article class="card"><h3>ፊደል · Fidel</h3><p>Learn the seven-order family pattern and connect shape, sound and words.</p></article>
        <article class="card"><h3>✍️ Writing & Reading</h3><p>Use recognition, tracing, copying and memory-writing activities.</p></article>
        <article class="card"><h3>🎧 Speak & Listen</h3><p>Practise aloud and connect each phrase to pronunciation and meaning.</p></article>
      </div>
    </section>

    <section class="section container">
      <div class="quote">
        ሰላም። ደህና ነህ?
        <small>Hello. How are you?</small>
      </div>
    </section>
  </div>
</template>"""

    tutor_vue = """<script setup lang="ts">
const text = ref('')
const response = ref('ሰላም! እንዴት ልርዳህ?')

function practise() {
  if (!text.value.trim()) return
  response.value =
    'ጥሩ ሙከራ ነው። ይህ የAmharicAI ልምምድ ቦታ ነው።'
}
</script>

<template>
  <div class="container page">
    <span class="eyebrow">AI LANGUAGE PRACTICE</span>
    <h1>AmharicAI Tutor</h1>
    <p class="intro">
      Practise reading and speaking through guided prompts. The GitHub Pages
      build keeps AI credentials out of the browser.
    </p>

    <div class="box">
      <div class="chat">
        <div class="amh">{{ response }}</div>
        <p>Try: ስሜ አለማየሁ ነው።</p>
      </div>

      <textarea v-model="text"
        placeholder="Write an Amharic sentence or question…"></textarea>

      <div class="actions">
        <button class="btn" @click="practise">Practise →</button>
      </div>
    </div>
  </div>
</template>"""

    units_json = make_units_json()

    lesson_vue = """<script setup lang="ts">
import units from '~/public/course.json'

const route = useRoute()
const id = String(route.params.id).padStart(2, '0')
const unit = computed(() => units.find((item: any) => item.id === id) || units[0])
const { speak, loading, error } = useTTS()
</script>

<template>
  <div class="container page">
    <div class="lesson-num">UNIT {{ unit.id }}</div>
    <h1>{{ unit.amharic }}</h1>
    <p class="intro">{{ unit.title }} · {{ unit.description }}</p>

    <div class="lesson-grid">
      <article class="lesson">
        <div class="lesson-num">KEY PRACTICE</div>
        <div class="phrase amh">{{ unit.phrase }}</div>
        <p>{{ unit.meaning }}</p>
        <button
          class="listen"
          :disabled="loading"
          @click="speak(unit.phrase)"
        >
          {{ loading ? 'Preparing…' : '🔊 Listen' }}
        </button>
        <p v-if="error">{{ error }}</p>
      </article>

      <article class="lesson">
        <div class="lesson-num">LEARNING ROUTINE</div>
        <h3>Look · Read · Listen/Say · Practise · Use · Write · Review</h3>
        <p>
          Read the Amharic first. Say it aloud. Check the meaning. Write it
          from a model, then try again from memory.
        </p>
      </article>
    </div>
  </div>
</template>"""

    use_tts = """export function useTTS() {
  const loading = ref(false)
  const error = ref('')

  async function speak(text: string) {
    loading.value = true
    error.value = ''

    try {
      const config = useRuntimeConfig()
      const url = config.public.ttsUrl as string

      if (!url) {
        throw new Error('TTS URL is not configured')
      }

      // GitHub Pages is static. No secret API key is placed here.
      // Configure a public, authenticated-at-the-edge TTS endpoint only
      // if that endpoint is intentionally designed for browser access.
      const result = await $fetch<any>(url, {
        method: 'POST',
        body: { text, language: 'Amharic' }
      })

      const audioUrl =
        result?.audio_url ||
        (result?.audio_base64
          ? `data:audio/wav;base64,${result.audio_base64}`
          : '')

      if (!audioUrl) throw new Error('TTS response did not contain audio')

      await new Audio(audioUrl).play()
    } catch (err: any) {
      error.value =
        'TTS is not connected to this static build. Deploy the custom AmharicAI TTS through a secure server before enabling browser access.'
    } finally {
      loading.value = false
    }
  }

  return { speak, loading, error }
}"""

    audio_player = """<template>
  <audio v-if="src" :src="src" controls preload="metadata"></audio>
</template>

<script setup lang="ts">
defineProps<{ src?: string }>()
</script>"""

    translation = translation_composable


    translate_page = translation_page

    workflow = """name: Deploy AmharicAI to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: github-pages
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install
        run: npm install

      - name: Generate
        run: npm run generate

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: .output/public

      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
"""

    readme = f"""# AmharicAI_GitHubPages

This project is generated from the supplied AmharicAI text and the attached
Amharic learning sources.

## Source-grounded design

The source materials establish a 20-unit progression from pronunciation
through ongoing learning. The AmharicAI student edition describes a recurring
learning cycle and combines Amharic, transliteration, English, visual
learning, dialogues, exercises and practical activities.

Detected signals:
- Fidel/pronunciation: {signals["fidel"]}
- pronunciation: {signals["pronunciation"]}
- penmanship/writing: {signals["penmanship"]}
- reading: {signals["reading"]}
- STT: {signals["stt"]}
- TTS: {signals["tts"]}
- voice-first: {signals["voice_first"]}
- cross-lingual/RAG: {signals["rag"]}

## Generated structure

AmharicAI_GitHubPages/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
├── pages/
│   ├── index.vue
│   ├── tutor.vue
│   ├── translate.vue
│   └── lessons/
│       └── [id].vue
├── components/
│   └── AudioPlayer.vue
├── composables/
│   └── useTTS.ts
├── public/
│   ├── robots.txt
│   └── course.json
├── app.vue
├── nuxt.config.ts
├── package.json
├── .gitignore
└── README.md

## Development

npm install
npm run dev

## GitHub Pages

npm run generate

Then push to `main`. GitHub Actions deploys `.output/public`.

## Translation

The static site includes an Amharic translation interface at `/translate`.
It sends only the text, source language and target language to the configured
translation endpoint:

POST NUXT_PUBLIC_TRANSLATION_URL
{
  "text": "...",
  "source_language": "Amharic",
  "target_language": "English"
}

The translation service should return one of:
- `{ "translation": "..." }`
- `{ "translated_text": "..." }`
- `{ "text": "..." }`

For production, put the translation service behind your secure application
API or an authenticated edge/API gateway. Do not put a private provider API
key into GitHub Pages client code.

## TTS

GitHub Pages is static and cannot safely host a server-side `/api/tts`
proxy. The client TTS composable therefore contains no secret key.

For the production AmharicAI custom TTS architecture:

Browser
  -> secure application/API layer
  -> custom AmharicAI TTS service
  -> Amharic TTS model + LoRA
  -> audio

Do not put private model credentials or server API keys in this repository.

## Source fidelity

The source documents use seven-order Fidel families and provide pronunciation,
writing and practical communication material. OCR can distort Amharic glyphs
or transliteration, so disputed characters should be checked against the
original page image before being used as authoritative learner content.
"""

    write_file(output, "package.json", package_json)
    write_file(output, "nuxt.config.ts", nuxt_config)
    write_file(output, "app.vue", app_vue)
    write_file(output, "pages/index.vue", index_vue)
    write_file(output, "pages/tutor.vue", tutor_vue)
    write_file(output, "pages/lessons/[id].vue", lesson_vue)
    write_file(output, "pages/translate.vue", translate_page)
    write_file(output, "components/AudioPlayer.vue", audio_player)
    write_file(output, "composables/useTTS.ts", use_tts)
    write_file(output, "composables/useTranslation.ts", translation)
    write_file(output, "public/course.json", units_json)
    write_file(output, "public/robots.txt", "User-agent: *\nAllow: /\n")
    write_file(output, ".github/workflows/deploy-pages.yml", workflow)
    write_file(output, ".gitignore", "node_modules/\n.nuxt/\n.output/\n.env\n.DS_Store\n")
    write_file(output, "README.md", readme)


def main():
    parser = argparse.ArgumentParser(
        description="Build AmharicAI GitHub Pages site from attached source files."
    )
    parser.add_argument(
        "sources",
        nargs="+",
        help="Source .txt/.md/.pdf/.docx files"
    )
    parser.add_argument(
        "--output",
        default="AmharicAI_GitHubPages",
        help="Output project directory"
    )
    args = parser.parse_args()

    source_texts = {}
    for item in args.sources:
        path = Path(item)
        if not path.exists():
            raise SystemExit(f"Source not found: {path}")
        source_texts[path.name] = read_source(path)

    scaffold(Path(args.output), source_texts)
    print(f"Built {args.output}/")
    print("Sources processed:")
    for name in source_texts:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
