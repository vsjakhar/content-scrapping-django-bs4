from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Scrap


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def scrap(request):
    a_list = Scrap.objects.all()
    context = {'year': '2018', 'article_list': a_list}
    return render(request, 'demo/scrap.html', context)