from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('books/',views.BookListAPIView.as_view()),
    path('journal/',views.JournalListAPIView.as_view()),
    # path('todos/<int:pk>/',views.OneListView.as_view()),
]
