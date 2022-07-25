from . import views
from django.urls import path

urlpatterns = [
    path('', views.loginUser, name="home"),
    path('login/', views.loginUser, name="login"),
]
