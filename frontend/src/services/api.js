import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000',
});

export default {
    getTeams: (params) => api.get('/teams', { params }),
    getPlayers: (reqData) => {
      console.log('====================================');
      console.log("reqData  -->> ", reqData);
      console.log('====================================');
      return api.get(`/players?name=${reqData.name}`, { reqData })
    },
    // getPlayers: (params) => api.get(`/players?name=${params}`, { params }),
    getMatches: (params) => api.get('/matches', { params }),
    getAreas: () => api.get('/areas'),
  };