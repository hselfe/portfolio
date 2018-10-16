from django.shortcuts import render

# Create your views here.
from .models import CV

# Create your views here.
def cv(request):
    cvs = CV.objects
    return render(request, 'cv/cv.html', {'cvs':cvs})
