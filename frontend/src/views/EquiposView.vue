<template>
  <section>
    <div class="teams">
      <div v-for="team in teams" :key="team.id">
        <p>{{ team.name }}</p>
        <br />
        <img
          class="teams-views"
          :src="require(`@/assets/${team.image}`)"
          :alt="team.name"
        />
      </div>
    </div>
  </section>
</template>

<script>
import teams from '@/teams'

export default {
  name: 'EquiposViews',
  data() {
    return { teams: teams.teams }
  },
  props: {
    slug: {
      type: String,
      require: true,
    },
  },
  methods: {},
  computed: {
    team() {
      return teams.teams.find((t) => {
        return t.slug
      })
    },
  },
}
</script>

<style>
.image-teams {
  max-width: 600px;
  height: auto;
  width: auto;
  max-height: 400px;
}
.teams-views {
  display: flex;
  justify-content: space-between;
  width: 300px;
  height: 300px;
  margin: auto;
}

p {
  margin: 0 40px;
  font-size: 20px;
  text-align: center;
}

.cards {
  display: flex;
}

.cards img {
  max-width: 200px;
}

.card {
  padding: 0 20px;
  position: relative;
}

.card__text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 25px;
  font-weight: bold;
  text-decoration: none;
}

.image-teams {
  max-width: 600px;
  height: auto;
  width: auto;
  max-height: 400px;
}
</style>
