from django.contrib import admin
from .models import *

@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'contact_number', 'availability')
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'contact_number', 'insurance_provider')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'dentist', 'appointment_date', 'status')

@admin.register(MedicalCondition)
class MedicalConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(PatientMedicalCondition)
class PatientMedicalConditionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'condition', 'diagnosis_date', 'status')

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')

@admin.register(PatientTreatment)
class PatientTreatmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'treatment', 'treatment_date', 'status')

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referring_dentist', 'referred_patient', 'referral_type', 'status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'payment_date', 'payment_method', 'status')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'quantity', 'cost')

@admin.register(DentistInventory)
class DentistInventoryAdmin(admin.ModelAdmin):
    list_display = ('dentist', 'inventory_item', 'quantity_used', 'usage_date')
