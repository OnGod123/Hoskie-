from django.conf import settings
from django.db import models
import uuid
from django.contrib.auth.hashers import make_password

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    new_password = models.CharField(max_length=128
