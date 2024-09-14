from django.shortcuts import render
from .models import userModel, Player

from django.shortcuts import get_object_or_404
from .forms import PlayerForm
# 

# Create your views here.
def myNewApp(request):
    dbData= userModel.objects.all() #CRUD operation : read
    return render(request, 'newApp/myNewApp.html', {'dbData':dbData})

def userDetails(request, my_id):
    dbValue= get_object_or_404(userModel, pk=my_id)
    return render (request, 'newApp/user_details.html', {'dbValue': dbValue})
#'dbValue' is name assigned to recieved data dbValue

def player(request):
    playerss= None # placeholder for list of players to display
    if request.method == 'POST':
        form = PlayerForm(request.POST)
     #valid form ?
        if form.is_valid():
            #get the selected national team
            nation_player=form.cleaned_data['national_team']
            #filter players based on selected national team
            playerss= Player.objects.filter(national_team=nation_player)
    else:
        form=PlayerForm()

    return render(request, 'newApp/playerform.html', {'form':form,'players':playerss})
