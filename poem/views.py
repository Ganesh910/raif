from django.shortcuts import render
from django.http import HttpResponse
from .models import Poem

# Create your views here.

def index(request):
    poem = Poem.objects.all()
    context = {
        'posts':poem,
        'app_name':'poem',
        'path_name':'poem',
        'title':'Poems',
    }
    return render(request, 'index.html', context)

def view_poem(request, post_id):
    poem = Poem.objects.get(id=post_id)
    context = {
        'post':poem
    }
    return render(request, 'post.html', context)