<template>
    <div class="login">

        <div class="q-pa-md">
            <q-card class="my-card">
                <q-card-section>
                    <q-form @submit="processLogin" class="q-gutter-md">

                        <div class="text-h6">Identification
                            <q-circular-progress v-if="loginInProgress" indeterminate rounded size="25px" color="primary" class="q-ma-xs" style="float: right;" />
                        </div>

                        <q-separator />

                        <!-- <q-input v-model="username" filled label="Nom d'utilisateur *" style="width: inherit;" lazy-rules :rules="[val => val && val.length > 0 || 'Entrer le nom d\'utilisateur']" /> -->
                        <q-input v-model="username" filled label="Nom d'utilisateur *" style="width: inherit;" lazy-rules :rules="[val => val && val.length > 0 || 'Entrer l\'email']" />

                        <q-input v-model="password" filled :type="isPwd ? 'password' : 'text'" label="Mot de passe *" lazy-rules :rules="[val => val && val.length > 0 || 'Entrer le mot de passe']">

                            <template v-slot:append>
                                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd = !isPwd" />
                            </template>
                        </q-input>
                        <q-separator />

                        <div class="q-gutter-md" align="right">
                            <q-btn label="connexion" type="submit" color="primary" icon="login" />
                        </div>
                    </q-form>
                </q-card-section>
            </q-card>
        </div>
    </div>
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'Login',
    components: {},
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            email: '',
            username: '',
            password: '',
            isPwd: true,
            loginInProgress: false,
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        processLogin() {
            this.loginInProgress = true;

            // store.session.user = 

            // do something here to log in and remove setTimeout above !
            setTimeout(() => {
                this.loginInProgress = false;
                this.$router.push({ name: "ItemsList" });
            }, 2000);

        }
    }
}
</script>

<style scoped>
.login {
    max-width: 450px;
    padding-top: 20vh;
    margin: auto;
}
</style>