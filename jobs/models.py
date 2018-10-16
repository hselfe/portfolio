from django.db import models

# Create your models here.
class Home(models.Model):
    header = models.CharField(max_length=200)
    fulltext = models.TextField()

    def __str__(self):
        return "Edit Home"

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    fulltext = models.TextField()
    feedback = models.TextField()

    def __str__(self):
        return self.summary

class About(models.Model):
    headertext = models.TextField()
    fulltext = models.TextField()

    def __str__(self):
        return "Edit About"

class Contact(models.Model):
    fulltext = models.TextField()

    def __str__(self):
        return "Edit Contact"
