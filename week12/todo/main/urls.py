from django.urls import path
from rest_framework import routers

from .views import ToDoListView, ToDoListsView,ToDosView, ToDoView
from .viewscol.views import ToDoListCBV, ToDoListsCBV
from .viewscol import views
from .viewscol.mixins import TodoListsView,TodoListTodosView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'lists', TodoListsView,basename='lists')
router.register(r'lists/<int:pk>/todo', TodoListTodosView, basename='list-todos')

urlpatterns = [
    path('', ToDoListsView.as_view()),
    path('<int:pk>/', ToDoListView.as_view()),
    path('<int:pk>/todo/', ToDosView.as_view()),
    path('<int:pk>/todo/<int:pk2>/', ToDoView.as_view()),
    # path('cbv/', views.ToDoListsCBV.as_view()),
    # path('cbv/<int:pk>/', views.ToDoListsCBV.as_view()),
]+router.urls

# urlpatterns = format_suffix_patterns(urlpatterns) + router.urls
