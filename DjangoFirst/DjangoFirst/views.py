from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world, You are at DjangoFirst Homepage")

def about(request):
    return HttpResponse("Hello world, You are at DjangoFirst Aboutpage")

def contact(request):
    return HttpResponse("Hello world, You are at DjangoFirst Contact page")
