from . import views
from django.urls import path

urlpatterns = [
    path('', views.profilePage, name="profile"),
    path('login/', views.loginUserPage, name="login"),
    path('register/', views.registerPage, name="register"),
]
