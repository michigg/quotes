from django.db import models

MAX_QUOTE_LENGTH = 1024
MAX_AUTHOR_LENGTH = 32


# Create your models here.
class Statement(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=MAX_QUOTE_LENGTH)
    order_id = models.PositiveIntegerField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['order_id']

    def __str__(self):
        return f'{self.author.name}: {self.text[:40] + ".." if len(self.text) > 40 else self.text}'


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateField(null=False, blank=False)
    statements = models.ManyToManyField('Statement', null=False, blank=False)

    def __str__(self):
        return f'{self.id}: {", ".join(str(seg) for seg in self.statements.all())}'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_AUTHOR_LENGTH, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
