import { createApp } from 'vue'
import { Quasar } from 'quasar'
import quasarLang from 'quasar/lang/fr'
import App from './App.vue'
import { router } from './router.js'

const app = createApp(App)
app.use(Quasar, {
    config: {
        plugins: {},
        lang: quasarLang
    }
})

// mconsole.log(quasarLang)
// TODO - FIND WHY LANGUAGE PACK IMPORT WITH VITE IS NOT WORKING, LINE BELOW IS A WORKAROUND
Quasar.lang.set(quasarLang)

app.use(router)
app.mount('#q-app')