from django.urls import path
from .views import PatientDetailView

urlpatterns = [
    path('profile/', PatientDetailView.as_view(), name='patient-profile'),
]