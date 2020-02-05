from django import forms
from .models import Citizen, Candidate, Data_Manager, Data_Creator, Suggestion, Comment, Article, Session

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        exclude = ['user']

