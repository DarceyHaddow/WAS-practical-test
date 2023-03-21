from django.shortcuts import render
from django.http import HttpResponse
from school_news.models import Page

# Create your views here.
def index(request):
    page_list = Page.objects.all()

    context_dict = {}
    context_dict['pages'] = page_list
    return render(request, 'school_news/index.html', context=context_dict)
