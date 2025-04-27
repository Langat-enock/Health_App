# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models




from django.db import models

class Doctor(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)





class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'client'

class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} enrolled in {self.enrollment_date}"
    class Meta:
        db_table = 'enrollment'


class HealthProgram(models.Model):
    PROGRAM_CHOICES = [
        ('TB', 'Tuberculosis'),
        # ('MAL', 'Malaria'),
        # ('HIV', 'HIV/AIDS'),
    ]
    name = models.CharField(max_length=20, choices=PROGRAM_CHOICES)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.get_name_display()

class ClientProfile(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    medical_history = models.TextField(blank=True)

    class Meta:
        db_table = 'client_profile'

    def __str__(self):
        return self.user.first_name

class ProgramEnrollment(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} in {self.program}"
    class Meta:
        db_table = 'program_enrollment'






