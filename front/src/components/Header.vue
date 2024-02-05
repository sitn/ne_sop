<template>
    <q-header class="bg-blue-grey text-white q-py-sm">

        <!-- 
    <div class="row full-height justify-center items-center" style="padding:0 12px;">

        <div class="col text-left">
            <div class="row items-center"> 
                <q-btn size="lg" flat @click="drawer = !drawer" round dense icon="menu" />
                <a href="https://www.ne.ch/autorites/DDTE/" target="_blank" class="q-px-md"><img src="/img/ne_logo_white.svg"
                        alt="Neuchâtel" /></a>
            </div>
        </div>

        <div class="col text-center text-body1">
            DDTE - Suivi des objets parlementaires
        </div>

        <div class="col text-right">
            <q-btn size="lg" flat @click="" round dense icon="account_circle" />
        </div>

    </div>
    -->

        <q-toolbar>

            <q-btn size="lg" text-color="white" flat @click="store.drawer = !store.drawer" round dense icon="sym_o_menu" />

            <q-toolbar-title class="gt-xs">
                <a href="https://www.ne.ch/autorites/DDTE/" target="_blank"><img src="img/ne_logo_white.svg" alt="Neuchâtel" /></a>
            </q-toolbar-title>

            <div class="text-center text-body1 gt-sm">DDTE - Suivi des objets parlementaires</div>

            <q-space></q-space>

            <div class="text-center text-body1 gt-sm">{{ store.user.username }} <q-icon size="lg" name="account_circle" text-color="white" flat round dense />
            </div>

            <!-- 
        <q-btn size="lg" text-color="white" round label="" dense unelevated icon="sym_o_logout" @click="processLogout" v-if="$route.name !== 'Login'">
            <q-tooltip class="bg-black">Déconnexion</q-tooltip>
        </q-btn>
        -->

            <!-- 
        <q-btn-dropdown size="lg" label="" dense icon="account_circle" dropdown-icon="" unelevated v-if="$route.name !== 'Login'">
            <q-list style="width:180px">
                <q-item clickable v-close-popup @click="">
                    <q-item-section>
                        <q-item-label>Profil</q-item-label>
                    </q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="">
                    <q-item-section>
                        <q-item-label>Réglages</q-item-label>
                    </q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="">
                    <q-item-section>
                        <q-item-label>Aide</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator />

                <q-item clickable v-close-popup @click="processLogout">
                    <q-item-section>
                        <q-item-label>Déconnexion</q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </q-btn-dropdown>
        -->

        </q-toolbar>

    </q-header>
</template>


<script>
import { store } from '../store/store.js'

export default {
    name: 'Header',
    components: {},
    props: {},
    emits: [],
    data() {
        return {
            store,
        }
    },
    beforeCreate() {
    },
    async created() {
    },
    async mounted() {
    },

}
</script>

<style scoped></style>