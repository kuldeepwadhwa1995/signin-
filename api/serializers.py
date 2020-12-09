from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import UserModel

# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password','email')
        write_only_fields = ('password',)
        read_only_fields = ('id')

    # def create(self, validated_data):
    #     user = UserModel.objects.create(
    #         email=validated_data['email'],
    #     )

    #     user.set_password(validated_data['password'])
    #     user.save()

    #     return user