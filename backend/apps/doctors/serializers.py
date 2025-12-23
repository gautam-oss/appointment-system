from rest_framework import serializers
from .models import Doctor
from apps.users.serializers import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):
    # This nests the User info inside the Doctor object
    user = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialization', 'qualifications', 
                  'experience_years', 'consultation_fee', 'is_available']