<template>
    <q-layout view="hHh LpR fFf" class="shadow-2">

        <Header></Header>
        <Sidebar></Sidebar>

        <q-page-container>
            <q-page class="q-pa-md">

                <NotFound></NotFound>

            </q-page>
        </q-page-container>

    </q-layout>
</template>

<script>
import Header from '../components/Header.vue'
import Sidebar from '../components/Sidebar.vue'
import NotFound from '../components/NotFound.vue'


export default {
    name: 'Entity',
    components: { Header, Sidebar, NotFound },
}
</script>

<style scoped></style>