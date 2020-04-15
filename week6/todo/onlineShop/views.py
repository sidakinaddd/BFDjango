from django.http import Http404

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


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

    @action(methods=['Get'], detail=True)
    def products(self, request, pk):
        cur_status = self.request.query_params.get('status', None)
        if cur_status == '1':
            # category = Category.objects.get(id=self.kwargs['pk'])
            data = Product.sold_out_products.all()
            serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)
        elif cur_status == '2':

            data = Product.in_sell_products.all()
            serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = Product.objects.filter(category=Category.objects.get(id=self.kwargs['pk']))
            serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)

# class ProductView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         # print(Product.objects.filter(id=self.kwargs.get('pk2')))
#         category = Category.objects.get(id=self.kwargs['pk'])
#         return category.product_set.all()
#
#     def get_serializer_class(self):
#         return ProductSerializer
