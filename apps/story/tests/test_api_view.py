from django.urls import reverse
from rest_framework.test import APITestCase

from apps.story.models import Product


class ProductsAPITestCase(APITestCase):

    def test_products_view_with_no_exists_products(self):
        url = reverse('products-url')  # url = "/api/v1/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 0)

    def test_products_view_with_product(self):
        new_product = Product.objects.create(name='Телефон', description='Надёжный и китайский', price=25000)
        url = reverse('products-url')  # url = "/api/v1/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], new_product.id)
        self.assertEqual(response.data[0]['name'], new_product.name)
        self.assertEqual(response.data[0]['description'], new_product.description)
        self.assertEqual(response.data[0]['price'], new_product.price)


class ProductRetrieveAPIViewTestCase(APITestCase):

    def setUp(self):  # записи которые созданы в сетапе доступны во всех методах
        self.new_product = Product.objects.create(name='Телефон',
                                             description='Надёжный и китайский',
                                             price=25000)

    def test_get_product(self):  # записи которые создаются в тест-кейс методе, удаляются после выполнения тест-кейс метода
        url = reverse('product-url', kwargs={'pk': self.new_product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.new_product.id)
        self.assertEqual(response.data['name'], self.new_product.name)
        self.assertEqual(response.data['description'], self.new_product.description)
        self.assertEqual(response.data['price'], self.new_product.price)

    def test_delete_product(self):
        url = reverse('product-url', kwargs={'pk': self.new_product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_get_product_not_exists(self):
        url = reverse('product-url', kwargs={'pk': 123432})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_update_product_by_put(self):
        url = reverse('product-url', kwargs={'pk': self.new_product.id})
        update_product_data = {
            'name': 'Телефон обновленный',
            'description': 'Надёжный и китайский и обновленный',
            'price': 30000,
        }
        response = self.client.put(url, data=update_product_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.new_product.id)
        self.assertEqual(response.data['name'], update_product_data['name'])
        self.assertEqual(response.data['description'], update_product_data['description'])
        self.assertEqual(response.data['price'], update_product_data['price'])
        updated_product = Product.objects.get(id=self.new_product.id)  # обновляем переменную из базы данных
        self.assertEqual(updated_product.name, update_product_data['name'])
        self.assertEqual(updated_product.description, update_product_data['description'])
        self.assertEqual(updated_product.price, update_product_data['price'])
