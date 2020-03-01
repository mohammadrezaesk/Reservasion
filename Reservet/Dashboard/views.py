from django.shortcuts import render
from django.contrib.auth import login as lgn, authenticate
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required
from Home.models import Ruser,Advice
# Create your views here.


def Home (request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    typ= mainuser.typ
    if typ=="teacher":
        Advices = Advice.objects.filter(advisor=mainuser)
    else:
        Advices = Advice.objects.filter(noadvisor=mainuser)
    # type = 0
    # for teacher in Teachers:
    #     if teacher.user == request.user:
    #         type = 1
    # for student in Students:
    #     if student.user == request.user:
    #         type = 2
    # for parent in Parents:
    #     if parent.user == request.user:
    #         type = 3

    args = {"type":type,"Advice" : Advices,"mainuser":mainuser }  
    return render(request,"Dashboard/home.html",args)


def advices (request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    typ= mainuser.typ
    if typ=="teacher":
        Advices = Advice.objects.filter(advisor=mainuser)
    else:
        Advices = Advice.objects.filter(noadvisor=mainuser)

    args = {"type":type,"Advice" : Advices,"mainuser":mainuser }  
    return render(request,"Dashboard/advices.html",args)

