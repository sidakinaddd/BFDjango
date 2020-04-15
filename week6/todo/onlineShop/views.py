from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
# Create your views here.
class CategoryView(mixins.ListModelMixin,
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