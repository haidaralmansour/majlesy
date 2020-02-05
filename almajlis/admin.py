from django.contrib import admin
from .models import Citizen, Candidate, Data_Manager, Data_Creator, Session, Article, Comment, Suggestion

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Candidate)
admin.site.register(Data_Manager)
admin.site.register(Data_Creator)
admin.site.register(Session)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Suggestion)