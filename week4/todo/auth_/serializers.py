from rest_framework import serializers

from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'is_superuser', 'password')

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user
