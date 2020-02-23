from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.serializers import ItemSerializer, ListSerializer
from .models import List, Item
from django.http import Http404
class ManyListsView(APIView):

    def get(self, request, format=None):
        lists = List.objects.all()
        serializer=ListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=ListSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OneListView(APIView):
    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        list =self.get_object(pk)
        serializer = ListSerializer(list, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        list=self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)