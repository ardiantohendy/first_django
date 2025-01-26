from django.urls import path
from . import views #import from views.py

urlpatterns = [
    path('', views.index, name = 'index'),
    path('counter', views.counter, name = 'counter')
]