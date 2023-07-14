from django.shortcuts import render
from django.http import HttpResponse
from .models import Ghazals
# Create your views here.

def index(request):
    ghazals = Ghazals.objects.all()
    context = {
        'posts':ghazals,
        'app_name':'ghazals',
        'path_name':'ghazal'
        }
    return render(request, 'index.html', context)

def view_ghazal(request, post_id):
    ghazal = Ghazals.objects.get(id=post_id)
    return render(request, 'post.html', {
        'post':ghazal
    })