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
        #write_only_fields = ('password',)
       
        
    def create(self, validated_data):
            model1 = UserModel(
                email=self.validated_data['email']   
            )
            model1.password=make_password(self.validated_data['password'],None, 'pbkdf2_sha256') # make password is use for the validation 
            model1.save()
            print()
            return  model1



# class ChangePasswordSerializer(serializers.SeriModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ('password','email')

#         """
#         Serializer for password change endpoint.
#         """
#         old_password = serializers.CharField(required=True)
#         new_password = serializers.CharField(required=True)

# class ChangePasswordSerializer(ModelSerializer):
#     confirm_password = CharField(write_only=True)
#     new_password = CharField(write_only=True)
#     old_password = CharField(write_only=True)

#     class Meta:
#         model = UserModel
# #         fields = ['id', 'password', 'old_password', 'new_password','confirm_password']
# class PasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ('password')

#     def update(self, instance, validated_data):
#         instance.password = validated_data.get('password', instance.password)
#         instance.save()
#         return instance