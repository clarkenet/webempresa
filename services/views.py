from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    servs = Service.objects.all()
    return render(request, 'services/services.html', {"page_name": "Servicios", "services": servs})
