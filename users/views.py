from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from users.forms import CustomUserCreationForm

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
            print('User account was created')
            login(req, user)
            return redirect('profile')

        else:
            print('an error has ocurred during registration')

    context = {'form': form}
    return render(req, 'users/pages/register.html', context)


def profilePage(req):
    return render(req, 'users/pages/profile.html')
