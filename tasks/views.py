from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
tasks = ["foo","bar","baz"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="newtask")
    number = forms.IntegerField(label="Priority",min_value=1,max_value=10)
# Create your views here.

def index(request):
    return render(request, "tasks/index.html",{
        "tasks":tasks
    })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # if form is valid then save the cleaned data to a variable called tasks
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else: # if form is not valid
            return render(request, "tasks/add.html",{
                "form":form
            }) #send back the existing form data
    return render(request, "tasks/add.html",{
        "form":NewTaskForm()
    })