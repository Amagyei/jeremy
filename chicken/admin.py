from django.contrib import admin
from .models import chicken

# Register your models here.
admin.site.register(chicken)

class ChickenAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

