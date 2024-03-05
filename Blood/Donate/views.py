from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Donor

def index(request):
    return render(request,"Donate/index.html",{})

def register(request):
    if request.method == 'POST':
        
        full_name = request.POST['fullName']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        blood_group = request.POST['bloodGroup']
        birth_date = request.POST['birthDate']   
        gender = request.POST['gender']
        weight = request.POST['weight']
        state = request.POST['state']
        district = request.POST['district']
        zip_code = request.POST['zipCode']
        area = request.POST['area']
        landmarks = request.POST['landmarks']

           #validation
        if Donor.objects.filter(email=email).exists():
            messages.error(request,"Email already registered ! please try some other email id ")
            return redirect('register')
        if Donor.objects.filter(mobile=mobile).exists():
            messages.error(request,"Mobile Number already registered ! please try some other Mobile Number ")
            return redirect('register')
        if len(password)< 8:
            messages.error(request,'Password is too short ..')
            return redirect('register')

        #Save the data to database
        Donor.objects.create(
            full_name=full_name,
            mobile=mobile,
            email=email,
            password=password,
            blood_group=blood_group,
            birth_date=birth_date,
            gender=gender,
            weight=weight,
            state=state,
            district=district,
            zip_code=zip_code,
            area=area,
            landmarks=landmarks
        )

        return render(request,"Donate/index.html")
        

    return render(request,"Donate/register.html",{})

def searchUser(request):
    

    return render(request,"Donate/searchUser.html",{})



