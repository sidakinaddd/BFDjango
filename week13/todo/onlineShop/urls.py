from django.urls import path
from rest_framework import routers
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'products', ProductViewSet, basename='products')

# router.register(r'products', ProductsViewSet, basename='category-products')
urlpatterns = router.urls
