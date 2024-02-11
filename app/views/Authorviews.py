from app.models.authormodels import Author
from app.serializer.Authorserializer import Authorserializer
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Authorserializer