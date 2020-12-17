import data

from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/flappybeaver/')
def flappybeaver():
    return render_template ("flappybeaver.html")

@app.route('/crossybeaver/')
def crossybeaver():
    return render_template ("crossybeaver.html")

@app.route('/2048/')
def numbergame():
    return render_template ("2048.html")

@app.route('/snake/')
def snake():
    return render_template ("snake.html")

@app.route('/login/')
def login():
    return render_template ("login.html")

@app.route('/signup/')
def signup():
    return render_template ("signup.html")




if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5002', host='127.0.0.1')