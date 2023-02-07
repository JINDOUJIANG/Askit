# this is a new comment
# this is another commence from 1-24-2023
from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('css_testpage', views.css_testpage, name='css_testpage'),
    path('base_page', views.base_page, name='base_page'),
    path('main_page', views.main_page, name='main_page'),
    path('question_save', views.question_save, name='question_save'),
    path('new_question', views.new_question, name='new_question'),
    path('new_comment', views.new_comment, name='new_comment'),

]
