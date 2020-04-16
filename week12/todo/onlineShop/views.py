from django.http import Http404
import logging

from rest_framework.decorators import action

from rest_framework import viewsets, generics, status
from rest_framework import mixins
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

logger = logging.getLogger('categories')


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        is_top = self.request.query_params.get('status', None)

        if is_top == "True":
            return Category.top_categories.all()

        elif is_top == "False":
            print(is_top)
            return Category.not_top_categories.all()
        elif is_top is None:
            return Category.objects.all()
        else:
            logger.warning("Please give exact status of category. If this category is on top, write True, else False")
        # return Category.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['Get'], detail=True)
    def products(self, request, pk):

        cur_status = self.request.query_params.get('status', None)
        print(cur_status)
        if cur_status == '1':
            data = Product.sold_out_products.all()
            if data.count() == 0:
                logger.info("This category has no in_sell products")
            else:
                serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)
        elif cur_status == '2':
            data = Product.in_sell_products.all()
            if data.count() == 0:
                logger.info("This category has no sold_out products")
            else:
                serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)
        elif cur_status is None:
            data = Product.objects.filter(category=Category.objects.get(id=self.kwargs['pk']))
            if data.count() == 0:
                logger.warning("This category has no products")

            serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)
        elif cur_status not in ('1', '2', None):

            logger.warning("Please give exact status of category. If you want in_sell products , write 1 , else 2")
