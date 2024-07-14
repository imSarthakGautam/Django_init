from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello world, You are at DjangoFirst Homepage")
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("Hello world, You are at DjangoFirst Aboutpage")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello world, You are at DjangoFirst Contact page")
     return render(request, 'website/contact.html')

##Notes