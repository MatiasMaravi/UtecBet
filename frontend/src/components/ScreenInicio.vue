<template>
  <div class="Screen">
    <h1 class="title">
      UTECBET
    </h1>
    <head>
      <meta charset="utf-8" />

      <title>Formulario de Acceso</title>

      <meta name="viewport" content="width=device-width, initial-scale=1.0" />

      <meta name="author" content="Videojuegos & Desarrollo" />
      <meta
        name="description"
        content="Ejemplo de formulario de acceso basado en HTML5 y CSS"
      />
      <meta name="keywords" content="login,formulariode acceso html" />

      <link
        href="https://fonts.googleapis.com/css?family=Nunito&display=swap"
        rel="stylesheet"
      />
    </head>

    <body>
      <div id="contenedor">
        <img alt="image_main" src="../assets/bet.jpg" />
        <div id="contenedorcentrado">
          <div id="login">
            <form @submit.prevent="login">
              <label for="usuario">Usuario</label>
              <input
                id="usuario"
                v-model="usuario"
                name="usuario"
                placeholder="Usuario"
                required
              />

              <label for="password">Contraseña</label>
              <input
                id="password"
                v-model="password"
                placeholder="Contraseña"
                name="password"
                required
              />

              <button type="submit" title="Ingresar" name="Ingresar">
                Login
              </button>
            </form>
          </div>
          <div id="derecho">
            <div class="titulo">
              Bienvenido a la pagina de apuestas de la Universidad
            </div>
            <hr />
            <div class="pie-form">
              <router-link to="/register">
                Don't have an account? Register
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </body>
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
  name: 'ScreenInicio',
  components: '',
  data() {
    return {
      usuario: '',
      password: '',
    }
  },
  methods: {
    login() {
      console.log('login....')
      apiClient
        .post('/login', {
          username: this.usuario,
          password: this.password,
        })
        .then((response) => {
          console.log({ response })
        })
        .catch((response) => console.log(response))
    },
  },
}
</script>

<style>
.title {
  background: #5f6769;
}
img {
  width: 700px;
  height: 500px;
}
h1 {
  text-align: center;
}
p {
  text-align: center;
  text-justify: auto;
}

body {
  font-family: 'Overpass', sans-serif;
  font-weight: normal;
  font-size: 50%;
  color: #1b262c;

  margin: 0;
  background-color: #5f6769;
}

/* efectos para el contenedor de pantalla completa */
#contenedor {
  display: flex;
  align-items: right;
  justify-content: right;

  margin: 0;
  padding: 0;
  min-width: 100vw;
  min-height: 80vh;
  width: 30%;
  height: 30%;

  background-position: right;
  background-size: cover;
}

/* contenedor del login a la izquierda */
#contenedorcentrado {
  display: flex;
  align-items: right;
  justify-content: right;
  flex-direction: row;

  min-width: 400px;
  max-width: 700px;
  width: 90%;

  background-color: #5f6769;

  /*opacity: 0.50;
    filter: alpha(opacity=50);*/

  border-radius: 10px 10px 10px 10px;
  -moz-border-radius: 10px 10px 10px 10px;
  -webkit-border-radius: 10px 10px 10px 10px;

  -webkit-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);
  -moz-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);
  box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);

  padding: 20px;
  box-sizing: border-box;
}

/* formulario de login */
/* formulario de login */
#login {
  width: 100%;
  max-width: 320px;
  min-width: 320px;
  padding: 30px 30px 50px 30px;
  background-color: #719192;

  -webkit-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);
  -moz-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);
  box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);

  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;

  box-sizing: border-box;

  opacity: 1;
  filter: alpha(opacity=1);
}

#login label {
  display: block;
  font-family: 'Overpass', sans-serif;
  font-size: 120%;
  color: #3c4245;

  margin-top: 15px;
}

#login input {
  font-family: 'Overpass', sans-serif;
  font-size: 110%;
  color: #1b262c;

  display: block;
  width: 100%;
  height: 40px;

  margin-bottom: 10px;
  padding: 5px 5px 5px 10px;

  box-sizing: border-box;

  border: none;
  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;
}

#login input::placeholder {
  font-family: 'Overpass', sans-serif;
  color: #e4e4e4;
}

#login button {
  font-family: 'Overpass', sans-serif;
  font-size: 110%;
  color: #1b262c;
  width: 100%;
  height: 40px;
  border: none;

  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;

  background-color: #dfcdc3;

  margin-top: 10px;
}

#login button:hover {
  background-color: #3c4245;
  color: #dfcdc3;
}
/* formulario de login */
/* formulario de login */

/* seccion de la derecha */
/* seccion de la derecha */
/* por defecto */
#derecho {
  /*display: flex;
    align-items:center;
    justify-content:center;*/

  text-align: center;
  width: 100%;

  opacity: 0.7;
  filter: alpha(opacity=70);

  padding: 20px 20px 20px 50px;
  box-sizing: border-box;
}

.titulo {
  font-size: 150%;
  color: #dfcdc3;
}

.logo-empresa img {
  width: 60%;
}

hr {
  border-top: 1px solid #8c8b8b;
  border-bottom: 1px solid #dfcdc3;
}
.pie-form {
  font-size: 90%;
  text-align: center;
  margin-top: 15px;
}

.pie-form a {
  display: block;
  text-decoration: none;
  color: #dfcdc3;
  margin-bottom: 3px;
}

.pie-form a:hover {
  color: #719192;
}
/* seccion de la derecha */
/* seccion de la derecha */

/* ajustar a pantallas con ancho menor o igual a 775px; */
/* ajustar a pantallas con ancho menor o igual a 775px; */
@media all and (max-width: 400px) {
  #contenedorcentrado {
    flex-direction: column-reverse;

    min-width: 300px;
    max-width: 500px;
    width: 80%;

    background-color: #5f6769;

    /*opacity: 0.50;
        filter: alpha(opacity=50);*/

    border-radius: 10px 10px 10px 10px;
    -moz-border-radius: 10px 10px 10px 10px;
    -webkit-border-radius: 10px 10px 10px 10px;

    -webkit-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);
    -moz-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);
    box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.15);

    padding: 20px;
    box-sizing: border-box;
  }

  #login {
    margin: 0 auto;
  }

  #derecho {
    padding: 15px 15px 15px 15px;
  }

  #login label {
    text-align: left;
  }
}
</style>
