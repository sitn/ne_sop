import { createApp } from 'vue'
import { Quasar } from 'quasar'
import quasarLang from 'quasar/lang/fr'
import App from './App.vue'
import { router } from './router.js'

/*
import ItemsList from './views/ItemsList.vue'
import EntitiesList from './views/EntitiesList.vue'
import EventsList from './views/EventsList.vue'
import Event from './views/Event.vue'
import NewEvent from './views/NewEvent.vue'
import Statistics from './views/Statistics.vue'
import Item from './views/Item.vue'
import NewItem from './views/NewItem.vue'
import Entity from './views/Entity.vue'
import NewEntity from './views/NewEntity.vue'
import User from './views/User.vue'
import NewUser from './views/NewUser.vue'
import Login from './views/Login.vue'
import Admin from './views/Admin.vue'
import Help from './views/Help.vue'
*/

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