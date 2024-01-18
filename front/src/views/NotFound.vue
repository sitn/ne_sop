<template>
    <div class="notfound">
        <div class="q-pa-md">
            <div style="text-align: center;">

                <h2 style="font-weight: 500;">Page inconnue</h2>
                <q-icon name="warning" style="font-size: max(min(15vw, 150pt), 80pt); max-width: 100px;" color="warning"></q-icon>
                <h5>La page recherchée n'existe pas.<br>
                    (<a :href="linkString">{{ linkString }}</a>)</h5>

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
            link: null,
        }
    },
    computed: {
        linkString() {
            return window.location.href
        }
    }
}

</script>

<style scoped>
.notfound {
    padding-top: 40px;
    max-width: 50%;
    margin: auto;
}
</style>