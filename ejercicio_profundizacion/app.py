'''
Flask [Python]
Ejemplos de clase

Autor: malcardona

Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos la API 
de jsonplaceholder, retorna el request de la API y la almacena en una db.
'''

import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect

import funct
import user 

# Crear el server Flask
app = Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
# Asociamos nuestro controlador de la base de datos con la aplicacion
user.db.init_app(app)

# Este método se ejecutará solo una vez
# la primera vez que ingresemos a un endpoint
@app.before_first_request
def before_first_request_func():
    # Borrar y crear la base de datos
    user.db.drop_all()
    user.db.create_all()
    # Completar la base de datos
    user.fill()
    print("Base de datos generada")

@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h3>[GET] /user/{id}/titles__ --> Muestra cuantos titulos completó el usuario cuyo id es el pasado como parámetro en la URL estática </h3>"
        result += "<h3>[GET] /user/graph__--> Devuelve la comparativa de cuantos títulos completó cada usuario</h3>"
        result += "<h3>[GET] /user/titles__ --> Informa cuantos títulos completó cada usuario</h3>"
        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/user/{id}/titles__")
def titles():
    try:
        # Obtener de la query string los valores de limit y offset
        id = 0

        id_str = str(request.args.get(id))

        if(id_str is not None) and (id_str.isdigit()):
            id = int(id_str)

            data = user.title_completed_count(id)

        # Transformar json a json string para enviar al HTML
        return f"El usuario completo {data} titulos"
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    print('@malcardona start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)