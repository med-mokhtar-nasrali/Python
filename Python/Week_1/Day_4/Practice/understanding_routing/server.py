from flask import Flask , render_template # type: ignore
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/flask")
def flask():
    return "Hi Flask!"

@app.route("/say/<user_name>")
def hi(user_name):
    return render_template('names.html',user_name=user_name)

@app.route("/repeat/<int:number>/<word>")
def repeat(number,word):
    return render_template('many_words.html',number=number,word=word)



if __name__=="__main__":
    app.run(debug=True)