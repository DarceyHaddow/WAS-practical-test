from django.urls import path
from school_news import views

app_name = 'school_news'

urlpatterns = [
    path('', views.index, name='index'),
]
