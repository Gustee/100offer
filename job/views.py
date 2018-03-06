from django.shortcuts import render

# Create your views here.


def jobs(request):
    return render(request,'job/jobs.html')

def details(request):
    return render(request,'job/details.html')