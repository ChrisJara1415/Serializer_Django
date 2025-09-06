from django.contrib import admin

from .models import categoria, producto, marca

admin.site.register(categoria)
admin.site.register(producto)
admin.site.register(marca)