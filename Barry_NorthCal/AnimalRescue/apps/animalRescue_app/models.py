from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class UploadImageModel(models.Model):
    title = models.CharField(max_length = 45)
    image = models.FileField(upload_to = 'uploads/')
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = UserManager()

class FosterParent(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    city = models.CharField(max_length = 45)
    zipcode = models.CharField(max_length=5)
    street_address = models.CharField(max_length = 45)
    email_address = models.CharField(max_length = 45)
    phone_regex = RegexValidator(regex = '^\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$', message = "Please format phone number as: (555) 123-4567")
    phone_number = models.CharField(validators=[phone_regex], max_length = 14, blank = True)
    animal_type_preference = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Content(models.Model):
    name = models.CharField(max_length = 45)
    image = models.FileField(upload_to = 'uploads/')
    description = models.FileField(max_length = 100, default="Description")
    data = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Animal(models.Model):
    #when an animal of a certain type is found admin can pull fosterparent list based on preference
    DOG = 'DOG'
    CAT = 'CAT'
    GERBLE = 'GERBLE'
    HAMSTER = 'HAMSTER'
    ANIMAL_TYPE_CHOICES = (
    (DOG, 'Dog'), (CAT, 'Cat'), (GERBLE, 'Gerble'), (HAMSTER, 'Hamster')
    )
    type = models.CharField(max_length = 45, choices = ANIMAL_TYPE_CHOICES)
    name = models.CharField(max_length = 45)
    location = models.CharField(max_length = 75)
    image = models.FileField(upload_to = 'uploads/')
    description = models.FileField(max_length = 100, default="Description")
    fosterParent = models.ForeignKey(FosterParent, blank = True, null = True)
    adoption_ready = models.BooleanField(default = False)
    foster_ready = models.BooleanField(default = False)
    viewable = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
