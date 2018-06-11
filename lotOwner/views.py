from django.shortcuts import render,redirect
from accounts.models import OwnerProfile
from .models import LotDetails
from .forms import LotDetailsForm,LocationForm,OwnerProfileForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    current_user=request.user.id
    title='Welcome lot owner'
    current_user_name=OwnerProfile.objects.filter(id=request.user.id)

    if current_user_name.exists():
        current_profile=OwnerProfile.objects.get(id=request.user.id)
        lots=LotDetails.objects.filter(owner=current_profile)




    if request.method == 'POST':
        form=LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (home,current_profile.id)
    else:
        form=LocationForm()
    if request.method == 'POST':
        form1=OwnerProfileForm(request.POST)
        if form1.is_valid():
            user_profile=form1.save(commit=False)
            user_profile.user=request.user
            return redirect (home,current_profile.id)
    else:
        form1=OwnerProfileForm()
    return render (request,'Lot/home.html',{"title":title,"lots":lots,"current_profile":current_profile,"form":form,"form1":form1})
def Lotdetail(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)
    current_user=request.user
    if request.method == 'POST':
        form=LotDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            details=form.save(commit=False)
            details.owner=current_profile
            details.save()
            return redirect (home,current_profile.id)
    else:
        form=LotDetailsForm()

    return render(request,'Lot/details.html',{"form":form,"current_profile":current_profile,"current_user":current_user})
