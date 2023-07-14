from django.db import models
# Create your models here.

class Nazm(models.Model):
    date_written = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=255)
    content = models.TextField()