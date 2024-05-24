from django.db import models
import uuid

class User(models.Model):
    # Choices for relationship status, sexual orientation, and race...
    # (You can reuse the choices defined in the previous Person model)

    username_or_email = models.CharField(max_length=254, unique=True)  # Max length for email field
    password = models.CharField(max_length=128)  # Password field

    # File path field for binary data
    file_path = models.FileField(upload_to='uploads/%Y/%m/%d/')

    # Additional fields as needed

    def __str__(self):
        return self.username_or_email

