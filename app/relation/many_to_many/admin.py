from django.contrib import admin

# Register your models here.
from relation.many_to_many.models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)