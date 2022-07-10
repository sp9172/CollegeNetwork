from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . forms import PersonForm,personloginForm
from . models import PersonModel


@csrf_exempt

def Home(request):
    return render(request,'main.html')

def singup(request):
    if request.method=='POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
        context={
            'form':form
        }
        return render(request,'Registration.html',context)

    else:
        if request.method=='GET':
            form=PersonForm()
            context={
            'form':form
        }
        return render(request,'Registration.html',context)
    

def user_login(request):
    if request.method=='POST':
        username=PersonModel.POST.get()
        password=PersonModel.POST.get()
        
    form=personloginForm()

    context={
        'form':form
    }

    return render(request,'login.html',context)