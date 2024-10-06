from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializer import BookSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
