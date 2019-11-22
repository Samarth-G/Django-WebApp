from django.db import models

class Questions(models.Model):
    questionText = models.CharField(max_length=300)
    pubDate = models.DateTimeField('published on')



class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=150)
    totalVote = models.IntegerField(default=0)