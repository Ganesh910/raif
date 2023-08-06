from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    context = {
        'post':{'title':'Raif',
                'date_written':"Urf Ganesh Pandey",
                 'content':"Step into my poetic realm! I'm Ganesh Pandey, a Computer Engineering student who loves to express through heartfelt verses. \n\nIn the world of codes and tech, I found a beautiful escape in poetry. Words became my canvas to paint emotions and dreams.\n\nHere, you'll find my poems, each a glimpse into my heart. From nature's wonders to human connections, I explore it all.\n\nLet's embark on this journey together, where technology and poetry unite. I hope my words touch your soul.\n\nWelcome and enjoy!" }
    }
    return render(request, 'post.html', context)

def home(request):
    context = {
        'post':{
        'title':"Raif Writes",
        'date_written':"This Is Home (page)",
        'content':"While my homepage is still taking shape, I invite you to join me on this voyage of words and emotions. Soon, this space will be filled with the magic of poetry, where nature's beauty and human experiences intertwine. \n\nIn the meantime, stay tuned, for I am crafting each verse with care, just for you. Let's embark on this poetic adventure together, celebrating the harmony of technology and the art of expression. \n\nThank you for your patience, and I can't wait to share my poems with you soon!"
        }
    }
    return render(request, 'post.html', context)
