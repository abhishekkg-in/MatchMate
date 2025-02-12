<template>
  <q-page class="teams-page">
    <div class="header">
      <h1>Football Clubs ⚽</h1>
      <p>Explore the world's top football teams</p>
    </div>

    <div class="team-grid">
      <q-card
        v-for="team in teams"
        :key="team.id"
        class="team-card"
        bordered
        flat
      >
        <q-img :src="team.logo" class="team-logo" />

        <q-card-section>
          <div class="text-h6 text-bold">{{ team.name }}</div>
          <div class="text-subtitle2">{{ team.country }}</div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import { useTeamStore } from "../stores/teamStore"
import { storeToRefs } from 'pinia';
const {getTeams} = useTeamStore()
const { teams } = storeToRefs(useTeamStore())

onMounted(() => {
  getTeams()
})

</script>

<style scoped>
/* Page Styling */
.teams-page {
  padding: 20px;
  text-align: center;
  background: linear-gradient(135deg, #064635, #154c79);
  min-height: 100vh;
}

/* Header Section */
.header {
  color: white;
  margin-bottom: 20px;
}

/* Team Grid */
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  justify-content: center;
  padding: 0 10px;
}

/* Team Cards */
.team-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
  padding: 15px;
}

.team-card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 15px rgba(255, 255, 255, 0.3);
}

/* Team Logos */
.team-logo {
  width: 100px;
  height: 100px;
  margin: auto;
  display: block;
}
</style>
