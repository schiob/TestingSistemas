from primer_parcial import Tri_from_file
import pytest

def test_is_equilatero():
    expected = "Es equilatero"
    real = Tri_from_file("is_equilatero.txt")
    assert expected == real

def test_is_equilatero2():
    expected = "Es equilatero"
    real = Tri_from_file("is_equilatero2.txt")
    assert expected == real

def test_no_triangulo():
    expected = "No es triangulo"
    real = Tri_from_file("no_triangulo.txt")
    assert expected == real

def test_no_triangulo2():
    expected = "No es triangulo"
    real = Tri_from_file("no_triangulo2.txt")
    assert expected == real

def test_no_triangulo3():
    expected = "No es triangulo"
    real = Tri_from_file("no_triangulo3.txt")
    assert expected == real

def test_is_isoceles():
    expected = "Es iscoceles"
    real = Tri_from_file("is_isoceles.txt")
    assert expected == real

def test_is_isoceles2():
    expected = "Es iscoceles"
    real = Tri_from_file("is_isoceles2.txt")
    assert expected == real

def test_is_escaleno():
    expected = "Es Escaleno"
    real = Tri_from_file("is_escaleno.txt")
    assert expected == real
