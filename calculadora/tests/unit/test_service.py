'''import pytest
from src.service import services
import json

def test_service_mostrar_teclado():
    expected_response= dict()
    expected_response= {"digitos": ["1", "2", "3", "4", "5", "6", "7", "8", "9"], 
        "operadores": ["+", "-", "x", "/"], 
        "especiales": ["C", "O",".", "="]}
    assert json.loads(services.mostrar_teclado()[0]) == expected_response


def test_service_limpiar_memoria():
    expected_response = dict()
    expected_response= {'pantalla':'0'}
    assert json.loads(services.limpiar_memoria()[0]) == expected_response


def test_service_leer_digito_inicial():
    services.limpiar_memoria()
    digito='5'
    expected_response = dict()
    expected_response= {'pantalla':'5'}
    assert json.loads(services.leer_digito(digito)[0]) == expected_response


'''
