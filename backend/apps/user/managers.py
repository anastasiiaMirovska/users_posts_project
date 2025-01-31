from django.contrib.auth.models import UserManager as Manager


class UserManager(Manager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=Ture')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=Ture')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=Ture')

        user = self.create_user(email, password, **extra_fields)
        return user

