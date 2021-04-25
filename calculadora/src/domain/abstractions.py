import abc


class AbstractMemoria(abc.ABC):
    def __init__(self):
        self.numero_actual = '0'
        self.numero_anterior = '0'
        self.operando_1 = 0
        self.operando_2 = 0
        self.operador = ''

    @abc.abstractmethod
    def get_pantalla(self):
        raise NotImplementedError

    @abc.abstractmethod
    def clean_memoria(self):
        raise NotImplementedError

    @abc.abstractmethod
    def ejecutar_operacion(self):
        raise NotImplementedError

    def set_numero_actual(self, numero):
        self.numero_anterior = self.numero_actual
        self.numero_actual = numero

    def set_operando_1(self, operando_1):
        self.operando_1 = operando_1

    def set_operando_2(self, operando_2):
        self.operando_2 = operando_2

    def set_operador(self, operador):
        self.operador = operador


class AbstractTeclado(abc.ABC):
    def __init__(self):
        self.digitos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.operadores = ['+', '-', 'x', '/']
        self.especiales = ['C', 'O', '.', '=']

    @abc.abstractmethod
    def get_teclas(self):
        raise NotImplementedError

    @abc.abstractmethod
    def leer_digito(self, digito, memoria: AbstractMemoria):
        raise NotImplementedError

    @abc.abstractmethod
    def leer_punto(self, memoria: AbstractMemoria):
        raise NotImplementedError

    @abc.abstractmethod
    def leer_operador(self, operador, memoria: AbstractMemoria):
        raise NotImplementedError
