import pytest
from Numeros import numero



@pytest.mark.parametrize(
    "entrada, expected",
    [
        ([51, -12, -3, 0, 2],f'2 numero positivo\n2 numero negativo\n3 numero par\n2 numero impar'),
        ([0, 1, 2, 3, 4],f'4 numero positivo\n0 numero negativo\n3 numero par\n2 numero impar'),
        ([-1, -2, -3],f'0 numero positivo\n3 numero negativo\n1 numero par\n2 numero impar'),
        ([0,],f'0 numero positivo\n0 numero negativo\n1 numero par\n0 numero impar')

    ]
)
def test_entrada(entrada, expected):
    assert numero(entrada) == expected