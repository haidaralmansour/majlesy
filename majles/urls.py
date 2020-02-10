"""majles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from almajlis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name='home'), 
    
    path('session/list/',views.session_list ,name='session-list'),
    path('session/<int:session_id>/detail/',views.session_detail ,name='session-detail'),
    path('article/list/',views.article_list ,name='article-list'),
    path('article/<int:article_id>/detail/',views.article_detail ,name='article-detail'),
    path('article/<int:article_id>/update/',views.article_update ,name='article-update'),
    path('article/create/',views.article_create ,name='article-create'),
    path('article/<int:article_id>/delete/',views.article_delete ,name='article-delete'),
    path('session/<int:session_id>/delete/',views.session_delete ,name='session-delete'),
    path('session/create/',views.session_create ,name='session-create'),
    path('session/<int:session_id>/update/',views.session_update ,name='session-update'),
    path('logout/',views.logout_view,name='logout'),

    path('citizen/register/',views.citizen_register ,name='citizen-register'),
    path('citizen/login/',views.citizen_login ,name='citizen-login'),
    path('citizen/create/',views.citizen_create ,name='citizen-create'),
    path('candidate/register/',views.candidate_register ,name='candidate-register'),
    path('candidate/login/',views.candidate_login ,name='candidate-login'),
    path('candidate/create/',views.candidate_create ,name='candidate-create'),
    path('comment/<int:session_id>/create/',views.comment_create ,name='comment-create'),
    path('comment/<int:comment_id>/update/',views.comment_update ,name='comment-update'),
    path('manager/approval/<int:comment_id>/',views.manager_approval ,name='manager-approval'),
    path('comment/<int:comment_id>/delete/',views.comment_delete ,name='comment-delete'),

    path('no/access',views.no_access ,name='no-access'),
    path('unapproved/comments/',views.unapproved_comments ,name='unapproved-comments'),
    path('mysessions/',views.my_sessions ,name='my_sessions'),
    path('myarticles/',views.my_articles ,name='my-articles'),
    path('candidates/',views.candidate_list ,name='candidate-list'),
    path('candidate/profile/',views.candidate_profile ,name='candidate-profile'),
    path('citizen/profile/',views.citizen_profile ,name='citizen-profile'),
    path('profile/',views.profile ,name='profile'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
