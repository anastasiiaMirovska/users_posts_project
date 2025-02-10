from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from core.services.file_service import upload_user_photos

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

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NameValidator.pattern, RegexEnum.NameValidator.message)])
    surname = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NameValidator.pattern, RegexEnum.NameValidator.message)])
    age = models.IntegerField(validators=[V.MinValueValidator(6), V.MaxValueValidator(100)])
    phone = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.PhoneValidator.pattern, RegexEnum.PhoneValidator.message)])
    birthday = models.DateField()
    city = models.CharField(max_length=30, validators=[V.RegexValidator(RegexEnum.NameValidator.pattern, RegexEnum.NameValidator.message)])
    country = models.CharField(max_length=30, validators=[V.RegexValidator(RegexEnum.NameValidator.pattern, RegexEnum.NameValidator.message)])
    nationality = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=upload_user_photos, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
