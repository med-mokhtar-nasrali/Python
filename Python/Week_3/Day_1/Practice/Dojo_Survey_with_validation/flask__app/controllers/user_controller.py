from flask__app import app
from flask import render_template , redirect , request
from flask__app.modules.user_model import User

#Display Route For The Form
@app.route('/')
def display_form():
    return render_template ("form.html")

#Action Route
@app.route('/user', methods=['POST'])
def submit():
    data = {
        **request.form
    }
    if not User.validate_form(data):
        return redirect("/")
    id = User.save(data)
    return redirect("/result/"+str(id))


#Display Route
@app.route("/result/<int:id>")
def display_result(id):
    user = User.show({"id":id})
    return render_template("result.html",user=user)