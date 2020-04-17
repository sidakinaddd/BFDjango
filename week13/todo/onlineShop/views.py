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
from auth_.models import MyUser
logger = logging.getLogger('categories')


# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     print('Request finished')

# @receiver(post_save, sender=MyUser)
# def create_category_of_user(sender, instance, created,**kwargs):
#     if created:
#         Category.objects.create(name='New category',owner= instance)
#         print('category created')




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

    @action(methods=['GET', 'POST'], detail=True)
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


class ProductViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated)

    def get_queryset(self):
        return Product.objects.all()
