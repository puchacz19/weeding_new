from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('services/', views.services, name="services"),
    path('story/', views.story, name="story"),
    path('tables/', views.tables, name="tables"),
    path('location/', views.location, name="location"),
]
