from django.urls import  path

from .views import testing

urlpatterns = [
    path('', testing, name="test")
]