# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import UserSerializer
#from django.contrib.auth.models import User
from rest_framework import status
from .models import UserModel
from django.contrib.auth.hashers import make_password
from passlib.handlers.django import django_pbkdf2_sha256

# Create your views here.

@api_view(['POST'])
def signup_view(request):
    if request.method == "POST": 
        serializer = UserSerializer(data = request.data)
        data = {} 
        if serializer.is_valid():
            acc=serializer.save()
            data['response']= "sucessfully register a new user "
            data['email']=acc.email
            data['password']=acc.password
            data['id']=acc.id
            print(data) 
        else:
            serializer.errors
    return Response(data)

@api_view(['GET'])
def signin_view(request):
        if request.method=="GET":
                # serializer= UserSerializer(data=request.data)
                data={}
                # if serializer.is_valid():
                # signin=serializer.save()
                data['responce']='sucessfully sign in'

                # data['email']=signin.email
                django_hash = data['password']
                is_verified = django_pbkdf2_sha256.verify(data['password'], django_hash)
                if is_verified:
                    print('Correct!!')
                # 5 else:
                #         data=serializer.errors
        return Response(data)

