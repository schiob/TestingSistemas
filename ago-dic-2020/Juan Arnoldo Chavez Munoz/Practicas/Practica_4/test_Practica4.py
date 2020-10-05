from Practica_4 import calculating_average
import pytest

def test_calculating_average():
    listilla_pilla = [
        {'usuario': 'Arnold', 'correo': 'arnold@hotmail.com', 'puntos': '95'}, 
        {'usuario': 'Astro', 'correo': 'aaaastro@hotmail.com', 'puntos': '90'}, 
        {'usuario': 'Zoe', 'correo': 'zoe84@outlook.com', 'puntos': '78'},
        {'usuario': 'tuilai', 'correo': 'tuil123@gmail.com', 'puntos': '82'},
        {'usuario': 'Ricky', 'correo': 'ricky_ricon@outlook.com', 'puntos': '84'}
    ] 
    assert calculating_average(listilla_pilla)


def test_calculating_average2():
    listilla_pilla_2 = [
        {'usuario': 'Arnold', 'correo': 'arnold@hotmail.com', 'puntos': '95'}, 
        {'usuario': 'Astro', 'correo': 'aaaastro@hotmail.com', 'puntos': '90'}, 
        {'usuario': 'Zoe', 'correo': 'zoe84@outlook.com', 'puntos': '78'},
        {'usuario': 'Ricky', 'correo': 'ricky_ricon@outlook.com', 'puntos': '84'}
    ]
    
    with pytest.raises(Exception) as excinfo:   
        calculating_average(listilla_pilla_2)
        assert str(excinfo.value) == "At least 1 mail from each type"

def test_calculating_average3():
    listilla_moxitha = [
        {'usuario': 'Arnold', 'correo': 'aAAArnold@HotmAIl.Com', 'puntos': '95'}, 
        {'usuario': 'Astro', 'correo': 'aAAaastro@hOtmAil.cOM', 'puntos': '90'}, 
        {'usuario': 'Zoe', 'correo': 'zoE84@OutLooK.com', 'puntos': '78'},
        {'usuario': 'Ricky', 'correo': 'riCkY_ricon@ouTlOok.Com', 'puntos': '84'},
        {'usuario': 'LaLA', 'correo': 'LaLa@GmAiL.Com', 'puntos': '84'}
    ]
    for dicc in listilla_moxitha:
        print(dicc.values())
        for value in dicc:
            dicc[value] = dicc[value].lower()
    assert calculating_average(listilla_moxitha)
