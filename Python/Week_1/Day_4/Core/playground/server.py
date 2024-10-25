from flask import Flask ,render_template  # type: ignore
app = Flask(__name__)

@app.route("/play")
def three():
    return render_template("three_boxes.html")

@app.route("/play/<int:number>")
def print_boxes(number):
    return render_template('print_boxes.html', number=number)

@app.route("/play/<int:number>/<color>")
def chose_color(number,color):
    return render_template('chose_color.html', number=number ,color=color)

if __name__=="__main__":
    app.run(debug=True)