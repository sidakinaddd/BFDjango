from rest_framework import generics
from rest_framework import mixins, viewsets
from ..serializers import TodoListSerializer, TodoSerializer
from ..models import ToDoList, ToDo

from rest_framework.permissions import IsAuthenticated


class TodoListsView(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoListSerializer

    def get_queryset(self):
        return ToDoList.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoListTodosView(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(todo_list=self.kwargs.get('pk'))


    def perform_create(self, serializer):
        list_id = self.kwargs.get('pk')
        serializer.save(list=ToDoList.objects.get(id=list_id))

