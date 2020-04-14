from rest_framework import serializers
from .models import ToDo, ToDoList
from auth_.serializers import UserSerializer


class TodoListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = UserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'owner', 'created_at')


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    todo_list = TodoListSerializer(required=False)
    is_done = serializers.BooleanField(required=True)

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'todo_list', 'is_done')
