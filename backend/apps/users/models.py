import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # IDs are better as UUIDs for security (prevents guessing user ID 1, 2, 3...)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk: # If this is a new user
            self.role = self.base_role
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username