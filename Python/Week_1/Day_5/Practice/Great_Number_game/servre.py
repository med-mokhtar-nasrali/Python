from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    number = session['number']
    
    if guess < number:
        feedback = 'Too low!'
        correct = False
    elif guess > number:
        feedback = 'Too high!'
        correct = False
    else:
        feedback = 'Correct! You guessed the number!'
        correct = True
    
    return render_template('index.html', feedback=feedback, correct=correct)

@app.route('/reset')
def reset():
    session.pop('number', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
