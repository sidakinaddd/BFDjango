from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, UserProfile

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


@admin.register(UserProfile)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city')

