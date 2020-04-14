from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import ToDoList, ToDo
from .serializers import TodoListSerializer, TodoSerializer, TodoListsSerializer,TodosSerializer
from django.http import Http404

class ToDoListsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDoList.objects.for_user(user=self.request.user)

    def get_serializer_class(self):
        return TodoListsSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class ToDoListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TodoListSerializer


class ToDosView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDo.objects.filter(todo_list=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TodosSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('pk')
        serializer.save(list=ToDoList.objects.get(id=list_id))


class ToDoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDo.objects.filter(todo_list=self.kwargs.get('pk'), id=self.kwargs.get('pk2'))

    def get_serializer_class(self):
        return TodoSerializer
