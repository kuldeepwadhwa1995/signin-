# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import UserSerializer
#from django.contrib.auth.models import User
from rest_framework import status
from .models import UserModel

# Create your views here.

@api_view(['POST'])
def signup_view(request):
    if request.method == "POST": 
        serializer = UserSerializer(data = request.DATA)
        data = {} 
        if serializer.is_valid():
            acc=serializer.save()
            data['response']= "sucessfully register a new user "
            data['email']=acc.email
            data['password']=acc.password
            data['id']=acc.id
        else:
            serializer.errors
    return Response(data)