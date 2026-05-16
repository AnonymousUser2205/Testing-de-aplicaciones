class Calculadora:
    """
    Una clase simple de calculadora para demostrar operaciones aritméticas básicas.
    """

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b
