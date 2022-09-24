from django import http
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from flask import request_finished
from . forms import *
from . models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group



@csrf_exempt

def Home(request):
    return render(request,'main.html')

@csrf_exempt
def Index(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form =ImageForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/indexpage')
        elif request.method=='GET':
            form=ImageUploading.objects.all()
            return render(request,'index.html',{'form':form})
        else:
            form=ImageForm()
            # return render(request,'index.html',{'form':form})
        return render(request,'index.html',{'form':form})
    return HttpResponseRedirect('')

    
         
    
@csrf_exempt
def singup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        # mobile=request.POST['mobile']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # if len(username) > 10:
        #     messages.error(request,'Username must be 10 charaters')
        #     return redirect('/')

        # if not username.isalnum():
        #     messages.error(request,'user alphabets and numbers')
        #     return redirect('/')


        if pass1 != pass2:
           messages.error(request,'password must be same')
           return redirect('/')



        userauth = User.objects.create_user(username,email,pass1)
        userauth.first_name = fname
        userauth.last_name = lname
        userauth.save()
        # group = Group.objects.get(name='Student')
        # user.groups.add(group)
        return redirect('/')

    else:
        return HttpResponse('404 bad request') 

    
@csrf_exempt
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


    

@csrf_exempt
def userprofile(request):
    if request.method=='POST':
        mno=request.POST['mobileno']
        dbo=request.POST['dbo']
        addres=request.POST['addres']
        # blood=request.POST['blood']

        userprofile=UserProfile (mobile=mno,dateofbirth=dbo, address=addres)
        userprofile.save()
        messages.success(request,"Profile Create Successfully !")
    return render(request,'UserProfile.html')

    

    # if request.method=='GET':
    #     form=userprofileform()
    #     return render(request,'UserProfile.html',{'form':form})
    # elif request.method=='POST':
    #     form=userprofileform(request.POST)
    #     if form.is_valid():
    #         messages.success(request,'Profile Update !')
    #         return render(request,'UserProfile.html',{'form':form})
        


@csrf_exempt
def AddPost(request):
    if request.method=='POST':
        userpost =PostForm(request.POST)
        if userpost.is_valid():
            userpost.save()
            return redirect('/indexpage')
    elif request.method=='GET':
        userpost=PostUploading.objects.all()
        return render(request,'index.html',{'form':userpost})
    else:
        userpost=PostForm()
        # return render(request,'index.html',{'form':form})
    return render(request,'index.html',{'form':userpost})