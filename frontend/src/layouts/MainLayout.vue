<template>
  <div>

    <q-layout view="lHh Lpr lFf">
      <!-- Left Navigation Drawer -->
      <q-drawer
        v-model="leftDrawerOpen"
        show-if-above
        bordered
        :width="240"
        class="bg-dark text-white"
      >
        <q-scroll-area class="fit">
          <q-list padding class="q-mt-lg">
            <q-item-label header class="text-weight-bold text-accent">
              Sports Hub
            </q-item-label>
  
            <q-separator color="accent" class="q-mb-sm" />
  
            <q-item
              v-for="nav in navItems"
              :key="nav.title"
              clickable
              v-ripple
              :to="nav.to"
              exact
              class="q-my-xs"
            >
              <q-item-section avatar>
                <q-icon :name="nav.icon" color="accent" />
              </q-item-section>
  
              <q-item-section>
                <q-item-label class="text-weight-medium">{{ nav.title }}</q-item-label>
              </q-item-section>
            </q-item>
  
            <q-separator color="accent" class="q-mt-md" />
  
            <!-- Favorites Section -->
            <div class="q-pa-md">
              <div class="text-caption text-grey-4 q-mb-sm">Favorites</div>
              <q-item
                v-for="fav in favoriteTeams"
                :key="fav.id"
                clickable
                class="q-mb-xs rounded-borders"
              >
                <q-item-section avatar>
                  <q-avatar color="primary" text-color="white">
                    {{ fav.name.charAt(0) }}
                  </q-avatar>
                </q-item-section>
                <q-item-section>{{ fav.name }}</q-item-section>
              </q-item>
            </div>
          </q-list>
        </q-scroll-area>
      </q-drawer>
  
      <!-- Page Header -->
      <q-header elevated class="bg-dark text-white">
        <q-toolbar>
          <q-btn
            flat
            dense
            round
            icon="menu"
            aria-label="Menu"
            @click="toggleLeftDrawer"
            class="q-mr-sm"
          />
  
          <q-toolbar-title class="text-weight-bold">
            <q-icon name="sports_soccer" size="md" class="q-mr-sm" />
            Football Tracker
          </q-toolbar-title>
  
          <!-- Search Bar -->
          <!-- <q-input
            dense
            outlined
            v-model="searchQuery"
            placeholder="Search teams, players..."
            class="q-ml-md search-input"
            @update:model-value="handleSearch"
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input> -->
  
          <!-- Theme Toggle -->
          <q-btn
            flat
            round
            :icon="$q.dark.isActive ? 'light_mode' : 'dark_mode'"
            @click="$q.dark.toggle()"
            class="q-ml-md"
          />
        </q-toolbar>
      </q-header>
  
      <!-- Page Footer -->
      <q-footer elevated class="bg-dark text-grey-4">
        <q-toolbar>
          <q-toolbar-title class="text-center text-caption">
            © 2025 Football Tracker. All rights reserved. | 
            Abhishek Kumar Gupta
            <!-- <q-icon name="public" class="q-mx-xs" />
            Live scores powered by API Sports -->
          </q-toolbar-title>
        </q-toolbar>
      </q-footer>
  
      <!-- Main Content Area -->
      <q-page-container>
        <home-view />
        <!-- <router-view :search-query="searchQuery" /> -->
      </q-page-container>
    </q-layout>
  </div>
    
</template>
  
  <script setup>
  import { ref } from 'vue'
  import HomeView from '../views/HomeView.vue'
  
  const leftDrawerOpen = ref(false)
  const searchQuery = ref('')
  
  const navItems = [
    { title: 'Home', icon: 'home', to: '/' },
    { title: 'Teams', icon: 'groups', to: '/teams' },
    { title: 'Matches', icon: 'event', to: '/matches' },
    { title: 'Players', icon: 'person', to: '/players' },
    { title: 'Standings', icon: 'leaderboard', to: '/standings' }
  ]
  
  // Sample favorite teams - replace with real data
  const favoriteTeams = ref([
    { id: 1, name: 'Manchester United' },
    { id: 2, name: 'Real Madrid' },
    { id: 3, name: 'Bayern Munich' }
  ])
  
  const toggleLeftDrawer = () => {
    leftDrawerOpen.value = !leftDrawerOpen.value
  }
  
  const handleSearch = () => {
    // Emit search event or handle search logic
    console.log('Searching for:', searchQuery.value)
  }
  </script>
  
  <style lang="scss" scoped>
  
  </style>