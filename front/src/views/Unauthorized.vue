<template>
    <div class="unauthorized">
        <div class="q-pa-md">
            <div style="text-align: center;">

                <h2 style="font-weight: 500;">Accès non autorisé</h2>
                <q-icon class="text-red" name="front_hand" style="font-size: max(min(15vw, 150pt), 80pt); max-width: 100px;"></q-icon>
                <h4>Vous n'êtes pas autorisé·e à accéder à ce contenu.</h4>
                <p>Contacter le support: <a :href="mailtostring">{{ email_webmaster }}</a></p>
            
            </div>
        </div>
            

    </div>
</template>

<script>

export default {
    name: 'Unauthorized',
    data() {
        return {
            email_webmaster: import.meta.env.VITE_WEBMASTER_EMAIL,
        }
    },
    computed: {
        mailtostring() {
            return `mailto:${this.email_webmaster}&subject=SOP - Access`
        }
    },
}

</script>

<style scoped>
.unauthorized {
    padding-top: 40px;
    max-width: 50%;
    margin: auto;
}
</style>