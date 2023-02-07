# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Question

def base_page(request):
  return render(request, "base_page.html")

def question_save(request):
  question = request.POST['your_question']
  body = request.POST['body']
  question = Question.objects.create(question=question,body=body)
  question.save()

  return HttpResponseRedirect('main_page')

def main_page(request):
    questions = Question.objects.all()
   
    context = { 'questions': questions }
    print("99999999999")
    print(questions)
    print("99999999999")
   
    return render(request, "main_page.html", context)

def new_question(request):
  return render(request, "new_question.html")

def new_comment(request):
  
  return render(request, "new_comment.html")


