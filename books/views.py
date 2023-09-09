from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from books.serializers import BookSerializer

from books.models import Book

class BookListAPIView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
    def get(self, request):
        books=Book.objects.all()
        books_list=[book.title for book in books]
        return Response(books_list)
