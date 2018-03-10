from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def login_in(request):
    return render(request,'user/login_in.html')

def sign_up(request):
    return render(request,'user/sign_up.html')

def login(request):
    return render(request,'user/login.html')

def mailConfirmation(request):
    return render(request,'user/mailconfirmation.html')

def personal_info(request):
    return render(request,'user/personal_info.html')

def account(request):
    return render(request,'user/account.html')

def career_info(request):
    return render(request,'user/career_info.html')

def experience(request):
    return render(request,'user/experience.html')

def signin(request):
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username != '123' and password != '123':
            ret = {'msg': 1}
        else:
            ret = {'msg': 0}
        return HttpResponse(json.dumps(ret))

def signup(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username != '123' and password != '123':
            ret = {'msg': 1}
        else:
            ret = {'msg': 0}
        return HttpResponse(json.dumps(ret))

def setting(request):
    return render(request, 'user/setting.html')