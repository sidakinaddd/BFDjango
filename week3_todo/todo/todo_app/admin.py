from django.contrib import admin
from .models import List
# Register your models here.
from .models import Item
admin.site.register(List)
admin.site.register(Item)
