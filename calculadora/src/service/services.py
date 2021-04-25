from src.domain.model import calculadora, InvalidInput, validate, get_error_message
import json 


def mostrar_teclado() :
   return json.dumps(calculadora.mostrar_teclado()), 200


def leer_digito( 
        digit: int,

) :
   try:
           validate({"digito":digit})
           return json.dumps(calculadora.leer_digito(digit)), 200
   except InvalidInput as e:
           return  get_error_message(e.errors), 400
        

def leer_punto() :
   return json.dumps(calculadora.leer_punto())

def limpiar_memoria() :
        return json.dumps(calculadora.limpiar_memoria()), 200

def leer_operador( 
        operador: str
) :
   try:
           validate({"operador":operador})
           return  json.dumps(calculadora.leer_operador(operador)), 200
   except InvalidInput as e:
           return  get_error_message(e.errors), 400

def ejecutar_operacion() :
        return json.dumps(calculadora.ejecutar_operacion())