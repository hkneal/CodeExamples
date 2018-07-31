from django import forms

from .models import UploadImageModel, Animal, FosterParent, Content
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


DOG = 'DOG'
CAT = 'CAT'
GERBIL = 'GERBIL'
HAMSTER = 'HAMSTER'
ANIMAL_TYPE_CHOICES = (
(DOG, 'Dog'), (CAT, 'Cat'), (GERBIL, 'Gerbil'), (HAMSTER, 'Hamster')
)


class LoadContent_Form(forms.Form):
    name = forms.CharField(label='Name' '(optional)', max_length=45, required=False)
    description = forms.CharField(label='Description', max_length=100, required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':32}))
    data = forms.CharField(label='Text Data', max_length=255, required=False, widget=forms.Textarea(attrs={'rows':10, 'cols':40}))

class FileFieldForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=30, min_length=3)
    image = forms.FileField(label='Select a file')
    description = forms.CharField(label='Description:', max_length=200, min_length=3)

class RegisterAnimal_Form(forms.Form):
    type = forms.ChoiceField(label='Animal Type', choices=ANIMAL_TYPE_CHOICES, required=True)
    name = forms.CharField(label='Name' '(optional)', max_length=45, required=False)
    location = forms.CharField(label='City,Street Address', max_length=75, min_length=3, required=True)
    description = forms.CharField(label='Description', max_length=100, required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':32}))
    image = forms.FileField(label='Select an image (optional)', required=False)

class UpdateAnimal_Form(forms.Form):
    type = forms.ChoiceField(label='Animal Type', choices=ANIMAL_TYPE_CHOICES, required=True)
    name = forms.CharField(label='Name', max_length=45, required=False)
    location = forms.CharField(label='City,Street Address', max_length=75, min_length=3)
    description = forms.CharField(label='Description', max_length=100, required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':32}))
    image = forms.FileField(label='Select an image (optional)', required=False)
    adoption_ready = forms.BooleanField(required = False)
    foster_ready = forms.BooleanField(required = False)
    viewable = forms.BooleanField(required = False)


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    city = forms.CharField(max_length = 45)
    zipcode = forms.CharField(max_length=5)
    street = forms.CharField(max_length = 45)
    phone_regex = RegexValidator(regex = '^\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$', message = "Please format phone number as: (555) 123-4567")
    phone_number = forms.CharField(validators=[phone_regex], max_length = 14)
    # animal_type_preference = forms.CharField(max_length = 45)
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2', 'street', 'city', 'zipcode', 'phone_number' )

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password')

#class AdoptPet_Form(forms.Form):
