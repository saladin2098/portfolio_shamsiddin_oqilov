from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, UserCreationForm

# Create your views here.

def register_view(request):
    form = RegisterForm
    user = User
    if request.POST:
        form = RegisterForm(request.POST)
        print('Request POTS')
        if form.is_valid():
            form.save()
            print('Form save')
            return redirect('login-page')
        
    context = {'form': form}
    return render(request, 'register_page.html', context)



def login_view(request):

  
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username: ', username, 'password: ', password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('username or password is incorrect')             

    return render(request, 'login.html')
