from django.db import models
from .authormodels import Author


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title