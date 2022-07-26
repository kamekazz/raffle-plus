from django.shortcuts import render

# Create your views here.


def loginUserPage(req):
    return render(req, 'users/pages/login.html')


def registerPage(req):
    return render(req, 'users/pages/register.html')


def profilePage(req):
    return render(req, 'users/pages/profile.html')
