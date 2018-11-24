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


def poll_detail(request, poll_id):
    """
    Render the poll_detail.html template which allows a user to vote
    on the choices of a poll
    """
    poll = Poll.objects.get(id=poll_id)
    

    context = {'poll': poll}
    return render(request, 'polls/poll_detail.html', context)


# Create your views here.
