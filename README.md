# AmharicAI Nuxt Repository

A source-first Nuxt 3 application for Amharic learning and server-side TTS integration.

## Run

```bash
npm install
cp .env.example .env
npm run dev
```

Open http://localhost:3000.

## TTS architecture

The browser calls the Nuxt server. Provider credentials remain server-side.

- `POST /api/tts`
- `GET /api/health`
- `POST /api/admin/tts-test`
- `POST /api/admin/tts-secrets`

Replace the placeholder custom TTS forwarding logic with the exact API contract of the validated AmharicAI TTS backend before production deployment.