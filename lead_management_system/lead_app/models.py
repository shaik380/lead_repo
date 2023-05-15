from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(('open', 'Open'), ('pending', 'Pending'), ('completed', 'Completed')), default='open')

class Mapping(models.Model):
    db_field = models.CharField(max_length=255)
    csv_header = models.CharField(max_length=255)