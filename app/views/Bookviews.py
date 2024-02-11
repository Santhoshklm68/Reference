from app.models.bookmodels import Book
from rest_framework import viewsets
from app.serializer.Bookserializer import Bookserializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer