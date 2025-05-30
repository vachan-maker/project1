from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

now = datetime.now()

# Create your views here.
def index(request):
    if(now.month == 1 and now.day == 1):
        return HttpResponse("Happy New Year")
    else:
        return HttpResponse("There is still time my friend")
    

# CS50 implementation
def newyear(request):
    return render(request,"new/index.html",{
        "newyear":now.month == 1 and now.day == 1
    })