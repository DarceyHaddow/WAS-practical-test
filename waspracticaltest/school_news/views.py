from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'School News'}
    return render(request, 'school_news/index.html', context=context_dict)
