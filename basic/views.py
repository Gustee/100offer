from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'basic/index.html')

def test(request):
    return render(request,'basic/classifier.html')

# def page_not_found(request):
#     return render(request,'basic/404.html')