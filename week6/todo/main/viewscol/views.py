from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from ..models import ToDoList
from ..serializers import TodoListsSerializer, TodoListSerializer
from django.http import Http404


# class based viewscol


class ToDoListsCBV(APIView):
    def get(self, request, format=None):
        todo_lists = ToDoList.objects.for_user(user=self.request.user)
        serializer = TodoListsSerializer(todo_lists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoListCBV(APIView):
    def get_object(self, pk):
        try:
            return ToDoList.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        todo_list = self.get_object(pk)
        serializer = TodoListSerializer(todo_list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo_list = self.get_object(pk)
        serializer = TodoListSerializer(todo_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo_list = self.get_object(pk)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
