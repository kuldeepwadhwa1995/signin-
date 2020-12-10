from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import UserModel
from django.contrib.auth.hashers import make_password
from passlib.handlers.django import django_pbkdf2_sha256

# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password','email')
        write_only_fields = ('password',)
        
def create(self, validated_data):
        model1 = UserModel(
            email=self.validated_data['email']   
        )
        model1.password=make_password(self.validated_data['password'],None, 'pbkdf2_sha256') # make password is use for the validation 
        print(email)
        print(password)
        model1.save()
        return  model1
