from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class BookNow(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    home = models.CharField(max_length=30)

class AddPlace(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="house/images/place")
    sub_image1 = models.ImageField(upload_to="house/images/place",default="")
    sub_image2 = models.ImageField(upload_to="house/images/place",default="")
    sub_image3 = models.ImageField(upload_to="house/images/place",default="")
    place_name = models.TextField()
    about_place = models.TextField()
    place_loacation = models.TextField()
    city = models.TextField()
    

    def __str__(self):
        return self.city
    

class Type(models.Model):
    villa_appartment = models.CharField(max_length=30)

    def __str__(self):
        return self.villa_appartment
    

class AddVillaApartment(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="house/images/house")
    sub_image1 = models.ImageField(upload_to="house/images/home")
    sub_image2 = models.ImageField(upload_to="house/images/home")
    sub_image3 = models.ImageField(upload_to="house/images/home")
    villa_or_apartment_name = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    about = models.TextField()
    loacation = models.TextField()
    city = models.TextField()
    bed = models.CharField(max_length=14)
    washroom = models.CharField(max_length=14)

    def __str__(self):
        return self.villa_or_apartment_name
    

class CustomerReview(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    image = models.ImageField(upload_to="house/images/rivews")
    description = models.TextField()