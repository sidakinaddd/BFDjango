from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ToDo, ToDoList


# Register your models here.
@admin.register(ToDoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # fieldsets = (
    #     (None, {'fields': ('name', 'created_at')}),
    # )
    ordering = ['created_at']
    search_fields = ['name']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owmer=request.user)




@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_done',)
    list_filter = (
        ('todo_list', admin.RelatedOnlyFieldListFilter),
    )
    ordering = ['created_at']
    search_fields = ['name']

