from django.shortcuts import render

# Create your views here.


def loginUser(req):
    return render(req, 'users/pages/login.html')
