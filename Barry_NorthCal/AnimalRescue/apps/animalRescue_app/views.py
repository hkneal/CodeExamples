from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from .tokens import account_activation_token
from .forms import FileFieldForm, RegisterAnimal_Form, SignupForm, LoginForm, UpdateAnimal_Form, LoadContent_Form
from .models import UploadImageModel, Animal, FosterParent, Content

def checkAuth(req):
    if req.user.is_authenticated:
        return True
    else:
        return False

def checkUsername(req):
    if req.user.username == "hiramneal":
        return True
    else:
        return False

def index(req):
    # Animal.objects.all().delete()
    # User.objects.all().delete()
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    context = {
        'loggedIn' : logged_in,
        'all_Animals' : all_Animals,
        'auth_for_edit' : auth_for_edit
    }
    return render(req, 'animalRescue_app/index.html', context)

def upload_file(req):
    if req.method == 'POST':
        form = RegisterAnimal_Form(req.POST, req.FILES)
        if form.is_valid():
            newdoc = Animal(type = form.cleaned_data['type'], name = form.cleaned_data['name'], location = form.cleaned_data['location'], image = req.FILES['image'], description = form.cleaned_data['description'])
            newdoc.save()
            context = {
                'message' : newdoc.name + " has been created, Thank You!  You will be notified after the animal has been safely picked up.",
                'registerAnimalForm' : RegisterAnimal_Form(),
                'type' : newdoc.type,
                'name' : newdoc.name,
                'image' : newdoc.image
            }
            return render(req, 'animalRescue_app/register.html', context)
        else:
            context = {
            'registerAnimalForm' : form
            }
            return render(req, 'animalRescue_app/register.html', context)
    else:
        context = {
            'registerAnimalForm' : RegisterAnimal_Form(),
        }
        return render(req, 'animalRescue_app/register.html', context)

