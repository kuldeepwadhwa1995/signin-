# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.contrib.auth.models import  User
from django.db import models

# Create your models here.
class UserModel(models.Model):
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)

def __str__(self):
        return self.email
