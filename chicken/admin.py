from django.contrib import admin
from .models import chicken,chicken_data_upload

# Register your models here.
admin.site.register(chicken)
admin.site.register(chicken_data_upload)

class ChickenAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

