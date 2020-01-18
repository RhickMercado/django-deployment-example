from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=None)
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=None)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    firstName = models.CharField(max_length=128, unique=False)
    lastName = models.CharField(max_length=128, unique=False)
    eMail = models.EmailField(max_length=256, unique=True)
