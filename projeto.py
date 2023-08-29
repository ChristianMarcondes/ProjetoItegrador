from django.db import models
from django.utils import timezone

class UsersQuiz(models.Model):
    UserName = models.CharField(max_length=200)
    UserSex = models.CharField(max_length=50) 
    UserAge=models.IntegerField(default=0)
    UserProfession= models.CharField(max_length=60)
    UserEmail=models.CharField(max_length=80)

class Result(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    IdUserName= models.ForeignKey(UsersQuiz)
    choiceText = models.CharField(max_length=256)
    ChoiceText_Number=models.IntegerField(default=0)
    
