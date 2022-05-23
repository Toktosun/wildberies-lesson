from django import forms
from django.contrib import admin
from .models import Product, ProductCategory, News


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def has_add_permission(self, request):
        news_count = News.objects.all().count()
        if news_count >= 1:
            return False
        else:
            return True
