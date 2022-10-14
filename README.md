<center>

<span style="color:orange">

# UtecBet

</span>


![imagen_1](https://www.casasapuestasdeportivas.es/wp-content/uploads/2020/04/mejores-casas-de-apuestas-en-espana.png)

</center>

<span style="color:white">

## Integrantes.
***
- Matias Fabricio Maravi Anyosa
- Jerimy Pierre Sandoval Rivera
- Gian Marco Arteaga
  
</span>

## Descripción del proyecto.

***
Somos un grupo de estudiantes del 3er ciclo de la Universidad de Ingeniería y Tecnología (UTEC) que implementarán una casa de apuestas con el nombre de UtecBet.

### Propuesta de negocio:
La casa de apuestas tendrá en un inicio, solo el acceso a partidos de fútbol, con opción extra de ver las estadísticas, estratégias utilizadas en los juegos entre otras funcionalidades. Será un espacio en donde nos adaptaremos a las necesidades del jugador potencial. Iremos aprendiendo de ellos, para que con el pasar del tiempo logremos ser la casa de apuesta que esté más cercano al cliente. También buscamos generar un momento de entretenimiento para los estudiantes universitarios, un lugar donde encuentren divertirse con los amigos y con la familia.
***
## Objetivos principales 
***
### Misión 
Nuestra misión brindar entretenimiento donde los clientes puedan sentirse cómodos al momento de interactuar con nuestra página. Que a través de una Web API nuestra aplicación permita apostar a nuestros usuarios de forma segura y accesible.

### Visión

Deseamos lograr una empresa de apuestas que no solo este en el rubro de futbol, sino tambien con basquetball, voley, y otros deportes. Por otro lado, a través del aumento de la cantidad de usuarios nos plantemaos mejorar la calidad de interaccion e incluir distintos métodos de pago.

***
## Modelos

Los modelos a trabajar son: Usuario, Apuesta, Transacción, Partido

![Imagen](images\DBP-MODELOS.jpg)

## Información acerca de las tecnologías utilizadas en Front-end, Back-end y Base de datos.
***
Flask-Login
Flask-Admin
Flask-Bootstrap

***
## Licencia
***
Pendiente
***
## Información acerca de las API. Solicitudes y respuestas de cada endpoint utilizado en el sistema.
*** 
- index.html es el inicio del proyecto y el usuario puede escoger entre registrarse y logearse
- /login -> Es el endpoint para que el usuario pueda iniciar sesion
- /sigunp -> Es el endpoint para que el usuario pueda registrarse
- /logout -> Es el endpoint para que el usuario salga de la sesion -No funciona Actualmente-
- /matches -> Es el endpoint para que el usuario pueda ver los partidos del dia
***

## Hosts.
***
- localhost:5432
***
## Forma de autenticación. (Autenticación Básica: Usuario/Contraseña)
***
- Existe un Register y un login. Cuando el usuario se registra su contraseña se encripta
***
## Manejo de errores HTTP: 500, 400, 300, 200, 100, 

***
- Se ha manejado los errores 404 por si un usuario intenta iniciar sesion con una cuenta que no existe.
- Se ha manejado los errores 409 por si un usuario intenta registrarse con una cuenta que ya existe en la base de datos.
***
## Cómo ejecutar el sistema (Deployment scripts).
***
python app.py