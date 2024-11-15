from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'dentists', views.DentistViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'medical_conditions', views.MedicalConditionViewSet)
router.register(r'patient_medical_conditions', views.PatientMedicalConditionViewSet)
router.register(r'treatments', views.TreatmentViewSet)
router.register(r'patient_treatments', views.PatientTreatmentViewSet)
router.register(r'referrals', views.ReferralViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'dentist_inventory', views.DentistInventoryViewSet)

urlpatterns = [
    path('dental/', include(router.urls)),
]