from django.urls import path
from . import views

app_name='ghazals'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:post_id>", views.view_ghazal, name='ghazal')
]