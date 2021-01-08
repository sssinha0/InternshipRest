from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):
    if request.method=='POST':
        f=request.POST.get('fname')
        l=request.POST.get('lname')
        u=request.POST.get('uname')
        e=request.POST.get('eaddress')
        p=request.POST.get('pass1')
        c=request.POST.get('pass2')
        if p!=c:
            messages.warning(request, 'not match password')
            return redirect('login')
        elif User.objects.filter(username=u).exists():
            messages.warning(request,"username already exits")
            return redirect('register')
        elif User.objects.filter(email=e).exists():
            messages.warning(request,"email already taken")
            return redirect('register')
        else:      
            user=User.objects.create_user(first_name=f,username=u,email=e,password=p,last_name=l)
            user.save()
            messages.success(request, 'You have Successfully Register')
            return redirect('login')
            print(f,l,u,e,p,c)
        
    return render(request,'register.html')
def usr_login(request):
    if request.method=='POST':
        uname=request.POST.get('loguname')
        passw=request.POST.get('logpass')
        user = authenticate(request,username=uname, password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Please enter valid details or register first')
            return redirect('login')
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def usr_logout(request):
    logout(request)
    return redirect(request,'home')

