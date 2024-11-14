from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import ListItem

# Create your views here.
def list(request):
    if request.method == 'POST':
        print('Received data:', request.POST['itemText'])
        ListItem.objects.create(item_text = request.POST['itemText'])
    all_items = ListItem.objects.all()
    return render(request, 'mylist/index.html', {'all_items': all_items})
    # return HttpResponse("You are looking at you're to do list that is beeing build right now!")

def delete_item(request):
    if request.method == 'POST':
        print('deleting data', request.POST.get('itemId'))
        item_id = request.POST.get('itemId')
        item = ListItem.objects.get(id = item_id)
        item.delete()
    all_items = ListItem.objects.all()
    return render(request, 'mylist/index.html', {'all_items:': all_items})
    #return HttpResponseRedirect(reverse('mylist'))