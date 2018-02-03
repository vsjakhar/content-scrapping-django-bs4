from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Scrap

import json
from bs4 import BeautifulSoup
from urllib.request import urlopen



def index(request):
	html = urlopen("http://www.donbest.com/nfl/odds/20180204.html")
	# print(html)
	soup = BeautifulSoup(html, 'html.parser')
	finalh = soup.prettify()
	#print(soup.prettify())
	return HttpResponse(finalh)

def scrapa(request):
	html = urlopen("http://www.donbest.com/nfl/odds/20180204.html")
	soup = BeautifulSoup(html, 'html.parser')
	links = []
	for link in soup.find_all('a'):
		links.append([link.get('href')])
		print(link.get('href'))
	finalh = json.dumps({'data':links})
	return HttpResponse(finalh, content_type='application/json')

def scrapta(request):
	html = urlopen("http://www.donbest.com/nfl/odds/20180204.html")
	soup = BeautifulSoup(html, 'html.parser')
	links = []
	for link in soup.find('table').find_all('a'):
		links.append([link.get('href')])
		print(link.get('href'))
	finalh = json.dumps({'data':links})
	return HttpResponse(finalh, content_type='application/json')

def scrapcls(request):
	html = urlopen("http://www.donbest.com/nfl/odds/20180204.html")
	soup = BeautifulSoup(html, 'html.parser')
	links = []
	for link in soup.find('div',class_='odds_gamesHolder').find_all('a'):
		links.append([link.get('href')])
		print(link.get('href'))
	finalh = json.dumps({'data':links})
	return HttpResponse(finalh, content_type='application/json')

def scrap(request):
    a_list = Scrap.objects.all()
    context = {'year': '2018', 'article_list': a_list}
    return render(request, 'demo/scrap.html', context)