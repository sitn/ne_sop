<template>
    <!-- HEADER -->
    <q-layout view="hHh LpR fFf" class="shadow-2">
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

                <q-btn size="lg" flat @click="drawer = !drawer" round dense icon="menu" />

                <q-toolbar-title class="">
                    <a href="https://www.ne.ch/autorites/DDTE/" target="_blank"><img src="/img/ne_logo_white.svg"
                            alt="Neuchâtel" /></a>
                </q-toolbar-title>

                <div class="text-center text-body1">DDTE - Suivi des objets parlementaires</div>

                <q-space></q-space>

                <q-btn-dropdown size="lg" label="" dense icon="account_circle" dropdown-icon="" unelevated>
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

                        <q-item clickable v-close-popup @click="">
                            <q-item-section>
                                <q-item-label>Déconnexion</q-item-label>
                            </q-item-section>
                        </q-item>
                    </q-list>
                </q-btn-dropdown>

                <!-- <q-btn size="lg" flat @click="" round dense icon="account_circle" /> -->

            </q-toolbar>

        </q-header>

        <q-drawer v-model="drawer" show-if-above :mini="miniState" @mouseover="miniState = false"
            @mouseout="miniState = true" mini-to-overlay :mini-width=70 :width="300" :breakpoint="500"
            :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'">
            <q-scroll-area class="fit" :horizontal-thumb-style="{ opacity: 0 }">
                <q-list padding>
                    <q-item clickable v-ripple active-class="bg-indigo-2 text-orange" to="/items">
                        <!-- active -->
                        <q-item-section avatar>
                            <q-icon name="sym_o_list_alt" size="lg" />
                        </q-item-section>

                        <q-item-section>
                            Objets parlementaires
                        </q-item-section>
                    </q-item>

                    <q-item clickable v-ripple to="/persons">
                        <q-item-section avatar>
                            <q-icon name="sym_o_groups" size="lg" color="grey-7" />
                        </q-item-section>

                        <q-item-section>
                            Personnes et groupes
                        </q-item-section>
                    </q-item>

                    <q-item clickable v-ripple to="/events">
                        <q-item-section avatar>
                            <q-icon name="sym_o_schedule" size="lg" color="grey-7" class="custom-font" />
                        </q-item-section>

                        <q-item-section>
                            Calendrier
                        </q-item-section>
                    </q-item>

                    <!-- <q-separator /> -->

                    <q-item clickable v-ripple to="/statistics">
                        <q-item-section avatar>
                            <q-icon name="sym_o_bar_chart" size="lg" color="grey-7" />
                        </q-item-section>

                        <q-item-section>
                            Statistiques
                        </q-item-section>
                    </q-item>
                </q-list>
            </q-scroll-area>
        </q-drawer>

        <q-page-container>
            <q-page class="q-pa-md">

                <router-view></router-view>

            </q-page>
        </q-page-container>
    </q-layout>
</template>
  
<script>
/* import objets_parlementaires from './assets/data/objets_parlementaires.json' */
import { ref } from 'vue'
import items from './assets/data/items.json'

console.log(items)

export default {
    name: 'App',
    components: {
    },
    setup() {
        return {
            drawer: ref(false),
            miniState: ref(true)
        }
    },
    data() {
        return {
        }
    },
    mounted() {

    },
    computed: {

    },
    watch: {

    },
    methods: {


    }

}
</script>
  
<style>
@import './assets/styles/main.css';
@import './assets/styles/quasar.prod.css';

/*
.material-symbols-outlined {
    font-variation-settings:
        'FILL' 1,
        'wght' 400,
        'GRAD' 0,
        'opsz' 24 !important
}
*/
</style>