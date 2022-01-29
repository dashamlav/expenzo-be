
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts import UserType, CurrencyType
from rest_framework.authtoken.models import Token


class AppUser(AbstractUser):
    #first_name, last_name, password, is_staff, is_active is handled in AbstractUser.

    username = models.CharField(max_length=50, null=False, blank=False, default='user')
    email = models.EmailField(null=False, blank=False, unique=True, db_index=True)
    userType = models.CharField(max_length=3, choices=UserType.Choices, default=UserType.DEFAULT, null=False, blank=False)
    defaultCurrency = models.CharField(max_length=3, choices=CurrencyType.Choices, null=False, blank=False, default=CurrencyType.INR)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

