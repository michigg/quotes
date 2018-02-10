from django.contrib import admin
from fachschaftszitat.models import Author, Quote

# Register your models here.
admin.site.register(Author, Quote)
