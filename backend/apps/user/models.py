from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.user.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_logout = models.DateTimeField(null=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.PhoneValidator.pattern, RegexEnum.PhoneValidator.message)])
    birthday = models.DateField()
    city = models.CharField(max_length=30, validators=[V.RegexValidator(RegexEnum.CityCountryNameValidator.pattern, RegexEnum.CityCountryNameValidator.message)])
    country = models.CharField(max_length=30, validators=[V.RegexValidator(RegexEnum.CityCountryNameValidator.pattern, RegexEnum.CityCountryNameValidator.message)])
    nationality = models.CharField(max_length=20)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
