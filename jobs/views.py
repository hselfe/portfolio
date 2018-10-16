from django.shortcuts import render

from .models import Home
from .models import Job
from .models import About
from .models import Contact

# Create your views here.
def home(request):
    homes = Home.objects
    jobs = Job.objects.order_by('id')
    return render(request, 'jobs/home.html', {'jobs':jobs, 'homes':homes})

def about(request):
    abouts = About.objects
    return render(request, 'jobs/about.html', {'abouts':abouts})

def contact(request):
    contacts = Contact.objects
    return render(request, 'jobs/contact.html', {'contacts':contacts})
