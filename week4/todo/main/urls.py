from django.urls import path
from .views import ToDoListView, ToDoListsView,ToDosView, ToDoView

urlpatterns = [
    path('', ToDoListsView.as_view()),
    path('<int:pk>/', ToDoListView.as_view()),
    path('<int:pk>/todo/', ToDosView.as_view()),
    path('<int:pk>/todo/<int:pk2>/', ToDoView.as_view()),
]