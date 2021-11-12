from power import power, times

import pytest

def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8
    with pytest.raises(TypeError):
        power(2, 3)


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6