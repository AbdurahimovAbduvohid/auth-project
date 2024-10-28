from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# superuser control users
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError('Email adresi kiritilishi shart')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, password=None):
        user = self.create_user(email, name, surname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# users model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100,  default="def.name")
    surname = models.CharField(max_length=50,  default="def.surname")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # superuser
    objects = CustomUserManager()

    # Unique identifier email ishlatiladi
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.email
