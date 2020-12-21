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
import crypt
import  crypto
from cryptography.fernet import Fernet
import socket
import sys
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import APIException




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

@api_view(['POST'])
def signin_view(request):
        if request.method=="POST":
                #serializer= UserSerializer(data=request.data)
                data=request.data   # get the data by using this method 

                # if serializer.is_valid():
                # signin=serializer.save()
                #data['responce']='sucessfully sign in'

                #data['email']=signin.email
                user = UserModel.objects.filter(email = data['email']).first()  # get the data from the data base 
                django_hash = user.password   # get the password from database 
                is_verified = django_pbkdf2_sha256.verify(data['password'],django_hash) # compare the both password 
                if is_verified:
                    print('Correct!!')
                else:
                    raise APIException("Incorrect Password!")
        return Response(data)




@api_view(['POST'])
def forgot_view(request):
    if request.method == 'POST':
        #serializer= UserSerializer(data=request.data)
        data=request.data   # get the data by using this method 
        # data['email']=request.data.get('email')
        # new_password=request.POST.get('new_password')
        # confirm_password=request.data.get('confirm_password')
        
        # print (new_password)
        # print (new_password)
        # print (new_password)
        # print (confirm_password)
        # print (confirm_password)
        # print (confirm_password)
        print (data)
        print ('data   =>> ', data)
        # data['responce']='sucessfully forgot the password'
        user = UserModel.objects.filter(email = data['email']).first() #get the email from database by createing the object of model 
        #encry(email)
        smtp_view(user.email)
    return  HttpResponse(data)

def forgot(request):
    if request.method == 'POST':
        # forgot2='127.0.0.1:8000/forgot1'
        message = request.GET.get('token') # get the email from the parameter 
        de=decry(message)
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')

        #encry(confirm_password)

        user = UserModel.objects.filter(email = de).first()
        print(user.email)
        #decry(user.email)
        print(confirm_password)
        user.password=make_password((confirm_password),None, 'pbkdf2_sha256')
        print(user.password)
        
        user.save()
       
        #user = UserModel.objects.get(email=email) 
    return render(request,'forgot.html')




def smtp_view(email):
    subject = 'send the mail'
    email_from = settings.EMAIL_HOST_USER
    email1=encry(email)
    print("smtp",email)
    #decry(email)
    
    html_content = render_to_string('mail.html', {"forgot2":  'http://localhost:8000/api/forgot1/?token=' + email1})
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

# def enc(confirm_password):
#     user = UserModel
#     print(user)
#     user.password= f.encrypt(confirm_password)
#     print(password)
#     return HttpResponse("done")


def encry(email):  #get the string type 
    # key = Fernet.generate_key() #this is your "password"
    cipher_suite = Fernet(b'ui38faJP-KwsX2MaYkuX0uaTrP4vkLLbS-RV1GoSVRI=')
    encoded_text = cipher_suite.encrypt(str.encode(str(email)))  # type cast into byte because encrypt function apply only on byte then convert into into bytes 
    de=encoded_text.decode()   # byte code 
    print(de, '  encrypted \n\n\n')
    return de



# def encry(email):  #get the string type 
#     # key = Fernet.generate_key() #this is your "password"
#     cipher_suite = Fernet(b'ui38faJP-KwsX2MaYkuX0uaTrP4vkLLbS-RV1GoSVRI=')
#     print(email)
#     print(type(email)) #string
#     encoded_text = cipher_suite.encrypt(str.encode(str(email)))  # type cast into byte because encrypt function apply only on byte then convert into into bytes 
#     print (type(encoded_text))# check the type of encoded text 
#     print (encoded_text)
#     print (type(encoded_text)) #byte code 
#     de=encoded_text.decode()   # byte code 
#     print(de)
#     print("de")
#     return de
def decry(email):
    cipher_suite = Fernet(b'ui38faJP-KwsX2MaYkuX0uaTrP4vkLLbS-RV1GoSVRI=')
    decoded_text = cipher_suite.decrypt(str.encode(str(email))) #use the encode() from  str_library to convert the str into byte code because the encrypt function apply only on byte code  
    print(decoded_text)  # string email
    return  decoded_text


