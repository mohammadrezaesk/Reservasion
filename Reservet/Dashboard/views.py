from django.shortcuts import render , redirect 
from django.contrib.auth import login as lgn, authenticate
from django.contrib.auth import logout as lgt
import json
from django.http import JsonResponse , HttpResponse
from django.contrib.auth.decorators import login_required
from Home.models import Ruser,Advice,Time,classroom
# Create your views here.
def checktime(day,start,end,step,user,free):
    h = 1
    
    minute = 0
    res = []
    step = (step/10)+(free/10)
    b = (end-start)*6
    while b>0:
        adtimes = Advice.objects.filter(status__lte='1',classroomi__teacher__user__username=user,day=day,start__gte=h,end__lte=h+step-1)
        print(adtimes)
        if(len(adtimes)==0):
            res.append([day,h,h+step-1,start])
            print(day,h)
        h+=step
        b-=step
    return res
def Home (request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    typ= mainuser.typ
    # if typ=="teacher":
    #     Advices = Advice.objects.filter()
    # else:
    #     Advices = Advice.objects.filter(noadvisor=mainuser)
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

    args = {"type":typ,"mainuser":mainuser }  
    return render(request,"Dashboard/home.html",args)


def advices (request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    typ= mainuser.typ
    if typ=="teacher":
         Advices = Advice.objects.filter(classroomi__teacher=mainuser)
    else:
         Advices = Advice.objects.filter(classroomi__stpar=mainuser)

    args = {"type":typ,"Advice":Advices,"mainuser":mainuser }  
    return render(request,"Dashboard/advices.html",args)


def times (request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    times = Time.objects.filter(advisor=mainuser)
    typ= mainuser.typ
    # if typ=="teacher":
    #     Advices = Advice.objects.filter(advisor=mainuser)
    # else:
    #     Advices = Advice.objects.filter(noadvisor=mainuser)
    week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    args = {"type":typ,"mainuser":mainuser,"times":times , "week":week}  

    if request.method=="POST":
        for i in week:
            start = request.POST[i+"_start"]
            end = request.POST[i+"_end"]
            parent = request.POST[i+"_parent"]
            student = request.POST[i+"_student"]
            if int(start)<int(end) and int(start)+int(end)<48 :
                baby = Time.objects.get(advisor=mainuser , day=i)
                baby.start=start
                baby.end=end
                baby.parent_length = parent
                baby.student_length = student
                baby.save()
        return render(request,"Dashboard/times.html",args)    
    return render(request,"Dashboard/times.html",args)

def timeline (request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    times = Time.objects.filter(advisor=mainuser)
    typ= mainuser.typ
    # if typ=="teacher":
    #     Advices = Advice.objects.filter(advisor=mainuser)
    # else:
    #     Advices = Advice.objects.filter(noadvisor=mainuser)
    week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    args = {"type":typ,"mainuser":mainuser,"times":times , "week":week}  
    return render(request,"Dashboard/timeline.html",args)

def newadvices(request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    classes = classroom.objects.filter(stpar=mainuser)
    alltime = [[]]
    typ= mainuser.typ
    print(request.user.username)
    if typ=="teacher":
        return redirect("/dashboard/")
    else:
        args = {"type":typ,"mainuser":mainuser,"times":times, "classes":classes}  
    if request.method=="POST":
        data = json.loads(request.body)
        clasrooom = classes.get(teacher__user__username=data['username'])
        advc = Advice.objects.create(day=data['day'],start=data['start'],end=data['end'],classroomi=clasrooom,desc=" ",status='1',time=data['time'])
        advc.save()
        return HttpResponse(json.dumps({'msg':"dashboard"}),content_type='application/json')
    return render(request,"Dashboard/newadvice.html",args)
def showtime(request):
    rusers = Ruser.objects.all()
    mainuser = Ruser.objects.get(user=request.user)
    times = Time.objects.filter(advisor=mainuser)
    typ= mainuser.typ
    result=[]
    if request.method=='POST':
        data = json.loads(request.body)
        times = Time.objects.filter(advisor__user__username=data['name'])
        
        for i in times:
            step = i.parent_length
            if typ=="student":
                print(2134)
                step = i.student_length
            result.append(checktime(i.day,int(i.start),int(i.end),int(step),data['name'],10))
    
        return HttpResponse(json.dumps({'msg':result}),content_type='application/json')
    else:
        return HttpResponse(json.dumps({'msg':'bye'}),content_type='application/json')
    