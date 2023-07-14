from django.shortcuts import render
from django.http import HttpResponse
from .models import Nazm

# Create your views here.

def index(request):
    nazms = Nazm.objects.all()
    context = {
        'posts':nazms,
        'app_name':'nazm',
        'path_name':'nazm'
    }
    return render(request, 'index.html', context)

def view_nazm(request, post_id):
    nazm = Nazm.objects.get(id=post_id)
    context = {
        'post':nazm
    }
    return render(request, 'post.html', context)