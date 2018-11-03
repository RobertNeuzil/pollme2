from django.shortcuts import render
from django.http import HttpResponse


def polls_list(request):
	return HttpResponse("<h1> polls_list page </h1>")


# Create your views here.
