from flask import (
    Flask, g, redirect, render_template, request, session, url_for, make_response
)
from flask_sqlalchemy import SQLAlchemy

import random

#create a Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    flappy_score = db.Column(db.Integer)
    crossy_score = db.Column(db.Integer)
    twenty_score = db.Column(db.Integer)
    snake_score = db.Column(db.Integer)

@app.route('/sign_up/user', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['psw']
            checkpassword = request.form['psw-repeat']
            if password == checkpassword:
                user = User(username=username, password=password, flappy_score=0, crossy_score=0, twenty_score=0, snake_score=0)
                db.session.add(user)
                db.session.commit()
                return render_template("signup.html", Title="Sign Up", redtext="Added New User: " + username + '. Now go log in.', filledUsername=username)
            else:
                return render_template("signup.html", Title="Sign Up", redtext='Password does not match confirmed password.', filledUsername=username)
        except:
            return render_template("signup.html", Title="Sign Up", redtext = 'That username is taken. This one is probably available.', filledUsername= 'xX_' + username + '_Xx')
    else:
        render_template('signup.html', Title="Login", redtext="I don't think you're on the right page mang", filledUsername="")

@app.route('/log_in/user/', methods=['GET','POST'])
def searchUser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']
        try:
            checkUser = User.query.filter_by(username=username).first()
            if password == checkUser.password:
                logged_in = 1
                loginUsername = username
                #resp = make_response(render_template('home.html'))
                #resp.set_cookie(username, logged_in)
                #resp, (on next line)
                return render_template('home.html', Title="Home", loginUsername=username, logged_in=1, flappy_score=checkUser.flappy_score, crossy_score=checkUser.crossy_score, twenty_score=checkUser.crossy_score, snake_score=checkUser.snake_score)
                #sign the user in
            else:
                return render_template('login.html', Title="Login", redtext="Incorrect username and/or password.", filledUsername=username)
        except:
            return render_template('login.html', Title="Login", redtext="Incorrect username and/or password.", filledUsername=username)
    else:
        return render_template('login.html', Title="Login", redtext="I don't think you're on the right page mang", filledUsername="")

@app.route('/sign_out/user', methods=['GET','POST'])
def sign_out():
    return render_template('home.html', loginUsername='', logged_in=0)

@app.route('/signup/', methods=['GET','POST'])
def signup(redtext='', filledUsername=''):
    return render_template("signup.html", Title="Sign Up", redtext=redtext, filledUsername=filledUsername)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template("login.html", Title="Login", redtext="", filledUsername="")

#connects default URL to a function
@app.route('/', methods=['GET', 'POST'])
def goHome():
    return redirect(url_for('home'))

@app.route('/home/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", Title="Home", loginUsername='', logged_in=0)

@app.route('/flappybeaver/', methods=['GET', 'POST'])
def flappybeaver():
    return render_template("flappybeaver.html", Title="Flappy Beaver", width="1000")

@app.route('/crossybeaver/', methods=['GET', 'POST'])
def crossybeaver():
    return render_template("crossybeaver.html", Title="Crossy Beaver", width="570")

@app.route('/2048/', methods=['GET', 'POST'])
def numbergame():
    return render_template("2048.html", Title="2048", width="500")

@app.route('/snake/', methods=['GET', 'POST'])
def snake():
    return render_template("snake2.html", Title="Snake", width="500")

@app.route('/scorepage/', methods=['GET', 'POST'])
def scorepage():
    return render_template("scorepage.html", Title="Scores page", width="1000")

import requests



@app.route('/restapi/quote/', methods=['GET', 'POST'])
def quote():
# call to random quote web api
    import requests

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"en"}

    headers = {
    'x-rapidapi-key': "be43b38cedmsh17c4689e2c1a95fp18da84jsnd77b7103f602",
    'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #quote = response.text

    start1 = 'ent":'
    end1 = ',"ur'
    quote1 = response.text[response.text.find(start1)+len(start1):response.text.find(end1)+len(start1)-5]

    quote = quote1 + " - " + random.choice(['Noah Ahooja','Ryan Luo','Aiden Tung'])

    return render_template("home.html", Title="Home", loginUsername='', logged_in=0, quote=quote)

@app.route('/restapi/word/', methods=['GET', 'POST'])
def word():
    # call to random quote web api
    import requests

    url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

    headers = {
    'x-rapidapi-key': "be43b38cedmsh17c4689e2c1a95fp18da84jsnd77b7103f602",
    'x-rapidapi-host': "random-words-with-pronunciation.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    #quote = response.text

    word1 = response.text

    word = word1 + " - " + random.choice(['Websters Dictionary'])


    return render_template("home.html", Title="Home", loginUsername='', logged_in=0, word=word)

@app.route('/restapi/joke/', methods=['GET', 'POST'])
def joke():
    # call to random quote web api
    import requests

    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

    querystring = {"format":"json","blacklistFlags":"nsfw,racist","idRange":"0-150","type":"single,twopart"}

    headers = {
        'x-rapidapi-key': "be43b38cedmsh17c4689e2c1a95fp18da84jsnd77b7103f602",
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params = querystring)

    #quote = response.text

    joke1 = response.text

    joke = joke1 + " - " + random.choice(['Websters Dictionary'])


    return render_template("home.html", Title="Home", loginUsername='', logged_in=0, joke=joke)

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5002', host='127.0.0.1')




