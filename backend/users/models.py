from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Standard fields like username, email, password are included in AbstractUser
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_citizen = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username