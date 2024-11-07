from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from flask import render_template,session,redirect,flash,request





#Display Route for the home page and the user logged in currnently
@app.route("/recipes")
def recipes_dashboard():
    if "user_id"not in session:
        return redirect('/')
    recipes = Recipe.get_all()
    logged_user = User.get_by_id({"id":session["user_id"]})
    return render_template("recipes.html", recipes = recipes , user = logged_user)

#Display Route fort the create form 
@app.route("/recipes/new")
def new_recipe():
    if "user_id"not in session:
        return redirect('/')
    return render_template("create.html")

#Action Route for creating the form
@app.route("/recipes/create",methods=["POST"])
def add_recipe():
    if Recipe.validate(request.form):
        data = {
            **request.form,
            "user_id":session["user_id"]
        }
        Recipe.create(data)
        return redirect("/recipes")
    return redirect("/recipes/new")


#Display route for the about of the recipe
@app.route("/recipes/<int:id>")
def show_one(id):
    if "user_id"not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({"id":id})
    logged_user = User.get_by_id({"id":session["user_id"]})
    return render_template("show.html",recipe = recipe,user = logged_user)


#Display Route for the edit page
@app.route('/recipes/edit/<int:id>')
def edit(id):
    if "user_id"not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({"id":id})
    return render_template("edit.html",recipe = recipe)


#Action Route for the edit
@app.route("/recipes/update/<int:id>",methods=["POST"])
def update(id):
    if Recipe.validate(request.form):
        data = {
            **request.form,
            "id": id
        }
        Recipe.update(data)
        return redirect('/recipes')
    return redirect(f'/recipes/edit/{id}')

#Action Route
@app.route("/recipes/delete/<int:id>",methods = ["POST"])
def delete(id):
    Recipe.delete({"id":id})
    return redirect("/recipes")