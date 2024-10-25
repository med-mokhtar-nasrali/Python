from flask import Flask,session,render_template,request,redirect#type:ignore
app = Flask(__name__)
app.secret_key = 'skey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)

    name = request.form['user_name']
    location= request.form['location']
    language= request.form['language']
    comments = request.form['comments']
    

    session['user_name']=name
    session['location']=location
    session['language']=language
    session['comments']=comments
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')    

if __name__=='__main__':
    app.run(debug=True)