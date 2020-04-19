from django.contrib import admin
from django.contrib import admin
# Register your models here.
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','status','description','price')
    search_fields = ['name', 'price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','owner', 'status')



# номера зантые не занятые 2 менеджера

