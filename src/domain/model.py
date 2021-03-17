from __future__ import annotations

from cerberus import Validator


class Memoria:
    def __init__(self):
        self.numero_actual='0'
        self.numero_anterior='0'
        self.operando_1=0
        self.operando_2=0
        self.operador=''

    def get_pantalla(self):
        return {"pantalla":self.numero_actual}
    
    def clean_memoria(self):
        self.numero_actual='0'
        self.numero_anterior='0'
        self.operando_1=0
        self.operando_2=0
        self.operador=''

    def set_numero_actual(self, numero):
        self.numero_anterior = self.numero_actual
        self.numero_actual = numero
    
    def set_operando_1(self,operando_1):
        self.operando_1= operando_1
    
    def set_operando_2(self,operando_2):
        self.operando_2= operando_2
    
    def set_operador(self,operador):
        self.operador= operador
    
    def ejecutar_operacion(self):
         self.operando_2=float(self.numero_actual)
         expresion= str(self.operando_1)+str(self.operador)+str(self.operando_2)
         self.operando_1= 0
         self.operando_2=0
         self.operador=''
         self.numero_actual='0'
         self.numero_anterior='0'
         return {"pantalla":eval(expresion)}

class Teclado:
    def __init__(self):
        self.digitos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.operadores = ['+', '-', 'x', '/']
        self.especiales = ['C', 'O', '.', '=']

    def get_teclas(self):
        teclas = dict()
        teclas = {"digitos": self.digitos,
                  "operadores": self.operadores,
                  "especiales": self.especiales
                  }
        return teclas

    def leer_digito(self, digito, memoria: Memoria):
        # Escribir digito en memoria
        if memoria.numero_actual == '0' :
            memoria.set_numero_actual(str(digito))
        else :
            numero=str(memoria.numero_actual)+str(digito)
            memoria.set_numero_actual(str(numero))
        return  memoria.get_pantalla()
    
    def leer_punto(self, memoria: Memoria):
        # Escribir punto en memoria
        if memoria.numero_actual == '0' :
            memoria.set_numero_actual('0.')
        elif memoria.numero_actual.count('.') < 1:
            numero=str(memoria.numero_actual)+'.'
            memoria.set_numero_actual(str(numero))
        return  memoria.get_pantalla()
    
    def leer_operador(self, operador, memoria: Memoria):
        # Escribir operador en memoria
        if memoria.numero_actual == '0' :
            if operador == '-':
                memoria.set_numero_actual('-')
        else:
            if memoria.operando_1 == 0:
                memoria.set_operando_1(float(memoria.numero_actual))   
            elif memoria.operador != '':
                memoria.ejecutar_operacion()
                
            memoria.set_operador(operador)
            memoria.set_numero_actual('0')

        return  memoria.get_pantalla()

class Calculadora:
    def __init__(self):
        self.teclado = Teclado()
        self.memoria = Memoria()

    def mostrar_teclado(self):
        return self.teclado.get_teclas()
    
    def limpiar_memoria(self):
        self.memoria.clean_memoria()
        return self.memoria.get_pantalla()

    def leer_digito(self, digito):
        return self.teclado.leer_digito(digito,self.memoria)
    
    def leer_punto(self):
        return self.teclado.leer_punto(self.memoria)
    
    def leer_operador(self,operador):
        return self.teclado.leer_operador(operador,self.memoria)
    
    def ejecutar_operacion(self):
        return self.memoria.ejecutar_operacion()
        

calculadora = Calculadora()


def get_error_message(errors):

    error_codes = [str(e.code) for e in errors]
    error_paths = [e.schema_path for e in errors]
    description = ""

    if len(error_codes) != 0:
        invalid_params = ', '.join(
            set([error[0] for error in error_paths])).upper()
        description = str("El siguiente parámetro tiene valor inválido: {}").format(
            invalid_params)

    response = {
        'error': description
    }

    return response


class InvalidInput(Exception):
    def __init__(self, errors, message=f'The request contains errors'):
        self.errors = errors
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'The request contains errors: {self.errors}'


def validate(request):
    schema = {
        'digito': {
            'type': 'string',
            'required':False,
            'nullable': False,
            'minlength': 1,
            'maxlength': 1,
            'regex':'[0-9]?$'
        },
        'operador':{
            'type': 'string',
            'required':False,
            'nullable': False,
            'minlength': 1,
            'maxlength': 1,
            'regex':'[\+\-\*\/]$'
        }
    }
    v = Validator()
    if v.validate(request, schema) is False:
        raise InvalidInput(v._errors)



