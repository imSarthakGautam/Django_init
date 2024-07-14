from django.shortcuts import render

# Create your views here.
def myNewApp(request):
    return render(request, 'newApp/myNewApp.html')


