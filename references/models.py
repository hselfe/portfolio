from django.db import models

# Create your models here.

class Reference(models.Model):
    image = models.ImageField(upload_to='images/')
    company = models.CharField(max_length=200)
    reference_name = models.TextField()
    email_address = models.TextField()
