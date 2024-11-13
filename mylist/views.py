from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def list(request):
    return render(request, 'mylist/index.html')
    # return HttpResponse("You are looking at you're to do list that is beeing build right now!")