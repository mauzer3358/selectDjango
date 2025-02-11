from django.contrib import admin
from .models import DirectorModel

# Register your models here.

@admin.register(DirectorModel)
class Dirctor(admin.ModelAdmin):
    list_display = ('name', 'genre', 'experience','price')
    search_fields = ('name', 'price',)
    list_per_page = 5