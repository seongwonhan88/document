from django.contrib import admin

# Register your models here.
from many_to_many.models import Pizza, Topping, FacebookUser

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
