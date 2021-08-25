from django.http import HttpResponse
from django.shortcuts import render
from .models import FarmItem


def index(request):
    crops = FarmItem.objects.all()
    return render(request, 'index.html', {'items': crops})
