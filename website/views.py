from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        # send an email

        send_mail(
            'Message from: ' + first_name + ' ' + last_name + '. Subject: ' + subject,# subject
            message, # message
            email, # form email
            ['piotr.puchalaa@gmail.com'], # to Email
            fail_silently=False,

        )

        return render(request, 'home.html', {'first_name' : first_name})
    else:
        return  render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        # send an email

        send_mail(
            'Message from: ' + first_name + ' ' + last_name + '. Subject: ' + subject,# subject
            message, # message
            email, # form email
            ['piotr.puchalaa@gmail.com'], # to Email
            fail_silently=False,

        )

        return render(request, 'contact.html', {'first_name' : first_name})
    else:
        return  render(request, 'contact.html', {})

def gallery(request):
    return  render(request, 'gallery.html', {})

def services(request):
    return  render(request, 'services.html', {})

def story(request):
    return  render(request, 'story.html', {})

def location(request):
    return  render(request, 'location.html', {})

def tables(request):
    return  render(request, 'tables.html', {})