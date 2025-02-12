<template>
    <q-card class="my-card bg-dark text-white">
      <q-img :src="placeholderImage" ratio="1">
        <div class="absolute-bottom">
          <div class="text-h6">{{ team.name }}</div>
          <div class="text-subtitle2">
            Founded: {{ team.founded || 'N/A' }}
          </div>
        </div>
      </q-img>
  
      <q-card-actions class="bg-primary">
        <q-btn flat icon="sports_soccer">Players</q-btn>
        <q-space />
        <q-btn flat icon="schedule">Matches</q-btn>
      </q-card-actions>
    </q-card>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  
  const props = defineProps({
    team: {
      type: Object,
      required: true,
    },
  });
  
  const placeholderImage = computed(() =>
    `https://picsum.photos/400/200?random=${props.team.id}`
  );
  </script>