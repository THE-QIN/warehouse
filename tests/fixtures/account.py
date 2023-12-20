import pytest
from django.urls import reverse
from  test import status
from fixtures import Product, Warehouse

@pytest.fixture
def products(db):
    return [Product.objects.create(name=f'Product {i}') for i in range(1, 6)]

@pytest.fixture
def warehouse(db):
    return Warehouse.objects.create(name='Warehouse 1')

def test_calculation(client):
    url = reverse('calculation')
    response = client.post(url, {'x': 5, 'y': 5})
    assert response.status_code == status.HTTP_200_OK
    assert response.data == 25

    response = client.post(url, {'x': 3.5, 'y': 2})
    assert response.status_code == status.HTTP_200_OK
    assert response.data == 7

def test_warehouse_creation(client):
    url = reverse('warehouse-list')
    data = {'name': 'Warehouse 1'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

def test_product_creation(client):
    url = reverse('product-list')
    data = {'name': 'Product 1'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

def test_warehouse_validation(client, warehouse):
    url = reverse('warehouse-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

def test_product_validation(client, products):
    url = reverse('product-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5

def test_warehouse_stock_validation(client, warehouse, products):
    warehouse.products.add(*products)
    warehouse.save()
    url = reverse('warehouse-detail', args=[warehouse.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['products_count'] == 5

def test_warehouse_stock_update(client, warehouse, products):
    warehouse.products.add(products[0])
    warehouse.save()
    url = reverse('warehouse-detail', args=[warehouse.id])
    response = client.patch(url, {'remove_product': products[0].id})
    assert response.status_code == status.HTTP_200_OK
    assert response.data['products_count'] == 0