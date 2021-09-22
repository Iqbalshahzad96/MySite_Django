from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    firstName = CharField(max_length=264)
    lastName = CharField(max_length=264)
    email = EmailField(max_length=254,unique=True)

    def __str__(self):
        return str(self.firstName)