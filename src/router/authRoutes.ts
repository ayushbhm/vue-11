// src/router/authRoutes.ts
import type { RouteRecordRaw } from 'vue-router'; 
import Auth from '../views/auth/auth.vue'; 
import CustomerRegister from '../views/auth/customer_register.vue'; 
import AuthLayout from '../layouts/AuthLayout.vue'; 
import professional_register from '../views/auth/professional_register.vue'
const authRoutes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'Login',
    component: Auth,
  },
  {
    path: '/register',
    name: 'CustomerRegister',
    component: CustomerRegister, 
    meta: { layout: AuthLayout },
  },
  {
    path:'/professional_register',
    name: 'professional_register',
    component: professional_register
  }
];

export default authRoutes;