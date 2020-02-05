from django import forms
from .models import Citizen, Candidate, Data_Manager, Data_Creator, Suggestion, Comment, Article, Session
from django.contrib.auth.models import User 
class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        exclude = ['user']

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ['user']


class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())