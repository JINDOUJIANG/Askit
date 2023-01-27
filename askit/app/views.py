# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import QuestionForm
from app.models import Person

def input_name_form(request):
  return render(request, "input_name_form.html")

def base_page(request):
  first_name = request.POST.get("first_name")
  last_name = request.POST.get("last_name")
  p = Person.objects.create(first_name = first_name, last_name = last_name)
  p.save()
  context = { "p": p }
  return render(request, "base_page.html", context)

def main_page(request):
  new_question_form = QuestionForm(request.POST)
  context = {"new_question_form": new_question_form}
  return render(request, "main_page.html", context)

def test(request):
  return render(request, "test.html")

def new_question(request):
  new_question_form = QuestionForm(request.POST)
  context = { "new_question_form": new_question_form }
  print('The request method is: ', request.method)
  print('The POST data is:', request.POST)
  return render(request, "new_question.html", context)

def new_comment(request):
  
  return render(request, "new_comment.html")
# def search(request):
#   latest_search = 
