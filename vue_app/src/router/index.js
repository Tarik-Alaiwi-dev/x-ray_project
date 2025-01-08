import { createRouter, createWebHistory } from 'vue-router';
import store from '../store'; // ✅ Import Vuex store
import HomeView from '../views/HomeView.vue';
import PatientView from '../views/PatientView.vue';
import TechnicianView from '../views/TechnicianView.vue';
import LoginView from '../views/LoginView.vue';
import ChoosePatient from '../views/ChoosePatient.vue';
import ChooseDate from '../views/ChooseDate.vue';
import DoctorView from '../views/DoctorView.vue';

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { requiresAuth: true } // ✅ Protected
  },
  {
    path: '/patient',
    name: 'patient',
    component: PatientView,
    meta: { requiresAuth: true } // ✅ Protected
  },
  {
    path: '/technician',
    name: 'technician',
    component: TechnicianView,
    meta: { requiresAuth: true } // ✅ Protected
  },
  {
    path: '/doctor',
    name: 'doctor',
    component: DoctorView,
    meta: { requiresAuth: true } // ✅ Protected
  },
  {
    path: '/choose-patient',
    name: 'choose-patient',
    component: ChoosePatient,
    meta: { requiresAuth: true } // ✅ Protected
  },
  {
    path: '/choose-date',
    name: 'choose-date',
    component: ChooseDate,
    meta: { requiresAuth: true } // ✅ Protected
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue'),
    meta: { requiresAuth: true } // ✅ Protected
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// ✅ Add a global navigation guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = store.state.isAuthenticated;

  if (!isAuthenticated && to.path !== '/login') {
    next('/login');  // 🔴 Redirect to login if NOT logged in
  } else if (isAuthenticated && to.path === '/login') {
    next('/');  // 🔵 Redirect to home if ALREADY logged in
  } else {
    next(); // ✅ Allow navigation
  }
});

export default router;
