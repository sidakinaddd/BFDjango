from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from todo_app import views


urlpatterns = [
    path('todos/',views.ManyListsView.as_view()),
    path('todos/<int:pk>/',views.OneListView.as_view()),
]
