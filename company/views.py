from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request,'company/info.html')

def new(request):
    return render(request,'company/new.html')

def position(request):
    return render(request,'company/position.html')

def applicant(request):
    return render(request,'company/applicant.html')

