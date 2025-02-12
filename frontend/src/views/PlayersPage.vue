<template>
    <q-page class="q-pa-md players-page">
      <div class="header">
        <h2 class=" text-white">⚽ Top Football Players</h2>
        <q-input 
          v-model="searchQuery" 
          outlined 
          dense 
          placeholder="Search players..." 
          class="q-mt-md search-bar"
          clearable
        >
          <template v-slot:prepend>
            <q-icon name="search" />
          </template>
        </q-input>
      </div>
  
      <q-table
        flat
        bordered
        :rows="filteredPlayers"
        :columns="columns"
        row-key="id"
        dense
        class="players-table q-mt-md"
      >
        <template v-slot:body-cell-avatar="props">
          <q-td :props="props">
            <q-avatar size="40px">
              <img :src="props.row.avatar" :alt="props.row.name" />
            </q-avatar>
          </q-td>
        </template>
  
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <q-btn color="primary" dense label="View Profile" icon="visibility" />
          </q-td>
        </template>
      </q-table>
    </q-page>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, watch } from "vue";
  import { usePlayersStore } from "../stores/playersStore"
  import { storeToRefs } from 'pinia';
  const {getPlayers} = usePlayersStore()
  const { players } = storeToRefs(usePlayersStore())
  const searchQuery = ref("");
  import { debounce } from 'lodash';

  const debouncedSearch = debounce((query) => {
  getPlayers({ name: query });
}, 500);

  const filteredPlayers = ref(players)
  
//   const players = ref([
//     {
//       id: 1,
//       name: "Lionel Messi",
//       position: "Forward",
//       club: "Inter Miami",
//       nationality: "Argentina",
//       avatar: "https://upload.wikimedia.org/wikipedia/commons/b/b8/Lionel_Messi_WC2022.jpg",
//     },
//     {
//       id: 2,
//       name: "Cristiano Ronaldo",
//       position: "Forward",
//       club: "Al Nassr",
//       nationality: "Portugal",
//       avatar: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg",
//     },
//     {
//       id: 3,
//       name: "Kylian Mbappé",
//       position: "Forward",
//       club: "Paris Saint-Germain",
//       nationality: "France",
//       avatar: "https://upload.wikimedia.org/wikipedia/commons/a/a5/Kylian_Mbapp%C3%A9_2018.jpg",
//     },
//     {
//       id: 4,
//       name: "Kevin De Bruyne",
//       position: "Midfielder",
//       club: "Manchester City",
//       nationality: "Belgium",
//       avatar: "https://upload.wikimedia.org/wikipedia/commons/7/79/Kevin_De_Bruyne_2018.jpg",
//     },
//     {
//       id: 5,
//       name: "Robert Lewandowski",
//       position: "Striker",
//       club: "Barcelona",
//       nationality: "Poland",
//       avatar: "https://upload.wikimedia.org/wikipedia/commons/6/69/Robert_Lewandowski_2018.jpg",
//     },
//   ]);
  
  const columns = [
    { name: "avatar", label: "Player", align: "left", field: "avatar" },
    { name: "name", label: "Name", align: "left", field: "name" },
    { name: "position", label: "Position", align: "left", field: "position" },
    { name: "club", label: "Club", align: "left", field: "club" },
    { name: "nationality", label: "Nationality", align: "left", field: "nationality" },
    // { name: "action", label: "Actions", align: "center" },
  ];

  watch(searchQuery, (newVal) => {
    debouncedSearch(newVal);
    });

//   watch(searchQuery ,() => {
//     getPlayers({name: searchQuery.value})
//     // console.log("query changed --->> ", searchQuery.value)
//   })

  watch(players, () => {
    filteredPlayers.value = players.value
  })
  



  onMounted(() => {
      getPlayers({name: searchQuery.value})
  })



  </script>
  
  <style scoped>
  .players-page {
    background: linear-gradient(135deg, #0b3d91, #1d2671);
    min-height: 100vh;
    padding: 20px;
  }
  
  .header {
    text-align: center;
  }
  
  .search-bar {
    max-width: 400px;
    margin: auto;
  }
  
  .players-table {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    backdrop-filter: blur(10px);
  }
  
  .q-table__card {
    background: transparent !important;
    color: white;
  }
  
  .q-table th,
  .q-table td {
    color: white;
  }
  
  .q-btn {
    border-radius: 8px;
  }
  </style>
  