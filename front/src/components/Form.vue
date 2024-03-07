<template>
    <div class="row justify-center q-my-lg">


        <div class="col" style="max-width: 880px;">

            <div class="row justify-center">

                <q-form ref="form" class="col" @validation-success="validationSuccess" @validation-error="validationError" greedy no-reset-focus no-error-focus>
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
    props: { 'edit': Boolean, 'model': Object, 'changewatch': Boolean }, // { 'title': String },
    emits: ['editEvent', 'validationEvent'],
    data() {
        return {
            store,
            editMode: this.edit,
            valid: null,
        }
    },
    mounted() {
        this.validateForm()
        store.dialogs.warning = false
    },
    watch: {
        model: {
            handler(newValue, oldValue) {
                // console.log(`${this.$options.name} | watch: model`)
                this.validateForm()
            },
            deep: true
        },
    },
    methods: {
        validateForm() {
            this.$nextTick(() => { this.$refs.form.validate() })
        },
        validationSuccess() {
            // console.log(`${this.$options.name} | validationSuccess()`)
            this.valid = true
            this.model.valid = true
            // store.valid = true
            this.$emit('validationEvent', true)
        },
        validationError() {
            // console.log(`${this.$options.name} | validationError()`)
            this.valid = false
            this.model.valid = false
            // store.valid = false
            this.$emit('validationEvent', false)
        },
        async save(redirectTo) {

            // console.log(`${this.$options.name}.vue | save()`)

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

        },
    }
}
</script>

<style scoped></style>