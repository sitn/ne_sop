// store.js
import { reactive } from 'vue'
import entities from '../assets/data/entities.json'
import items from '../assets/data/items.json'
import events from '../assets/data/events.json'

export const store = reactive({
    dev: true,
    entities: entities,
    items: items,
    events: events,
})