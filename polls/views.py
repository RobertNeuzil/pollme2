from django.shortcuts import render
from django.http import HttpResponse
from .models import Poll 

def polls_list(request):
	'''
	Renders the polls list template, which lists all the currently availble polls
	'''
	
	polls = Poll.objects.all()

	context = {
	'polls': polls
	}
	
	return render(request, 'polls/polls_list.html', context)


# Create your views here.
