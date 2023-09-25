<template>
    <div class="row justify-center q-mb-lg">

        <div class="col-sm-12 col-md-8">

            <!-- EDIT MODE TOGGLE -->
            <div class="row justify-end q-px-md q-mb-none">
                <q-toggle v-model="editMode" @update:model-value="toggleEdit()" label="Modification">
                    <q-tooltip class="bg-black">Activer/Désactiver le mode modification</q-tooltip>
                </q-toggle>
            </div>

            <div class="row justify-centerbg-grey ">
                <div class="col">
                    <slot name="body"></slot>
                </div>
            </div>

        </div>
    </div>
</template>

<script>

export default {
    name: 'Form',
    components: {},
    props: { 'title': String, 'edit': Boolean },
    emits: ['editEvent'],
    setup() {
        return {

        }
    },
    data() {
        return {
            model: null,
            editMode: this.edit
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        toggleEdit() {
            console.log('toggleEdit')
            this.$emit('editEvent', this.editMode);
        }
    }
}
</script>

<style scoped></style>