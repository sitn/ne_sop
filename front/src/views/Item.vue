<template>
    <div class="">

        <!-- Breadcrumbs navigation -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
                <q-breadcrumbs-el :label="item.number.toString()" />
            </q-breadcrumbs>
        </div>

        <!-- General information -->
        <FormSection title="Informations générales">
            <template v-slot:content>
                <div class="text-h6">Informations générales</div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="item.number" label="N°" />
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-select bg-color="white" outlined v-model="item.type" :options="objectTypes" label="Type">
                        </q-select>
                    </div>
                </div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col">
                        <q-input bg-color="white" outlined v-model="item.title" label="Titre" />
                    </div>
                </div>

                <div class="bg-light-blue-1 q-my-md q-pa-md">
                    {{ item }}
                </div>
            </template>
        </FormSection>

        <!-- Processing -->
        <FormSection title="Traitement">
            <template v-slot:content>
                <div class="text-h6">Traitement</div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-select bg-color="white" outlined v-model="item.services.lead" :options="serviceOptions"
                            option-label="name" option-value="id" label="Service principal" clearable>
                            <template v-slot:option="scope">
                                <q-item v-bind="scope.itemProps">
                                    <q-item-section>
                                        <q-item-label>{{ scope.opt.name }}</q-item-label>
                                    </q-item-section>
                                </q-item>
                            </template>
                        </q-select>
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-select bg-color="white" outlined v-model="item.services.support" :options="serviceOptions"
                            option-label="name" option-value="id" label="Service(s) en appui" multiple clearable>
                            <template v-slot:option="scope">
                                <q-item v-bind="scope.itemProps">
                                    <q-item-section>
                                        <q-item-label>{{ scope.opt.name }}</q-item-label>
                                    </q-item-section>
                                </q-item>
                            </template>
                        </q-select>
                    </div>
                </div>

                <div class="row q-py-md">
                    <q-item tag="label" v-ripple>
                        <q-item-section avatar>
                            <q-checkbox v-model="item.urgent" val="true" color="blue" />
                        </q-item-section>
                        <q-item-section>
                            <q-item-label>Urgent</q-item-label>
                            <q-item-label caption>Demande nécessite un traitement prioritaire</q-item-label>
                        </q-item-section>
                    </q-item>
                    <q-item tag="label" v-ripple>
                        <q-item-section avatar>
                            <q-checkbox v-model="item.writtenResponse" val="true" color="blue" />
                        </q-item-section>
                        <q-item-section>
                            <q-item-label>Réponse écrite</q-item-label>
                            <q-item-label caption>Demande nécessite une réponse écrite</q-item-label>
                        </q-item-section>
                    </q-item>
                </div>

            </template>
        </FormSection>

        <!-- Events -->
        <FormSection title="Calendrier">
            <template v-slot:content>
                <div class="text-h6">Calendrier</div>

                <div class="bg-light-blue-1 q-my-md q-pa-md">
                    {{ item.events }}
                </div>

            </template>
        </FormSection>

        <!-- Documents -->
        <FormSection title="Documents">
            <template v-slot:content>
                <div class="text-h6">Documents</div>

                  <div class="q-pa-md">
                    <q-table
                    :title="'Documents formels (' + formalDocumentRows.length + ')'"
                    :rows="formalDocumentRows"
                    :columns="formalDocumentColumns"
                    row-key="name"
                    >
                    <template v-slot:body="props">
                        <q-tr :props="props">
                            <q-td key="version" :props="props">
                                {{ props.row.version }}
                            </q-td>
                            <q-td key="filename" :props="props">
                                <a href="#" @click.prevent="downloadRessource(props.row)">
                                    {{ props.row.filename }}
                                </a>
                            </q-td>
                            <q-td key="filesize" :props="props">
                                {{ props.row.filesize }}
                            </q-td>
                            <!-- <q-td key="format" :props="props">
                                {{ props.row.format }}
                            </q-td> -->
                            <q-td key="auteur" :props="props">
                                {{ props.row.author }}
                            </q-td>
                            <q-td key="date" :props="props">
                                {{ props.row.date }}
                            </q-td>
                            <!-- <q-td key="etape" :props="props">
                                {{ props.row.step }}
                            </q-td> -->
                            <!-- <q-td key="type" :props="props">
                                {{ props.row.type }}
                            </q-td> -->
                            <q-td key="note" :props="props">
                                {{ props.row.note }}
                            </q-td>
                            <q-td key="action" :props="props">
                                <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)"
                                    icon="delete"></q-btn>
                            </q-td>
                        </q-tr>
                    </template>
                </q-table>
                </div>
                
                <div class="q-pa-md">
                  <q-table
                  :title="'Pièces jointes (' + attachementRows.length + ')'"
                  :rows="attachementRows"
                  :columns="attachementColumns"
                  row-key="name"
                  >
                  <template v-slot:body="props">
                      <q-tr :props="props">
                          <q-td key="version" :props="props">
                              {{ props.row.version }}
                          </q-td>
                          <q-td key="filename" :props="props">
                              <a href="#" @click.prevent="downloadRessource(props.row)">
                                  {{ props.row.filename }}
                              </a>
                          </q-td>
                          <q-td key="filesize" :props="props">
                              {{ props.row.filesize }}
                          </q-td>
                          <q-td key="format" :props="props">
                              {{ props.row.format }}
                          </q-td>
                          <q-td key="auteur" :props="props">
                              {{ props.row.author }}
                          </q-td>
                          <q-td key="date" :props="props">
                              {{ props.row.date }}
                          </q-td>
                          <!-- <q-td key="etape" :props="props">
                              {{ props.row.step }}
                          </q-td> -->
                          <!-- <q-td key="type" :props="props">
                              {{ props.row.type }}
                          </q-td> -->
                          <q-td key="note" :props="props">
                              {{ props.row.note }}
                          </q-td>
                          <q-td key="action" :props="props">
                              <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)"
                                  icon="delete"></q-btn>
                          </q-td>
                      </q-tr>
                  </template>
              </q-table>
              </div>
                <div class="bg-light-blue-1 q-my-md q-pa-md">
                    {{ formalDocumentRows }}
                    <!-- {{ item.documents }} -->
                </div>

            </template>
        </FormSection>


    </div>
