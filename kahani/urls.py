from django.urls import path
from . import views

# To avoid namespace collisions
app_name  = "kahani"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:kahani_id>", views.view_kahani, name="post")
]