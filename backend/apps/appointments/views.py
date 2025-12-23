from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # If user is a Doctor, return appointments where they are the doctor
        if user.role == 'DOCTOR':
            return Appointment.objects.filter(doctor__user=user)
        # If user is a Patient, return appointments where they are the patient
        elif user.role == 'PATIENT':
            return Appointment.objects.filter(patient__user=user)
        return Appointment.objects.none()

    def perform_create(self, serializer):
        # Automatically assign the logged-in patient
        # (The frontend sends the doctor_id in the body)
        serializer.save(patient=self.request.user.patient_profile)

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to Cancel (Destroy) or Update status of an appointment
    """
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'DOCTOR':
            return Appointment.objects.filter(doctor__user=user)
        return Appointment.objects.filter(patient__user=user)