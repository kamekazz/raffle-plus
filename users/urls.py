from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginUser, name="login"),
]
