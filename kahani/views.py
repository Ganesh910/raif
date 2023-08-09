from django.shortcuts import render
from django.http import HttpRequest
from .models import Kahani

# Create your views here.

def index(request):
    kahani = Kahani.objects.all()
    context = {
        "posts":kahani,
        'app_name':'kahani',
        'path_name':'kahani',
        'title':'कहानी',
    }
    return render(request, "index.html", context)

# It will render the page for a story. Take id for the kahani as input
def view_kahani(request, post_id):

    # get me the story from the models with this id
    kahani = Kahani.objects.get(id=post_id)

    # render the kahani.html page and pass the values of kahani
    return render(request, "post.html", {
        "post":kahani
    })