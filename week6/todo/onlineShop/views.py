from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.

# class CategoryViewSet(NestedViewSetMixin,ModelViewSet):
#     serializer_class = CategorySerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         return Category.objects.for_user(user=self.request.user)
#
#
# class ProductViewSet(NestedViewSetMixin,ModelViewSet):
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticated, )
#     queryset = Product.objects.all()

class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Product.objects.filter(category=Category.objects.get(id=3))

    def perform_create(self, serializer):
        category_id = self.kwargs.get('pk')
        serializer.save(category=Category.objects.get(id=category_id))
