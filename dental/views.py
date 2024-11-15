from rest_framework import viewsets
from .models import *
from .serializers import *

class DentistViewSet(viewsets.ModelViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalConditionViewSet(viewsets.ModelViewSet):
    queryset = MedicalCondition.objects.all()
    serializer_class = MedicalConditionSerializer

class PatientMedicalConditionViewSet(viewsets.ModelViewSet):
    queryset = PatientMedicalCondition.objects.all()
    serializer_class = PatientMedicalConditionSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

class PatientTreatmentViewSet(viewsets.ModelViewSet):
    queryset = PatientTreatment.objects.all()
    serializer_class = PatientTreatmentSerializer

class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class DentistInventoryViewSet(viewsets.ModelViewSet):
    queryset = DentistInventory.objects.all()
    serializer_class = DentistInventorySerializer
