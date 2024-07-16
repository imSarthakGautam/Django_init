from django.shortcuts import render
from .models import userModel

from django.shortcuts import get_object_or_404

# Create your views here.
def myNewApp(request):
    dbData= userModel.objects.all()
    return render(request, 'newApp/myNewApp.html', {'dbData':dbData})

def userDetails(request, my_id):
    dbValue= get_object_or_404(userModel, pk=my_id)
    return render (request, 'newApp/user_details.html', {'dbValue': dbValue})



