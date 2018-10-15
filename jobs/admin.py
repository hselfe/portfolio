from django.contrib import admin

# Register your models here.
from .models import Job
from .models import About
from .models import Contact

admin.site.register(Job)
admin.site.register(About)
admin.site.register(Contact)
