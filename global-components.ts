// plugins/global-components.ts
import Button from '~/components/Button.vue';

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component('Button', Button);
});
