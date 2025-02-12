import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { Quasar } from 'quasar'
import 'quasar'

import '@quasar/extras/roboto-font/roboto-font.css'
import '@quasar/extras/material-icons/material-icons.css'
import '@quasar/extras/material-symbols-outlined/material-symbols-outlined.css'
import '@quasar/extras/material-symbols-rounded/material-symbols-rounded.css'
import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'
// import './src/css/quasar-variables.sass'

import './style.css'
import App from './App.vue'
import router from './router'

import { Notify, Loading } from 'quasar'
const pinia = createPinia()
const app = createApp(App)

app.use(Quasar, {
    plugins: { Notify, Loading }, // Add plugins here
    config: {
      brand: {
        primary: '#2a9d8f',
        secondary: '#264653',
        accent: '#e9c46a',
        dark: '#1a1a1a',
      }
    }
  })
app.use(pinia)
app.use(router)

app.mount('#app')
