from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    medical_history = models.TextField(blank=True, help_text="Known allergies or past conditions")

    def __str__(self):
        return f"Patient: {self.user.username}"