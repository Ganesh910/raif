from django.urls import path
from . import views

app_name='story'
urlpatterns=[
    path("", views.index, name='index'),
    path("<int:post_id>", views.view_story, name='story')
]