from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Quote, Statement, Author

# Register your models here.
admin.site.register(Quote)
admin.site.register(Statement)
admin.site.register(Author)

UserAdmin.list_display = ('id',) + UserAdmin.list_display
