from django.contrib import admin
from .models import Manufacturer, Car, FCUser

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(FCUser)