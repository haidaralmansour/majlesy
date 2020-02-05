from django.shortcuts import render
from .models import Citizen
from .forms import CitizenForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .models import Citizen, Candidate, Data_Manager, Data_Creator, Suggestion, Comment, Article, Session
# Create your views here.


def session_list(request):
    context = {
        "sessions":Session.objects.all()
    }
    return render(request, 'session_list.html', context)

def article_list(request):
    context = {
        "articles":Article.objects.all()
    }
    return render(request, 'article_list.html', context)


# def citizen_Signup(request):
#     context = {
#         "signup"
#     }    


