<template>
  <q-page class="q-pa-md flex flex-center column team-mate-home">
    <div class="header">
      <h2 class="text-white">Welcome to MatchMate ⚽</h2>
      <p class="text-white">Your Ultimate Sports Management Platform</p>
      <q-btn color="primary" label="Explore Teams" class="q-mb-md" to="/teams" />
    </div>

    <!-- <q-card class="my-card">
      <q-card-section>
        <q-item-label header>
          <q-icon name="groups" size="md" class="q-mr-sm" />
          Featured Clubs
        </q-item-label>
      </q-card-section>
    </q-card> -->

    <div class="club-grid">
      <q-card v-for="(club, index) in clubs" :key="index" class="club-card">
        <q-img :src="club.logo" class="club-logo" />
        <q-card-section class="text-center">
          <q-item-label class="club-name">{{ club.name }}</q-item-label>
          <q-item-label caption class="club-country">{{ club.country }}</q-item-label>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const clubs = ref([
  {
    name: 'FC Barcelona',
    country: 'Spain',
    logo: 'https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg',
  },
  {
    name: 'Manchester United',
    country: 'England',
    logo: 'https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg',
  },
  {
    name: 'Bayern Munich',
    country: 'Germany',
    logo: 'https://upload.wikimedia.org/wikipedia/commons/1/1f/FC_Bayern_München_logo_%282017%29.svg',
  },
])
</script>

<style scoped>
.team-mate-home {
  padding: 20px;
  text-align: center;
  background: linear-gradient(135deg, #0b3d91, #1d2671);
  min-height: 100vh;
}

.club-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  width: 100%;
  padding: 20px;
}

.club-card {
  width: 100%;
  max-width: 400px;
  margin: auto;
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
  transition: transform 0.3s;
}

.club-card:hover {
  transform: translateY(-5px);
}

.club-logo {
  height: 150px;
  object-fit: contain;
  background: white;
  padding: 10px;
}

.club-name {
  font-size: 1.2rem;
  font-weight: bold;
  color: #fff;
}

.club-country {
  color: #ddd;
}
</style>
