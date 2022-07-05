import http
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . forms import SingUpForm,UserLoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def Home(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return HttpResponseRedirect('login')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
@csrf_exempt
def singup(request):
    if request.method=='POST':

        form=SingUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=SingUpForm()
    return render(request,'Registration.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

                form = UserLoginForm(request=request,data=request.POST)
                if form.is_valid():

                    uname= form.cleaned_data['username']
                    userp= form.cleaned_data['password']
                    user = authenticate(username=uname,password=userp)
                    if user is not None:

                        login(request,user)
                        messages.success(request,"Login Successfully !")
                        return HttpResponseRedirect('/')
        else:
         form = UserLoginForm()

        return render(request,'Login.html',{'form':form})
    else:
         return HttpResponseRedirect('/')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('login')