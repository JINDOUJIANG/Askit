from . import views
from django.urls import path

app_name = 'askit'

urlpatterns = [
    path('', views.main_page, name='main_page'),
]
