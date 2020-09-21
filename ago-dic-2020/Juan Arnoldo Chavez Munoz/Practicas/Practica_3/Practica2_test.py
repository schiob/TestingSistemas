from Practica_2 import sortPants, getCandidates, tryToSell
import pytest

def test_sortPants():
    dicti = {
      "person": "jesus",
      "id": 1,
      "person": "lalala",
      "id": 2
    }
    assert sortPants(dicti), "invalid type of data"

#Este test pasa porque corregí un poco el archivo principal
def test_getCandidates():
    empty_list = {}
    assert getCandidates(empty_list), "Expected a dictionary"

def test_getCandidates2():
    empty_list = []
    if len(getCandidates(empty_list)) == 0:
       assert getCandidates(empty_list), "value can't be empty"
    assert getCandidates(empty_list)
    
def test_tryToSell():
    a, b = 1,8
    assert tryToSell(a,b)

def test_tryToSell2():
    c = 1000
    d = []
    assert tryToSell(c,d)