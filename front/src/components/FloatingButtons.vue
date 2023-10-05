<template>
    <!-- FLOATING ACTION BUTTONS -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]" class="justify-center items-center">

        <div class="column items-center q-py-xs">

            <!-- SAVE BUTTON -->
            <div class="q-py-xs">
                <q-btn :loading="wait" fab icon="sym_o_save" color="green-5" @click="save()" v-if="editMode & buttons.save">
                    <q-tooltip class="bg-black">Enregistrer</q-tooltip>
                </q-btn>
            </div>

            <!-- DELETE BUTTON -->
            <div class="q-py-xs">
                <q-btn fab icon="sym_o_delete_forever" color="red" @click="remove()" v-if="editMode & buttons.deletion">
                    <q-tooltip class="bg-black">Supprimer</q-tooltip>
                </q-btn>
            </div>

            <!-- EDIT/VIEW MODE BUTTON -->
            <div class="q-py-xs">
                <q-btn fab :icon="editMode ? 'sym_o_visibility' : 'sym_o_edit'" color="blue" @click="switchEdit()">
                    <q-tooltip class="bg-black">{{ editMode ? 'Visualisation' : 'Modification' }}</q-tooltip>
                </q-btn>
            </div>

        </div>

    </q-page-sticky>
</template>

<script>

export default {
    name: 'FloatingButtons',
    components: {},
    props: { 'edit': Boolean, 'wait': Boolean, 'buttons': Object },
    emits: ['saveEvent', 'editEvent', 'deleteEvent'],
    setup() {
        return {

        }
    },
    data() {
        return {
            waitMode: this.wait,
            editMode: this.edit
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        switchEdit() {
            this.editMode = !this.editMode
            console.log(`${this.$options.name}.vue | editEvent(${this.editMode})`)
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