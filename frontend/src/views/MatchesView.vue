<template>
  <div class="box">
    <h1>Matches:</h1>
    <div class="Matches" v-for="match in matches" :key="match.code">
      <a>{{ match.local }}</a>
      <a>VS</a>
      <a>{{ match.visit }}</a>

      <label for="bet">Bet:</label>

      <form @submit.prevent="register">
        <input v-model="bet" type="text" name="bet" />
        <br />

        <button type="submit">Register</button>
        <br />
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default {
  name: 'MatchesView',
  data() {
    return {
      local: '',
      visit: '',
      matches: null,
    }
  },
  methods: {
    get_matches() {
      apiClient
        .get('/matches')
        .then((response) => {
          console.log({ response })
          this.matches = response.data.matches
        })
        .catch((response) => console.log(response))
    },
  },
  created() {
    this.get_matches()
  },
}
</script>

<style>
.Matches {
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}
.box {
  display: flex;
  background: cornflowerblue;
}
</style>
