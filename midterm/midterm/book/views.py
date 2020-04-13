from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.http import Http404
from rest_framework import mixins, generics
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView

class BookListAPIView(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = ( IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # self.top_ten()
        return self.list(request, *args, **kwargs)
    def post(self, request, format=None):
        serializer=BookSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OneBookView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = BookSerializer(list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        list =self.get_object(pk)
        serializer = BookSerializer(list, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        list=self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalListAPIView(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    permission_classes = ( IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # self.top_ten()
        return self.list(request, *args, **kwargs)
    def post(self, request, format=None):
        serializer=JournalSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OneJournalView(APIView):
    def get_object(self, pk):
        try:
            return Journal.objects.get(pk=pk)
        except Journal.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = JournalSerializer(list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        list =self.get_object(pk)
        serializer = JournalSerializer(list, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        list=self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)