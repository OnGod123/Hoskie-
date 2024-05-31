from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True, blank=True)

