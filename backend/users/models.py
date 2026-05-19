from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Define the available roles
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('CITIZEN', 'Citizen'),
        ('DRIVER', 'Driver'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CITIZEN')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.role}"