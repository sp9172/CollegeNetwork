from django.http import HttpResponseRedirect
from django.shortcuts import render
from . forms import SingUpForm,UserLoginForm

# Create your views here.
# def Home(request):
#     return HttpResponseRedirect('index.html')


def Home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def singup(request):
    form=SingUpForm()


    return render(request,'Registration.html',{'form':form})


def user_login(request):
    form = UserLoginForm()
    return render(request,'Login.html',{'form':form})
