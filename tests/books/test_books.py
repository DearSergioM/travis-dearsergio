import pytest 
from library.books.models import *

#EJEMPLOS ====================================================

@pytest.mark.django_db
def test_author_name():
     author = Author.objects.create(name='Paulo', last_name='Coelho')
     print('This is my authors name: ', author.name)
     assert author.last_name == 'Coelho'
     assert Author.objects.all().count() == 1
     author.delete()
     assert Author.objects.all().count() == 0
    
@pytest.mark.django_db
@pytest.mark.parametrize(
    'nombre, apellido',
    (
        ('Paulo', 'Coelho'),
        ('Haruki', 'Murakami')
    )
)
def test_author_name(nombre, apellido):
    author = Author.objects.create(name=nombre, last_name=apellido)
    print('This is my authors name: ', author.name )
    assert Author.objects.all().count() == 1
    author.delete()
    assert Author.objects.all().count() < 1

#EJERCICIO ====================================================

@pytest.mark.django_db
def test_country_name():
    country = Country.objects.create(name='Canada')
    print('This is a country name: ', country.name)
    assert country.name == 'Canada'
    assert Country.objects.all().count() == 1
    country.delete()
    assert Country.objects.all().count() == 0

@pytest.mark.django_db
def test_country_name_is_str():
    country = Country.objects.create(name='Canada')
    print('This is a country name not a number: ', country.name)
    assert type(country.name)  is not int
    assert Country.objects.all().count() == 1
    country.delete()
    assert Country.objects.all().count() == 0

@pytest.mark.django_db
def test_category_name():
    category = Category.objects.create(name='Horror')
    print('This is a category name: ', category.name)
    assert category.name is not 'Sci-Fi'
    assert Category.objects.all().count() == 1
    category.delete()
    assert Category.objects.all().count() == 0

@pytest.mark.django_db
def test_book_name_price():
    book = Book.objects.create(name='Alice in Wonderland', publish_year=1865,
    pages=260, price=19.99)
    print('This is the book name: ', book.name, ' Price: $',book.price)
    assert book.name == 'Alice in Wonderland' and book.price is not 20.99
    assert Book.objects.all().count() == 1
    book.delete()
    assert Book.objects.all().count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize(
    'nombre, year, paginas ,precio',
    (
        ('100 años de soledad', 2015, 200 ,29.99),
        ('Nocturna', 2009, 350, 5.99),
        ('Oscura', 2010, 186, 6.99),
        ('Eterna', 2012, 284, 7.99)
    )
)
def test_book_year_price(nombre, year, paginas, precio):
    book = Book.objects.create(name=nombre, publish_year=year, pages=paginas, price=precio)
    print('This is my authors name: ', book.name, ' Year: ', book.publish_year, ' the price is: ', book.price)
    assert Book.objects.all().count() == 1
    book.delete()
    assert Book.objects.all().count() < 1



@pytest.mark.django_db
@pytest.mark.parametrize(
    'nombre, year, paginas ,precio',
    (
        ('100 años de soledad', 2015, 200 ,29.99),
        ('Nocturna', 2009, 350, 25.99),
        ('Oscura', 2010, 186, 16.99),
        ('Eterna', 2012, 284, 7.99)
    )
)
def test_bookprice(nombre, year, paginas, precio):
    book = Book.objects.create(name=nombre, publish_year=year, pages=paginas, price=precio)
    print('This is my books name: ', book.name, ' the price is less than 50.00: ', book.price)
    print('Less than 50 pavos: ',(float(book.price) <= 50.00))
    assert float(book.price) <= 50.00
    book.delete()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'libro, year, paginas ,precio, pais',
    (
        ('100 años de soledad', 2015, 200 ,29.99, 'Mexico'),
        ('Nocturna', 2009, 350, 5.99, 'Canada'),
        ('Oscura', 2010, 186, 6.99, 'USA'),
        ('Eterna', 2012, 284, 7.99, 'España')
    )
)
def test_book_country(libro, year, paginas ,precio, pais):
    book = Book.objects.create(name = libro,  publish_year=year, pages=paginas, price=precio)
    country = Country.objects.create(name = pais)
    print('This is my authors name: ', book.name, 'Pais de origen: ', country.name)
    assert country.name is not 'Russian'
    assert book.publish_year is not 1000
    country.delete()
    book.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
	'categoria',
	(
		('Fantasy'),
		('Drama'),
		('Romance'),
        ('Horror'),
        ('Sci-Fi'),
    )
)
def test_category_lenght(categoria):
    category = Category.objects.create(name = categoria)
    print('Categoria:', category.name)
    print('Menor de 128 caracteres: ',(len(category.name) <= 128))
    assert len(category.name) <= 128
    category.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
	'pais',
	(
		('MEX'),
		('USA'),
		('CHN'),
        ('SPA'),
        ('RUS'),
    )
)
def test_country_type(pais):
    country = Country.objects.create(name = pais)
    print('Categoria:', country.name)
    print('Es string: ',(type(country.name) is not int))
    assert type(country.name)  is not int
    country.delete()

# @pytest.mark.django_db
# def test_author_with_monkey(monkeypatch):
# 	autor = Author.objects.create(name='Nombre', last_name='Apellido')

# 	class AuthorQuerysetMock():
# 		def _init_(self):
# 			self.some_value = 1

# 		def count(self):
# 			return 4

# 	def model_count_mock():
# 		return AuthorQuerysetMock()

# 	monkeypatch.setattr(Author.objects, 'count', model_count_mock)

# 	assert Author.objects.all().count() == 4
# 	print('Haciendo el monkeypatch')