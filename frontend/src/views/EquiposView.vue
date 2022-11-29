<template>
  <section class="teams-player">
    <div class="teams">
      <form @submit="team_id">
        <label for="id_team">id</label>
        <br />
        <input v-model="_id" type="text" name="id_team" />
        <button type="submit">search</button>
      </form>
      <div v-if="informacion">
        <div v-for="team in informacion.response" :key="team.id">
          <p class="team-name">{{ team.team.name }}</p>
          <img class="team_main" :src="team.team.logo" />
          <br />
          <div v-for="player in team.players" :key="player.id">
            <div class="content-box">
              <p class="player-name">{{ player.name }}</p>
              <br />
              <img class="players" :src="player.photo" />
              <br />
              <p class="info-player">
                Position:{{ player.position }}
                <br />
                Age: {{ player.age }}
              </p>
            </div>
            <br />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
const axios = require('axios')
let id_aux = '3'

let options_3 = {
  method: 'GET',
  url: 'https://api-football-v1.p.rapidapi.com/v3/players/squads',
  params: { team: id_aux },
  headers: {
    'X-RapidAPI-Key': 'dd596990d8msh3ada5c9de7498bdp15d212jsn2f2428932959',
    'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com',
  },
}

export default {
  name: 'EquiposViews',
  data() {
    return {
      informacion: null,
      description: null,
      _id: '1',
    }
  },
  created() {
    console.log('get teams by suad')
    axios
      .request(options_3)
      .then((response) => {
        console.log(response.data)
        this.informacion = response.data
      })
      .catch(function (error) {
        console.error(error)
      })
  },
}
</script>

<style>
.team_main {
  max-width: 600px;
  height: 300px;
  width: 300px;
  max-height: 400px;
  margin: auto;
  display: block;
}
.players {
  height: 200px;
  width: 200px;
  margin: auto;
  display: block;
}
.content-box {
  box-sizing: content-box;
  width: 50%;
  border: solid #5b6dcd 10px;
  padding: 5px;
  margin: auto;
}
.teams-player {
  background: #4decf1;
}
.info-player {
  font-size: 20px;
}
.player-name {
  font-size: 25px;
}
.team-name {
  font-size: 70px;
}
</style>
