from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'quiz_app'
urlpatterns = [
    path('main/', views.show_mainpage, name = 'quiz_mainpage'),

]
