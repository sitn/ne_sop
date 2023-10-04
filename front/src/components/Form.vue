<template>
    <div class="row justify-center q-my-lg">

        <div class="col-xs-12 col-sm-12 col-md-8">

            <!-- EDIT MODE TOGGLE -->
            <!-- 
            <div class="row justify-end q-pa-xs">
                <q-toggle v-model="editMode" @update:model-value="toggleEdit()" label="Modification" v-if="toggle === true">
                    <q-tooltip class="bg-black">Activer/Désactiver le mode modification</q-tooltip>
                </q-toggle>
            </div>
            -->

            <div class="row justify-centerbg-grey">
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
    props: { 'title': String, 'edit': Boolean, 'toggle': Boolean },
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