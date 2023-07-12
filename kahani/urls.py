from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:kahani_id>", views.view_kahani, name="kahani")
]