from django.db import models

# Create your models here.
class CV(models.Model):
    image = models.ImageField(upload_to='images/')
    cv_header = models.TextField()
    cv_text = models.TextField()
