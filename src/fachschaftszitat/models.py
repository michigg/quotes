from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

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
        if self.author:
            return f'{self.author.name}: {self.text[:40] + ".." if len(self.text) > 40 else self.text}'
        else:
            return f'{self.id}'


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Group, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateField(null=False, blank=False)
    statements = models.ManyToManyField('Statement')

    def __str__(self):
        return f'{self.id}: {", ".join(str(seg) for seg in self.statements.all())}'


@receiver(pre_delete, sender=Quote)
def delete_related_statements(sender, instance, using, **kwargs):
    for statement in instance.statements.all():
        statement.delete()


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_AUTHOR_LENGTH, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Gif(models.Model):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"
    TYPE_CHOICES = [(ERROR, "Error"), (SUCCESS, "Success")]

    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    video_url = models.URLField(unique=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} - {self.type} - {self.creator} - {self.video_url}'
