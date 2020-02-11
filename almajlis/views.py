from django.shortcuts import render, redirect
from .forms import CitizenForm, UserSignup, UserLogin, CandidateForm, CommentForm, CommentManagerForm, ArticleForm, SessionForm, SuggestionForm
from django.contrib.auth import login, authenticate, logout
from .models import Citizen, Candidate, Data_Manager, Data_Creator, Suggestion, Comment, Article, Session
# Create your views here.


def candidate_list(request):
    context ={
        "candidates": Candidate.objects.all()
    }
    return render(request,'candidate_list.html', context)

def session_list(request):
    creator_flag = False
    if Data_Creator.objects.filter(user=request.user).count() == 1:
        creator_flag=True
    context = {
        "sessions":Session.objects.all(),
        "creator": creator_flag
    }
    return render(request, 'session_list.html', context)

def article_list(request):
    creator_flag = False
    if Candidate.objects.filter(user=request.user).count() == 1:
        creator_flag=True
    context = {
        "articles":Article.objects.all(),
        "creator": creator_flag
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

def citizen_update(request):
    citizen = Citizen.objects.get(user=request.user)
    form = CitizenForm(instance = citizen)
    if request.method=="POST":
        form = CitizenForm(request.POST, request.FILES, instance=citizen)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        "form":form,
        "citizen":citizen
    }
    return render(request, 'citizen_update.html', context)

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
    return redirect('home')

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

def candidate_update(request):
    candidate = Candidate.objects.get(user=request.user)
    form = CandidateForm(instance = candidate)
    if request.method=="POST":
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        "form":form,
        "candidate":candidate
    }
    return render(request, 'candidate_update.html', context)

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
    return redirect('home')

def comment_create(request, session_id):
    if Citizen.objects.filter(user=request.user).count() != 1:
        return redirect('no-access')
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
        "articles": Article.objects.all()[:4],
        "sessions": Session.objects.all()[:5]
    }
    return render(request, 'home.html', context)

def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    session = comment.session
    comment.delete()
    return redirect('session-detail', session.id)

def session_detail(request, session_id):
    creator_flag = False
    citizen_flag =False
    if Data_Creator.objects.filter(user=request.user).count() == 1:
        creator_flag=True
    if Citizen.objects.filter(user=request.user).count() == 1:
        creator_flag=True
    session = Session.objects.get(id=session_id)
    comments = Comment.objects.filter(session=session,approved=True)
    suggestions = Suggestion.objects.filter(session=session)
    context = {
        "session": session,
        "comments": comments,
        "suggestions":suggestions,
        "creator": creator_flag,
        "citizen": citizen_flag
    }
    return render(request, 'session_detail.html', context)
   
def article_create(request):
    if Candidate.objects.filter(user=request.user).count() != 1:
        return redirect("no-access")
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
    if Data_Creator.objects.filter(user=request.user).count() != 1:
        return redirect("no-access")
    form = SessionForm()
    if request.method=="POST":
        form = SessionForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            data_creator = Data_Creator.objects.get(user=request.user)
            session.creator = data_creator
            session.save()
            return redirect('suggestion-create', session.id)
    context = {
        "form":form
    }
    return render(request, 'session_create.html', context)

def session_update(request, session_id):
    if Data_Creator.objects.filter(user=request.user).count() != 1:
        return redirect('no-access')
    session = Session.objects.get(id=session_id)
    suggestions = Suggestion.objects.filter(session=session)
    form = SessionForm(instance = session)
    if request.method=="POST":
        form = SessionForm(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session-detail', session.id)
    context = {
        "form":form,
        "session":session,
        "suggestions":suggestions
    }
    return render(request, 'session_update.html', context)

def session_delete(request, session_id):
    session = session.objects.get(id=session_id)
    session.delete()
    return redirect('session-list')

def no_access(request):
    return render(request, 'no_access.html')

def candidate_profile(request):
    if Candidate.objects.filter(user=request.user).count() != 1:
        return redirect('no-access')
    candidate= Candidate.objects.get(user=request.user)
    articles = Article.objects.filter(creator=candidate)
    context={
        "profile":candidate,
        "articles":articles
    }
    return render(request, "candidate_profile.html", context)

def citizen_profile(request):
    if Citizen.objects.filter(user=request.user).count() != 1:
        return redirect('no-access')
    citizen = Citizen.objects.get(user=request.user)
    context={
        "profile":citizen
    }
    return render(request, "citizen_profile.html", context)

def profile(request):
    if Citizen.objects.filter(user=request.user).count() == 1:
        return redirect('citizen-profile')
    elif Candidate.objects.filter(user=request.user).count() == 1:
        return redirect('candidate-profile')
    elif Data_Creator.objects.filter(user=request.user).count() == 1:
        return redirect('my-sessions')
    elif Data_Manager.objects.filter(user=request.user).count() == 1:
        return redirect('unapproved-comments')
    else:
        return redirect('no-access')
    
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
        "sessions":sessions,
        "profile":data_creator
    }
    return render(request, "my_sessions.html", context)

def unapproved_comments(request):
    if Data_Manager.objects.filter(user=request.user).count() != 1:
        return redirect("no-access")
    not_comments =  Comment.objects.filter(approved=False)
    comments =  Comment.objects.filter(approved=True)
    context={
        "not_approved": not_comments,
        "comments":comments
    }
    return render(request, "unapproved_comments.html", context)

def about(request):
    return render(request, "about.html")

def suggestion_create(request, session_id):
    form = SuggestionForm()
    session = Session.objects.get(id=session_id)
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid:
            suggestion = form.save(commit=False)
            suggestion.session = session
            suggestion.save()
            return redirect('session-detail', session_id)
    context = {
        "form": form,
        "session": session
    }
    return render(request, 'suggestion_create.html', context)


def suggestion_update(request,suggestion_id):
    suggestion = Suggestion.objects.get(id=suggestion_id)
    form = SuggestionForm(instance=suggestion)
    if request.method == "POST":
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid:
            form.save()
            return redirect('session-detail', session_id)
    context = {
        "form": form,
        "suggestion": suggestion
    }
    return render(request, 'suggestion_update.html', context)

def suggestion_delete(request,suggestion_id):
    suggestion = Suggestion.objects.get(id=suggestion_id)
    session = suggestion.session
    suggestion.delete()
    return redirect('session-detail', session.id)

def visit_profile(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    context = {
        "profile": candidate
    }
    return render(request, "visit_profile.html", context)

  













  




