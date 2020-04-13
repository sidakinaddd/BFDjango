from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','user_type')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )