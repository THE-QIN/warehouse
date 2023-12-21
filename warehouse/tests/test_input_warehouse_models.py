from warehouse.models import Warehouse, Company, Product, Stock
import pytest
"""
NOTES: JIKA ERROR BUAT TIDAK ERROR.
"""
@pytest.mark.django_db
def test_input_warehouse():
    # membuat record di database
    company_indofood = Company.objects.create(name="indofood")
    # membuat relasi product ke company
    mie_kuah = Product.objects.create(name="mie kuah", company=company_indofood)

    # sekarang kita punya company dan product dari company tsb
    # kita akan membuat gudang / warehouse yang akan menyimpan jumlah produk dari indofood

    # sebenarnya product sudah punya relasi dengan company. jadi gudang tidak perlu relasi ke company
    gudang_besar_selatan = Warehouse.objects.create(name="Gudang selatan")
    # kita bisa menggunakan stock untuk relasikan barang dengan gudang
    # kita buat insert_product ke dalam gudang dengan membuat method insert_stock
    # dengan argument atau input insert_stock(Product models, jumlah yang di masukkan)

    gudang_besar_selatan.insert_stock(mie_kuah, 12)
    
    # kita query atau cari dulu stock data nya
    # kita cari berdasarkan warehouse + product
    gudang_selatan_stock = Stock.objects.get(warehouse=gudang_besar_selatan, products=mie_kuah)
    # lalu kita test hasil di dalam gudang, apakah sama yang di masukkan
    assert gudang_selatan_stock.quantity == 12
    # kita coba tambahkan lagi
    gudang_besar_selatan.insert_stock(mie_kuah, 3)
    # seharus nya di sini menjadi 15.. 12+3
    # kita refresh dlu baca database nya
    gudang_selatan_stock.refresh_from_db()
    # lalu kita test hasilnya
    assert gudang_selatan_stock.quantity == 15

@pytest.mark.django_db
def test_output_warehouse():
    """
    Buat hal yang sama, tetapi ini barang keluar
    """
    pass