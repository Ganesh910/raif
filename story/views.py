from django.shortcuts import render
from django.http import HttpResponse
from .models import Story

# Create your views here.
def index(request):
    stories = Story.objects.order_by("-date_written")
    context = {
        'posts':stories,
        'app_name':'story',
        'path_name':'story',
        'title':'Stories',
    }

    return render(request, 'index.html', context)

def view_story(request, post_id):
    story = Story.objects.get(id=post_id)
    context = {
        "post":story
    }

    return render(request, 'post.html', context)