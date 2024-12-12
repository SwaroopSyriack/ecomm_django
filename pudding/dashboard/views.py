from django.shortcuts import render
from item.models import Item

# Create your views here.

def index(request):
    items = Item.objects.filter(created_by = request.user)
    return render(request,'dashboard/index.html',{
        'items' : items,
        
    }) 