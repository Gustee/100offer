from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request,'resume/basic.html')

def test2(request):
    return render(request,'resume/100offer.html')
def career(request):
    return render(request,'resume/career.html')
def experience(request):
    return render(request,'resume/experience.html')
def info(request):
    return render(request,'resume/info.html')
def self_intro(request):
    return render(request,'resume/self_intro.html')
def showcase(request):
    return render(request,'resume/showcase.html')
def skill(request):
    return render(request,'resume/skill.html')
def social_media(request):
    return render(request,'resume/social_media.html')
def test(request):
    return render(request,'resume/test.html')