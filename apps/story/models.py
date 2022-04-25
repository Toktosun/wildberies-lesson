from django.db import models, transaction


class ProductCategory(models.Model):
    """Категория товаров"""

    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """Модель для Товаров"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, null=True,
                                 related_name='products')

    @property
    def category_name(self):
        return self.category.title

    def __str__(self):
        return self.name


# cat = ProductCategory.objects.create(title='Электроника')
# prod1 = Product.objects.create(category=cat, name='Айфон')
# prod2 = Product.objects.create(category=cat, name='Эирподс')
# prod3 = Product.objects.create(category=cat, name='Монитор')
#
# print(prod3.name)  # Монитор
# print(prod2.category.title)  # Электроника
# print(cat.title)  # Электроника
#
# print(cat.products.all())  # куерисет [prod1, prod2, prod3]


# class Genre(models.Model):
#     title = models.CharField()
#
#
# class Cinema(models.Model):
#     title = models.CharField()
#     genre = models.ForeignKey(to=Genre, related_name='movies')
#
#
# Genre.objects.prefetch_related('movies').all()
# Cinema.objects.select_related('genre').all()
#
#
# # harry_potter = Cinema.objects.first()
# # harry_potter.genre.title  # Фантастика
# #
# # fantastic = Genre.objects.first()
# # fantastic.movies.all()  # куерисет [мстители, поттер, властелин колец]
#
#
# class HashTag(models.Model):
#     name = models.CharField(unique=True)
#
#
# class Publication(models.Model):
#     image = models.ImageField()
#     tags = models.ManyToManyField(to=HashTag, related_name='publications')
#
#
# publication_qs = Publication.objects.prefetch_related('tags').all()
# for pub in publication_qs:
#     print(pub.tags.all())
#
#
# hashtags_qs = HashTag.objects.prefetch_related('publications').all()
# for tag in hashtags_qs:
#     print(tag.publications.all())
#

# class ElectronicProduct(models.Model):
#     name = models.CharField()
#
#
# class ElectronicProductDetail(models.Model):
#     memory = models.CharField()
#     battery = models.CharField()
#     product = models.OneToOneField(to=ElectronicProduct, related_name='detail')
#
#
# products = ElectronicProduct.objects.select_related('detail').all()
# for p in products:
#     print(p.detail.memory)
#
#
# details = ElectronicProductDetail.objects.select_related('product').all()
# for d in details:
#     print(d.product.name)
