from django.shortcuts import render

from users.forms import CustomUserCreationForm

# Create your views here.


def loginUserPage(req):
    return render(req, 'users/pages/login.html')


def registerPage(req):
    form = CustomUserCreationForm()
    context = {'form': form}
    return render(req, 'users/pages/register.html', context)


def profilePage(req):
    return render(req, 'users/pages/profile.html')
