from django.shortcuts import render
from .models import *

# Create your views here.


def IndexView(request):
    summarisedService = SummarisedServiceModel.objects.all()

    context = {
        "summarisedService": summarisedService
    }

    return render(request, 'client/index.html', context)


def AboutView(request):
    return render(request, 'client/about.html')


def ServicesView(request):
    services = ServiceModel.objects.all()

    context = {
        "services": services
    }

    return render(request, 'client/services.html', context)


def GalleryView(request):
    images = GalleryModel.objects.all()

    context = {
        "images": images
    }

    return render(request, 'client/gallery.html', context)


def ContactView(request):
    return render(request, 'client/contactUs.html')

