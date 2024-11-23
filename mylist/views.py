import json
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
    all_items = ListItem.objects.all().order_by('done')
    return render(request, 'mylist/index.html', {'all_items': all_items})

def delete_item(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        item_id = data.get('itemId')
        print('deleting data', item_id)
        item = ListItem.objects.get(id = item_id)
        item.delete()
    all_items = ListItem.objects.all()
    return render(request, 'mylist/index.html', {'all_items:': all_items})

def toggle_done(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        item = ListItem.objects.get(id=item_id)
        item.done = not item.done  
        item.save()
    all_items = ListItem.objects.all()
    return HttpResponseRedirect(reverse('mylist'))