from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    now = datetime.now()
    if(now.month == 1 and now.day == 1):
        return HttpResponse("Happy New Year")
    else:
        return HttpResponse("There is still time my friend")