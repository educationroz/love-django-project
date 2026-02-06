from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request, 'pages/page1.html')

def page2(request):
    return render(request, 'pages/page2.html')

def page3(request):
    return render(request, 'pages/page3.html')

def page4(request):     
    return render(request, 'pages/page4.html')

def page5(request):
    return render(request, 'pages/page5.html')

def page6(request):
    return render(request, 'pages/page6.html')