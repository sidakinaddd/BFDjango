from django.contrib import admin
from django.contrib import admin
# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ['name', 'status']
# номера зантые не занятые 2 менеджера

