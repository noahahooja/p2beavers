from flask import (
    Flask, g, redirect, render_template, request, session, url_for
)
from flask_sqlalchemy import SQLAlchemy

#create a Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    flappy_score = db.Column(db.Integer)
    crossy_score = db.Column(db.Integer)
    twenty_score = db.Column(db.Integer)
    snake_score = db.Column(db.Integer)

    def __str__(self):
        return f'{ self.username }'

@app.route('/sign_up/user', methods=['POST'])
def index():
    try:
        username = request.form['username']
        password = request.form['psw']
        checkpassword = request.form['psw-repeat']
        if password == checkpassword:
            user = User(username=username, password=password, flappy_score=0, crossy_score=0, twenty_score=0, snake_score=0)
            db.session.add(user)
            db.session.commit()
            return render_template("signup.html", Title="Sign Up", redtext="Added New User: " + f'{ user.username }' + '. Now go log in.', filledUsername=username)
        else:
            return render_template("signup.html", Title="Sign Up", redtext = 'Password does not match confirmed password.', filledUsername=username)
    except:
        return render_template("signup.html", Title="Sign Up", redtext = 'That username is taken. This one is probably available.', filledUsername= 'xX_' + username + '_Xx')

@app.route('/sign_in/user', methods=['GET', 'POST'])
def search(username, password):
    checkUser = User.query.filter_by(username=username).first()
    if password == checkUser.password:
        pass
        #sign the user in

@app.route('/get/user', methods=['GET', 'POST'])
def get_user(password):
    user = User.query.filter_by(password=password).first()
    return f'Signed in as: ' + str(user)

@app.route('/<password>')
def find_user(password):
    user = User.query.filter_by(password=password).first()
    return f'That user is: ' + str(user)

#connects default URL to a function
@app.route('/', methods=['GET', 'POST'])
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html", Title="Home")

@app.route('/flappybeaver/', methods=['GET', 'POST'])
def flappybeaver():
    return render_template ("flappybeaver.html", Title="Flappy Beaver", width="1000")

@app.route('/crossybeaver/', methods=['GET', 'POST'])
def crossybeaver():
    return render_template ("crossybeaver.html", Title="Crossy Beaver", width="570")

@app.route('/2048/', methods=['GET', 'POST'])
def numbergame():
    return render_template ("2048.html", Title="2048", width="500")

@app.route('/snake/', methods=['GET', 'POST'])
def snake():
    return render_template ("snake2.html", Title="Snake", width="500")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template ("login.html", Title="Login")

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    return render_template ("signup.html", Title="Sign Up", redtext='', filledUsername='')

@app.route('/restapi/joke', methods=['GET', 'POST'])
def joke():
# call to random joke web api
    url = 'https://quotes15.p.rapidapi.com/quotes/random/'
    resp = request.args.get(url)

# formatting variables from return
    setup = resp.json()[0]['setup']

    return render_template('joke.html', setup = setup)

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5002', host='127.0.0.1')




