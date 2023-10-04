<template>
    <!-- FLOATING ACTION BUTTONS -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]">

        <!-- SAVE BUTTON -->
        <div class="q-py-xs">
            <q-btn :loading="wait" fab icon="sym_o_save" color="amber-14" @click="save()" v-if="editMode">
                <q-tooltip class="bg-black">Enregistrer</q-tooltip>
            </q-btn>
        </div>

        <!-- EDIT/VIEW MODE BUTTON -->
        <div class="q-py-xs">
            <q-btn fab :icon="editMode ? 'sym_o_visibility' : 'sym_o_edit'" color="blue" @click="switchEdit()">
                <q-tooltip class="bg-black">{{ editMode ? 'Visualisation' : 'Modification' }}</q-tooltip>
            </q-btn>
        </div>

    </q-page-sticky>
</template>

<script>

export default {
    name: 'FloatingButtons',
    components: {},
    props: { 'edit': Boolean, 'wait': Boolean },
    emits: ['saveEvent', 'editEvent'],
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
            console.log(`FloatingButtons.vue | editEvent(${this.editMode})`)
            this.$emit('editEvent', this.editMode)

        },
        save() {
            console.log('FloatingButtons.vue | saveEvent')
            this.$emit('saveEvent')
        }
    }
}
</script>

<style scoped></style>