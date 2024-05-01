from django.db import models
from django.utils import timezone

# Create your models here.
class contact(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Email = models.CharField(max_length=100, blank=False) 
    Message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    DisplayFields = ['Name', 'Email', 'Message', 'timestamp']
    FilterFields = ['timestamp'] 

    def __str__(self):
        return self.Name 
