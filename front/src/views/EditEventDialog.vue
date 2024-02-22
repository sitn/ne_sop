<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Modifier l'évenement</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- FORM -->
            <EventForm class="col" v-model="event" :edit="edit" :changewatch="false"></EventForm>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup :disable="!event.valid" />
        </q-card-actions>
    </q-card>
</template>

<script>
import { store } from '../store/store.js'
import EventForm from "../components/EventForm.vue"

export default {
    name: 'EditEventDialog',
    components: { EventForm },
    props: { 'modelValue': Object },
    emits: ['update:modelValue'],
    data() {
        return {
            store,
            event: null,
            edit: true,
            valid: false,
        }
    },
    created() {
        // console.log(`${this.$options.name}.vue | created()`)
        this.event = Object.assign({}, this.modelValue) // assign a copy of the model value, to bypass reactivity
        // this.event = this.modelValue
    },
    methods: {
        save() {
            // console.log(`${this.$options.name}.vue | save()`)
            Object.assign(this.modelValue, this.event)
            this.$emit('update:modelValue', this.modelValue)
        }
    }
}
</script>

<style scoped></style>