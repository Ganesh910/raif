from django.db import models

# Create your models here.

class Kahani(models.Model):
    date_written = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()
