from django.shortcuts import render , redirect
from django.contrib.auth import login as lgn, authenticate
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home (request):
    return render(request,"Home/home.html")


def Login (request):
    args = {"type":1}
    if request.method == 'GET' and request.user.is_authenticated == False:
        return render(request, 'Home/login.html', args)
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('/dashboard')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        i = authenticate(request, username=username, password=password)
        if i:
            lgn(request, i)
            return redirect('/dashboard')
        return render(request, 'Home/login.html', args)
@login_required
def Logout(request):
    lgt(request)
    return redirect('/home')
