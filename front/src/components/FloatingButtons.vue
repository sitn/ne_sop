<template>
    <!-- FLOATING ACTION BUTTONS -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]" class="justify-center items-center z-top">

        <div class="column items-center q-py-xs">

            <!-- SAVE BUTTON -->
            <div class="q-py-xs">
                <q-btn :loading="wait" fab icon="sym_o_save" color="green-5" @click="save()" v-if="editMode & saveButton.render" :disabled="saveButton.disable">
                    <q-tooltip class="bg-black">Enregistrer</q-tooltip>
                </q-btn>
            </div>

            <!-- DELETE BUTTON -->
            <div class="q-py-xs">
                <q-btn fab icon="sym_o_delete_forever" color="red" @click="remove()" v-if="editMode & deleteButton.render" :disabled="deleteButton.disable">
                    <q-tooltip class="bg-black">Supprimer</q-tooltip>
                </q-btn>
            </div>

            <!-- EDIT/VIEW MODE BUTTON -->
            <div class="q-py-xs">
                <q-btn fab :icon="editMode ? 'sym_o_close' : 'sym_o_edit'" color="blue" @click="switchEdit()">
                    <q-tooltip class="bg-black">{{ editMode ? 'Fermer' : 'Modifier' }}</q-tooltip>
                </q-btn>
            </div>

        </div>

    </q-page-sticky>

    <!-- SEAMLESS BOTTOM DIALOG WARNING ON UNSAVED CHANGES -->
    <q-dialog v-model="store.warning" no-focus seamless position="bottom">
        <q-card class="bg-blue-1" style="width: 300px">

            <q-card-section class="row items-center no-wrap">

                <q-avatar size="md" font-size="22px" color="red" text-color="white" icon="front_hand" class="q-mx-md" />
                <div>
                    <div class="text-weight-bold">Modification non enregistrée</div>
                </div>

                <q-space />

            </q-card-section>
        </q-card>
    </q-dialog>

    <!-- EXIT DIALOG WARNING ON UNSAVED CHANGES -->
    <q-dialog v-model="store.exit">
        <q-card class="bg-yellow">

            <q-card-section class="row justify-center items-center no-wrap q-mt-md q-pa-none">
                <q-avatar size="xl" font-size="28px" color="red" text-color="white" icon="front_hand" class="row justify-center items-center q-mx-md" />
            </q-card-section>

            <q-card-section class="row justify-center items-center no-wrap q-ma-none">
                <div class="text-weight-bold">Modification non enregistrée</div>
            </q-card-section>

            <q-card-actions align="right">
                <q-btn outline label="Quitter sans enregistrer" icon="sym_o_close" color="black" @click="exit()" v-close-popup />
                <q-btn outline label="Enregistrer" icon="sym_o_save" color="black" @click="save(store.navigation.to)" :disable="saveButton.disable" v-close-popup />
            </q-card-actions>

        </q-card>
    </q-dialog>
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'FloatingButtons',
    components: {},
    props: { 'edit': Boolean, 'wait': Boolean, 'buttons': Object },
    emits: ['saveEvent', 'editEvent', 'deleteEvent'],
    setup() {
        return {}
    },
    data() {
        return {
            store,
            waitMode: this.wait,
            editMode: this.edit
        }
    },
    computed: {
        saveButton() { return { render: ['active', 'disable'].includes(this.buttons.save), disable: this.buttons.save === 'disable' } },
        deleteButton() { return { render: ['active', 'disable'].includes(this.buttons.deletion), disable: this.buttons.deletion === 'disable' } }
    },
    mounted() {

    },
    methods: {
        switchEdit() {
            // console.log(`${this.$options.name}.vue | editEvent(${this.editMode})`)
            this.editMode = !this.editMode
            this.$emit('editEvent', this.editMode)
        },
        async save(redirect = null) {

            // console.log(`${this.$options.name}.vue | saveEvent`)
            // this.$emit('saveEvent', { redirect: redirect })
            this.$emit('saveEvent', redirect)

            // console.log(`${this.$options.name}.vue | store.navigation.to: ${store.navigation.to}`)
            // this.$router.push({ path: store.navigation.to })

        },
        remove() {
            // console.log(`${this.$options.name}.vue | deleteEvent`)
            this.$emit('deleteEvent')
        },
        exit() {
            // console.log(this.$router)
            // console.log(this.$route)
            // console.log(`store.navigation.to: ${store.navigation.to}`)

            this.store.warning = false
            this.store.exit = false

            // console.log(`${this.$options.name}.vue | store.navigation.to: ${store.navigation.to}`)

            this.$router.push({ path: store.navigation.to })
        },
    }
}
</script>

<style scoped></style>