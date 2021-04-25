#pylint: disable=redefined-outer-name
import time
import pytest
from src.domain.model import Memoria, Teclado, Calculadora




@pytest.fixture
def memoria():
    return Memoria()

@pytest.fixture
def teclado():
    return Teclado()

@pytest.fixture
def calculadora(memoria, teclado):
    return Calculadora(teclado,memoria)

