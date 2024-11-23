from django.shortcuts import render
from .models import Track 

# Create your views here.
def home(request):
    return render(request, 'ngempela/home.html')

def ngempela(request):
    tracks = Track.objects.all()
    return render(request, 'ngempela/ngempela.html', {'tracks': tracks})

def about(request):
    return render(request, 'ngempela/about.html')

def contact(request):
    return render(request, 'ngempela/contact.html')
