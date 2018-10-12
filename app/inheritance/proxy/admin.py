from django.contrib import admin

# Register your models here.
from inheritance.proxy.models import User1


class User1Admin(admin.ModelAdmin):
    list_display = ['name', 'is_admin']


admin.site.register(User1, User1Admin)
