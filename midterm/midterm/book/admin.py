from django.contrib import admin
from .models import  Book, Journal
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'created_date', 'num_pages', 'publisher')
    # search_fields = ('name', 'price')
    # ordering = ('-price',)


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'created_date', 'type', 'publisher')
