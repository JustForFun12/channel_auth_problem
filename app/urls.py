from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('room/<str:group_name>', views.room),
    path('login', views.login)
]
