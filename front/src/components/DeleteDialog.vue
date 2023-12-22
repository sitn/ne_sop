<template>
  <!-- DELETE DIALOG -->
  <q-dialog :model-value="modelValue" @hide="close()">
    <q-card>

      <q-card-section class="row items-center">
        <q-avatar icon="sym_o_delete_forever" color="red" text-color="white" />
        <span class="q-ml-sm">{{ content }}</span>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Annuler" color="primary" v-close-popup />
        <q-btn flat label="Supprimer" color="red" @click="remove" v-close-popup />
      </q-card-actions>

    </q-card>
  </q-dialog>
</template>

<script>
export default {
  name: 'DeleteDialog',
  props: {
    'modelValue': Boolean,
    'content': {type: String, default: () => 'Supprimer définitivement cette entrée et tous les éléments liés?'}
  },
  emits: ['update:modelValue', 'deleteEvent'],
  methods: {
    remove() {
      this.$emit('deleteEvent')
    },
    close() {
      this.$emit('update:modelValue', false)
    }
  }
}
</script>

