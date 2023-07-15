from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    context = {
        'post':{'title':'Raif',
                'date_written':"Urf Ganesh Pandey",
                 'content':"Kya janna chahte ho mere baare mein? \n You are here, it means you already know me. So go and just read my poems. \n \n And yes, don't forget to DM me to say ki wah Ganesh kya likhta hai tu. Bs pr dil se khna hai tumhe, let's assume I haven't asked you to say this to me :) " }
    }
    return render(request, 'post.html', context)

def home(request):
    context = {
        'post':{
        'title':"Raif Writes",
        'date_written':"This Is Home (page)",
        'content':"Mitr! I am too busy right now! I'll make a different Home page later. Tb tk tum Navigation Bar se Kaam chala lo please. \n Don't forget to check out About page, I've left a special message for you there ;)"
        }
    }
    return render(request, 'post.html', context)