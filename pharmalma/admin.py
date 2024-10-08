# pharmalma/admin.py

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cis_code', 'cip_code')  # Champs à afficher dans la liste
    search_fields = ('name', 'cis_code', 'cip_code')         # Champ de recherche
