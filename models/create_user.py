from django.db import models
import uuid

class Person(models.Model):
    RELATIONSHIP_CHOICES = (
        ('single', 'Single'),
        ('in_relationship', 'In a Relationship'),
        ('engaged', 'Engaged'),
        ('married', 'Married'),
        ('complicated', 'It\'s Complicated'),
    )

    SEXUAL_ORIENTATION_CHOICES = (
        ('gay', 'Gay'),
        ('lesbian', 'Lesbian'),
        ('straight', 'Straight'),
        ('other', 'Other'),
    )

    RACE_CHOICES = (
        ('white', 'White'),
        ('black', 'Black'),
        ('asian', 'Asian'),
        ('hispanic', 'Hispanic'),
        ('other', 'Other'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    relationship_status = models.CharField(max_length=15, choices=RELATIONSHIP_CHOICES)
    sexual_orientation = models.CharField(max_length=10, choices=SEXUAL_ORIENTATION_CHOICES)
    race = models.CharField(max_length=10, choices=RACE_CHOICES)
    phone_number = models.CharField(max_length=15)  # Adjust max_length as needed
    social_media_api = models.URLField()  # Assuming this will hold social media API URL
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Password field

    # Additional fields as needed

