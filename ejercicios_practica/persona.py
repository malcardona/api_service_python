#!/usr/bin/env python
'''
Heart DB manager
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para administrar la base de datos de registro de personas
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    
    def __repr__(self):
        return f"Persona:{self.name} de edad {self.age}"


def insert(name, age):
    # Crear una nueva persona
    person = Persona(name=name, age=age)

    # Agregar la persona a la DB
    db.session.add(person)
    db.session.commit()


def report(limit=0, offset=0):
    # Obtener todas las personas
    query = db.session.query(Persona)
    if limit > 0:
        query = query.limit(limit)
        if offset > 0:
            query = query.offset(offset)

    json_result_list = []

    # De los resultados obtenidos pasar a un diccionario
    # que luego será enviado como JSON
    # TIP --> la clase Persona podría tener una función
    # para pasar a JSON/diccionario
    for person in query:
        json_result = {'name': person.name, 'age': person.age}
        json_result_list.append(json_result)

    return json_result_list

def dashboard():
    x_q = db.session.query(Persona.id)
    x_axe =[x for x in x_q]
    print(x_axe)

    #if x_axe is None or len(x_axe) == 0:
        #return []
    
    y_q =db.session.query(Persona.age)
    y_axe =[y for y in y_q]
    print(y_axe)

    #if y_axe is None or len(y_axe) == 0:
        #return []
    
    return x_axe, y_axe


if __name__ == "__main__":
    print("Test del modulo heart.py")

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

    # Aquí se puede ensayar todo lo que necesitemos con nuestra DB
    # ...

    dashboard()

    db.session.remove()
    db.drop_all()