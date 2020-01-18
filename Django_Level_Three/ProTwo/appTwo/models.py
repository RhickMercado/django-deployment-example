from django.db import models

# Create your models here.

class User(models.Model):
    lastName = models.CharField(max_length=128, unique=False)
    firstName = models.CharField(max_length=128, unique=False)
    eMail = models.EmailField(max_length=256, unique=False)
