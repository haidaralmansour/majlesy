from django.shortcuts import render
from .models import Citizen
from .forms import CitizenForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
# Create your views here.


def session_list(request):
    context = {
        "session":Session.objects.all()
    }
    return render(request, 'session_list.html', context)

def article_list(request):
    context = {
        "article":Article.objects.all()
    }
    return render(request, 'article_list.html', context)


# def citizen_Signup(request):
#     context = {
#         "signup"
#     }    


