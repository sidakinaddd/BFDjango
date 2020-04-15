from django.urls import path
from rest_framework import routers
from .models import Product, Category
from .serializers import  ProductSerializer, CategorySerializer
from .views import CategoryView
router = routers.DefaultRouter()
router.register('categories', CategoryView, basename='lists')

urlpatterns = router.urls