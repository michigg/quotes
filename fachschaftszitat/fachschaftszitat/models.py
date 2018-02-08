from django.db import models

MAX_QUOTE_LENGTH = 1024
MAX_AUTHOR_LENGTH = 32


# Create your models here.
class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    quote = models.CharField(max_length=MAX_QUOTE_LENGTH, unique=True, null=False, blank=False)
    timestamp = models.DateField(null=False, blank=False)
    authors = models.ManyToManyField('Author', null=False, blank=False)

    def __str__(self):
        return self.quote


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_AUTHOR_LENGTH, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
