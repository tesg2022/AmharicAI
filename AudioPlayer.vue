<template><audio v-if="src" :src="src" controls preload="metadata"></audio></template>
<script setup lang="ts">defineProps<{src:string}>()</script>