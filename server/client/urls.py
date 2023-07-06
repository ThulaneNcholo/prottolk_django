
from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('about', views.AboutView, name='about'),
    path('services', views.ServicesView, name='services'),
    path('gallery', views.GalleryView, name='gallery'),
    path('contact', views.ContactView, name='contact'),
]
