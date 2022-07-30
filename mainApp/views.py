from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import LoginForm, RegisterForm


def RegisterView(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = RegisterForm() 
    return render(request, 'register.html',{'form':fm})

def LoginView(request):
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uemail = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uemail, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        fm = LoginForm()
    return render(request, 'login.html',{'form':fm})
