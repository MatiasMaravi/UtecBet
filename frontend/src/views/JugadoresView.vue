<template>
  <div>
    <section>
      <h1>Team</h1>
      <h2>{{ experience.name }}</h2>
      <div class="experience-detail">
        <img
          :src="require(`@/assets/${experience.image}`)"
          :alt="experience.name"
        />
        <p>{{ experience.description }}</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'JugadoresView',
  props: {
    slug: {
      type: String,
      required: true,
    },
    jugadoreSlug: {
      type: String,
      required: true,
    },
  },
  computed: {
    jugador() {
      return teams.teams.find((jugador) => {
        return jugador.slug === this.slug
      })
    },
    experience() {
      return this.jugador.jugadores.find((jugador) => {
        return jugador.slug === this.jugadorSlug
      })
    },
  },
}
</script>

<style></style>
