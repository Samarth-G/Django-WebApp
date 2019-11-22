from django.db import models

class Questions(models.Model):

    questionText = models.CharField(max_length=300)
    pubDate = models.DateTimeField('published on')

    def __str__(self):
        return self.questionText

class Choice(models.Model):

    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=150)
    totalVote = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText