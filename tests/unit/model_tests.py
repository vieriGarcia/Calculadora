import pytest
from src.domain.model import validate, InvalidInput, calculadora

def test_calculadora_mostrar_teclado():
    teclado= dict()
    teclado= {"digitos": ["1", "2", "3", "4", "5", "6", "7", "8", "9"], 
        "operadores": ["+", "-", "x", "/"], 
        "especiales": ["C", "O",".", "="]}
    assert calculadora.mostrar_teclado() == teclado


def test_calculadora_limpiar_memoria():
    calculadora.limpiar_memoria()
    assert calculadora.memoria.numero_actual == '0'
    assert calculadora.memoria.numero_anterior == '0'
    assert calculadora.memoria.operando_1 == 0
    assert calculadora.memoria.operando_2 == 0
    assert calculadora.memoria.operador ==''

def test_calculadora_leer_digito_inicial():
    calculadora.limpiar_memoria()
    digito=5
    calculadora.leer_digito(digito)
    assert calculadora.memoria.numero_actual == str(digito)

def test_calculadora_leer_digito_despues_de_digito():
    calculadora.limpiar_memoria()
    calculadora.leer_digito(5)
    calculadora.leer_digito(7)
    assert calculadora.memoria.numero_actual == '57'

def test_calculadora_leer_operador():
    calculadora.limpiar_memoria()
    operador= '+'
    calculadora.leer_digito(5)
    calculadora.leer_operador(operador)
    assert calculadora.memoria.numero_actual == '0'
    assert calculadora.memoria.operando_1 == 5
    assert calculadora.memoria.operador == operador

def test_validate_digito():
    param = {
        'digito': 'hj'
    }
    with pytest.raises(InvalidInput, match='The request contains errors'):
        validate(param)

def test_validate_operador():
    param = {
        'operador': 'x'
    }
    with pytest.raises(InvalidInput, match='The request contains errors'):
        validate(param)