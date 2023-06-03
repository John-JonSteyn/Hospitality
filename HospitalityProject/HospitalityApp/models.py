from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class MedicalHistory(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_condition = models.CharField(max_length=255)
    treatment = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Medical History for {self.patient}'
