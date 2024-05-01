from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    location1 = models.CharField(max_length=100, blank=False) 
    location2 = models.CharField(max_length=100, blank=False)
    order = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) 
    DisplayFields = ['user', 'name', 'location1', 'location2', 'order', 'timestamp']
    FilterFields = ['timestamp'] 

    def __str__(self):
        return self.name 

class CustomerProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
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