@login_required
def loadImage(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if logged_in and auth_for_edit:
        if req.method == 'POST':
            form = FileFieldForm(req.POST, req.FILES)
            if form.is_valid():
                newdoc = UploadImageModel(title = form.cleaned_data['title'], image = req.FILES['image'], description = form.cleaned_data['description'])
                newdoc.save()
                context = {
                    'success_message' : "Image has been created!",
                    'fileFieldForm' : FileFieldForm(),
                    'loadContentForm' : LoadContent_Form(),
                    'title' : newdoc.title,
                    'image' : newdoc.image,
                    'description' : newdoc.description
                }
                return render(req, 'animalRescue_app/loadContent.html', context)
            else:
                context = {
                'fileFieldForm' : form,
                'loadContentForm' : LoadContent_Form()
                }
                return render(req, 'animalRescue_app/loadContent.html', context)
    else:
        context = {
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/index.html', context)

@login_required
def loadContent(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if logged_in and auth_for_edit:
        if req.method == 'POST':
            form = LoadContent_Form(req.POST)
            if form.is_valid():
                newdoc = Content(name = form.cleaned_data['name'], description = form.cleaned_data['description'], data = form.cleaned_data['data'])
                newdoc.save()
                #print UploadFileModel.objects.all()
                context = {
                    'success_message' : "Content has been created!",
                    'fileFieldForm' : FileFieldForm(),
                    'loadContentForm' : LoadContent_Form(),
                    'name' : newdoc.name,
                    'data' : newdoc.data,
                    'description' : newdoc.description
                }
                return render(req, 'animalRescue_app/loadContent.html', context)
            else:
                context = {
                'loadContentForm' : form,
                'fileFieldForm' : FileFieldForm()
                }
                return render(req, 'animalRescue_app/loadContent.html', context)
    else:
        context = {
            #'fileFieldForm' : FileFieldForm(),
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/index.html', context)

@login_required
def loadAnyContent(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if logged_in and auth_for_edit:
        context = {
            'fileFieldForm' : FileFieldForm(),
            'loadContentForm' : LoadContent_Form(),
        }
        return render(req, 'animalRescue_app/loadContent.html', context)
    else:
        context = {
            #'fileFieldForm' : FileFieldForm(),
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/index.html', context)

def registerAnimal(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    if not req.user.is_authenticated:
        context = {
            'success_message' : "Please Signup/Login first in order to register an animal for pick up.",
            'return_site' : "register",
            'signupForm' : SignupForm(),
            'loginForm' : LoginForm()
        }
        print context
        return render(req, 'animalRescue_app/signup.html', context)
    else:
        context = {
            'loggedIn' : logged_in,
            'registerAnimalForm' : RegisterAnimal_Form(),
            'fileFieldForm' : FileFieldForm()
            # 'form' : CityAdminForm()
        }
        return render(req, 'animalRescue_app/register.html', context)

def adoptaPet(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    context = {
        'loggedIn' : logged_in,
        'all_Animals' : all_Animals,
        'auth_for_edit' : auth_for_edit
        #'signupForm' : SignupForm(),
        #'loginForm' : LoginForm()
    }
    return render(req, 'animalRescue_app/adopt.html', context)

def adopt_animal(req, id):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if not req.user.is_authenticated:
        context = {
            'success_message' : "Thank you for considering adopting, Please Signup/Login first.",
            'return_site' : "adopt",
            'signupForm' : SignupForm(),
            'loginForm' : LoginForm()
        }
        return render(req, 'animalRescue_app/signup.html', context)
    else:
        animal = Animal.objects.get(id=id)
        context = {
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit,
            'success_message' : "You have indicated your interest in apdoting " + animal.name + " we will contact with further details.",
            'all_Animals' : all_Animals
        }
        return render(req, 'animalRescue_app/adopt.html', context)

def successStories(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    context = {
        'loggedIn' : logged_in,
        'fileFieldForm' : FileFieldForm()
    }
    return render(req, 'animalRescue_app/success.html', context)

def volunteer(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    if not req.user.is_authenticated:
        context = {
            'success_message' : "Thank you for considering volunteering, Please Signup/Login first.",
            'return_site' : "volunteer",
            'signupForm' : SignupForm(),
            'loginForm' : LoginForm()
        }
        return render(req, 'animalRescue_app/signup.html', context)
    else:
        context = {
            'loggedIn' : logged_in,
            'fileFieldForm' : FileFieldForm()
        }
        return render(req, 'animalRescue_app/volunteer.html', context)

def donate(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    context = {
        'loggedIn' : logged_in,
        'fileFieldForm' : FileFieldForm()
    }
    return render(req, 'animalRescue_app/donate.html', context)

def contactUs(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    context = {
        'loggedIn' : logged_in,
        'fileFieldForm' : FileFieldForm()
    }
    return render(req, 'animalRescue_app/contact.html', context)

def aboutUs(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    context = {
        'loggedIn' : logged_in,
        'fileFieldForm' : FileFieldForm()
    }
    return render(req, 'animalRescue_app/about.html', context)

def ourStaff(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    context = {
        'loggedIn' : logged_in,
        'fileFieldForm' : FileFieldForm()
    }
    return render(req, 'animalRescue_app/staff.html', context)

def signup(req, return_site):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(req)
            mail_subject = 'Activate your account for North California Animal Rescue.'
            message = render_to_string('animalRescue_app/active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            context = {
            'return_site' : return_site,
            'signupForm' : SignupForm(),
            'loginForm' : LoginForm(),
            'success_message' : 'Please confirm your email address to complete the registration'
            }
            # return HttpResponse('Please confirm your email address to complete the registration')
            return render(req, 'animalRescue_app/signup.html', context)
        else:
            #return HttpResponse('Activation link is invalid!')
            context = {
            'return_site' : return_site,
            'signupForm' : form,
            'loginForm' : LoginForm(),
            'error_message' : 'Signup information is incorrect!'
            #Handle the retuned messages from the login form
            }
            return render(req, 'animalRescue_app/signup.html', context)
    else:
        context = {
        'return_site' : return_site,
        'signupForm' : SignupForm(),
        'loginForm' : LoginForm()
        }
        return render(req, 'animalRescue_app/signup.html', context)

def loginUser(req, return_site):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        form = LoginForm(data=req.POST)
        if user is not None:
            login(req, user)
        # if form.is_valid():
            context = {
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit,
            'registerAnimalForm' : RegisterAnimal_Form(),
            'success_message' : 'You are Now Logged In!'
            }
            if return_site == "adopt":
                return render(req, 'animalRescue_app/adopt.html', context)
            elif return_site == "volunteer":
                return render(req, 'animalRescue_app/volunteer.html', context)
            else:
                return render(req, 'animalRescue_app/register.html', context)
        else:
            #return HttpResponse('Activation link is invalid!')
            context = {
            'return_site' : return_site,
            'signupForm' : SignupForm(),
            'loginForm' : form,
            'error_message' : 'Login information is incorrect!'
            #Handle the retuned messages from the login form
            }
            return render(req, 'animalRescue_app/signup.html', context)
    else:
        context = {
        'return_site' : return_site,
        'signupForm' : SignupForm(),
        'loginForm' : LoginForm(),
        'error_message' : 'Please enter a proper username and password!'
        }
    return render(req, 'animalRescue_app/signup.html', context)

@login_required
def logoutUser(req):
    logout(req)
    logged_in = False
    all_Animals = Animal.objects.all()
    context = {
        #'fileFieldForm' : FileFieldForm(),
        'success_message' : 'You are now logged out.',
        'loggedIn' : logged_in,
        'all_Animals' : all_Animals
    }
    return render(req, 'animalRescue_app/index.html', context)

def activate(req, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(req, user)
        # return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        context = {
        'signupForm' : SignupForm(),
        'loginForm' : LoginForm(),
        'success_message' : 'Thank you for your email confirmation. You are now logged in!'
        }
        return render(req, 'animalRescue_app/adopt.html', context)
    else:
        #return HttpResponse('Activation link is invalid!')
        context = {
        'signupForm' : SignupForm(),
        'loginForm' : LoginForm(),
        'error_message' : 'Activation link is invalid!'
        }
        return render(req, 'animalRescue_app/adopt.html', context)

@login_required
def update_animal(req, id):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if logged_in and auth_for_edit:
        animal = Animal.objects.get(id=id)
        if req.method == 'POST':
            form = UpdateAnimal_Form(req.POST, req.FILES)
            if form.is_valid():
                if req.FILES.get('image', False):
                    newAnimal = Animal.objects.get(id=id)
                    newAnimal.image = req.FILES['image']
                    newAnimal.save()
                    Animal.objects.filter(id=id).update(type = form.cleaned_data['type'], name = form.cleaned_data['name'], image = newAnimal.image, location = form.cleaned_data['location'], adoption_ready = form.cleaned_data['adoption_ready'], foster_ready = form.cleaned_data['foster_ready'], viewable = form.cleaned_data['viewable'], description = form.cleaned_data['description'])
                else:
                    Animal.objects.filter(id=id).update(type = form.cleaned_data['type'], name = form.cleaned_data['name'], image = animal.image, location = form.cleaned_data['location'], adoption_ready = form.cleaned_data['adoption_ready'], foster_ready = form.cleaned_data['foster_ready'], viewable = form.cleaned_data['viewable'], description = form.cleaned_data['description'])
                # print "animal object", animal
                context = {
                    'success_message' : 'Animal successfully updated!',
                    #'fileFieldForm' : FileFieldForm(),
                    'loggedIn' : logged_in,
                    'auth_for_edit' : auth_for_edit,
                    'all_Animals' : all_Animals
                }
                return render(req, 'animalRescue_app/index.html', context)
                # return redirect('home', context)
            else:
                context = {
                'error_message' : 'Input on the form is invalid!',
                'animal' : animal,
                'loggedIn' : logged_in,
                'auth_for_edit' : auth_for_edit,
                'updateAnimalForm' : form
                }
                return render(req, 'animalRescue_app/updateAnimal.html', context)
        else:
            context = {
                'animal' : animal,
                'loggedIn' : logged_in,
                'auth_for_edit' : auth_for_edit,
                'updateAnimalForm' : UpdateAnimal_Form(initial={'location' : animal.location, 'type' : animal.type, 'name' : animal.name, 'description' : animal.description, 'adoption_ready' : animal.adoption_ready, 'foster_ready' : animal.foster_ready, 'viewable':animal.viewable}),
            }
            return render(req, 'animalRescue_app/updateAnimal.html', context)
    else:
        context = {
            #'fileFieldForm' : FileFieldForm(),
            'error_message' : "You must be logged in as an adminstrator!",
            'loggedIn' : logged_in,
            'auth_for_edit' : auth_for_edit,
            'all_Animals' : all_Animals
        }
        return render(req, 'animalRescue_app/index.html', context)

@login_required
def delete_animal(req, id):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    if logged_in and auth_for_edit:
        Animal.objects.get(id=id).delete()
        context = {
            #'fileFieldForm' : FileFieldForm(),
            'success_message' : "Animal deleted!",
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/index.html', context)
    else:
        auth_for_edit = False
        logged_in = False
        context = {
            #'fileFieldForm' : FileFieldForm(),
            'error_message' : "You must be logged in as an adminstrator!",
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/index.html', context)

@login_required
def viewAllAnimals(req):
    logged_in = (checkAuth(req))
    auth_for_edit = (checkUsername(req))
    all_Animals = Animal.objects.all()
    all_Users = User.objects.all()
    if logged_in and auth_for_edit:
        context = {
        'all_Animals' : all_Animals,
        'all_Users' : all_Users,
        'loggedIn' : logged_in,
        'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/allAnimals_admin.html', context)
    else:
        context = {
            #'fileFieldForm' : FileFieldForm(),
            'error_message' : "You must be logged in as an adminstrator!",
            'loggedIn' : logged_in,
            'all_Animals' : all_Animals,
            'auth_for_edit' : auth_for_edit
        }
        return render(req, 'animalRescue_app/index.html', context)
