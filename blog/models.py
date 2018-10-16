from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    link_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
