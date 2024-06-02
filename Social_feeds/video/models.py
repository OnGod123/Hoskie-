# models.py

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file_path = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)

