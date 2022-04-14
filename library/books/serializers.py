from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['id', 'name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
	# author = AuthorSerializer()
	authors = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Book
		fields = ['id', 'name', 'publish_year', 'pages', 'price', 'created_at', 'updated_at', 'authors']
	
	"""
	# def f(*args,**kwargs):  f(1,2,3,key1:4,key2:5):

	def create(self, vdata):
		author = vdata.pop('author')
		author_instance = Author.objects.create(**author)
		book_instance = Book.objects.create(author = author_instance, **vdata)
		return book_instance
	"""

class BooksAuthorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = BooksAuthors
		fields = ['id', 'book', 'author']


class BooksCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksCountry
        fields = ['id', 'book', 'country']

class BooksCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksCategory
        fields = ['id', 'book', 'category']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']