import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

export const URL_BASE = process.env.APP_BASE_URL ? `${process.env.APP_BASE_URL}/api` : "/api"
createApp(App).mount('#app')
