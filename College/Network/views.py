from django.http import JsonResponse
from django.shortcuts import render
from . models import PersonModel
from . serializer import PersonSerializer

from rest_framework import status
from rest_framework . renderers import JSONRenderer
from rest_framework. parsers import JSONParser  


def Home(request):
    if request.method =='GET':
        form=PersonModel()
        # serializers=PersonSerializer(form)
        # json_data=JSONRenderer().render(serializers.data)
        return render(request,'Registration.html',{'form':form})