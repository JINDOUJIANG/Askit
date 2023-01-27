# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Question

def base_page(request):
  return render(request, "base_page.html")

def main_page(request):
  return render(request, "main_page.html")

def new_question(request):
  your_question = request.POST["your_question"]
  body = request.POST["body"]
  question = Question.objects.create(question=your_question,body=body)
  context = { "question": question }
  return render(request, "new_question.html", context)

def new_comment(request):
  
  return render(request, "new_comment.html")

# def search(request):
#   latest_search = 
