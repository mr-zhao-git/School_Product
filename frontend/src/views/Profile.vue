<script setup>
const userId = 1
const exportData = ()=> window.open(`http://localhost:8000/api/export/?user_id=${userId}`)
</script>
<template><h2>个人中心</h2><div class='card'>观看历史/我的收藏（可接入 ratings/favorites 接口）</div><button @click='exportData'>导出个性化推荐</button></template>
