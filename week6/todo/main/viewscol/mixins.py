from rest_framework import generics
from rest_framework import mixins, viewsets
from ..serializers import TodoListSerializer
from ..models import ToDoList,ToDo
from rest_framework.permissions import IsAuthenticated

class TodoListsView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)