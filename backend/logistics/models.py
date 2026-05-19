from django.db import models
from django.conf import settings

class WastePickupRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Assignment'),
        ('ASSIGNED', 'Driver Assigned'),
        ('IN_TRANSIT', 'Driver in Transit'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    
    WASTE_CATEGORIES = (
        ('PLASTIC', 'Plastic Waste'),
        ('ORGANIC', 'Organic / Food Waste'),
        ('E_WASTE', 'Electronic Waste'),
        ('PAPER', 'Paper & Cardboard'),
        ('GLASS', 'Glass & Bottles'),
        ('MIXED', 'Mixed Recyclables'),
    )

    # Relationship to our Custom User (The Citizen)
    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='pickup_requests'
    )
    
    # Address & Geospatial Coordinates
    pickup_address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # AI Estimation & Metadata
    waste_image = models.ImageField(upload_to='waste_uploads/', null=True, blank=True)
    waste_category = models.CharField(max_length=15, choices=WASTE_CATEGORIES, default='MIXED')
    estimated_volume_m3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    calculated_carbon_offset = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    # Logistics Tracking
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    preferred_window = models.CharField(max_length=100) # e.g., "Saturday, 10:00 AM - 02:00 PM"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pickup #{self.id} - {self.citizen.username} ({self.status})"


class DriverAssignment(models.Model):
    # Relates a pending request to a specific driver
    pickup_request = models.OneToOneField(
        WastePickupRequest, 
        on_delete=models.CASCADE, 
        related_name='assignment'
    )
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='driver_tasks'
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Driver {self.driver.username} -> Request #{self.pickup_request.id}"