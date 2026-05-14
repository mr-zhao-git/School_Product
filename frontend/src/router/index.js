import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Category from '../views/Category.vue'
import Recommend from '../views/Recommend.vue'
import Profile from '../views/Profile.vue'
import Admin from '../views/Admin.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/category', component: Category },
    { path: '/recommend', component: Recommend },
    { path: '/profile', component: Profile },
    { path: '/admin', component: Admin },
  ]
})
