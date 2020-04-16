from .models import MyUser
from .serializers import UserSerializer
from rest_framework import generics

from rest_framework.permissions import AllowAny


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserSerializer
