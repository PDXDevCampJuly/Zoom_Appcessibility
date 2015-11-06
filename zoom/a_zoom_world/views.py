from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import *

from PIL import Image


# Create your views here.


# def index(request):
# # I need to change this path to a log_in page
#     return render(request, 'update_user.html')

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

    return render(request, 'update_user.html',
                  {'user_form': user_form,
                   'registered': registered})


     #----This is for a user already in the system ----#

def login_zoom_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')

            else:
                return HttpResponse("It seems this account is not valid.")
        else:
            print("Login Information is Invalid")
            return HttpResponse("Login Information is Invalid")

    else:
        return render(request, 'log_in.html')

#---logout---#


def log_out(request):
    logout(request)

    return HttpResponseRedirect("/")


def properties_listing(request):
    # main list of properties
    # we want to fetch all properties from database and pass to template"
    listings = Property.objects.all()
    for i in listings:
        i.picture = i.photo_property.get(featured=True)

    return render(request, 'homepage_properties.html', {'listing': listings})


def property_description(request, property_id):
    property_info = Property.objects.get(pk=property_id)
    feature_photo = property_info.photo_property.get(featured=True)

    return render(request, 'big_description.html', {'property': property_info, 'feature_photo': feature_photo})


def new_listing(request):
    return render(request, 'new_listing.html')


def property_gallery_page(request, property_id):
    photo_gallery = Photo.objects.filter(property_photos__pk=property_id)
    for i in photo_gallery:
        i.picture = i.photo

    return render(request, 'property_gallery.html', {'photo_gallery': photo_gallery, 'property_id': property_id})


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_use(request):
    return render(request, 'terms_of_use.html')

#----------------------- Update Classes


class UserUpdateMain(UpdateView):
    model = User
    fields = '__all__'