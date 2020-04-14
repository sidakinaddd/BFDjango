from django.urls import path
from .views import ToDoListAPIView

urlpatterns = [
    path('todolists/', ToDoListAPIView.as_view())
]