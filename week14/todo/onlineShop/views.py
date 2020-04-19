from django.http import Http404
import logging
from django.core.signals import request_finished
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.decorators import action, api_view

from rest_framework import viewsets, generics, status
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        is_top = self.request.query_params.get('status', None)
        if is_top == "True":
            user_categories = Category.top_categories.filter(owner=self.request.user)
        elif is_top == "False":
            user_categories = Category.not_top_categories.filter(owner=self.request.user)
        elif is_top is None:
            user_categories = Category.objects.filter(owner=self.request.user)
        return user_categories

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        logger.info(f'Category with id = {serializer.data["id"]} has been created by user')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Category with id = {serializer.data["id"]} has been updated by user ')

    @action(methods=['GET', 'POST'], detail=True)
    def products(self, request, pk):
        cur_status = self.request.query_params.get('status', None)
        if cur_status == '1':
            data = Product.sold_out_products.all()
        elif cur_status == '2':
            data = Product.in_sell_products.all()
        elif cur_status is None:
            data = Product.objects.filter(category=Category.objects.get(id=self.kwargs['pk']))
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Product with id = {serializer.data["id"]} has been created by user')
