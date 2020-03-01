from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Ruser (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    typ = models.CharField(default="student",max_length=10)
    def __str__(self):
        return self.user.username

class Advice (models.Model):
    advisor = models.ForeignKey(Ruser,on_delete=models.CASCADE,related_name='advisor')
    noadvisor = models.ForeignKey(Ruser,on_delete=models.CASCADE,related_name='noadvisor')
    desc = models.CharField(default=" ",max_length=1000)
    time = models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return self.advisor.user.username