from django.test import TestCase

from apps.story.models import Product, ProductCategory
from apps.story.serializers import ProductSerializer, ProductCategorySerializer


class ProductSerializerTestCase(TestCase):

    def test_product_serializer(self):
        product = Product.objects.create(name='Наушники', description='супер', price=20000)
        srz = ProductSerializer(product, many=False)
        expected_data = {
            'id': product.id,
            'name': 'Наушники',
            'description': 'супер',
            'price': 20000,
        }
        self.assertEqual(srz.data, expected_data)

    def test_product_serializer_many(self):
        Product.objects.create(name='Наушники', description='супер', price=20000)
        Product.objects.create(name='Наушники', description='супер', price=20000)
        product_qs = Product.objects.all()
        srz = ProductSerializer(product_qs, many=True)
        self.assertIsInstance(srz.data, list)
        self.assertEqual(len(srz.data), 2)


class ProductCategorySerializerTestCase(TestCase):

    def test_product_category_serializer(self):
        cat1 = ProductCategory.objects.create(title='Электроника')
        srz = ProductCategorySerializer(cat1, many=False)
        expected_data = {
            'id': cat1.id,
            'name': 'Электроника',
            'products': [],
        }
        result = srz.data
        self.assertEqual(result, expected_data)

    def test_product_category_with_product_serializer(self):
        cat1 = ProductCategory.objects.create(title='Электроника')
        phone = Product.objects.create(name='Xiaomi Note 10 PRO', price=20000,
                                       description='новинка', category=cat1)

        srz = ProductCategorySerializer(cat1, many=False)
        expected_data = {
            'id': cat1.id,
            'name': 'Электроника',
            'products': [
                {
                    'id': phone.id,
                    'name': phone.name,
                    'description': phone.description,
                    'price': phone.price,
                    'category_name': cat1.title,
                }
            ],
        }
        result = srz.data
        self.assertEqual(result, expected_data)

