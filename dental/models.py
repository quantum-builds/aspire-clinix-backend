from django.db import models

class Dentist(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50, unique=True)
    availability = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('No Show', 'No Show'),
    ])

    def __str__(self):
        return f'{self.patient.name} with {self.dentist.name} on {self.appointment_date}'


class MedicalCondition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class PatientMedicalCondition(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.ForeignKey(MedicalCondition, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Active', 'Active'),
        ('Resolved', 'Resolved'),
    ])

    def __str__(self):
        return f'{self.patient.name} - {self.condition.name}'


class Treatment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class PatientTreatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    treatment_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ])

    def __str__(self):
        return f'{self.patient.name} - {self.treatment.name}'


class Referral(models.Model):
    referring_dentist = models.ForeignKey(Dentist, related_name='referring_dentist', on_delete=models.CASCADE)
    referred_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referral_type = models.CharField(max_length=255, choices=[
        ('Implants', 'Implants'),
        ('Periodontology', 'Periodontology'),
        ('Oral Surgery', 'Oral Surgery'),
        ('Dentures', 'Dentures'),
        ('Root Canal', 'Root Canal'),
        ('Paediatric dentistry', 'Paediatric dentistry'),
        ('Orthodontics', 'Orthodontics'),
        ('Treatment Planning and Advice', 'Treatment Planning and Advice'),
        ('Other', 'Other'),
    ])
    referral_details = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
    ])

    def __str__(self):
        return f'{self.referred_patient.name} referred by {self.referring_dentist.name}'


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50, choices=[
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
        ('Insurance', 'Insurance'),
    ])
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ])

    def __str__(self):
        return f'Payment of {self.amount} by {self.patient.name}'


class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name


class DentistInventory(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_used = models.IntegerField()
    usage_date = models.DateField()

    def __str__(self):
        return f'{self.dentist.name} used {self.inventory_item.item_name}'
