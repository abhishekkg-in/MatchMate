import { defineStore } from "pinia";
import api from '../services/api'

export const usePlayersStore = defineStore("playersStore", {
  state: () => ({
    players: [
    ]
  }),

  actions: {
    async getPlayers(reqData){
        await api.getPlayers(reqData).then((res) => {
            const data = res.data
            this.players = data
            console.log('====================================');
            console.log("teams data ==>> ", this.players);
            console.log('====================================');
        }).catch((err) => {
            console.error('error loading teams -->> ', err)
        })
    }
  }
});
