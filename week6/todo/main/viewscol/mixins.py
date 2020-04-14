from rest_framework import generics
from rest_framework import mixins
from ..serializers import TodoListsSerializer, TodoListSerializer
from ..models import ToDoList
from rest_framework.permissions import IsAuthenticated

class TodoListsView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoListsSerializer

    def get_queryset(self):
        return ToDoList.objects.for_user(user=self.request.user)
    lookup_field = 'pk'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)


class TodoListView(generics.GenericAPIView,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoListSerializer

    def get_one(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)