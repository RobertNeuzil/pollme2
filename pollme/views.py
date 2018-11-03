from django.http import HttpResponse
import datetime
from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    html = f'The current time is {now}'
    return HttpResponse(html)

def home(request):
	now = datetime.datetime.now()
	context = {
	'now': now
	}
	return render(request, 'home.html', context)


