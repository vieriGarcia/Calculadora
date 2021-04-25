import pytest
from src.domain.model import validate, InvalidInput

@pytest.mark.parametrize(
    ["inp", "expected"],
    [(5,5),(1.34,1.34)],
)
def test_memoria_set_numero_actual(memoria,inp,expected):
    memoria.set_numero_actual(inp)
    assert memoria.numero_actual==expected



@pytest.mark.parametrize(
    ["inp", "expected"],
    [(6,6),(1.34,1.34)],
)
def test_memoria_set_operando_1(memoria,inp,expected):
    memoria.set_operando_1(inp)
    assert memoria.operando_1==expected


@pytest.mark.parametrize(
    ["inp", "expected"],
    [(8,8),(45.34,45.34)],
)
def test_memoria_set_operando_2(memoria,inp,expected):
    memoria.set_operando_2(inp)
    assert memoria.operando_2==expected


@pytest.mark.parametrize(
    ["inp", "expected"],
    [('+','+'),('-','-'),('*','*'),('/','/')],
)
def test_memoria_set_operador(memoria,inp,expected):
    memoria.set_operador(inp)
    assert memoria.operador==expected


@pytest.mark.parametrize(
    ["inp", "expected"],
    [(5,{"pantalla":5}),(1.34,{"pantalla":1.34})],
)
def test_memoria_get_pantalla(memoria,inp,expected):
    memoria.set_numero_actual(inp)
    assert memoria.get_pantalla()==expected


def test_memoria_clean_memoria(memoria):
    memoria.clean_memoria()
    assert memoria.numero_actual == '0'
    assert memoria.numero_anterior == '0'
    assert memoria.operando_1 == 0
    assert memoria.operando_2 == 0
    assert memoria.operador == ''

@pytest.mark.parametrize(
    ["inp", "expected"],
    [([1,1,'+'],{"pantalla":2}),([0.5,10,'*'],{"pantalla":5})],
)
def test_memoria_ejecutar_operacion(memoria,inp,expected):
    memoria.set_operando_1(inp[0])
    memoria.set_numero_actual(inp[1])
    memoria.set_operador(inp[2])

    assert memoria.ejecutar_operacion() == expected
    assert memoria.numero_actual == '0'
    assert memoria.numero_anterior == '0'
    assert memoria.operando_1 == 0
    assert memoria.operando_2 == 0
    assert memoria.operador == ''


def test_memoria_sin_implementar_ejecutar_operacion(memoria_sin_implementar):
    with pytest.raises(NotImplementedError):
        print(memoria_sin_implementar.ejecutar_operacion())


def test_memoria_sin_implementar_get_pantalla(memoria_sin_implementar):
    with pytest.raises(NotImplementedError):
        print(memoria_sin_implementar.get_pantalla())

def test_memoria_sin_implementar_clean_memoria(memoria_sin_implementar):
    with pytest.raises(NotImplementedError):
        print(memoria_sin_implementar.clean_memoria())