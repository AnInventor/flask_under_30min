from flask import Blueprint, render_template, request, url_for, redirect

views = Blueprint(__name__, "views")

# routes
@views.route("/")
def home():
    return "This is home page"

#pass args
@views.route("/home")
def home2():
    return render_template("index.html", name="AnInventor")

#function parameter
@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)

#request 
@views.route("/pass")
def passer():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

#redirect
@views.route("/go-to")
def got_to_home():
    return redirect(url_for("views.home2")) 
