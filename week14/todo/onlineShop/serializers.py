from rest_framework import serializers
from .models import Category, Product
from rest_framework.validators import UniqueTogetherValidator

from auth_.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    def validate(self, data):
        if len(data['name']) < 3:
            raise serializers.ValidationError("name should contain at least 3 letters")
        return data

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'status', 'description', 'image', 'attachment')
        read_only_fields = ['owner']
        validators = [
            UniqueTogetherValidator(
                queryset=Category.objects.all(),
                fields=['name', 'description']
            )
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'description', 'price', 'status')
