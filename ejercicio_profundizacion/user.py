'''
User DB manager
---------------------------
Autor: malcardona

'''

from ast import If
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import funct

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String)
    completed = db.Column(db.Boolean)
    
    def __repr__(self):
        return f"El usuario {self.userId} completo el titulo {self.title}? --> {self.completed}"

def fill():
    data = funct.extract('https://jsonplaceholder.typicode.com/todos')
    #datalist = [x for x in data]
    for x in data:
        user = User(id=x['id'], userId=x['userId'], title=x['title'], completed=x['completed'])
        db.session.add(user)
    db.session.commit()

def title_completed_count(userId):
    completed_count = db.session.query(User).filter(User.userId == userId).filter(User.completed == True).count()

    return completed_count

def title_completed_axes():
    x = db.session.query(User).filter(User.id).with_entities()
    return x 

if __name__ == "__main__":
    print("Test del modulo user.py")
# Crear una aplicación Flask para testing
    # y una base de datos fantasma (auxiliar o dummy)
    # Referencia:
    # https://stackoverflow.com/questions/17791571/how-can-i-test-a-flask-application-which-uses-sqlalchemy
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdatabase.db"
    # Bindear la DB con nuestra app Flask
    db.init_app(app)
    app.app_context().push()

    db.create_all()

 ## Funciones para probar
    
fill()

base = title_completed_axes()
print(base)