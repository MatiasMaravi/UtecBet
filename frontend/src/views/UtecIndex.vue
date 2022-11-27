<template>
  <div class="presentation">
    <h1 class="titulo">¿Quienes somos?</h1>
    <p class="parrafo_1">
      Somos un grupo de estudiantes de la universidad de Ingenieria y Tecnologia
      UTEC.
    </p>
    <img
      class="utec"
      alt="utec_image"
      src="../assets/nosotros_01.jpg"
      width="500"
      height="250"
    />
  </div>
</template>

<script>
export default {
  name: 'UtecIndex',
}
</script>

<style>
h1.titulo {
  margin: auto;
  text-align: center;
}
p.parrafo_1 {
  margin: auto;
  text-align: center;
}
img.utec {
  display: block;
  margin: auto;
}
.presentation {
  background: purple;
}
</style>
