from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request,'dashboard.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,'Invalid credentials')
            return render(request,'login.html')
    context={}
    return render(request,'login.html')


def Register(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,user + ' You have successfully registered')
            

            return render(request,'login.html')
        else:
            #messages.success(request, 'You have not successfully registered')
            context = {'form':form}
            return render(request,'Registeradmin.html',context)


    context = {'form':form}
    return render(request,'Registeradmin.html',context)

