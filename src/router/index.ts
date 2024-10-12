import { createRouter, createWebHistory } from 'vue-router'
import authRoutes from './authRoutes' // Import auth routes
import HomeView from '../views/HomeView.vue'

const routes = [
  ...authRoutes,
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
   
    component: () => import('../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
