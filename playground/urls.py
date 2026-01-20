from django.urls import path
from . import views

# URL Configuration - URLconf
urlpatterns = [
    path('', views.first_page),
    path('hello/', views.say_hello),
]