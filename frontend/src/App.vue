<template>
  <NavComponent />
  <router-view />
</template>
<script>
import NavComponent from './components/NavComponent.vue'

export default {
  components: {
    NavComponent,
  },
}
</script>
<style>
#app {
  color: #2c3e50;
}
</style>
