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
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import random
from django.template.loader import render_to_string


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
                #serializer= UserSerializer(data=request.data)
                data=request.data   # get the data by using this method 

                # if serializer.is_valid():
                # signin=serializer.save()
                data['responce']='sucessfully sign in'

                #data['email']=signin.email
                user = UserModel.objects.filter(email = data['email']).first()  # get the data from the data base 
                django_hash = user.password   # get the password from database 
                is_verified = django_pbkdf2_sha256.verify(data['password'],django_hash) # compare the both password 
                if is_verified:
                    print('Correct!!')
                # 5 else:
                #         data=serializer.errors
        return Response(data)




@api_view(['GET'])
def forgot_view(request):
    if request.method=="GET":
        #serializer= UserSerializer(data=request.data)
        data=request.data   # get the data by using this method 
        print ('data   =>> ', data)
        # data['responce']='sucessfully forgot the password'
        user = UserModel.objects.filter(email = data['email']).first() #get the email from database by createing the object of model 
        smtp_view(user.email)
    return  HttpResponse(data)

def forgot(request):
    forgot2='127.0.0.1:8000/forgot1'
    return render(request,'forgot.html',{"forgot2" : forgot2})




def smtp_view(email):
    subject = 'send the mail'
    email_from = settings.EMAIL_HOST_USER
    html_content = render_to_string('mail.html', {"forgot2": "http://127.0.0.1:8000/forgot"})
    #recipient_list = ['kuldeepwadhwa1995@gmail.com']
    #otp=random.randrange(1111,9999)
    message = render_to_string('mail.html')
    email = EmailMultiAlternatives(subject,message, email_from,[email])
    email.attach_alternative(html_content, "text/html")
    #forgot_api()
    email.send()
    return HttpResponse({"status": True})


# def forgot_api(request):
#     return render(request,'forgot.html')

