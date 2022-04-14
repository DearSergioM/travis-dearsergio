from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'booksauthor', views.BooksAuthorsViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'bookscategory', views.BooksCountryViewSet)
router.register(r'bookscountry', views.BooksCategoryViewSet)
router.register(r'', views.BookViewSet)

urlpatterns = [
	path('', include(router.urls)),
]