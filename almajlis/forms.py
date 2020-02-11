from django import forms
from .models import Citizen, Candidate, Data_Manager, Data_Creator, Suggestion, Comment, Article, Session
from django.contrib.auth.models import User 

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        exclude = ['user']
        labels = {
            'dob':"Date of Birth"
        }
        widgets={
        'dob': forms.DateInput(attrs={"type":"date"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['creator','approved_by','approved','session']

class CommentManagerForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['approved']

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ['user']
        labels = {
            'dob':"Date of Birth"
        }
        widgets={
        'dob': forms.DateInput(attrs={"type":"date"}),
        }



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

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['creator']
        
        widgets={
        'date_of_article': forms.DateInput(attrs={"type":"date"}),
        }


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session 
        exclude = ['creator']

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion 
        exclude = ['session']
        
          
