from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')           # <- no 'image' here
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'updated_at')  # fields that exist
    list_filter = ('category',)
    search_fields = ('name',)
