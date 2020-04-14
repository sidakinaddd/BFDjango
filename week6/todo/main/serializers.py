from rest_framework import serializers
from .models import ToDo, ToDoList
from auth_.serializers import UserSerializer


class TodoListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'owner', 'created_at')


class TodoListsSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'name')


class TodosSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # todo_list = TodoListSerializer(read_only=True)
    is_done = serializers.BooleanField(read_only=True)

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'is_done')


class TodoSerializer(serializers.ModelSerializer):
    todo_list = TodoListSerializer(read_only=True)

    # is_done = serializers.BooleanField(read_only=True)

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'is_done', 'created_at', 'finish_on', 'is_done', 'todo_list')
