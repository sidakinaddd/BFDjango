from django.urls import path
from rest_framework import routers
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .views import CategoryViewSet, ProductView, ProductsViewSet

router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'products', ProductsViewSet, basename='category-products')
urlpatterns = [
    path('categories/<int:pk>/products/<int:pk2>',ProductView.as_view()),

]+router.urls
