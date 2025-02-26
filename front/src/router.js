import { createRouter, createWebHashHistory, createWebHistory } from "vue-router";
import { store } from "./store/store.js";

import ItemsList from "./views/ItemsList.vue";
import EntitiesList from "./views/EntitiesList.vue";
import DocumentsList from "./views/DocumentsList.vue";
import Document from "./views/Document.vue";
import EventsList from "./views/EventsList.vue";
import Event from "./views/Event.vue";
import Statistics from "./views/Statistics.vue";
import Item from "./views/Item.vue";
import Entity from "./views/Entity.vue";
// import User from './views/User.vue'
// import NewUser from './views/NewUser.vue'
// import Admin from './views/Admin.vue'
import Help from "./views/Help.vue";
import Unauthorized from "./views/Unauthorized.vue";
import NotFound from "./components/NotFound.vue";

const routes = [
  { path: "/unauthorized", name: "Unauthorized", component: Unauthorized },
  { path: "/", redirect: "/items" },
  { path: "/items", name: "ItemsList", component: ItemsList },
  { path: "/items/:id(\\d+)", name: "Item", component: Item, props: true },
  { path: "/items/new", name: "NewItem", component: Item },
  { path: "/documents", name: "DocumentsList", component: DocumentsList },
  { path: "/documents/:id(\\d+)", name: "Document", component: Document, props: true },
  { path: "/entities", name: "EntitiesList", component: EntitiesList },
  { path: "/entities/:id(\\d+)", name: "Entity", component: Entity, props: true },
  { path: "/entities/new", name: "NewEntity", component: Entity },
  { path: "/events", name: "EventsList", component: EventsList },
  { path: "/events/:id(\\d+)", name: "Event", component: Event, props: true },
  { path: "/events/new", name: "NewEvent", component: Event },
  { path: "/statistics", name: "Statistics", component: Statistics },
  // { path: '/admin', name: 'Admin', component: Admin },
  // { path: '/admin/users/:id(\\d+)', name: 'User', component: User, props: true },
  // { path: '/admin/users/new', name: 'NewUser', component: NewUser },
  { path: "/help", name: "Help", component: Help },
  { path: "/:pathMatch(.*)*", name: "NotFound", component: NotFound },
];

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

// navigation guards
router.beforeEach(async (to, from) => {
  if (store.user === null) {
    store.user = await store.getCurrentUser();
  }

  store.navigation.from = from.fullPath;
  store.navigation.to = to.fullPath;
  //  return false to cancel the navigation
  // console.log(`from: ${from}, to: ${to}`)

  if (!(store.user && store.user.username) && to.name !== "Unauthorized") {
    router.push({ name: "Unauthorized" });
  }

  // DISPLAY WARNING DIALOG
  if (store.dialogs.warning) {
    // console.log(from)
    // console.log(to)

    store.dialogs.exit = true;
    return false;
  } else {
    return true;
  }
});
