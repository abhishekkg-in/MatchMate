import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TeamsPage from '../views/TeamsPage.vue'
import MatchesPage from '../views/MatchesPage.vue'
import PlayersPage from '../views/PlayersPage.vue'
import standings from '../views/Standings.vue'
import Standings from '../views/Standings.vue'



const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView
        },
        {
            path: "/teams",
            name: "teams",
            component: TeamsPage
        },
        {
            path: "/matches",
            name: "matches",
            component: MatchesPage
        },
        {
            path: "/players",
            name: "players",
            component: PlayersPage
        },
        {
            path: "/standings",
            name: "standings",
            component: Standings
        }
    ]
})

export default router