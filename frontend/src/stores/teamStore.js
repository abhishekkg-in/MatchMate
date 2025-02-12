import { defineStore } from "pinia";
import api from '../services/api'

export const useTeamStore = defineStore("teamStore", {
  state: () => ({
    teams: [
    //   { id: 1, name: "Manchester United", country: "England", logo: "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg" },
    //   { id: 2, name: "FC Barcelona", country: "Spain", logo: "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg" },
    //   { id: 3, name: "Real Madrid", country: "Spain", logo: "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg" },
    //   { id: 4, name: "Bayern Munich", country: "Germany", logo: "https://upload.wikimedia.org/wikipedia/en/1/1b/FC_Bayern_München_logo_%282017%29.svg" },
    //   { id: 5, name: "Juventus", country: "Italy", logo: "https://upload.wikimedia.org/wikipedia/commons/1/15/Juventus_FC_2017_logo.svg" },
    //   { id: 6, name: "Paris Saint-Germain", country: "France", logo: "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg" }
    ]
  }),

  actions: {
    async getTeams(reqData){
        await api.getTeams(reqData).then((res) => {
            const data = res.data
            this.teams = data
            console.log('====================================');
            console.log("teams data ==>> ", data);
            console.log('====================================');
        }).catch((err) => {
            console.error('error loading teams -->> ', err)
        })
    }
  }
});
