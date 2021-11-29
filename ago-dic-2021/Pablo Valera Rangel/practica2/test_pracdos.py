import pytest
from practica2a import sumaNumeros


@pytest.mark.parametrize("input_a, input_b, expected")(

    [
        (10, 2, 12),
        (51, 52, 103),
        (sumaNumeros(3, 2), 15, 20),
        (10, sumaNumeros(3, 5), 18),
        (0, 12, 12),
        (15, 0, 15),
        (3*5, 4*4, 31),
        (7, 20, 3*9),
        (2, 2, 5)  # FALLA A PROPOSITO
    ]
)
def test_suma_multiple(input_a, input_b, expected):
    assert sumaNumeros(input_a, input_b) == expected
