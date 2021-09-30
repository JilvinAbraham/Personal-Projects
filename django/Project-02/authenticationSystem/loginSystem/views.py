from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signIn(request):
    if request.user.is_authenticated:
        return HttpResponse('This is the home page')
    else:

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("This is the home page")
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, 'loginSystem/signIn.html')


def signUp(request):
    if request.user.is_authenticated:
        return HttpResponse('This is the home page')
    else:

        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "User {0} created succesfully.".format(user))
                return redirect('users-signin')

        context = {'form': form}
        return render(request, 'loginSystem/signUp.html', context)


def logoutUser(request):
    print(request.user)
    logout(request)
    return redirect('users-signin')
