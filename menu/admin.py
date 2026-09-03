from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'image')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_formatted', 'tags')
    list_filter = ('category',)
    search_fields = ('name', 'tags')