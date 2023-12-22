class Gudang:
    def __init__(self):
        self.barang = 0

    def masukkan(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah barang tidak boleh negatif")
        self.barang += jumlah

    def keluarkan(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah barang tidak boleh negatif")
        if jumlah > self.barang:
            raise ValueError("Jumlah barang tidak cukup")
        self.barang -= jumlah