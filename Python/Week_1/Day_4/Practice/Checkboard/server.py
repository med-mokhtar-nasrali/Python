from flask import Flask, render_template 
app = Flask(__name__) 



@app.route('/')
def display():
    return render_template('first.html')


@app.route('/<int:num>')
def display_by_x(num):
    return render_template('second.html', num=num)



@app.route('/<int:hieght>/<int:width>')
def display_by_x_y(hieght,width):
    return render_template('third.html',hieght=hieght,width=width)


if __name__=="__main__":
    app.run(debug=True)