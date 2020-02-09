from django.shortcuts import render, redirect
from .forms import CitizenForm, UserSignup, UserLogin, CandidateForm, CommentForm, CommentManagerForm, ArticleForm
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


def comment_create(request, session_id):
    session = Session.objects.get(id=session_id)
    form = CommentForm()
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            citizen = Citizen.objects.get(user=request.user)
            comment.creator = citizen
            comment.session = session
            comment.save()
            return redirect('session-detail', comment.session.id)
    context = {
        "form":form,
        "session":session
    }
    return render(request, 'comment_create.html', context)

def manager_approval(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if Data_Manager.objects.filter(user=request.user).count() != 1 :
        return redirect('session-list')
    manager=Data_Manager.objects.get(user=request.user)
    form = CommentManagerForm(instance = comment)
    if request.method=="POST":
        form = CommentManagerForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved_by = manager
            comment.save()
            return redirect('unapproved-comments')
    context = {
        "form":form,
        "comment":comment
    }
    return render(request, 'manager_approval.html', context)

def comment_update(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance = comment)
    if request.method=="POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('session-detail', comment.session.id)
    context = {
        "form":form,
        "comment":comment
    }
    return render(request, 'comment_update.html', context)


def home(request):
    context = {
        "articles": Article.objects.all(),
        "sessions": Session.objects.all()
    }
    return render(request, 'home.html', context)

def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    session = comment.session
    comment.delete()
    return redirect('session-detail', session.id)


def session_detail(request, session_id):
    session = Session.objects.get(id=session_id)
    comments = Comment.objects.filter(session=session,approved=True)
    suggestions = Suggestion.objects.filter(session=session)
    context = {
        "session": session,
        "comments": comments,
        "suggestions":suggestions
    }
    return render(request, 'session_detail.html', context)
   

def article_create(request):
    form = ArticleForm()
    if request.method=="POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            candidate = Candidate.objects.get(user=request.user)
            article.creator = candidate
            article.save()
            return redirect('article-list')
    context = {
        "form":form
    }
    return render(request, 'article_create.html', context)    


def article_update(request, article_id):
    article = Article.objects.get(id=article_id)
    form = ArticleForm(instance = article)
    if request.method=="POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-detail', article.id)
    context = {
        "form":form,
        "article":article
    }
    return render(request, 'article_update.html', context)


    
def article_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('article-list')


def article_detail(request,article_id):
    article = Article.objects.get(id=article_id)
    context = {
        "article": article
    }
    return render(request, 'article_detail.html', context)


def session_create(request):
    form = sessionForm()
    if request.method=="POST":
        form = sesionForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            data_creator = Data_Creator.objects.get(user=request.user)
            session.creator = data_creator
            session.save()
            return redirect('session-list')
    context = {
        "form":form
    }
    return render(request, 'session_create.html', context)


def session_update(request, session_id):
    session = session.objects.get(id=session_id)
    form = sessionForm(instance = session)
    if request.method=="POST":
        form = sessionForm(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session-detail', session.id)
    context = {
        "form":form,
        "session":session
    }
    return render(request, 'session_update.html', context)


def session_delete(request, session_id):
    session = session.objects.get(id=session_id)
    session.delete()
    return redirect('session-list')

def no_access(request):
    return render(request, 'no_access.html')

def my_articles(request):
    if Candidate.objects.filter(user=request.user).count() != 1:
        return redirect('no-access')
    candidate= Candidate.objects.get(user=request.user)
    articles = Article.objects.filter(creator=candidate)
    context={
        "articles":articles
    }
    return render(request, "my_articles.html", context)

def my_sessions(request):
    if Data_Creator.objects.filter(user=request.user).count() != 1:
        return redirect('no-access')
    data_creator= Data_Creator.objects.get(user=request.user)
    sessions = Session.objects.filter(creator=data_creator)
    context={
        "sessions":sessions
    }
    return render(request, "my_sessions.html", context)

def unapproved_comments(request):
    comments =  Comment.objects.filter(approved=False)
    context={
        "comments":comments
    }
    return render(request, "unapproved_comments.html", context)
  













  




