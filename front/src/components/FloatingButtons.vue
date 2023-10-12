<template>
    <!-- FLOATING ACTION BUTTONS -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]" class="justify-center items-center">

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
            // saveButton: {}, // { render: ['active', 'disable'].includes(this.buttons.save), disable: this.buttons.save === 'disable' },
            // deleteButton: {},// { render: ['active', 'disable'].includes(this.buttons.deletion), disable: this.buttons.deletion === 'disable' },
            waitMode: this.wait,
            editMode: this.edit
        }
    },
    computed: {
        /* saveButton() { return { render: ['active', 'disable'].includes(this.buttons.save), disable: !store.valid } },  */
        saveButton() { return { render: ['active', 'disable'].includes(this.buttons.save), disable: this.buttons.save === 'disable' } },
        deleteButton() { return { render: ['active', 'disable'].includes(this.buttons.deletion), disable: this.buttons.deletion === 'disable' } }
    },
    mounted() {

    },
    watch: {
        /*
        buttons: {
            handler(newValue, oldValue) {
                console.log(`${this.$options.name}.vue | watch buttons`)
                this.saveButton = { render: ['active', 'disable'].includes(this.buttons.save), disable: this.buttons.save === 'disable' }
                this.deleteButton = { render: ['active', 'disable'].includes(this.buttons.deletion), disable: this.buttons.deletion === 'disable' }

                console.log(`${this.$options.name}.vue | saveButton`)
                console.log(`${this.$options.name}.vue | buttons`)
                console.log(this.buttons)
                console.log(this.saveButton)
                console.log(oldValue)
                console.log(newValue)
            },
            deep: true
        }
        */
    },
    methods: {
        switchEdit() {
            console.log(`${this.$options.name}.vue | editEvent(${this.editMode})`)
            this.editMode = !this.editMode
            this.$emit('editEvent', this.editMode)
        },
        save() {
            console.log(`${this.$options.name}.vue | saveEvent`)
            this.$emit('saveEvent')
        },
        remove() {
            console.log(`${this.$options.name}.vue | deleteEvent`)
            this.$emit('deleteEvent')
        }
    }
}
</script>

<style scoped></style>