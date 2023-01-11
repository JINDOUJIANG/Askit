# this is a coment
from . import views
from django.urls import path

app_name = 'askit'

urlpatterns = [
    path('main_page', views.main_page, name='main_page'),
    path('test', views.test, name='test'),
    path('new_question', views.new_question, name='new_question'),
    path('base_page', views.base_page, name='base_page'),
    # path('search', views.search, name='search'),

]
