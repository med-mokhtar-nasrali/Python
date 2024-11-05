from flask_app import app
from flask_app.models.user_model import User
from flask import render_template,redirect,request,flash


#Display Route For Main Page
@app.route("/")
def display_form():
    return render_template("index.html")

#Action Route For Main Page
@app.route("/user/create",methods=["POST"])
def create_user():
    if not User.email_validation(request.form):
        return redirect("/")
    else: 
        id=User.insert_email(request.form)
    return redirect("/success/" + str(id))

@app.route("/success/<int:id>")
def display_all(id):
    user = User.get_by_id({'id': id})
    all_users = User.get_all()
    return render_template("success.html", user = user, all_users = all_users)
