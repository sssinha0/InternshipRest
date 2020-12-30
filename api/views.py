from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'a.html',{'title':'shashi','link':'http://127.0.0.1:8000/profile/'})
def profile(request):
    return render(request,'a.html',{'title':'sinha','link':'http://127.0.0.1:8000/'})
def expression(request):
    a=int(request.GET['text1'])
    b=int(request.GET['text2'])
    c=a*2+b
    return render(request,'output.html',{'result':c})