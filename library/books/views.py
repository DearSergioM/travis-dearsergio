from rest_framework import viewsets
from rest_framework import permissions
from library.books.serializers import *

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = []

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []

class BooksCountryViewSet(viewsets.ModelViewSet):
    queryset = BooksCountry.objects.all()
    serializer_class = BooksCountrySerializer
    permission_classes = []

class BooksCategoryViewSet(viewsets.ModelViewSet):
    queryset = BooksCategory.objects.all()
    serializer_class = BooksCategorySerializer
    permission_classes = []

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer
    permission_classes = []

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = []