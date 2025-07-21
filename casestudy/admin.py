from django.contrib import admin
from .models import Client, Location, Industry, Casestudy

# Register your models here.
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Industry)
admin.site.register(Casestudy)