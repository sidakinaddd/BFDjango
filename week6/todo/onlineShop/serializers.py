from rest_framework import serializers
from .models import Category, Product
from auth_.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner')


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=False)
    category = CategorySerializer(read_only=True)
    description = serializers.CharField(read_only=False)
    price = serializers.IntegerField(read_only=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'description', 'price')
