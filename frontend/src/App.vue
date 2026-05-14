<template>
  <div class='container'>
    <h1>🎬 电影个性化推荐系统</h1>
    <nav>
      <router-link to='/'>首页</router-link> |
      <router-link to='/category'>分类</router-link> |
      <router-link to='/recommend'>推荐</router-link> |
      <router-link to='/profile'>个人中心</router-link> |
      <router-link to='/admin'>管理端</router-link>
    </nav>
    <router-view />
  </div>
</template>
<style>
body { font-family: Arial; background: #f3f6fa; }
.container { max-width: 1000px; margin: auto; background: white; padding: 20px; border-radius: 12px; }
.card { border: 1px solid #ddd; border-radius: 8px; padding: 10px; margin: 10px 0; }
button { background: #409eff; color: white; border: 0; padding: 6px 10px; border-radius: 5px; }
</style>
