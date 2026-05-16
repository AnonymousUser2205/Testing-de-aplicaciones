import pytest
from app.calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_sumar_exitoso(calc):
    """Caso exitoso: suma de dos números positivos."""
    assert calc.sumar(2, 3) == 5

def test_dividir_por_cero_error(calc):
    """Caso de error: división por cero debe lanzar ValueError."""
    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        calc.dividir(10, 0)

def test_multiplicar_por_cero_borde(calc):
    """Caso borde: multiplicar cualquier número por cero debe dar cero."""
    assert calc.multiplicar(100, 0) == 0
    assert calc.multiplicar(0, 0) == 0

def test_restar_exitoso(calc):
    """Prueba adicional: resta exitosa."""
    assert calc.restar(10, 5) == 5
