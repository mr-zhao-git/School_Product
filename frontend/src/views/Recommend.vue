<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
const rec = ref([]); const hot = ref([]); const userId = 1
onMounted(async()=>{rec.value=(await axios.get('http://localhost:8000/api/recommend/',{params:{user_id:userId}})).data;hot.value=(await axios.get('http://localhost:8000/api/hot/')).data})
</script>
<template><h2>推荐</h2><h3>个性化推荐</h3><div class='card' v-for='m in rec' :key='m.id'>{{m.title}}</div><h3>热门榜单</h3><div class='card' v-for='m in hot' :key='m.id'>{{m.title}}🔥{{m.hot_index}}</div></template>
