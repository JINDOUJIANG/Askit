from django.db import models

# Create your models here.
# I may need to create a Question model here for new_question to trigger
# Question model may have two fields: question, body
# class QuestionForm(forms.Form):
#     question_title = forms.CharField(max_length=50)
#     question_body = forms.CharField(max_length=300)

    # def __str__(self):
    #     return self.question_title + '' + self.question_body

# This Person model is used for test database
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + '' + self.last_name