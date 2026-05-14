<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
const movies = ref([])
onMounted(async () => { movies.value = (await axios.get('http://localhost:8000/api/home/')).data })
</script>
<template><h2>首页 · 高分电影</h2><div class='card' v-for='m in movies' :key='m.id'>{{ m.title }}｜{{ m.avg_score }}</div></template>
