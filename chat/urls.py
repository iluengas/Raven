# urls.py

from django.urls import path
from .views import base_view

urlpatterns = [
    path('', base_view, name='base_view'),
]