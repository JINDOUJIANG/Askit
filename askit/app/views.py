# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import QuestionForm

def base_page(request):
  return render(request, "base_page.html")

def main_page(request):
  return render(request, "main_page.html")

def test(request):
  return render(request, "test.html")

def new_question(request):
  new_question_form = QuestionForm()

  print('The request method is: ', request.method)
  print('The POST data is:', request.POST)
  return render(request, "app/templates/new_question.html", {'new_question_form': new_question_form})

# def search(request):
#   latest_search = 
