<template>
  <button
    :class="['custom-button', type, { disabled }]"
    :disabled="disabled"
    @click="handleClick"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  type: { type: String, default: 'primary' }, // 'primary', 'secondary', 'danger'
  disabled: { type: Boolean, default: false },
});

const emit = defineEmits(['click']);

const handleClick = (event: MouseEvent) => {
  if (!props.disabled) {
    emit('click', event);
  }
};
</script>

<style scoped>
.custom-button {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border: 1px solid transparent;
}

.custom-button.primary {
  background-color: #126b55;
  color: #fff;
}

.custom-button.primary:hover:not(:disabled) {
  background-color: #0d3d32;
}

.custom-button.secondary {
  background-color: #fff;
  color: #16352e;
  border-color: #dbe7e1;
}

.custom-button.secondary:hover:not(:disabled) {
  background-color: #f5f5f5;
}

.custom-button.danger {
  background-color: #dc3545;
  color: #fff;
}

.custom-button.danger:hover:not(:disabled) {
  background-color: #c82333;
}

.custom-button.disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
