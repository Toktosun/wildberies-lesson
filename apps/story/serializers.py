from rest_framework import serializers

from apps.story.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(min_value=0, max_value=100_000, required=True,
                                     help_text='текущая цена для товара. может быть отредактирован администратором')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category_name',)


class ProductCategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)
    name = serializers.CharField(source='title')

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'products')
