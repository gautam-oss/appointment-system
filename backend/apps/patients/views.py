from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientDetailView(generics.RetrieveUpdateAPIView):
    """
    Allow a patient to view/update their own profile.
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the profile of the currently logged-in user
        return self.request.user.patient_profile