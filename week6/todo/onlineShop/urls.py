from django.urls import path
from rest_framework import routers
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .views import CategoryViewSet, ProductViewSet
# from rest_framework_extensions.routers import NestedRouterMixin
#
# class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
#     pass
#
#
#
# router= NestedDefaultRouter()
# categories_router= router.register('categories', CategoryViewSet, basename='categories')
# categories_router.register(
#     'products',ProductViewSet,
#     basename='category-products',
#     parents_query_lookups=['category']
# )
router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'categories/<int:pk>/products', ProductViewSet, basename='category-products')
urlpatterns = router.urls
