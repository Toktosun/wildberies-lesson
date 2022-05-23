"""wildberies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.story.views import ProductListCreateAPIView, \
    ProductRetrieveAPIView, ProductCategoryListAPIView, GetMeAPIView, \
    NewsViewSet, ProfileAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Wildberies API",
      default_version='v1',
      description="RESTful app for provide API for mobile & web-front applications. ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),

    # regex
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

    path('api/v1/products/', ProductListCreateAPIView.as_view(), name='products-url'),
    path('api/v1/products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-url'),
    path('api/v1/categories/', ProductCategoryListAPIView.as_view(), name='categories-url'),
    path('api/v1/me/', GetMeAPIView.as_view()),
    path('api/v1/profile/', ProfileAPIView.as_view()),

    path('api/v1/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += router.urls
