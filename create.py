from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    nickname = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, key='email')

if __name__ == "__main__":
    """create each table"""
    db.create_all()
    try:
        u1 = Users(name='Aiden Tung', nickname='Aiden', email='aiden@example.com')
        u2 = Users(name='Nolan D'Esopo, nickname='Nolan', email='nolan@example.com')
        u3 = Users(name='Ryan Luo', nickname='Ryan', email='ryan@example.com')
        u4 = Users(name='Noah Ahooja', nickname='Noah', email='noah@example.com')
        u5 = Users(name= 'John Mortenson', nicknake='Mr M', email='jmort1021@yahoo.com')
        session.add_all([u1, u2, u3, u4])
        session.commit()
    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print(row.nickname)
        print(row.email)