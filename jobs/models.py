from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    fulltext = models.TextField()
    feedback = models.TextField()

class About(models.Model):
    headertext = models.TextField()
    fulltext = models.TextField()

class Contact(models.Model):
    fulltext = models.TextField()
