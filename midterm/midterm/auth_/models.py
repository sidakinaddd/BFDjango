from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.

class MyUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'superAdmin'),
        (2, 'guest'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=1)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)


