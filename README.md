# Practica5_Login_parte_2
Andre Alexander Hidrogo Rocha 13/11/2023 Segunda parte del login por medio de Flask

#### Mensajes desde la ruta a la plantilla
Para mandar mensajes utilizaremos flash, para ello debemos agregar la variable sercret_key en el archivo config.py a la clase DevelopmentConfig.

El mensaje flash lo agregaremos en la ruta /login con el siguiente comando:
``` python
flash("acceso rechazado")
```
y agregamos ese codigo en el html:
``` html 
{% with messages = get_flashed_messages() %}
   {% if messages %}
     <ul>
       {% for message in messages %}
         <li class="alert alert-warning">{{ message }}</li>
       {% endfor %}
     </ul>
   {% endif %}
 {% endwith %}
````

#### Creacion de la base de datos
Para crear la base de datos simplemente ejecuta los comandos que estan en el script.sql y depues puedes agregar mas usuario si asi lo deseas.

Para utilizar los datos de la base de datos tienes que crear el archivo users.py en la carpeta entities de la siguiente manera:
``` python
class User:
def __init__(self, id, username, password, usertype, fullname="") -> None:
self.id = id
self.username = username
self.password = password
self.fullname = fullname
self.usertype = usertype
```
Despues crearas el archivo ModelUsers.py en la carpeta models junto con el archivo __init__.py

Por ultimo deberas configurar las credenciales para la conexion, ten encuenta que estas varian dependiendo de los datos que registraste.
``` python
class DevelopmentConfig:
DEBUG = True
SECRET_KEY = "qhrf$edjYTJ)*21nsThdK"
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "_Taller$2020.01BD"
MYSQL_DB = "store"
```
Tambien tendras que actualizae la ruta del login
``` html
@app.route("/login", methods=["GET", "POST"])
def login():
if request.method == "POST":
user = User(0, request.form['username'], request.form['password'],0)
logged_user = ModelUsers.login(db, user)
if logged_user != None:
if logged_user.usertype == 1:
return redirect(url_for("admin"))
else:
return redirect(url_for("home"))
else:
flash("Acceso rechazado...")
return render_template("auth/login.html")
else:
return render_template("auth/login.html")
```


