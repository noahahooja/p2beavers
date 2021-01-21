from flask import (
    Flask, g, redirect, render_template, request, session, url_for
)
from flask_sqlalchemy import SQLAlchemy

#create a Flask instance
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"

    username = db.Column(db.String(15), primary_key=True)
    password = db.Column(db.String(20))
    flappy_score = db.Column(db.Integer)
    crossy_score = db.Column(db.Integer)
    twenty_score = db.Column(db.Integer)
    snake_score = db.Column(db.Integer)

@app.route('/<username>/<password>')
def index(username, password):
    user = User(username=username, password=password, flappy_score=0, crossy_score=0, twenty_score=0, snake_score=0)
    db.session.add(user)
    db.session.commit()

    return '<h1>Added New User!</h1>'

@app.route('/<password>')
def get_user(password):
    user = User.query.filter_by(password=password).all()

    return f'<h1>That user is: { user.username }</h1>'

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html", Title="Home")

@app.route('/flappybeaver/')
def flappybeaver():
    return render_template ("flappybeaver.html", Title="Flappy Beaver", width="1000")

@app.route('/crossybeaver/')
def crossybeaver():
    return render_template ("crossybeaver.html", Title="Crossy Beaver", width="1000")

@app.route('/2048/')
def numbergame():
    return render_template ("2048.html", Title="2048", width="500")

@app.route('/snake/')
def snake():
    return render_template ("snake2.html", Title="Snake", width="500")

@app.route('/login/')
def login():
    return render_template ("login.html", Title="Login")

@app.route('/signup/')
def signup():
    return render_template ("signup.html", Title="Sign Up")

@app.route('/restapi/joke', methods=['GET', 'POST'])
def joke():
# call to random joke web api
    url = 'https://quotes15.p.rapidapi.com/quotes/random/'
    resp = request.get(url)

# formatting variables from return
    setup = resp.json()[0]['setup']

    return render_template('joke.html', setup = setup)

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5002', host='127.0.0.1')




