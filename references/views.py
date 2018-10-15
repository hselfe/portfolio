from django.shortcuts import render

from .models import Reference

# Create your views here.
def references(request):
    references = Reference.objects
    return render(request, 'references/references.html', {'references':references})
