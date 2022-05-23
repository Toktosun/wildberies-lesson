from django.db import models, transaction


class ProductCategory(models.Model):
    """Категория товаров"""

    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class TimeStampModel(models.Model):
    """Абстрактная Модель для отслеживание времени изменений"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class News(TimeStampModel):
    """Модель для новостей"""

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=True)
    description = models.TextField()


# class SocialNetwork(models.Model):  # TODO: хотим чтобы в данной модельке(*таблице в бд) было ТОЛЬКО ОДНА запись
#     facebook = models.URLField()
#     instagram = models.URLField()
