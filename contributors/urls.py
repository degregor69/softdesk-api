from django.urls import path
from .views import add_contributor

urlpatterns = [
    path('add/', add_contributor, name='add_contributor'),
]
