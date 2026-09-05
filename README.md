# AmharicAI Nuxt Custom TTS

Nuxt application foundation for the **AmharicAI custom TTS/LoRA backend only**.

## Architecture

```text
AmharicAI Nuxt
      |
      | POST /api/tts
      v
Custom AmharicAI TTS service
      |
      | POST /api/v1/tts
      v
Amharic TTS / LoRA model
      |
      v
audio_url
```

## Server configuration

Set these environment variables:

- `AMHARICAI_TTS_URL`
- `AMHARICAI_TTS_KEY`
- `AMHARICAI_TTS_MODEL`

Example:

```env
AMHARICAI_TTS_URL=https://your-tts-host
AMHARICAI_TTS_KEY=your-server-side-key
AMHARICAI_TTS_MODEL=AmharicAI-TTS-LoRA
```

Do not commit `.env` or expose the key to the browser.

## Backend contract

The Nuxt server sends:

```json
{
  "text": "ሰላም። ደህና ነህ?",
  "model": "AmharicAI-TTS-LoRA"
}
```

to:

```text
POST {AMHARICAI_TTS_URL}/api/v1/tts
```

The custom backend must return at least:

```json
{
  "audio_url": "https://..."
}
```

Additional response fields are passed through to the application.

## Important

This repository does **not** claim that an AmharicAI LoRA adapter has already been trained or deployed. The adapter is the integration point for the validated custom backend.

The secrets endpoint intentionally does not persist credentials. Use deployment environment variables or a production secret manager.

## Run

```bash
npm install
npm run dev
```
