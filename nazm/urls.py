from django.urls import path
from . import views


app_name="nazm"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:post_id>", views.view_nazm, name='nazm')
]