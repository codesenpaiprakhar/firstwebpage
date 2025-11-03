from flask import Flask, url_for, render_template, redirect, request 
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST','GET'])
def greet():
    if request.method=='POST':
        name = request.form['name']
        profession = request.form['profession']



        current_time = datetime.now()
        hour = current_time.hour

        if hour < 12:
            greeting = "Good Morning"
        elif 12 <= hour < 17:
            greeting = "Good Afternoon"
        elif 17 <= hour < 20:
            greeting = "Good Evening"
        else:
            greeting = "Good Night"

            # Redirect to the greetings page with name, profession, and greeting
        


    

    return render_template('greetings.html', name=name, profession=profession,greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)