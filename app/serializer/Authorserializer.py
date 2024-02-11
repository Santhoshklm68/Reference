from rest_framework import serializers
from app.models.authormodels import Author


class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =  [ "name", "bio"]

    