</template>

<script>
import items from '../assets/data/items.json'
import documents from '../assets/data/documents.json'
import entities from '../assets/data/entities.json'
import FormSection from "../components/FormSection.vue"


const formalDocumentColumns = [
  { name: 'version', align: 'center', label: 'version', field: 'version', sortable: true },
  { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true },
  { name: 'filesize', align: 'left', label: 'Taille', field: 'filesize', sortable: true },
//   { name: 'format', align: 'left', label: 'Format', field: 'format', sortable: true },
  { name: 'auteur', align: 'left', label: 'Auteur', field: 'author', sortable: true },
  { name: 'date', align: 'left', label: 'Date', field: 'date', sortable: true },
//   { name: 'etape', align: 'left', label: 'Étape', field: 'step', sortable: true },
//   { name: 'type', align: 'left', label: 'Type', field: 'type', sortable: true },
  { name: 'note', align: 'left', label: 'Note', field: 'note', sortable: true },
  { name: 'action', align: 'left', label: '', field: 'action' }
]
const attachementColumns = [
//   { name: 'version', align: 'center', label: 'version', field: 'version', sortable: true },
  { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true },
  { name: 'filesize', align: 'left', label: 'Taille', field: 'filesize', sortable: true },
  { name: 'format', align: 'left', label: 'Format', field: 'format', sortable: true },
  { name: 'auteur', align: 'left', label: 'Auteur', field: 'author', sortable: true },
  { name: 'date', align: 'left', label: 'Date', field: 'date', sortable: true },
//   { name: 'etape', align: 'left', label: 'Étape', field: 'step', sortable: true },
//   { name: 'type', align: 'left', label: 'Type', field: 'type', sortable: true },
  { name: 'note', align: 'left', label: 'Note', field: 'note', sortable: true },
  { name: 'action', align: 'left', label: '', field: 'action' }
]


export default {
    name: 'Item',
    components: { FormSection },
    props: { 'model': Object }, // 'rows': items
    emits: [],
    setup() {
        return {

            // model: ref(null),
        }
    },
    data() {
        return {
            item: items.find(e => e.id === this.$route.params.id),
            objectTypes: [
                'Amendement', 'Interpellation', 'Motion', 'Postulat', 'Projet de lois et décrets', 'Question', 'Rapport', 'Recommandation', 'Resolution'
            ],
            formalDocumentRows: documents.filter(e => e.ressourcetype === 'formal'),
            formalDocumentColumns: formalDocumentColumns,
            attachementRows: documents.filter(e => e.ressourcetype === 'attachement'),
            attachementColumns: attachementColumns,
            serviceOptions: entities.filter(e => e.type === "Service de l'état")
        }
    },
    computed: {
    },
    mounted() {
        
    },
    methods: {
        async downloadRessource(ressource) {
            console.log('téléchargement de la ressource', ressource)
        }
    }
}
</script>

<style scoped></style>