from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, SHOMIRA !</p>"


@app.route("/los_edificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8092/api/edificios/",
            auth=('SNRA', '12345678'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)



@app.route("/los_departamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8092/api/departamentos/",
            auth=('SNRA', '12345678'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_propietario':d['nombre_propietario'],'costo':d['costo'] ,
        'numero_cuartos':d['numero_cuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('SNRA', '12345678'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
