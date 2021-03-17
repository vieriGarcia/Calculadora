import os

from flask import Flask, request

from src.service import services

app = Flask(__name__)

@app.route("/teclado")
def mostrar_teclado():
    return services.mostrar_teclado()

@app.route("/limpiar_memoria")
def limpiar_memoria():
    return services.limpiar_memoria()

@app.route("/leer_digito")
def leer_digito():
    digit = request.args.get('digit')
    return services.leer_digito(
        digit
    )

@app.route("/leer_punto")
def leer_punto():
    return services.leer_punto()

@app.route("/leer_operador")
def leer_operador():
    operador = request.json['operador']
    print('entrypoint:',operador)
    return services.leer_operador(
        operador
    )

@app.route("/ejecutar_operacion")
def ejecutar_operacion():
    return services.ejecutar_operacion()

if  __name__ == '__main__':
	app.run()
