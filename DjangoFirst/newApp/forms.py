from django import forms
from .models import NationalTeam

class PlayerForm(forms.Form):
    national_team= forms.ModelChoiceField(queryset=NationalTeam.objects.all(), label="selct national team")

