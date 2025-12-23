from django.db import models
from django.contrib.auth import get_user_model

# We get the User model dynamically
User = get_user_model()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField(help_text="e.g. MBBS, MD")
    experience_years = models.PositiveIntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.user.username} - {self.specialization}"