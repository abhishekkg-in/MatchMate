import { defineStore } from "pinia";
import api from '../services/api'

export const useMatchStore = defineStore("matchStore", {
  state: () => ({
    matches: [
    //   {
    //     id: 1,
    //     homeTeam: "Manchester United",
    //     awayTeam: "Liverpool",
    //     homeLogo: "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
    //     awayLogo: "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
    //     score: "2 - 1",
    //     date: "2025-02-15",
    //     stadium: "Old Trafford",
    //     status: "Completed"
    //   },
    //   {
    //     id: 2,
    //     homeTeam: "Real Madrid",
    //     awayTeam: "FC Barcelona",
    //     homeLogo: "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
    //     awayLogo: "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
    //     score: "",
    //     date: "2025-02-18",
    //     stadium: "Santiago Bernabéu",
    //     status: "Upcoming"
    //   },
    //   {
    //     id: 3,
    //     homeTeam: "Juventus",
    //     awayTeam: "AC Milan",
    //     homeLogo: "https://upload.wikimedia.org/wikipedia/commons/1/15/Juventus_FC_2017_logo.svg",
    //     awayLogo: "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg",
    //     score: "",
    //     date: "2025-02-20",
    //     stadium: "Allianz Stadium",
    //     status: "Upcoming"
    //   }
    ]
  }),

  actions: {
    async getMatches(reqData){
        await api.getMatches().then((res) => {
            const data = res.data
            this.matches = data
            console.log("Matches -->> ", this.matches);
            
        }).catch((err) => {
            console.log("Error getting matches --> ", err);
        })
    }
  }



});
