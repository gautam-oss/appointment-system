from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListView(generics.ListAPIView):
    """
    Publicly list all doctors so patients can search.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]

class DoctorDetailView(generics.RetrieveUpdateAPIView):
    """
    Allow a doctor to update their own profile.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensure a user can only edit their OWN doctor profile
        return self.request.user.doctor_profile