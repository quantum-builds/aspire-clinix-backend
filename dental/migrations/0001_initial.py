# Generated by Django 5.0.1 on 2024-11-14 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('specialization', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=50, unique=True)),
                ('availability', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('insurance_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('insurance_policy_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DentistInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_used', models.IntegerField()),
                ('usage_date', models.DateField()),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.dentist')),
                ('inventory_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('No Show', 'No Show')], max_length=50)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.dentist')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_date', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Resolved', 'Resolved')], max_length=50)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.medicalcondition')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField()),
                ('payment_method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash', 'Cash'), ('Insurance', 'Insurance')], max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_type', models.CharField(choices=[('Implants', 'Implants'), ('Periodontology', 'Periodontology'), ('Oral Surgery', 'Oral Surgery'), ('Dentures', 'Dentures'), ('Root Canal', 'Root Canal'), ('Paediatric dentistry', 'Paediatric dentistry'), ('Orthodontics', 'Orthodontics'), ('Treatment Planning and Advice', 'Treatment Planning and Advice'), ('Other', 'Other')], max_length=255)),
                ('referral_details', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], max_length=50)),
                ('referred_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.patient')),
                ('referring_dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referring_dentist', to='dental.dentist')),
            ],
        ),
        migrations.CreateModel(
            name='PatientTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.patient')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental.treatment')),
            ],
        ),
    ]
