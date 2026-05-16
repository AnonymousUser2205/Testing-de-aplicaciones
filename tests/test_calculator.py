import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add_success(calc):
    """Caso exitoso: suma de dos números positivos."""
    assert calc.add(2, 3) == 5

def test_divide_by_zero_error(calc):
    """Caso de error: división por cero debe lanzar ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)

def test_multiply_by_zero_edge_case(calc):
    """Caso borde: multiplicar cualquier número por cero debe dar cero."""
    assert calc.multiply(100, 0) == 0
    assert calc.multiply(0, 0) == 0

def test_subtract_success(calc):
    """Prueba adicional: resta exitosa."""
    assert calc.subtract(10, 5) == 5
