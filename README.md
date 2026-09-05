# AmharicAI Website

A GitHub Pages-compatible Nuxt 3 website based on the AmharicAI course structure and the redevelopment decisions.

## Included
- AmharicAI landing page
- 20-unit course overview
- Fidel/pronunciation presentation
- Practical Amharic examples
- AI Tutor interface
- Responsive design
- GitHub Pages deployment workflow

## Important
GitHub Pages is used only for the static website. It cannot execute the secure `/api/tts` Nitro server route. The custom AmharicAI TTS backend should therefore be deployed separately on a Node/GPU-capable service and connected later through a production Nuxt/Nitro deployment.

## Local
npm install
npm run dev

## GitHub Pages
Push to `main`, then enable:
Settings → Pages → Source → GitHub Actions
