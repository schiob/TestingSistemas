
import pytest
from suma import suma


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (7,3,10),
        (3,7,10),
        (-3,5,2),
        (2,-3,-1),
        (1/2,3/4,1.25),
        (0.75,0.25,1)
    ]
)

def test_multiples_sumas(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected
