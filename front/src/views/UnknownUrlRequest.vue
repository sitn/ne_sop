<template>
    <div class="unknownurlrequest">
        <div class="q-pa-md">
            <div style="text-align: center;">

                <h2 style="font-weight: 500;">Page inconnue</h2>
                <q-icon name="warning" style="font-size: max(min(15vw, 150pt), 80pt); max-width: 100px;" color="warning"></q-icon>
                <h5>La page recherchée n'existe pas (<a :href="linkString">{{ linkString }}</a>).</h5>

            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: 'UnknownUrlRequest',
    data () {
        return {
            client_url: import.meta.env.VITE_CLIENT_URL,
            link: null,
        }
    },
    computed: {
        linkString() {
            return this.client_url + this.$route.fullPath
        }
    }
}

</script>

<style scoped>
.unknownurlrequest {
    padding-top: 40px;
    max-width: 50%;
    margin: auto;
}
</style>