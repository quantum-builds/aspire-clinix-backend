from rest_framework import serializers
from .models import *

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = ['id', 'name', 'address', 'contact_number', 'email', 'specialization', 'registration_number', 'availability']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'dob', 'gender', 'contact_number', 'email', 'address', 'insurance_provider', 'insurance_policy_number']

class AppointmentSerializer(serializers.ModelSerializer):
    dentist = DentistSerializer()
    patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'dentist', 'patient', 'appointment_date', 'status']

class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCondition
        fields = ['id', 'name', 'description']

class PatientMedicalConditionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    condition = MedicalConditionSerializer()

    class Meta:
        model = PatientMedicalCondition
        fields = ['patient', 'condition', 'diagnosis_date', 'status']

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['id', 'name', 'description', 'cost']

class PatientTreatmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    treatment = TreatmentSerializer()

    class Meta:
        model = PatientTreatment
        fields = ['patient', 'treatment', 'treatment_date', 'status']

class ReferralSerializer(serializers.ModelSerializer):
    referring_dentist = DentistSerializer()
    referred_patient = PatientSerializer()

    class Meta:
        model = Referral
        fields = ['referring_dentist', 'referred_patient', 'referral_type', 'referral_details', 'status']

class PaymentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Payment
        fields = ['patient', 'amount', 'payment_date', 'payment_method', 'status']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'item_name', 'description', 'quantity', 'cost']

class DentistInventorySerializer(serializers.ModelSerializer):
    dentist = DentistSerializer()
    inventory_item = InventorySerializer()

    class Meta:
        model = DentistInventory
        fields = ['dentist', 'inventory_item', 'quantity_used', 'usage_date']
