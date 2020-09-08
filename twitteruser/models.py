from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class TwitterUser(AbstractUser):
    name = models.CharField(max_length=40, unique=True)
    following = models.ManyToManyField('self', symmetrical=False)
