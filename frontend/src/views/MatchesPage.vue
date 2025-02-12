<template>
    <q-page class="matches-page">
      <div class="header">
        <h1>Football Matches ⚽</h1>
        <p>Check out upcoming and past matches</p>
      </div>
  
      <div class="match-grid">
        <q-card
          v-for="match in matches"
          :key="match.id"
          class="match-card"
          bordered
          flat
        >
          <q-card-section class="team-section">
            <div class="team" style="max-width: 30%;">
              <q-img :src="match.homeLogo" class="team-logo" />
              <span>{{ match.homeTeam }}</span>
            </div>
  
            <div class="score-box flex column">
              <q-badge
                :color="match.status === 'Completed' ? 'green' : 'blue'"
                class="status-badge"
              >
                {{ match.status }}
              </q-badge>
              <span class="score">{{ match.score }}</span>
            </div>
  
            <div class="team" style="max-width: 30%;">
              <q-img :src="match.awayLogo" class="team-logo" />
              <span>{{ match.awayTeam }}</span>
            </div>
          </q-card-section>
  
          <q-card-section class="match-details">
            <div><q-icon name="event" /> <span>{{ match.date }}</span></div>
            
            <div><q-icon name="place" class="icon" /> {{ match.stadium }}</div>
          </q-card-section>
        </q-card>
      </div>
    </q-page>
  </template>
  
  <script setup>
  import {onMounted, ref} from 'vue'
  import { useMatchStore } from "../stores/matchStore"; // Import Store
  import { storeToRefs } from 'pinia';
  const {getMatches} = useMatchStore()
  const { matches } = storeToRefs(useMatchStore())


  onMounted(() => {
      getMatches()
  })
  </script>
  
  <style scoped>
  /* Page Styling */
  .matches-page {
    padding: 20px;
    text-align: center;
    background: linear-gradient(135deg, #0b3d91, #1d2671);
    min-height: 100vh;
  }
  
  /* Header Section */
  .header {
    color: white;
    margin-bottom: 20px;
  }
  
  /* Match Grid */
  .match-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    justify-content: center;
    padding: 0 10px;
  }
  
  /* Match Cards */
  .match-card {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
    padding: 15px;
  }
  
  .match-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.3);
  }
  
  /* Team Section */
  .team-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
  }
  
  /* Team Details */
  .team {
    display: flex;
    align-items: center;
    flex-direction: column;
    color: white;
  }
  
  .team-logo {
    width: 50px;
    height: 50px;
    margin-bottom: 5px;
  }
  
  /* Match Details */
  .match-details {
    display: flex;
    justify-content: space-around;
    align-items: center;
    color: white;
    padding: 10px;
    font-size: 14px;
  }
  
  .match-details .icon {
    margin-left: 5px;
  }
  
  /* Score Box */
  .score-box {
    text-align: center;
  }
  
  .score {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
  }
  
  /* Status Badge */
  .status-badge {
    font-size: 12px;
    margin-bottom: 5px;
  }
  </style>
  