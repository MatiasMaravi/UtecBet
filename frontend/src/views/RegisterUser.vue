<template>
  <div class="overlay">
    <!-- LOGN IN FORM by Omar Dsoky -->
    <form @submit="register">
      <!--   con = Container  for items in the form-->
      <div class="con">
        <!--     Start  header Content  -->
        <header class="head-form">
          <h2>Register</h2>
        </header>
        <!--     End  header Content  -->
        <br />
        <div class="field-set">
          <!--   user name -->
          <span class="input-item">
            <i class="fa fa-user-circle"></i>
          </span>
          <!--   user name Input-->
          <input
            v-model="username"
            class="form-input"
            id="txt-input"
            type="text"
            placeholder="@UserName"
            required
          />

          <br />

          <!--   Password -->

          <span class="input-item">
            <i class="fa fa-key"></i>
          </span>
          <!--   Password Input-->
          <input
            v-model="password"
            class="form-input"
            type="password"
            placeholder="Password"
            id="pwd"
            name="password"
            required
          />

          <!--      Show/hide password  -->
          <span>
            <i class="fa fa-eye" aria-hidden="true" type="button" id="eye"></i>
          </span>

          <br />
          <!--        buttons -->
          <!--      button LogIn -->
          <button class="log-in">Log In</button>
        </div>
      </div>
    </form>
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
  name: 'RegisterUser',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    register() {
      console.log('register....')
      apiClient
        .post('/register', {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          console.log({ response })
          this.$router.push({ name: 'LoginUser' })
        })
        .catch((response) => console.log(response))
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Abel|Abril+Fatface|Alegreya|Arima+Madurai|Dancing+Script|Dosis|Merriweather|Oleo+Script|Overlock|PT+Serif|Pacifico|Playball|Playfair+Display|Share|Unica+One|Vibur');
form {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
body {
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
  background-attachment: fixed;
  background-repeat: no-repeat;
  opacity: 0.95;
  /* background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%); */
}

form .con {
  display: -webkit-flex;
  display: flex;

  -webkit-justify-content: space-around;
  justify-content: space-around;

  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;

  margin: 0 auto;
  width: 450px;
  min-height: 500px;
  height: auto;
  border-radius: 5px;
  margin: 2% auto;
  box-shadow: 0 9px 50px hsla(20, 67%, 75%, 0.31);
  padding: 2%;
  background-image: linear-gradient(-225deg, #e3fdf5 50%, #ffe6fa 50%);
}
header {
  margin: 2% auto 10% auto;
  text-align: center;
}
header h2 {
  font-size: 250%;
  font-family: 'Playfair Display', serif;
  color: #3e403f;
}
/*  A welcome message or an explanation of the login form */
header p {
  letter-spacing: 0.05em;
}

.input-item {
  background: #fff;
  color: #333;
  padding: 14.5px 0px 15px 9px;
  border-radius: 5px 0px 0px 5px;
}

input[class='form-input'] {
  width: 240px;
  height: 50px;

  margin-top: 2%;
  padding: 15px;

  font-size: 16px;
  font-family: 'Abel', sans-serif;
  color: #5e6472;

  outline: none;
  border: none;

  border-radius: 0px 5px 5px 0px;
  transition: 0.2s linear;
}
input[id='txt-input'] {
  width: 250px;
}
/* focus  */
input:focus {
  transform: translateX(-2px);
  border-radius: 5px;
}
button {
  display: inline-block;
  color: #252537;

  width: 280px;
  height: 50px;

  padding: 0 20px;
  background: #fff;
  border-radius: 5px;

  outline: none;
  border: none;

  cursor: pointer;
  text-align: center;
  transition: all 0.2s linear;

  margin: 7% auto;
  letter-spacing: 0.05em;
}
.submits {
  width: 48%;
  display: inline-block;
  float: left;
  margin-left: 2%;
}

/* buttons hover */
button:hover {
  transform: translatey(3px);
  box-shadow: none;
}

/* buttons hover Animation */
button:hover {
  animation: ani9 0.4s ease-in-out infinite alternate;
}
@keyframes ani9 {
  0% {
    transform: translateY(3px);
  }
  100% {
    transform: translateY(5px);
  }
}
</style>
