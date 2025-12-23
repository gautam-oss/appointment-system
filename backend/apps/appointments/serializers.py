from rest_framework import serializers
from .models import Appointment
from apps.doctors.serializers import DoctorSerializer
from apps.patients.serializers import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    # For Reading: Show full details
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    patient_details = PatientSerializer(source='patient', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 
                  'reason', 'status', 'doctor_details', 'patient_details']
        
        # Prevent the frontend from manually setting the patient/doctor via JSON
        # (We will set these automatically in the View based on the logged-in user)
        read_only_fields = ['patient', 'doctor', 'status']