from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from users.forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.


def loginUserPage(req):
    return render(req, 'users/pages/login.html')


def registerPage(req):
    form = CustomUserCreationForm()

    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(req, 'User account was created!')
            login(req, user)
            return redirect('profile')

        else:
            messages.error(req, 'An error has occurred during registration')

    context = {'form': form}
    return render(req, 'users/pages/register.html', context)


def profilePage(req):
    return render(req, 'users/pages/profile.html')
