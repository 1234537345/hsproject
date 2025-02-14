# Generated by Django 4.2.16 on 2024-09-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='name',
        ),
        migrations.AddField(
            model_name='department',
            name='departments',
            field=models.CharField(blank=True, choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], max_length=30, null=True),
        ),
    ]
