from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.question + '' + self.body 