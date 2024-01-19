<template>
    <q-layout view="hHh LpR fFf" class="shadow-2">

        <Header></Header>
        <Sidebar></Sidebar>

        <q-page-container>
            <q-page class="q-pa-md">

                <!-- Breadcrumbs navigation -->
                <div class="q-pa-sm q-gutter-sm">
                    <q-breadcrumbs style="font-size: 16px">
                        <q-breadcrumbs-el label="Statistiques" to="/statistics" />
                    </q-breadcrumbs>
                </div>

                <!-- Identification -->
                <FormSection title="Statistiques">
                    <template v-slot:content>

                    </template>
                </FormSection>

            </q-page>
        </q-page-container>

    </q-layout>
</template>

<script>
import FormSection from "../components/FormSection.vue"
import Header from '../components/Header.vue'
import Sidebar from '../components/Sidebar.vue'


export default {
    name: 'Help',
    components: { Header, Sidebar, FormSection },
    props: { 'model': Object },
    emits: [],
    setup() {
        return {

            // model: ref(null),
        }
    },
    data() {
        return {

        }
    },
    computed: {
    },
    watch: {
    },
    mounted() {

    },
    methods: {

    }
}
</script>

<style scoped></style>