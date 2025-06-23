from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from house.models import Contact, BookNow, AddPlace, AddVillaApartment, CustomerReview
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    places = AddPlace.objects.all()
    villas = AddVillaApartment.objects.all()
    reviews = CustomerReview.objects.all()
    context = {
        'places' : places, 
        'villas' : villas,
        'reviews' : reviews
        }
    return render(request,'realestate/index.html',context)

def about(request):
    return render(request,'realestate/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        thank = True
        contact = Contact(name=name, email=email, phone=phone, address=address, subject=subject, message=message)
        contact.save()
        # Send email to yourself
        full_message = f"""
        New contact form submission:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Address: {address}
        Subject: {subject}
        Message: {message}
        """

        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['jandicki12@gmail.com'],  # Your email
            fail_silently=False,
        )
        messages.success(request, "Thanks for contacting with us we'll back soon.")
        return redirect('/')
    return render(request,'realestate/contact.html')

def service(request):
    reviews = CustomerReview.objects.all()
    context = {'reviews':reviews}
    return render(request,'realestate/service.html',context)

def booking_now(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        place = request.POST.get('place','')
        home = request.POST.get('home','')
        thank = True
        booking = BookNow(name=name, email=email, phone=phone, address=address, place=place, home=home)
        booking.save()
        # Send email to yourself
        full_message = f"""
        New booking form submission:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Address: {address}
        place: {place}
        home: {home}
        """

        send_mail(
            subject=f"New Booking Form Submission: {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['jandicki12@gmail.com'],  # Your email
            fail_silently=False,
        )
        messages.success(request, "Thanks for booking with us we'll back soon.")
        return redirect('/')
    
    return render(request,'/')