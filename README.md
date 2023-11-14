# Practica5_Login_parte_2
Andre Alexander Hidrogo Rocha 13/11/2023 Segunda parte del login por medio de Flask

#### Mensajes desde la ruta a la plantilla
Para mandar mensajes utilizaremos flash, para ello debemos agregar la variable sercret_key en el archivo config.py a la clase DevelopmentConfig.

El mensaje flash lo agregaremos en la ruta /login con el siguiente comando:

flash("acceso rechazado")

y agregamos ese codigo en el html:

{% with messages = get_flashed_messages() %}
   {% if messages %}
     <ul>
       {% for message in messages %}
         .<li class="alert alert-warning">{{ message }}</li>
       {% endfor %}
     </ul>
   {% endif %}
 {% endwith %}

#### Creacion de la base de datos
Para crear la base de datos simplemente ejecuta los comandos que estan en el script.sql y depues puedes agregar mas usuario si asi lo deseas.

Para utilizar los datos de la base de datos tienes 
 
 

