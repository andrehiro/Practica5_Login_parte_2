from flask import Flask, redirect, render_template, request, url_for, flash
from config import config
from flask_mysqldb import MySQL
from models.ModelUsers import ModelUsers
from models.entities.users import User

app = Flask(__name__)
db = MySQL(app)
@app.route("/")
def index():
    return redirect("login")

@app.route("/home")
def home():
    return render_template("home.html")

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
    
@app.route("/admin")
def admin():
    # Código para la vista de administrador
    return render_template("admin.html")


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()