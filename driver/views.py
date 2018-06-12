from .forms import CardetailsForm
from django.shortcuts import render,redirect,get_object_or_404
from .models import Cardetails
from django.http import Http404
from accounts.models import DriverProfile
from accounts.forms import EditDriver,EditUserForm
# Create your views here.

def car_details(request):
    '''
    function to populate the details of the car
    '''
    title="Egesha | Car Details "
    current_user = request.user
    try:
        if request.method == 'POST':
            cardetails_form = CardetailsForm(request.POST, request.FILES)

            if cardetails_form.is_valid():
                cardetails = cardetails_form.save(commit=False)

                cardetails.user=current_user

                cardetails.save()

                return redirect('/driver/')

        else:
            cardetails_form = CardetailsForm

    except ValueError:
        Http404

    return render(request, 'user/cardetails.html', {"title":title,"cardetails_form": cardetails_form})


def edit_profile(request):
    '''
    function to populate the details of the car
    '''
    title="Egesha | Profile Form "
    current_user = request.user
    try:
        if request.method == 'POST':

            driver_form  = EditDriver(request.POST,request.FILES)
            user_form = EditUserForm(request.POST, request.FILES)
            if driver_form.is_valid() and user_form.is_valid():

                driverdetails = driver_form.save(commit=False)
                userdetails = user_form.save(commit=False)

                driverdetails.user=current_user
                userdetails.user=current_user

                driverdetails.save()
                userdetails.save()
                return redirect('/driver/')

        else:
            driver_form  = EditDriver
            user_form = EditUserForm

    except ValueError:
        Http404

    return render(request, 'user/profileform.html', {"title":title,"driver_form":driver_form,"user_form":user_form})

def home(request):
    '''
    function to display driver and car details
    '''

    try:
        cardetails = Cardetails.objects.filter(id = request.user.id)
        profile = DriverProfile.objects.filter(id =request.user.id)
        user = request.user
    except ValueError:
        Http404

    return render(request,'user/index.html',{"cardetails":cardetails,"profile":profile,"user":user})
