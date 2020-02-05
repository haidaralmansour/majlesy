from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Citizen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    civil_no = models.IntegerField(null=True)
    phone =  models.IntegerField()
    civil_image = models.ImageField(null=True)

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    civil_no = models.IntegerField(null=True)
    university =  models.CharField(max_length=120)
    years_of_experience = models.IntegerField()
    civil_image = models.ImageField(null=True)

class Data_Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Data_Creator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Session(models.Model):
    creator =  models.ForeignKey(Data_Creator, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(Candidate)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    creator = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    title= models.CharField(max_length=120)
    description= models.TextField()
    image = models.ImageField(blank=True, null=True)
    date_posted =  models.DateTimeField(auto_now_add=True)
    date_of_article = models.DateField()

class Suggestion(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    vote = models.IntegerField(default=True)

class Comment(models.Model):
    creator = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    vote= models.BooleanField(default=True)
    approved_by = models.ForeignKey(Data_Manager, on_delete=models.CASCADE, null=True, blank=True)
    approved = models.BooleanField(default=False)



