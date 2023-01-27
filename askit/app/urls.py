# this is a new comment
# this is another commence from 1-24-2023
from . import views
from django.urls import path

app_name = 'askit'

urlpatterns = [
    path('main_page', views.main_page, name='main_page'),
    path('new_question', views.new_question, name='new_question'),
    path('base_page', views.base_page, name='base_page'),
    path('new_comment', views.new_comment, name='new_comment'),
    # path('search', views.search, name='search'),

]
