from django.contrib import admin
from django.contrib import admin
# Register your models here.
from .models import Category, Product

@admin.register(Category,Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # fieldsets = (
    #     (None, {'fields': ('name', 'created_at')}),
    # )
    search_fields = ['name']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owmer=request.user)

    # номера зантые не занятые 2 менеджера