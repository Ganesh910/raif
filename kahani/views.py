from django.shortcuts import render
from django.http import HttpRequest
from .models import Kahani

# Create your views here.

def index(request):
    kahani = Kahani.objects.all()
    return render(request, "index.html", {
        "kahanis":kahani
    })

# It will render the page for a story. Take id for the kahani as input
def view_kahani(request, kahani_id):

    # get me the story from the models with this id
    kahani = Kahani.objects.get(id=kahani_id)

    # render the kahani.html page and pass the values of kahani
    return render(request, "post.html", {
        "kahani":kahani
    })