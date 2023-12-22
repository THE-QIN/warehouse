import pytest
from warehouse.tests.kelipatan import kelipatan

def test_kelipatan_positif():
    assert kelipatan(5,5) == 25
    assert kelipatan(3,5) == 15

def test_kelipatan_negatif():
    with pytest.raises(ValueError):
        kelipatan(-3,5)

def test_kelipatan_nol():
    with pytest.raises(ValueError):
        kelipatan(0,5)