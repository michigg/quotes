from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Quote, Statement, Author, Gif

# Register your models here.
admin.site.register(Quote)
admin.site.register(Statement)
admin.site.register(Author)
admin.site.register(Gif)

UserAdmin.list_display = ('id',) + UserAdmin.list_display
