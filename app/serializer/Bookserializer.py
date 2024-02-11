from rest_framework import serializers
from app.models.bookmodels import Book

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ "title", "author"]