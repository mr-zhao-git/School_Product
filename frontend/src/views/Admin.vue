<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import axios from 'axios'
const stats = ref({watch:[],search:[],good:0,bad:0})
onMounted(async()=>{
 stats.value = (await axios.get('http://localhost:8000/api/dashboard/')).data
 const chart1 = echarts.init(document.getElementById('watchChart'))
 chart1.setOption({series:[{type:'pie', data: stats.value.watch.map(i=>({name:i.user__username,value:i.total}))}]})
 const chart2 = echarts.init(document.getElementById('searchChart'))
 chart2.setOption({series:[{type:'pie', data: stats.value.search.map(i=>({name:i.category,value:i.total}))}]})
})
</script>
<template>
<h2>管理端</h2>
<div class='card'>评论统计：好评 {{stats.good}} / 差评 {{stats.bad}}</div>
<div id='watchChart' style='height:300px' class='card'></div>
<div id='searchChart' style='height:300px' class='card'></div>
<div class='card'>电影管理：上架/下架/基础信息查看（通过 Movie 表）</div>
<div class='card'>用户管理：增删改查（通过 users 接口）</div>
</template>
