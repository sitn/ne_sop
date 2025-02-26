<template>
    <q-drawer v-model="store.drawer" show-if-above :mini="miniState" @mouseover="miniState = false" @mouseout="miniState = true" mini-to-overlay :mini-width=70 :width="300" :breakpoint="500" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'">
        <q-scroll-area class="fit" :horizontal-thumb-style="{ opacity: 0 }">
            <q-list padding>
                <q-item clickable v-ripple to="/items" style="color:#757575" active-class="bg-light-blue-1 text-blue-grey-7">
                    <!-- active #dce4eb -->
                    <q-item-section avatar>
                        <q-icon name="sym_o_list_alt" size="lg" />
                    </q-item-section>

                    <q-item-section>
                        Objets parlementaires
                    </q-item-section>
                </q-item>

                <q-item clickable v-ripple to="/documents" style="color:#757575" active-class="bg-light-blue-1 text-blue-grey-7">
                    <!-- active #dce4eb -->
                    <q-item-section avatar>
                        <q-icon name="sym_o_file_present" size="lg" />
                    </q-item-section>

                    <q-item-section>
                        Documents
                    </q-item-section>
                </q-item>

                <q-item clickable v-ripple to="/entities" style="color:#757575" active-class="bg-light-blue-1 text-blue-grey-7">
                    <q-item-section avatar>
                        <q-icon name="sym_o_groups" size="lg" />
                    </q-item-section>

                    <q-item-section>
                        Parlementaires
                    </q-item-section>
                </q-item>

                <q-item clickable v-ripple to="/events" style="color:#757575" active-class="bg-light-blue-1 text-blue-grey-7">
                    <q-item-section avatar>
                        <q-icon name="sym_o_schedule" size="lg" class="material-symbols-outlined" />
                    </q-item-section>

                    <q-item-section>
                        Calendrier
                    </q-item-section>
                </q-item>

                <!-- <q-separator /> -->

                <q-item clickable v-ripple to="/statistics" style="color:#757575" class="custom-font" active-class="bg-light-blue-1 text-blue-grey-7">
                    <q-item-section avatar>
                        <q-icon name="sym_o_bar_chart" size="lg" />
                    </q-item-section>

                    <q-item-section>
                        Statistiques
                    </q-item-section>
                </q-item>

                <!--
                            <q-item clickable v-ripple to="/admin" style="color:#757575" class="custom-font" active-class="bg-light-blue-1 text-blue-grey-7">
                                <q-item-section avatar>
                                    <q-icon name="sym_o_admin_panel_settings" size="lg" />
                                </q-item-section>
        
                                <q-item-section>
                                    Administration
                                </q-item-section>
                            </q-item>
                            -->

                <q-item clickable v-ripple to="/help" style="color:#757575" class="custom-font" active-class="bg-light-blue-1 text-blue-grey-7">
                    <q-item-section avatar>
                        <q-icon name="sym_o_help" size="lg" /> <!-- color="grey-7" -->
                    </q-item-section>

                    <q-item-section>
                        Aide
                    </q-item-section>
                </q-item>


            </q-list>
        </q-scroll-area>
    </q-drawer>
</template>


<script>
import { store } from '../store/store.js'
import { ref } from 'vue'

export default {
    name: 'Sidebar',
    setup() {
        return {
            store,
            miniState: ref(true),
        }
    },

}
</script>

<style></style>