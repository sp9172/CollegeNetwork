from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from . forms import PersonForm,personloginForm
from . models import PersonModel
from django.contrib.auth.models import User
from django.contrib import messages



@csrf_exempt

def Home(request):
    return render(request,'main.html')

def Index(request):
    return render(request,'index.html')

def singup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        # mobile=request.POST['mobile']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username) > 10:
            messages.error(request,'Username must be 10 charaters')
            return redirect('/')

        if not username.isalnum():
            messages.error(request,'user alphabets and numbers')
            return redirect('/')


        if pass1 != pass2:
           messages.error(request,'password must be same')
           return redirect('/')



        userauth = User.objects.create_user(username,email,pass1)
        userauth.first_name = fname
        userauth.last_name = lname
        userauth.save()
        return redirect('/')

    else:
        return HttpResponse('404 bad request') 

    

def user_login(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('/indexpage')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/')
    return HttpResponse('404 bad request')

def userlogout(request):
    logout(request)
    messages.success(request,"Logout Sccessfully")
    return redirect('/')
    