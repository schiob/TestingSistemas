import pytest
from triangulos import tipo_triangulo


def test_triangulo_str():
    assert tipo_triangulo('salu2', 5, 5) == 'Los valores no pueden contener letras'
 
def test_triangulo_negativo():
    assert tipo_triangulo(0, -5, -15) == 'No es ningun triángulo'

def test_triangulo_largo():
    assert tipo_triangulo(1005, 5000000, 1005) == 'Los lados del triangulo no pueden ser tan grandes'


def test_triangulo_equilatero():
    assert tipo_triangulo(5, 5, 5) == 'Equilatero'


def test_triangulo_escaleno():
    assert tipo_triangulo(50, 55, 50) == 'Escaleno'


def test_triangulo_isosceles():
    assert tipo_triangulo(55, 55, 25) == 'Isósceles'
