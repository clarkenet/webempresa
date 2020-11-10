from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'core/home.html', {"page_name": "Portada"})


def about(request):
    return render(request, 'core/about.html', {"page_name": "Acerca de"})


def store(request):
    return render(request, 'core/store.html', {"page_name": "Visítanos"})
