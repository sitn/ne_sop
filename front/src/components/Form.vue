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
            oldData: null,
            newData: null,
        }
    },
    computed: {
        formData() {
            // console.log("this.form")
            // console.log(this.$refs.form)
            return Object.assign({}, this.model)
        }
    },
    mounted() {
        this.validateForm()
        store.oldFormData = Object.assign({}, this.model)
        store.warning = false
    },
    updated() {
        this.validateForm()
    },
    watch: {
        formData: {
            handler(newValue, oldValue) {

                store.newFormData = Object.assign({}, this.model)
                this.validateForm()

            },
            deep: true
        },
    },
    methods: {
        validateForm() {
            this.$nextTick(() => { this.$refs.form.validate() })

            let oldDataString = JSON.stringify(store.oldFormData).replaceAll(/"id":\d+,/gi, '').replaceAll(/"uuid":"[a-z0-9-]+",/gi, '')
            let newDataString = JSON.stringify(this.model).replaceAll(/"id":\d+,/gi, '').replaceAll(/"uuid":"[a-z0-9-]+",/gi, '')

            // console.log(oldDataString)
            // console.log(newDataString)

            if (oldDataString !== newDataString) {
                store.warning = true
            } else {
                store.warning = false
            }

        },
        validationSuccess() {
            // console.log(`${this.$options.name} | validationSuccess()`)
            this.valid = true
            this.model.valid = true
            store.valid = true
            this.$emit('validationEvent', true)
        },
        validationError() {
            // console.log(`${this.$options.name} | validationError()`)
            this.valid = false
            this.model.valid = false
            store.valid = false
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