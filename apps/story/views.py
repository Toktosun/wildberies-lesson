from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.story.models import Product, ProductCategory
from apps.story.serializers import ProductSerializer, ProductCategorySerializer


# альтернатива
# @api_view(['GET', 'POST'])
# def api_products(request):
#     if request.method == 'GET':
#         product_qs = Product.objects.all()
#         srz = ProductSerializer(product_qs, many=True)
#         return Response(srz.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         request_body = request.data
#         new_product = Product.objects.create(name=request_body['name'],
#                                              description=request_body['description'],
#                                              price=request_body['price'])
#         srz = ProductSerializer(new_product, many=False)
#         return Response(srz.data, status=status.HTTP_201_CREATED)


# select_related
# prefetch_related

# class ProductListAPIView(ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()


class ProductListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Get list of products',
        responses={
            '200': ProductSerializer(many=True),
        },
    )
    def get(self, request):
        product_qs = Product.objects.select_related('category').all()
        srz = ProductSerializer(product_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Create a product',
        request_body=ProductSerializer(many=False),
        responses={
            '201': ProductSerializer(many=False),
        },
    )
    def post(self, request):
        request_body = request.data
        new_product = Product.objects.create(
            name=request_body['name'], description=request_body['description'],
            price=request_body['price'])
        srz = ProductSerializer(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


# class ProductRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#

class ProductRetrieveAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Get detail of product',
        responses={
            '200': ProductSerializer(many=False),
            '404': 'Product not found.',
        }
    )
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        srz = ProductSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Delete a product',
        request_body=None,
        responses={'204': None}
    )
    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='Update detail of product',
        responses={
            '200': ProductSerializer(many=False),
        },
        request_body=ProductSerializer(many=False)
    )
    def put(self, request, pk):
        request_body = request.data
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404
        product.name = request_body['name']
        product.description = request_body['description']
        product.price = request_body['price']
        product.save()
        srz = ProductSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)


# альтернатива
# @api_view(['GET', 'DELETE'])
# def api_product(request, pk):
#     if request.method == 'GET':
#         try:
#             product = Product.objects.get(id=pk)
#         except Product.DoesNotExist:
#             return Response({'message': 'Product not found.'},
#                             status=status.HTTP_404_NOT_FOUND)
#         srz = ProductSerializer(product, many=False)
#         return Response(srz.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         try:
#             product = Product.objects.get(id=pk)
#         except Product.DoesNotExist:
#             return Response({'message': 'Product not found.'},
#                             status=status.HTTP_404_NOT_FOUND)
#         product.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryListAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Get categories with products',
        responses={
            '200': ProductCategorySerializer(many=True),
        },
    )
    def get(self, request):
        category_qs = ProductCategory.objects.all()
        srz = ProductCategorySerializer(category_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)
