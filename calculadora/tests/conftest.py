#pylint: disable=redefined-outer-name
import time
import pytest
from src.domain.model import Memoria, Teclado, Calculadora
from src.domain.abstractions import AbstractMemoria


class NotImplementedMemoria(AbstractMemoria):

    def get_pantalla(self):
        AbstractMemoria.get_pantalla(self)

    def clean_memoria(self):
        AbstractMemoria.clean_memoria(self)

    def ejecutar_operacion(self):
        AbstractMemoria.ejecutar_operacion(self)

@pytest.fixture
def memoria():
    return Memoria()

@pytest.fixture
def memoria_sin_implementar():
    return NotImplementedMemoria()

@pytest.fixture
def teclado():
    return Teclado()

@pytest.fixture
def calculadora(memoria, teclado):
    return Calculadora(teclado,memoria)

