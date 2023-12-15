<template>
    <div class="row justify-center q-my-lg">


        <div class="col" style="max-width: 880px;">

            <div class="row justify-center">

                <q-form ref="form" class="col" @validation-success="validationSuccess" @validation-error="validationError" greedy no-error-focus>
                    <slot name="body"></slot>
                </q-form>

            </div>

        </div>

    </div>
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'Form',
    components: {},
    props: { 'edit': Boolean, 'model': Object }, // { 'title': String },
    emits: ['editEvent', 'validationEvent'],
    data() {
        return {
            store,
            editMode: this.edit,
            valid: null,
        }
    },
    computed: {
        formData() {
            return Object.assign({}, this.model)
        }
    },
    mounted() {
        this.validateForm()
        store.warning = false
    },
    updated() {
        this.validateForm()
    },
    watch: {
        formData: {
            handler(newValue, oldValue) {
                this.validateForm()
                if ((JSON.stringify(newValue) !== JSON.stringify(oldValue))) {
                    store.warning = true
                }
            },
            deep: true
        },
    },
    methods: {
        validateForm() {
            this.$nextTick(() => { this.$refs.form.validate() })

            /*
            if (this.$refs.hasOwnProperty('form')) {
                if (this.$refs.form !== null) {
                    this.$nextTick(() => { this.$refs.form.validate() })
                }
            }
            */

        },
        validationSuccess() {
            console.log(`${this.$options.name} | validationSuccess()`)
            this.valid = true
            this.model.valid = true
            store.valid = true
            this.$emit('validationEvent', true)
        },
        validationError() {
            console.log(`${this.$options.name} | validationError()`)
            this.valid = false
            this.model.valid = false
            store.valid = false
            this.$emit('validationEvent', false)
        },
        async save(redirectTo) {

            console.log(`${this.$options.name}.vue | save()`)

            // saveTo(store.items, this.$route.params.id, this.item, store.navigation.to)

            // TODO: POST RECORD TO DATABASE
            /*
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            let ind = store.items.findIndex((e) => (e.id === this.$route.params.id))
            store.items[ind] = Object.assign({}, this.item)
            this.wait = false
            */

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

        },
    }
}
</script>

<style scoped></style>