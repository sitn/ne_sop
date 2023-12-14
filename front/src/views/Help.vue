<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Aide" to="/help" />
            </q-breadcrumbs>
        </div>

        <!-- HELP -->
        <FormSection title="Aide">
            <template v-slot:content>

            </template>
        </FormSection>

    </div>
</template>

<script>
import FormSection from "../components/FormSection.vue"


export default {
    name: 'Help',
    components: { FormSection },
    props: { 'model': Object },
    emits: [],
    data() {
        return {

        }
    },
    computed: {
    },
    mounted() {
    },
    methods: {
    }
}
</script>

<style scoped></style>