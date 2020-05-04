from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Ruser (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    typ = models.CharField(default="student",max_length=10)
    code = models.CharField(default="free",max_length=20)

    def __str__(self):
        return self.user.username
class classroom(models.Model):
    stpar = models.ForeignKey(Ruser,on_delete=models.CASCADE ,related_name='classnoadvisor')
    teacher = models.ForeignKey(Ruser,on_delete=models.CASCADE ,related_name='classadvisor')
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.teacher.user.username
class Advice (models.Model):
    classroomi = models.ForeignKey(classroom,on_delete="CASCADE",null=True)
    desc = models.CharField(default=" ",max_length=1000)
    status = models.IntegerField(default=1)
    day = models.CharField(default=" ",max_length=100)
    time = models.CharField(default=" ",max_length=100)
    start = models.IntegerField(default=0)
    score = models.IntegerField(default=5)
    end = models.IntegerField(default=0)
    def __str__(self):
        return self.classroomi.teacher.user.username
class Time (models.Model):
    advisor = models.ForeignKey(Ruser,on_delete=models.CASCADE)
    day = models.CharField(default=" ",max_length=100)
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=0)
    parent_length = models.IntegerField(default=0)
    student_length = models.IntegerField(default=0)
    def __str__(self):
        return self.day
