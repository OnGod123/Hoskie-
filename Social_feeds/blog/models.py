from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    content = models.TextField()
    video = models.FileField(upload_to="profile_videos", blank=True, null=True)  # Field for profile video
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blogs')  # Assuming you have a 'blogs' URL pattern

