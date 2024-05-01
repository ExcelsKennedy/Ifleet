from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Driver(models.Model):
    username = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zipcode = models.CharField(max_length=20, blank=True)
    car = models.CharField(max_length=25, blank=False)
    driver_license_number = models.CharField(max_length=50, blank=False)
    driver_license_expiry_date = models.DateField(null=True, blank=False)
    date_of_birth = models.DateField(null=True, blank=False)
    date_hired = models.DateField(null=True, blank=False)
    emergency_contact_name = models.CharField(max_length=100, blank=False)
    emergency_contact_phone = models.CharField(max_length=20, blank=False)
    DisplayFields = ['username', 'phone_number', 'address', 'city', 'driver_license_number', 'date_hired']
    FilterFields = ['username', 'date_hired'] 

    def __str__(self):
        return self.username 

class DriverProfile(models.Model):
    user = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='profile')  # Changed from User to Driver
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    DisplayFields = ['user', 'image']
    FilterFields = ['user'] 

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path) 

        if img.height > 300 or img.width > 300: 
            output_size = (300, 300) 
            img.thumbnail(output_size)
            img.save(self.image.path) 


class Inspection(models.Model):
    CATEGORY = (
        ('OK', 'OK'),
        ('NOT OK', 'NOT OK'),
    )

    FUEL = (
        ('Empty', 'Empty'),
        ('Almost Empty', 'Almost Empty'),
        ('1/4', '1/4'),
        ('1/2', '1/2'),
        ('Full', 'Full'),
    )

    VEHICLE_TYPE = (
        ('SUV', 'SUV' ),
        ('TRUCK', 'TRUCK'),
    )
    Driver = models.ForeignKey(Driver, models.CASCADE, null=True)
    vehicle = models.CharField(max_length=25, choices=VEHICLE_TYPE, blank=False, default=False)
    Mirrors = models.CharField(max_length=50, choices=CATEGORY, blank=False)
    Seats = models.CharField(max_length=100, choices=CATEGORY, blank=False) 
    Electronics = models.CharField(max_length=50, choices=CATEGORY, blank=False)
    Fuel_level = models.CharField(max_length=50, choices=FUEL, blank=False)
    Damage = models.CharField(max_length=50, choices=CATEGORY, blank=False)
    Medical_kit = models.CharField(max_length=50, choices=CATEGORY, blank=False)
    Body = models.CharField(max_length=50, choices=CATEGORY, blank=False)
    Tires = models.CharField(max_length=50, choices=CATEGORY, blank=False)
    General_Remarks = models.TextField(blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    DisplayFields = ['Driver', 'Mirrors', 'Seats', 'Electronics', 'Fuel_level', 'Damage', 'Medical_kit', 'Body', 'Tires', 'General_Remarks']
    FilterFields = ['Date'] 

class OrderAssignment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, blank=False)
    customer_email = models.EmailField(max_length=30, blank=False)
    current_location = models.CharField(max_length=100, blank=False) 
    delivery_location = models.CharField(max_length=100, blank=False)
    customer_order = models.TextField(blank=False)
    DisplayFields = ['driver', 'customer_name', 'customer_email', 'current_location', 'delivery_location', 'customer_order']
    FilterFields = ['driver', 'current_location', 'delivery_location']

class Vehicle(models.Model):
    CATEGORY = (
        ('SUV', 'SUV' ),
        ('TRUCK', 'TRUCK'),
    )
    vehicle_type = models.CharField(max_length=50, choices=CATEGORY, blank=False) 
    vehicle_model = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to='vehicle_pics', blank=False)
    license_plate_number = models.CharField(max_length=15, blank=False)
    DisplayFields = ['vehicle_type', 'vehicle_model', 'image', 'license_plate_number']
    FilterFields = ['vehicle_type'] 