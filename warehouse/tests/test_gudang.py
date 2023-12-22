import pytest
from gudang import Gudang

def test_gudang_masuk():
    gudang = Gudang()
    gudang.masukkan(5)
    assert gudang.barang == 5

def test_gudang_keluar():
    gudang = Gudang()
    gudang.masukkan(5)
    gudang.keluarkan(1)
    assert gudang.barang == 4

def test_gudang_keluar_lebih_dari_stok():
    gudang = Gudang()
    gudang.masukkan(5)
    with pytest.raises(ValueError):
        gudang.keluarkan(6)