<template>
  <div class="home">
    <img alt="utecbet logo" src="../assets/bet.jpg" />
    <ScreenInicio />
  </div>
</template>

<script>
import ScreenInicio from '@/components/ScreenInicio.vue'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: ScreenInicio,
  components: { ScreenInicio },
}
</script>
