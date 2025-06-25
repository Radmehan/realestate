from django.db import models
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import os
from io import BytesIO
from cssdesign .utils import extract_image_id, construct_new_link

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'house/service_account.json'
PARENT_FOLDER_ID = "1xtLZbtLQ4TYMjl6F73dLnfrfkJjvd6OL"

def authenticated() -> service_account.Credentials:
    return service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def upload_photo(image_data: bytes, file_name: str) -> str:
    creds = authenticated()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_name,
        'parents': [PARENT_FOLDER_ID]
    }

    media = MediaIoBaseUpload(BytesIO(image_data), mimetype='image/jpeg')
    file = service.files().create(body=file_metadata, media_body=media).execute()
    return file.get('id')


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
    image_id = models.CharField(max_length=255, null=True, blank=True)

    sub_image1 = models.ImageField(upload_to="house/images/place",default="")
    sub_image1_id = models.CharField(max_length=255, null=True, blank=True)

    sub_image2 = models.ImageField(upload_to="house/images/place",default="")
    sub_image2_id = models.CharField(max_length=255, null=True, blank=True)

    sub_image3 = models.ImageField(upload_to="house/images/place",default="")
    sub_image3_id = models.CharField(max_length=255, null=True, blank=True)

    place_name = models.TextField()
    about_place = models.TextField()
    place_loacation = models.TextField()
    city = models.TextField()
    

    def __str__(self):
        return self.city
    
    def save(self, *args, **kwargs):
        if self.image:
            file_name = os.path.basename(self.image.name)
            image_id = upload_photo(self.image.read(), file_name)
            if image_id:
                self.image_id = construct_new_link(image_id)
            else:
                self.image_id = "No ID Available"
        super().save(*args, **kwargs)

        if self.sub_image1:
            file_name = os.path.basename(self.sub_image1.name)
            sub_image1_id = upload_photo(self.sub_image1.read(), file_name)
            if sub_image1_id:
                self.sub_image1_id = construct_new_link(sub_image1_id)
            else:
                self.sub_image1_id = "No ID Available"
        super().save(*args, **kwargs)

        if self.sub_image2:
            file_name = os.path.basename(self.sub_image2.name)
            sub_image2_id = upload_photo(self.sub_image2.read(), file_name)
            if sub_image2_id:
                self.sub_image2_id = construct_new_link(sub_image2_id)
            else:
                self.sub_image2_id = "No ID Available"
        super().save(*args, **kwargs)

        if self.sub_image3:
            file_name = os.path.basename(self.sub_image3.name)
            sub_image3_id = upload_photo(self.sub_image3.read(), file_name)
            if sub_image3_id:
                self.sub_image3_id = construct_new_link(sub_image3_id)
            else:
                self.sub_image3_id = "No ID Available"
        super().save(*args, **kwargs)
    
    

class Type(models.Model):
    villa_appartment = models.CharField(max_length=30)

    def __str__(self):
        return self.villa_appartment
    

class AddVillaApartment(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="house/images/house")
    image_id = models.CharField(max_length=255, null=True, blank=True)
    sub_image1 = models.ImageField(upload_to="house/images/home")
    sub_image1_id = models.CharField(max_length=255, null=True, blank=True)
    sub_image2 = models.ImageField(upload_to="house/images/home")
    sub_image2_id = models.CharField(max_length=255, null=True, blank=True)
    sub_image3 = models.ImageField(upload_to="house/images/home")
    sub_image3_id = models.CharField(max_length=255, null=True, blank=True)
    villa_or_apartment_name = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    about = models.TextField()
    loacation = models.TextField()
    city = models.TextField()
    bed = models.CharField(max_length=14)
    washroom = models.CharField(max_length=14)

    def __str__(self):
        return self.villa_or_apartment_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            # Upload the image image to Google Drive
            file_name = os.path.basename(self.image.name)
            image_id = upload_photo(self.image.read(), file_name)
            
            # Check if image_id is not None
            if image_id:
                self.image_id = image_id

                
                modified_link = construct_new_link(image_id)
                self.image_id = modified_link

                super().save(*args, **kwargs)
            else:
                self.image_id = "No ID Available"
                super().save(*args, **kwargs)
        
        if self.sub_image1:
            # Upload the sub_image1 image to Google Drive
            file_name = os.path.basename(self.sub_image1.name)
            sub_image1_id = upload_photo(self.sub_image1.read(), file_name)
            
            # Check if sub_image1_id is not None
            if sub_image1_id:
                self.sub_image1_id = sub_image1_id

                
                modified_link = construct_new_link(sub_image1_id)
                self.sub_image1_id = modified_link

                super().save(*args, **kwargs)
            else:
                self.sub_image1_id = "No ID Available"
                super().save(*args, **kwargs)
        
        if self.sub_image2:
            # Upload the sub_image2 image to Google Drive
            file_name = os.path.basename(self.sub_image2.name)
            sub_image2_id = upload_photo(self.sub_image2.read(), file_name)
            
            # Check if sub_image2_id is not None
            if sub_image2_id:
                self.sub_image2_id = sub_image2_id

                
                modified_link = construct_new_link(sub_image2_id)
                self.sub_image2_id = modified_link

                super().save(*args, **kwargs)
            else:
                self.sub_image2_id = "No ID Available"
                super().save(*args, **kwargs)

        if self.sub_image3:
            # Upload the sub_image3 image to Google Drive
            file_name = os.path.basename(self.sub_image3.name)
            sub_image3_id = upload_photo(self.sub_image3.read(), file_name)
            
            # Check if sub_image3_id is not None
            if sub_image3_id:
                self.sub_image3_id = sub_image3_id

                
                modified_link = construct_new_link(sub_image3_id)
                self.sub_image3_id = modified_link

                super().save(*args, **kwargs)
            else:
                self.sub_image3_id = "No ID Available"
                super().save(*args, **kwargs)

    

class CustomerReview(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    image = models.ImageField(upload_to="house/images/rivews")
    image_id = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            # Upload the image image to Google Drive
            file_name = os.path.basename(self.image.name)
            image_id = upload_photo(self.image.read(), file_name)
            
            # Check if image_id is not None
            if image_id:
                self.image_id = image_id

                
                modified_link = construct_new_link(image_id)
                self.image_id = modified_link

                super().save(*args, **kwargs)
            else:
                self.image_id = "No ID Available"
                super().save(*args, **kwargs)