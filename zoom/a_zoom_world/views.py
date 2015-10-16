from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import *
from PIL import Image


# Create your views here.


def index(request):

    return render(request, 'new_user.html')

#-----New User----#
def join_zoom(request):
    registered = False
    if request.method == 'POST':
        user_form = Login(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

            return HttpResponseRedirect("/homepage/")
        else:
            print(user_form.errors)
    else:
        user_form = Login()

    return render(request, 'homepage_properties.html',
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
                return HttpResponseRedirect('/homepage/')

            else:
                return HttpResponse("It seems this account is not valid.")
        else:
            print("Login Information is Invalid")
            return HttpResponse("Login Information is Invalid")

    else:
        return render(request, 'homepage_properties.html')

#---logout---#
def logout(request):
    logout(request)
    return render(request, 'log_out.html')


def properties_listing(request):
    # we want to fetch all properties from database and pass to template"
    list = Property.objects.all()
    print(list)
    return render(request,'homepage_properties.html', {'list': list})