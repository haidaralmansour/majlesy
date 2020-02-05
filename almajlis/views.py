from django.shortcuts import render, redirect
from .forms import CitizenForm, UserSignup, UserLogin, CandidateForm
from django.contrib.auth import login, authenticate, logout
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


def citizen_register(request):
    form = UserSignup()
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            
            return redirect("citizen-create")
    context = {
        "form":form,
    }
    return render(request, 'register.html', context)

def citizen_create(request):
    form = CitizenForm()
    if request.method=="POST":
        form = CitizenForm(request.POST, request.FILES)
        if form.is_valid():
            citizen = form.save(commit=False)
            citizen.user = request.user
            citizen.save()
            return redirect('session-list')
    context = {
        "form":form
    }
    return render(request, 'citizen_create.html', context)

def citizen_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                
                return redirect('session-list')

    context = {
        "form":form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('success-page')


def candidate_create(request):
    form = CandidateForm()
    if request.method=="POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = request.user
            candidate.save()
            return redirect('session-list')
    context = {
        "form":form
    }
    return render(request, 'candidate_create.html', context)

def candidate_register(request):
    form = UserSignup()
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            
            return redirect("candidate-create")
    context = {
        "form":form,
    }
    return render(request, 'candidate_register.html', context)

def candidate_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                
                return redirect('session-list')

    context = {
        "form":form
    }
    return render(request, 'candidate_login.html', context)

def logout_view(request):
    logout(request)
    return redirect('success-page')



