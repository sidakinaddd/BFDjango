from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import ToDoList, ToDo
from .serializers import TodoListSerializer, TodoSerializer


# Create your views here.
class ToDoListAPIView(mixins.ListModelMixin,
                      generics.GenericAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    # authentication_classes = (JSONWebTokenAuthentication)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
