from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import *
from PIL import Image


# Create your views here.


# def index(request):
# # I need to change this path to a log_in page
#     return render(request, 'new_user.html')

#-----New User----#
def new_user(request):
    registered = False
    if request.method == 'POST':
        user_form = Login(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

            return HttpResponseRedirect("/log_in/")
        else:
            print(user_form.errors)
    else:
        user_form = Login()

    return render(request, 'log_in.html',
                  {'user_form': user_form,
                   'registered': registered})


     #----This is for a user already in the system ----#

def login_zoom_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.active:
                login(request, user)
                return HttpResponseRedirect('/log_in/')

            else:
                return HttpResponse("It seems this account is not valid.")
        else:
            print("Login Information is Invalid")
            return HttpResponse("Login Information is Invalid")

    else:
        return render(request, 'log_in.html')

#---logout---#
def logout(request):
    logout(request)
    return render(request, 'log_out.html')


def properties_listing(request):
    # we want to fetch all properties from database and pass to template"
    listing = Property.objects.all()
    for i in listing:
        i.picture = i.photo_property.all()[0]

    return render(request, 'homepage_properties.html', {'listing': listing})


def big_description_page(request):
    # I want to call one property listing and show all the cool things about the property
    # I will need to make a query from the database that gets info about property

    big_listing = Property.objects.all()
    for i in big_listing:
        i.picture = i.photo_property.all()
    #need to call amenities and needs here
    return render(request, 'big_description.html', {'big_listing': big_listing})



def new_listing(request):
    return render(request,'new_listing.html')


def property_gallery_page(request):
    photo_gallery = Photo.objects.all()
    for i in photo_gallery:
         i.picture = i.photo
    return render(request, 'property_gallery.html', {'photo_gallery': photo_gallery })


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_use(request):
    return render(request, 'terms_of_use.html')


