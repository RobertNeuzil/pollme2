from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = f'The current time is {now}'
    return HttpResponse(html)