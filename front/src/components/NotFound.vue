
<template>
    <div class="notfound">
        <div class="q-pa-md">
            <div style="text-align: center;">

                <q-icon name="warning" style="font-size: max(min(15vw, 150pt), 80pt); max-width: 100px;" color="warning"></q-icon>
                <h5>La page recherchée n'existe pas ou vous ne disposez pas des permissions nécessaires.<br></h5>
                <p><a href="">Retour à la page d'accueil</a></p>

            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: 'NotFound',
    data() {
        return {
            client_url: import.meta.env.VITE_CLIENT_URL,
        }
    },
    computed: {
        linkString() {
            return this.client_url
        }
    },
}

</script>

<style scoped>
.notfound {
    padding-top: 40px;
    max-width: 50%;
    margin: auto;
}
</style>