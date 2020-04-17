from .models import MyUser
from .serializers import UserSerializer
from rest_framework import generics

from rest_framework.permissions import AllowAny


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return MyUser.objects.all()

    def perform_create(self, serializer):
        username = self.request.data.pop('username')
        password = self.request.data.pop('password')

        user,created=MyUser.objects.get_or_create(username=username)
        user.set_password(password)
        user.save()
