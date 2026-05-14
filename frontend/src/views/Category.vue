<script setup>
import { ref } from 'vue'
import axios from 'axios'
const category = ref('科幻'); const list = ref([])
const load = async()=> list.value = (await axios.get('http://localhost:8000/api/category/', {params:{category:category.value}})).data
load()
</script>
<template><h2>分类</h2><input v-model='category'/><button @click='load'>筛选</button><div class='card' v-for='m in list' :key='m.id'>{{m.title}} - {{m.category}}</div></template>
