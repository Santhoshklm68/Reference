from django.contrib import admin

from .models.authormodels import Author
from .models.bookmodels import Book

admin.site.register(Author)
admin.site.register(Book)
